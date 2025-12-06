from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("post/new/", views.post_create, name="post_create"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/<int:pk>/edit/", views.post_update, name="post_update"),
    path("post/<int:pk>/delete/", views.post_delete, name="post_delete"),
    path("post/<int:pk>/like/", views.toggle_like, name="toggle_like"),
    path("post/<int:pk>/comment/", views.add_comment, name="add_comment"),
    path("users/<str:username>/", views.profile_detail, name="profile_detail"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("profile/delete/", views.profile_delete, name="profile_delete"),
    path("users/<str:username>/follow/", views.toggle_follow, name="toggle_follow"),
]


