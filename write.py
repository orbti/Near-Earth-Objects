import csv
import json


def write_to_csv(results, filename):
    """ Write query to a csv file after serializtion."""

    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()
        for elem in results:
            approache = elem.serialize()
            neo = approache['neo'].serialize()
            merge = approache | neo
            del merge['neo']
            writer.writerow(merge)


def write_to_json(results, filename):
    """ Write query to a json file after serializtion."""

    approaches = []
    for elem in results:
        approache = elem.serialize()
        approache['neo'] = approache['neo'].serialize()
        approaches.append(approache)
    with open(filename, 'w') as f:
        json.dump(approaches, f, indent=2)
