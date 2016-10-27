from csv import DictReader

from django.apps import apps
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    help = 'Import given csv file into given model'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str)
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        Model = apps.get_model(options['model'])

        with open(options['csv_file']) as f:
            records = list(DictReader(f))

        Model.objects.bulk_create(
            [Model(**data) for data in records]
        )

        self.stdout.write(self.style.SUCCESS(
            'Successfully imported "%s" records into "%s".' % (len(records), options['model'])))
