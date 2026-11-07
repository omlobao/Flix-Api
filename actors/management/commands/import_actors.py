import csv
from datetime import datetime
from django.core.management.base import BaseCommand, CommandParser
from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser):
         parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo com atores',
        )


    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birth_date = datetime.strptime(row['birth_date'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(
                    name=name,
                    birth_date=birth_date,
                    nationality=nationality,
                )
        self.stdout.write(self.style.SUCCESS('Base de dados de Atores implementada com sucesso!'))