from django.core.management.base import BaseCommand
from apps.management.models import Task

class Command(BaseCommand):
    help = 'Crea objetos si no existen en la base de datos'

    def handle(self, *args, **kwargs):
        tasks = Task.objects.all()
        for t in tasks:
            print(t)
        # objetos_a_crear = [
        #     {'field1': 'valor1', 'field2': 'valor2'},
        #     {'field1': 'valor3', 'field2': 'valor4'},
        # ]

        # for obj_data in objetos_a_crear:
        #     obj, created = TuModelo.objects.get_or_create(**obj_data)
        #     if created:
        #         self.stdout.write(self.style.SUCCESS(f'Objeto creado: {obj}'))
        #     else:
        #         self.stdout.write(self.style.WARNING(f'Objeto ya existe: {obj}'))
