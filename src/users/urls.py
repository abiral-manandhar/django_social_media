from django.urls import path
from .views import HomeView,profile, PostDetail
from .forms import UserLoginForm
from django.contrib.auth.views import LogoutView, LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', LoginView.as_view(template_name = 'users/home.html', authentication_form = UserLoginForm, redirect_authenticated_user=True), name = 'login',),
    path('register/', HomeView, name = 'register'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'),  name="logout"),
    path('profile/', profile, name = 'profile'),
    path('yourposts/detail/<int:pk>', PostDetail.as_view(), name="post-detail")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

