from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]
