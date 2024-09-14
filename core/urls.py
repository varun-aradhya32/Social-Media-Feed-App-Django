from django.urls import path, re_path
from . import views

from django.shortcuts import redirect

def redirect_to_feed(request):
    return redirect('feed')

urlpatterns = [
    path('', redirect_to_feed),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('feed/', views.feed, name='feed'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/comment/', views.comment_create, name='comment_create'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/like/', views.like, name='like'),
    re_path(r'^profile/(?!change-username/)(?P<username>\w+)/$', views.user_profile, name='user_profile'),
    path('guest/profile/<str:username>/', views.guest_profile, name='guest_profile'),
    path('profile/change-username/', views.change_username, name='change_username'),
    path('search/', views.search_users, name='search_users'),
]
