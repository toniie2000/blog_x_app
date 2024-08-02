from django.urls import path
from . import views

urlpatterns = [
    path('post_list', views.post_list, name='post_list'),
    path('post1/<int:post_id>/', views.post_detail, name='post_detail'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('create/', views.create_post, name='create_post'),
]
