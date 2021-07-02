from django.conf.urls import url
from .views import HomeView,PostDetailView,CreatePostView,UpdatePostView,DeletePostView
# from django.views.i18n import JavaScriptCatalog
app_name = 'Article'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='blog-home'),
    url(r'^post_detail/(?P<slug>[-\w]+)/$',PostDetailView.as_view(),name='post-detail'),
    url(r'^create_post/',CreatePostView.as_view(),name='create-post'),
    url(r'^update_post/(?P<slug>[-\w]+)/$',UpdatePostView.as_view(),name='update-post'),
    url(r'^delete_post/(?P<slug>[-\w]+)/$',DeletePostView.as_view(success_url='/'),name='delete-post'),
    ]
