from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('like/<int:pk>', views.add_like, name='add_like'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='detail'), 
    path('new_post/', views.PostCreateView.as_view(), name='new_post'), 
    path('comment/<int:pk>', views.comment_add),

]
