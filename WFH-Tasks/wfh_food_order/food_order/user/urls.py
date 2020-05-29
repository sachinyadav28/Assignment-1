from django.urls import path

from user.views import CreateUserView, CreateTokenView, ManageUserView

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('edit/', ManageUserView.as_view(), name='edit'),
]