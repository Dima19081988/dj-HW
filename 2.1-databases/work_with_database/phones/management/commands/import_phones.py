import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones_data = list(csv.DictReader(file, delimiter=';'))

        for entry in phones_data:
            phone = Phone(
	            id = int(entry['id']),
	            name = entry['name'],
	            image = entry['image'],
	            price = float(entry['price']),
	            release_date = entry['release_date'],
	            lte_exists=entry['lte_exists'].lower() in ['true', '1', 't', 'yes']
            )
            phone.save()
            self.stdout.write(self.style.SUCCESS(f'Добавлен телефон {phone.name}'))

