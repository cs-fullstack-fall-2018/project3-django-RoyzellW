from django.urls import path
from . import views

urlpatterns = [

    # home page to create user
    path('', views.createUser, name='signUp'),

    # page to logOut
    path('logout/', views.logout, name='logout'),

    # show login page
    path('login/', views.logIn, name='login'),

    # show a user specifc page
    path('user_page/', views.user_page, name='user_page'),

]