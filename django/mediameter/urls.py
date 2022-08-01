from django.urls import re_path as url
from django.views.generic import DetailView
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
#    url(r'^api/$', ListView.as_view(), name="apilist"),
    url(r'^api/gettweets$', TweetsAPIView.as_view(), name="detail"),   
    url(r'^api/gettweeters$', TweeterAPIView.as_view(), name="detail"), 
    url(r'^api/gettweetlist$', TweetListAPIView.as_view(), name="post")

    # url(r'^api/hashtags$', HashtagsAPIView.as_view(), name="posts"),
    # url(r'^api/tags$', TagsAPIView.as_view(), name="posts"),
    # url(r'^api/tweets$', TweetsAPIView.as_view(), name="posts"),
    # url(r'^api/tweet/[-@\w]+/$', PostAPIView.as_view(), name="post"),    
]

urlpatterns = format_suffix_patterns(urlpatterns)
