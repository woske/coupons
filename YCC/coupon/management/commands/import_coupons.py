from django.core.management.base import BaseCommand
from coupon.utils.import_csv import import_data_from_csv

class Command(BaseCommand):
    help = 'Import coupons and stores from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        import_data_from_csv(csv_file)
        self.stdout.write(self.style.SUCCESS('Imported data successfully'))
