import csv
from datetime import datetime, date
from tqdm import tqdm

from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from formularios.models import Necesidad
from base.models import Comuna, Contacto, Lugar, Persona, Participante


def iterate_csv(filepath):
    with open(filepath, 'r') as f:
        rows = csv.DictReader(f, delimiter='\t')
        for row in rows:
            yield row


def valid_phonenumber(number):
    return all(iter([
        number.isdigit(),
        len(number) == 11
    ]))


def datetime_from_date_str(date_str):
    date_format = '%m/%d/%Y'
    return datetime.strptime(date_str, date_format)


def resolve_comuna(comuna_name):
    if not comuna_name:
        print('Comuna ingresada inválida')
        return None
    comunas = Comuna.objects.filter(nombre=comuna_name)
    if len(comunas) == 1:
        return comunas[0]
    final_chars = 4 if len(comuna_name) >= 4 else len(comuna_name)
    comunas = Comuna.objects.filter(
        nombre__endswith=comuna_name[-final_chars:]
    )
    if len(comunas) == 0:
        print('Comuna ingresada inválida')
        return None

    print(f'Emparejando {comuna_name} con...')
    for index, comuna in enumerate(comunas, start=1):
        print(f'{index} - {comuna.nombre}')
    user_input = None
    while user_input is None:
        try:
            user_input = int(input(
                'Selecciona la comuna correspondiente ingresando su número'
            ))
        except (ValueError, TypeError):
            print('Número ingresado inválido')
            user_input = None
        if user_input is not None and user_input > len(comunas):
            print('Número ingresado inválido')
            user_input = None

    return comunas[user_input-1]


def insert_necesidades(filepath):
    for row in tqdm(iterate_csv(filepath)):
        comuna = resolve_comuna(row['comuna'].lower())
        if comuna is None:
            continue
        lugar = Lugar(
            localidad=row.get('localidad', ''),
            comuna=comuna
        )
        lugar.save()
        remitente = Persona(
            nombre=row.get('nombre', ''),
            apellido=row.get('apellido', ''),
            lugar=lugar
        )
        remitente.save()
        participante = Participante(
            persona = remitente,
            activo=True
        )
        participante.save()
        correo = row.get('correo', '')
        if correo:
            correo_contacto = Contacto(
                tipo_contacto=Contacto.TipoContacto.EMAIL,
                contenido=correo,
                persona=remitente
            )
            correo_contacto.save()
        telefono = row.get('telefono', '')
        if telefono and valid_phonenumber(telefono):
            tipo_telefono = Contacto.TipoContacto.TELEFONO_MOVIL
            if telefono.startswith('562'):
                tipo_telefono = Contacto.TipoContacto.TELEFONO_FIJO
            telefono_contacto = Contacto(
                tipo_contacto=Contacto.TipoContacto.TELEFONO_MOVIL,
                contenido=telefono,
                persona=remitente
            )
            telefono_contacto.save()
        for index in range(1, 3):
            tipo_red = row.get(f'tipo_red{index}', '')
            contenido = row.get(f'red{index}', '')
            if tipo_red and contenido:
                tipo_contacto = Contacto.TipoContacto[tipo_red.upper()]
                aux_contacto = Contacto(
                    tipo_contacto=tipo_contacto,
                    contenido=contenido,
                    persona=remitente
                )
                aux_contacto.save()
        fecha = row.get('fecha')
        if not fecha:
            fecha_insercion = datetime.now()
        else:
            fecha_insercion = datetime_from_date_str(fecha)
        necesidad = Necesidad(
            fecha_insercion=make_aware(fecha_insercion),
            remitente=participante,
            lugar=lugar,
            periodicidad=row.get('periodicidad', ''),
            descripcion=row.get('descripcion', '')
        )
        necesidad.save()


class Command(BaseCommand):
    help = 'Loads a CSV coming from Wix'

    def add_arguments(self, parser):
        parser.add_argument('FILEPATH', type=str)

    def handle(self, *args, **kwargs):
        FILEPATH = kwargs.get('FILEPATH')
        return insert_necesidades(FILEPATH)
