import django
import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'escrituracion.settings')
django.setup()
from agrupations.models import Proyect

PROYECTS = [
    ("ARBOLEDA ETP 1",  "Montería"),
    ("APP CASAS ETAPA IV",  "Cartagena"),
    ("APP II ETAPA III (117 CASAS)",  "Cartagena"),
    ("ARBOLEDA ETP 2",  "Montería"),
    ("LA PRIMAVERA 2 ET 2",  "Cartagena"),
    ("LAS ACACIAS VIS ETP I SUB ETP I",  "Cartagena"),
    ("LAS ACACIAS VIS ETP I SUB ETP III",  "Cartagena"),
    ("LAS ACACIAS VIS ETP II SUB ETP I",  "Cartagena"),
    ("MIRADOR PP ETP I",  "Cartagena"),
    ("ORO BLANCO ETAP 3",  "Cartagena"),
    ("PALO ALTO",  "Montería"),
    ("PIAMONTE ETP 1",  "Cartagena"),
    ("SAN ANGEL VIS",  "Cartagena"),
    ("SANDALO ETP  2",  "Cartagena"),
    ("SANDALO ETP 1",  "Cartagena"),
    ("VGI 2 ET VII (15) SUB ETP II",  "Cartagena"),
    ("VGI 2 ET VII (56) SUB ETP I",  "Cartagena"),
]


for index, row in df.iterrows():
    # Crea y guarda un nuevo Proyect
    proyect = Proyect(name=row(0)['name'], city_name=row(1)['city_id'])
    print(proyect["name"])