from csv import DictReader
import json
import pprint as pp
import sys
import argparse
import logging
import zipfile
import csv

log = logging.getLogger('onboarder')



def extract_esx_data(input_file, output_file):
    project = {}
    access_points = {}
    try:
        with zipfile.ZipFile(input_file, "r") as z:
            if "project.json" in z.namelist():
                with z.open("project.json") as f:
                   data = f.read()
                   project = json.loads(data.decode("utf-8"))
            if "accessPoints.json" in z.namelist():
                print("found accessPoints.json")
                with z.open("accessPoints.json") as f:
                   data = f.read()
                   access_points = json.loads(data.decode("utf-8"))
    except Exception as e:
       print(e)
    return project, access_points

def parse_arguments() -> dict:
    """
    Parses the CLI arguments and returns a dictionary containing the data.
    :return dict: Dictionary containing the CLI arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile',
                        type=str,
                        required=True,
                        help=".ESX File")
    parser.add_argument('-o', '--outputfile',
                        type=str,
                        required=True,
                        help="CSV Output File")
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    config = parse_arguments()
    print(config)
    log.info("Starting extraction...")
    try:
        project, access_points = extract_esx_data(config.inputfile, config.outputfile)
    except:
        print("Failed to extract project.json ZIP file")
        raise

    output_data = []
    for ap in access_points['accessPoints']:
        output = {"Vendor AP Name": ap['name'], "AP MAC Address": ""}
        output_data.append(output)
    fieldnames = ["Vendor AP Name", "AP MAC Address"]
    print(f'Writing CSV file {config.outputfile}')
    with open(config.outputfile, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in output_data:
            writer.writerow(entry)




    #main(sys.argv[1:])
