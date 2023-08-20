from django.urls import path
from .views import add_post, PostListView, LikeView, ListUsers, PostDetailView, PostJsonListView

from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'
from django.contrib.auth import  views as auth_views
urlpatterns = [
    path('add/', add_post, name = 'add'),
    path('list/', PostListView, name='post_list'),
    path('like/<int:pk>', LikeView.as_view(), name='like_toggle'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('api/like/<int:pk>', ListUsers.as_view(), name='like_api_toggle'),
    path('posts-json/<int:num_posts>/<int:pk>', PostJsonListView.as_view(), name="post-json-view"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
