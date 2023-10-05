import csv
from django.core.management.base import BaseCommand
from coupon.models import Coupon, Store  # Replace 'your_app' with your actual app name

class Command(BaseCommand):
    help = 'Import coupons from CSV'

    def add_arguments(self, parser):
        parser.add_argument("--file", action="store", type=str, help="CSV file path")

    def handle(self, *args, **options):
        file_path = options['file']

        try:
            with open(file_path, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    intro = row['intro']
                    store_name = row['store_link']
                    external_link = row['external_link']
                    body = row['body']

                    try:
                        store = Store.objects.get(name=store_name)
                    except Store.DoesNotExist:
                        store = Store.objects.create(
                            name=store_name,
                            external_link=external_link,
                            description=""  # Add any default value for description
                        )
                        store.save()

                    coupon = Coupon.objects.create(
                        intro=intro,
                        store_link=store,
                        external_link=external_link,
                        body=body,
                        path='/',  # Set a default path
                        depth=0,   # Set a default depth
                        title=intro,  # Set a default title
                        slug=intro.lower().replace(' ', '-'),  # Set a default slug
                    )
                    coupon.save()

                self.stdout.write(self.style.SUCCESS("CSV imported successfully"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {str(e)}"))
