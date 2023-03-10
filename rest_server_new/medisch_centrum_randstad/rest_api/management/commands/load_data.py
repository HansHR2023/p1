import csv
from django.core.management import BaseCommand
from rest_api.models import Netlify
import logging

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

logging.basicConfig(level="INFO")


class Command(BaseCommand):

    # Show this when the user types help
    help = "Loads data from csv"

    def validateValue(self, rowVal):
        res = rowVal.replace('.', '').isdecimal()
        logging.debug(f"rowVal : {rowVal}")
        logging.debug(res)
        return res

    def loadFromCSV(self, csvFile):
        logging.info(f"Loading data from {csvFile}")

        # Open file
        with open(csvFile) as fileObj:

            # Create reader object by passing the file
            # object to DictReader method
            readerObj = csv.DictReader(fileObj)

            # Iterate over each row in the csv file
            # using reader object
            for count, row in enumerate(readerObj):

                logging.info(f"Import row {count}")
                logging.debug(row)

                if any(row[key] in (None, "") for key in row):
                    logging.warning(f"Row {row} contains empty cell")

                # Create new object
                netlify = Netlify()

                netlify.genetic = row['genetic'] if self.validateValue(
                    row['genetic']) else None
                netlify.length = row['length'] if self.validateValue(
                    row['length']) else None
                netlify.mass = row['mass'] if self.validateValue(
                    row['mass']) else None
                netlify.exercise = row['exercise'] if self.validateValue(
                    row['exercise']) else None
                netlify.smoking = row['smoking'] if self.validateValue(
                    row['smoking']) else None
                netlify.alcohol = row['alcohol'] if self.validateValue(
                    row['alcohol']) else None
                netlify.sugar = row['sugar'] if self.validateValue(
                    row['sugar']) else None
                netlify.lifespan = row['lifespan'] if self.validateValue(
                    row['lifespan']) else None

                # Store object
                netlify.save()

    def handle(self, *args, **options):

        if Netlify.objects.exists():
            logging.warning('netlify data already loaded...exiting.')
            logging.warning(ALREADY_LOADED_ERROR_MESSAGE)

            return

        self.loadFromCSV('data/data.csv')
