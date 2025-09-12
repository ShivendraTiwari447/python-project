# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
# ]



# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),                    # home page
#     path('user/login/', views.user_login, name='user_login'),  # login page
# ]





# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),                   
#     path('user/login/', views.user_login, name='user_login'),  
#     path('login/', views.user_login, name='user_login'),
#     path('signup/', views.user_register, name='register'),  
#     path('user/login/', views.user_login),
#      path('events/', views.events_page, name='events'),
#      path('logout/', views.user_logout, name='user_logout'),
  


# ]




from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                    # Home page
    path('user/login/', views.user_login, name='user_login'),  # User login
    path('login/', views.user_login, name='user_login_alias'), # Optional alias for user login
    path('signup/', views.user_register, name='register'),     # Signup page
    path('events/', views.events_page, name='events'),         # Events page
    path('logout/', views.user_logout, name='user_logout'),    # Logout
    path('admin/login/', views.admin_login_view, name='admin_login'), # Admin login
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

]






# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('login/', views.user_login, name='user_login'),  # This must match fetch
#     path('signup/', views.user_register, name='register'),
#     path('user/login/', views.user_login, name='user_login'),  

# ]




