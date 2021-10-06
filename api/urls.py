from django.urls import path
from jwt_project.api.views.users import UserView,LoginView,UserInfoView
from jwt_project.utils.auth import SafeJWTAuthentication

# Create your urls here.

urlpatterns = [
    path('signup/', UserView.as_view()),
    path('login/', LoginView.as_view()),
    path('userinfo/', UserInfoView.as_view()),
    
]
