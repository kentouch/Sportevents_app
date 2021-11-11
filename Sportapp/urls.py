from .views import AddCommentView, PostList, CatListView, PostDetailView, LikeView, search_bar
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('search', search_bar, name='search-results'),
    path('category/<category>/', CatListView.as_view(), name='category'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='Add_comment'),
    path('like/<int:pk>', LikeView, name='like_post'),

] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)