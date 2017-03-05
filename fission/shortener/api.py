import random
import string
from django.conf import settings

from . import models


def shortened_url():
    """ Generates a random sequence of letters and numbers that will be used as
    a shortened link.
    """
    bounds = settings.SHORT_URL_LENGTH_BOUND
    charset = string.ascii_letters + string.digits

    # Length of the link are random, within specified bounds
    # Links include random numbers and lower- and uppercase letters
    length = random.randint(bounds[0], bounds[1])
    shortened = ''.join([random.choice(charset) for _ in range(length)])
    return shortened


def create_shortened_url(url, submitter):
    """Creates a shortened url record, saves it in the database, and returns a
    reference to it.
    """
    short = models.ShortenedUrl(
        full_url = url,
        short_url = shortened_url(),
        visits = 0,
        submitter = submitter
    )
    short.save()
    return short
