import json

from django.core.management.base import BaseCommand
from tqdm import tqdm

from base.models import Comuna, Region, Provincia


def insert_rpc(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        comunas_json = json.load(f)

    headers = comunas_json[0]
    for row in tqdm(comunas_json[1:]):
        region, _ = Region.objects.get_or_create(
            nombre=row[headers.index('nombre_region')].lower(),
            codigo=int(row[headers.index('cut_region')])
        )
        provincia, _ = Provincia.objects.get_or_create(
            nombre=row[headers.index('nombre_provincia')].lower(),
            codigo=int(row[headers.index('cut_provincia')]),
            defaults={
                'region': region
            }
        )
        comuna, _ = Comuna.objects.get_or_create(
            nombre=row[headers.index('nombre_comuna')].lower(),
            codigo=int(row[headers.index('cut_comuna')]),
            defaults={
                'provincia': provincia
            }
        )


class Command(BaseCommand):
    help = 'Loads a JSON file with regiones, provincias y comunas'

    def add_arguments(self, parser):
        parser.add_argument('FILEPATH', type=str)

    def handle(self, *args, **kwargs):
        FILEPATH = kwargs.get('FILEPATH')
        return insert_rpc(FILEPATH)
