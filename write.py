import csv
import json


def write_to_csv(results, filename):
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()
        for elem in results:
            ca = elem.serialize()
            neo = ca['neo'].serialize()
            merge = ca | neo
            del merge['neo']
            writer.writerow(merge)

def write_to_json(results, filename):
    l = []
    for elem in results:
            ca = elem.serialize()
            ca['neo'] = ca['neo'].serialize()
            l.append(ca)
    with open(filename, 'w') as f:
        json.dump(l, f, indent=2)