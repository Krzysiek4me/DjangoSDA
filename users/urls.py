from users.views import SignUpView, UserLoginView
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]