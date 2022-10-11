import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    with open(neo_csv_path) as f:
        reader = csv.DictReader(f)
        neos = []
        for line in reader:
            line['name'] = line['name'] or None
            line['diameter'] = float('nan') if line['diameter'] == '' else float(line['diameter'])
            line['pha'] = True if line['pha'] in [True, 'Y'] else False
            neo = NearEarthObject(
                designation=line['pdes'], 
                name=line['name'], 
                diameter=line['diameter'], 
                hazardous=line['pha']
            )
            neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    with open(cad_json_path) as f:
        reader = json.load(f)
        reader = [dict(zip(reader['fields'], data)) for data in reader['data']]
        approaches = []
        for line in reader:
            line['dist'] = float(line['dist']) if line['dist'] else float('nan')
            line['v_rel'] =  float(line['v_rel']) if line['v_rel'] else float('nan')
            approach = CloseApproach(
                _designation=line['des'], 
                time=line['cd'], 
                distance=line['dist'], 
                velocity=line['v_rel']
            )
            approaches.append(approach)
    return approaches
