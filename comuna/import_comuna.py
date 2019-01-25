import os
from django.contrib.gis.utils import LayerMapping

from .models import *

comuna_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../division_comunal/division_comunal.shp'))

comuna_mapping = {
    'nom_reg': 'NOM_REG',
    'nom_prov': 'NOM_PROV',
    'nom_com': 'NOM_COM',
    'shape_leng': 'SHAPE_LENG',
    'dis_elec': 'DIS_ELEC',
    'cir_sena': 'CIR_SENA',
    'cod_comuna': 'COD_COMUNA',
    'shape_le_1': 'SHAPE_Le_1',
    'shape_area': 'SHAPE_Area',
    'geom': 'MULTIPOLYGON',
}


def run(verbose = True):
    lm = LayerMapping(Comuna, comuna_shp, comuna_mapping, transform=True)
    lm.save(strict=True, verbose=verbose)


