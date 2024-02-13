from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.counter, name='counter'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('createpost', views.CreatePost, name='CreatePost'),
    path('post/<int:id>', views.post, name='post'),
    path('home', views.index, name='index'),
    path('update-post/<int:post_id>', views.updatepost, name='update_post'),
    # path('search', views.search_blogs, name='search_blogs'),
    path('delete-post/<int:post_id>/', views.deletepost, name="delete-post"),
    path('like/<int:post_id>', views.like_post, name='like'),
    path('comment/<str:post_id>', views.comment, name='comment'),
    path('languges', views.languges, name='languges'),
    path('blog', views.blog, name='blog'),
    path('updates', views.updates, name='updates'),
    path('userslist', views.userslist, name="users"),
    path('follow/<int:user_id>', views.follow, name="follow")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)