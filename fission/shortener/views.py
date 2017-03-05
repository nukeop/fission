import random

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader

from . import api
from . import models


def index(request):
    context = {
        'title': 'Link shortening service'
    }
    return render(request, 'shortener/index.html', context)


def link(request):
    shortened_url = None

    # Hard to avoid long lines here
    if models.ShortenedUrl.objects.filter(full_url=request.POST['long_url']).exists():
        shortened_url = models.ShortenedUrl.objects.filter(full_url=request.POST['long_url']).first()
    else:
        # To get a random user from the database, we first fetch the highest
        # id, then choose a random id within that range. Then we get the user
        # with that id or the first user with an id greater than that in case
        # records were deleted. Fetching all records and selecting a random one
        # would be ineffective from performance point of view.
        highest_id = User.objects.order_by('-id')[0].id
        rand_id = random.randint(1, highest_id+1)
        rand_user = User.objects.filter(id__gte=rand_id)[0]

        shortened_url = api.create_shortened_url(request.POST['long_url'],
                                                 rand_user)

    context = {
        'title': 'Your shortened link',
        'message': 'Here\'s your shortened link:',
        'link': request.build_absolute_uri(shortened_url.short_url)
    }
    return render(request, 'shortener/link.html', context)


def preview(request, shortened_url):
    url_record = get_object_or_404(models.ShortenedUrl,
                                   short_url=shortened_url)
    context = {
        'title': 'Link preview',
        'message': 'Link preview:',
        'full_url': url_record.full_url,
        'visits': url_record.visits,
        'submitter': url_record.submitter
    }
    return render(request, 'shortener/preview.html', context)


def shortened(request, shortened_url):
    url_record = get_object_or_404(models.ShortenedUrl,
                                   short_url=shortened_url)
    url_record.visits += 1
    url_record.save()

    return HttpResponseRedirect(url_record.full_url)
