from csv import DictReader

from django.core.management.base import BaseCommand, CommandError

from ...models import Record


class Command(BaseCommand):
    help = 'Import given csv file into `Record`'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file']) as f:
            records = list(DictReader(f))

        Record.objects.bulk_create(
            [Record(**data) for data in records]
        )

        self.stdout.write(self.style.SUCCESS('Successfully imported "%s" records.' % len(records)))
