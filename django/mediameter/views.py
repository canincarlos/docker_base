from datetime import datetime, timedelta
import pytz

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView
from django.db.models import Q

from .models import *

from .serializers import *

from rest_framework.settings import api_settings
from rest_framework import generics, renderers
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# 2019-10-02T14:34:23+21:44
tz_format = '%Y-%m-%dT$H:%M:%S+%H:%M'
td = timedelta(hours=18)
odt = datetime.now() - td
ndt = odt.strftime(tz_format)



##############
## Comments ##
##############
# @permission_classes([])
# @authentication_classes([])
# class TagsAPIView(generics.ListCreateAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer

#     def perform_create(self, serializer):
#         serializer.save()


# @permission_classes([])
# @authentication_classes([])
# class HashtagsAPIView(generics.ListCreateAPIView):
#     queryset = Hashtag.objects.all()
#     serializer_class = HashtagSerializer

#     def perform_create(self, serializer):
#         serializer.save()


@permission_classes([])
@authentication_classes([])
class TweetsAPIView(generics.ListCreateAPIView):
    queryset = Tweet.objects.order_by('-created').all()
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        serializer.save()


@permission_classes([])
@authentication_classes([])
class TweeterAPIView(generics.ListCreateAPIView):
    queryset = Tweeter.objects.all().order_by('name')
    serializer_class = TweeterSerializer

    def perform_create(self, serializer):
        serializer.save()


###################
## Search Events ##
###################
@permission_classes([])
@authentication_classes([])
class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        queryset = Tweet.objects.all().order_by('created')
        tweet_query = self.request.query_params.get('q', None)
        if tweet_query is not None:
            queryset = queryset.filter(tweeter__id=tweet_query).distinct().order_by('created')
        return queryset