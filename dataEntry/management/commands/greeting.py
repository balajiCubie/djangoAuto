from django.core.management import BaseCommand
from django.core.management.base import CommandParser

class Command(BaseCommand):
    help = 'greeting from user'
    def add_arguments(self, parser) :
        parser.add_argument('name', type=str , help="specifie the name")

    def handle(self, *args, **kwargs):
        name =kwargs['name']
        greeting = f'hello {name}'
        # dipalay outputin green like sucess
        self.stdout.write(self.style.SUCCESS(greeting))
        self.stdout.write(greeting)


