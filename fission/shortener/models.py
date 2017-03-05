from django.db import models
from django.contrib.auth.models import User


class ShortenedUrl(models.Model):
    full_url = models.CharField(max_length=2048) # the smallest maximum
                                                 # supported by all browsers
    short_url = models.CharField(max_length=2048)
    visits = models.IntegerField(default=0)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '\n'.join([
            'full_url: {}'.format(self.full_url),
            'short_url: {}'.format(self.short_url),
            'visits: {}'.format(self.visits),
            'submitter: {}'.format(self.submitter),
        ])
