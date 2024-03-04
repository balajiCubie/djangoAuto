# create a command a print hello word if in run the comment python manage.py helloworld  print hello world  in terminal
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints hello world'
    
    def handle(self, *args, **options):
        self.stdout.write('Hello world')
