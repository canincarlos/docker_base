from rest_framework import serializers
#from popolo.models import Person, Organization, Membership, Post

from mediameter.models import *

class MinTweetSerializer(serializers.ModelSerializer):
#    city_name = BaseCitySerializer()
    class Meta:
        model = Tweet
        fields = '__all__'


class TweeterSerializer(serializers.ModelSerializer):
    tweet_set = MinTweetSerializer(many=True)
    class Meta:
        model = Tweeter
        # fields = ('id', 'tweet_set')
        # depth = 2
        fields = '__all__'
    

class MinTweeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tweeter
        fields = ('handle', 'webpage')
        # depth = 2


class TweetSerializer(serializers.ModelSerializer):
    tweeter = MinTweeterSerializer()
    class Meta:
        model = Tweet
        # fields = ('id', 'created', 'datestamp', 'likes', 'retweets', 'text', 'tweeter')
        fields = '__all__'
        depth = 2


# class HashtagSerializer(serializers.ModelSerializer):
# #    city_name = BaseCitySerializer()
#     class Meta:
#         model = Hashtag
#         fields = '__all__'


# class TagSerializer(serializers.ModelSerializer):
# #    city_name = BaseCitySerializer()
#     class Meta:
#         model = Tag
#         fields = '__all__'
