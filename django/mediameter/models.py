from django.db import models
# from versatileimagefield.fields import VersatileImageField
from django.core.files.storage import FileSystemStorage


Ps = FileSystemStorage(location='media/mediameter/graphs/')

# Create your models here.

################
# Dex Entities #
################

# Two entities -- Tweeter, and their tweets
# add two more -- Tags, Hashtags


# class Tag(models.Model):
#     name = models.CharField(max_length=128, blank=False, null=False, unique=True)
#     description = models.TextField()

#     def __unicode__(self):
#         return u'%s' % (self.name)

#     def __str__(self):
#         return u'%s' % (self.name)


# class Hashtag(models.Model):
#     name = models.CharField(max_length=128, blank=False, null=False, unique=True)
#     tags = models.ManyToManyField(Tag, blank=False)
#     published = models.BooleanField()   
    
#     def __unicode__(self):
#         return u'%s' % (self.name)

#     def __str__(self):
#         return u'%s' % (self.name)

class ParentGroup(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    pgroup = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT)
    description = models.TextField()
    # tags = models.ManyToManyField(Tag, blank=False)
    # published = models.BooleanField()   
    
    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return u'%s' % (self.name)



class Tweeter(models.Model):
    twid = models.CharField(max_length=64,blank=False, null=False, unique=True)
    pgroup = models.ForeignKey('ParentGroup', blank=True, null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(max_length=128, blank=False, null=False)
    name = models.CharField(max_length=128, blank=True, null=True)
    handle = models.CharField(max_length=64, blank=True, null=True)
    favorites = models.IntegerField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    following = models.IntegerField(blank=True, null=True)
    total_faves = models.IntegerField(blank=True, null=True)
    total_rts = models.IntegerField(blank=True, null=True)
    total_twts = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    webpage = models.URLField(blank=True, null=True)
    # basegraph = VersatileImageField(upload_to='mediameter/graphs/', blank=True, null=True)
    # hashtags = models.ManyToManyField(Hashtag, blank=False)
    # likes = models.IntegerField(blank=False, null=False)
    # retweets = models.IntegerField(blank=False, null=False)
    # rating = models.CharField(max_length=128, blank=False, null=False)
    # tags = models.ManyToManyField(Tag, blank=FaForeignKeylse)
    # published = models.BooleanField(default=False)   
    
    def __unicode__(self):
        return u'%s' % (self.handle)

    def __str__(self):
        return u'%s' % (self.handle)

    # class Meta:
    #     unique_together = ("twid",)


class Tweet(models.Model):
    tweeter = models.ForeignKey(Tweeter, blank=False, null=False, on_delete=models.PROTECT)
    twid = models.CharField(max_length=64,blank=False, null=False)
    created = models.DateTimeField(max_length=128, blank=False, null=False)
    datestamp = models.CharField(max_length=16, blank=True, null=True)
    text = models.CharField(max_length=1024, blank=True, null=True)
    # is_quote = models.BooleanField()
    # quote_twid = models.CharField(max_length=64, blank=False, null=False)
    # quote_text = models.CharField(max_length=1024, blank=False, null=False)
    # hashtags = models.ManyToManyField(Hashtag, blank=False)
    likes = models.IntegerField(blank=True, null=True)
    retweets = models.IntegerField(blank=True, null=True)
    # rating = models.CharField(max_length=128, blank=False, null=False)
    # tags = models.ManyToManyField(Tag, blank=False)
    # published = models.BooleanField(default=False)   
    
    def __unicode__(self):
        return u'%s' % (self.text[:15])

    def __str__(self):
        return u'%s' % (self.text[:15])


    class Meta:
        unique_together = ("twid","tweeter")
        ordering = ['-created']