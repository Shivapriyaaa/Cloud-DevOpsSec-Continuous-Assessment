from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import CommentForm, PostForm, ProfileForm, UserRegistrationForm
from .models import BlogPost, Comment, Like, Profile


def home(request: HttpRequest) -> HttpResponse:
    posts = (
        BlogPost.objects.select_related("author")
        .prefetch_related("comments__author", "likes__user")
        .all()
    )
    liked_ids: set[int] = set()
    if request.user.is_authenticated:
        liked_ids = set(
            Like.objects.filter(user=request.user, post__in=posts).values_list(
                "post_id", flat=True
            )
        )
    context = {
        "posts": posts,
        "comment_form": CommentForm(),
        "liked_ids": liked_ids,
    }
    return render(request, "core/home.html", context)


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome! Your account has been created.")
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "core/register.html", {"form": form})


def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("home")
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "Signed in successfully.")
        return redirect("home")
    return render(request, "core/login.html", {"form": form})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.info(request, "You have been signed out.")
    return redirect("home")


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(
        BlogPost.objects.select_related("author").prefetch_related(
            Prefetch("comments", queryset=Comment.objects.select_related("author"))
        ),
        pk=pk,
    )
    comment_form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Please sign in to comment.")
            return redirect("login")
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Comment added.")
            return redirect("post_detail", pk=post.pk)
    user_liked = False
    if request.user.is_authenticated:
        user_liked = Like.objects.filter(user=request.user, post=post).exists()
    return render(
        request,
        "core/post_detail.html",
        {"post": post, "comment_form": comment_form, "user_liked": user_liked},
    )


@login_required
def post_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Blog created.")
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "core/post_form.html", {"form": form, "action": "Create"})


@login_required
def post_update(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated.")
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "core/post_form.html", {"form": form, "action": "Update"})


@login_required
def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    if request.method == "POST":
        post.delete()
        messages.info(request, "Blog deleted.")
        return redirect("home")
    return render(request, "core/post_confirm_delete.html", {"post": post})


@login_required
def toggle_like(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(BlogPost, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
        messages.info(request, "You unliked this post.")
    else:
        messages.success(request, "You liked this post.")
    next_url = request.POST.get("next") or reverse("post_detail", kwargs={"pk": pk})
    return redirect(next_url)


@login_required
def add_comment(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(BlogPost, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.success(request, "Comment added.")
    else:
        messages.error(request, "Please correct the comment and try again.")
    return redirect("post_detail", pk=pk)


def profile_detail(request: HttpRequest, username: str) -> HttpResponse:
    profile_user = get_object_or_404(User, username=username)
    profile = profile_user.profile
    posts = profile_user.posts.all()
    is_self = request.user.is_authenticated and request.user == profile_user
    is_following = False
    if request.user.is_authenticated and not is_self:
        is_following = profile in request.user.profile.following.all()
    context = {
        "profile_user": profile_user,
        "profile": profile,
        "posts": posts,
        "is_self": is_self,
        "is_following": is_following,
    }
    return render(request, "core/profile.html", context)


@login_required
def profile_edit(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile_detail", username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, "core/profile_edit.html", {"form": form})


@login_required
def profile_delete(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        user = request.user
        username = user.username
        logout(request)
        user.delete()
        messages.info(request, f"Profile {username} deleted.")
        return redirect("home")
    return render(request, "core/profile_delete.html")


@login_required
def toggle_follow(request: HttpRequest, username: str) -> HttpResponse:
    target_user = get_object_or_404(User, username=username)
    target_profile = target_user.profile
    user_profile = request.user.profile
    if target_user == request.user:
        messages.error(request, "You cannot follow yourself.")
    else:
        if target_profile in user_profile.following.all():
            user_profile.following.remove(target_profile)
            messages.info(request, f"You unfollowed {target_user.username}.")
        else:
            user_profile.following.add(target_profile)
            messages.success(request, f"You followed {target_user.username}.")
    return redirect("profile_detail", username=username)


