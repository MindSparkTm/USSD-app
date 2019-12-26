from django.conf.urls import url
from .views import Home,subscribe_user,CreatePost,PostDetailView,PostDeleteView,PostUpdateView
app_name ='blog'
urlpatterns = [
    url(r'^home/$', Home.as_view(), name='home'),
    url(r'^subscribe/$', subscribe_user, name='subscribed_user'),
    url(r'^post/create/$', CreatePost.as_view(), name='create_post'),
    url(r'^post/(?P<pk>\w+)/$',PostDetailView.as_view(),name='post_detail'),
    url(r'^post/(?P<pk>\w+)/delete/$', PostDeleteView.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>\w+)/update/$', PostUpdateView.as_view(), name='post_update'),

]