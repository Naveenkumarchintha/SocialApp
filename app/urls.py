from django.contrib import admin
from django.urls import path
from .authentication import RegistrationAPIView, LoginAPIView
from .views import UserListAPIView, UserDetailAPIView, PostListAPIView, PostDetailAPIView, CommentListAPIView, CommentDetailAPIView,PostSearchAPIView, PostInfoAPIView,FollowAPIView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegistrationAPIView.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/users/', UserListAPIView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('api/posts/', PostListAPIView.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('api/comments/', CommentListAPIView.as_view(), name='comment-list'),
    path('api/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('api/posts/search/', PostSearchAPIView.as_view(), name='post-search'),
    path('api/posts/<int:pk>/info/', PostInfoAPIView.as_view(), name='post-info'),
    path('api/follow/', FollowAPIView.as_view(), name='follow'),
]

