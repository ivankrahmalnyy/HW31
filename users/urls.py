from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserCreateView, UserListView, UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    # Urls для аутентификации
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())


    # "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjAxNTcwMSwiaWF0IjoxNjY1OTI5MzAxLCJqdGkiOiJiZjRjNmE3M2UzYjY0MDMyYWU1ZGJlMTcyM2E2NzUyNiIsInVzZXJfaWQiOjExfQ.dkvD1JeAmTCiLhD6m4cG_S4hvkZ46-kA7olo2FpNp9M",
    #            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1OTI5NjAxLCJpYXQiOjE2NjU5MjkzMDEsImp0aSI6IjJhZWNkMDQ0MjAzYTQyMzFhZGMwMjdhOGY5ZDI3NmU1IiwidXNlcl9pZCI6MTF9.Hj5yz6-okAfdJnzTJPoRs8nEoLI2KkqASQkAQGa0R-A"
]


