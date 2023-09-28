import csv
from coupon.models import Coupon, Store

def import_data_from_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            store_name = row['store_name']
            store, created = Store.objects.get_or_create(name=store_name)
            store.external_link = row['store_link']
            store.save()

            coupon = Coupon(
                title=row['coupon_title'],
                date=row['coupon_date'],
                intro=row['coupon_intro'],
                body=row['coupon_body'],
                external_link=['external_link'],
                category_id=row['category_id'],  # You need to map CSV columns to Category IDs
                external_link=row['coupon_external_link'],
                code=row['coupon_code'],
            )
            coupon.save()
