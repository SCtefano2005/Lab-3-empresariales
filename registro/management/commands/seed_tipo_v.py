# registro/management/commands/seed_tipo_v.py

from django.core.management.base import BaseCommand
from registro.models import Tipo_V

class Command(BaseCommand):
    help = 'Seed the Tipo_V model with initial data'

    def handle(self, *args, **kwargs):
        tipos = ['Sedán', 'SUV', 'Hatchback', 'Camioneta']

        for tipo in tipos:
            obj, created = Tipo_V.objects.get_or_create(tipo=tipo)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {tipo}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Already exists: {tipo}'))
