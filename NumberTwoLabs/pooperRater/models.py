from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Place(models.Model):
    # Place data - general
    name = models.CharField(max_length=80)
    floor = models.IntegerField(null=True)

    unit = models.CharField(null=True, blank=True, max_length=5)
    address = models.CharField(null=True, blank=True, max_length=120)
    desc = models.TextField(null=True, blank=True)
    place_type = models.SmallIntegerField(null=True)
    start_hours = models.TimeField(null=True)
    end_hours = models.TimeField(null=True)
    pic = models.ImageField(null=True, blank=True)

    # Place data specific to yelp
    yelp_id = models.CharField(max_length=100, null=True, blank=True)
    yelp_categories = models.TextField(blank=True)

    # Place data specific to google
    google_id = models.CharField(max_length=100, null=True, blank=True)
    google_lat = models.SmallIntegerField(null=True, blank=True)
    google_long = models.SmallIntegerField(null=True, blank=True)

    type_conversion = {
        1: "placeholder",
        2: "bad food",
        3: "new string"
    }

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{}".format(self.name) + " Types: {}.".format(self.type_conversion[self.place_type])


class Rating(models.Model):
    # links
    user = models.ForeignKey(User)
    place = models.ForeignKey(Place)

    # Stars
    STAR_CONVERSION = (
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    )
    air_flow = models.PositiveSmallIntegerField(choices=STAR_CONVERSION)
    cleanliness = models.PositiveSmallIntegerField(choices=STAR_CONVERSION)
    available = models.PositiveSmallIntegerField(choices=STAR_CONVERSION)
    quality = models.PositiveSmallIntegerField(choices=STAR_CONVERSION)
    other = models.PositiveSmallIntegerField(choices=STAR_CONVERSION)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{}, {}".format(self.user, self.place)


class Comment(models.Model):
    rating = models.OneToOneField(Rating)
    body = models.TextField(null=True, blank=True)
    upvote = models.SmallIntegerField(null=True, blank=True)
    downvote = models.SmallIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{}".format(self.rating.user.username)


class Restroom(models.Model):
    # Identifying information
    place = models.ForeignKey(Place)
    floor = models.CharField(max_length=3, null=True, blank=True)
    local_identifier = models.SmallIntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Additional features
    type = models.SmallIntegerField(max_length=1)
    features = models.TextField(null=True, blank=True)

    type_conversion = {
        1: "test",
        2: "other"
    }


