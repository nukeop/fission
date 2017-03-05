import json
import sys

import requests
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


RANDOMUSER_API = 'https://randomuser.me/api/'


class Command(BaseCommand):
    help = 'Generates fake user accounts using data pulled from randomuser.me'


    def add_arguments(self, parser):
        parser.add_argument(
            'num',
            help='number of users to generate',
            type=int
        )


    def handle(self, *args, **options):
        if options['num'] > 0:
            text = requests.get(RANDOMUSER_API, params={
                'format': 'json',
                'results': options['num']
            }).text

            # Here we could also skip exception handling to get a more detailed
            # message from the json module, depending on the needs
            try:
                parsed = json.loads(text)
            except ValueError:
                print('randomuser.me api returned malformed data, aborting',
                      file=sys.stderr)
                return

            fake_users = []

            if parsed.get('results') is None:
                print(('no results key in data returned by randomuser.me api,'
                       'aborting'), file=sys.stderr)

            for result in parsed['results']:
                user = User(
                    username=result['login']['username'],
                    first_name=result['name']['first'],
                    last_name=result['name']['last'],
                    email=result['email'],
                    password=result['login']['password'],
                    date_joined=result['registered']
                )
                user.save()
