from .models import Coupon

# Open sample CSV file
csv_file = open('csv/test.csv') 

# Call import method
Coupon.import_csv(csv_file)
