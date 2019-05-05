# Python imports
import json

# Django imports
from django.core.management.base import BaseCommand, CommandError

# Module imports
from stores.models import Store, Product


class Command(BaseCommand):
    help = "Imports stores and products form json file"

    def add_arguments(self, parser):
        parser.add_argument('source', type=str, help="json file to be imported")

    def handle(self, *args, **options):

        json_file = options['source']

        with open(json_file, 'r') as json_file:
            json_data = json.load(json_file)
        json_file.close()

        for key in json_data.keys():
            store = Store.objects.create(store_name=key)

            store_products = json_data.get(key)

            for product in store_products:
                Product.objects.create(store=store, title=product['title'],
                    link=product['link'],
                    description=product['description'],
                    image_link=product['image_link'])

        self.stdout.write(self.style.SUCCESS(
            'Successfully imported json file data.'))
