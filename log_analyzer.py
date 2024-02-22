"""
Script to analyze JSON text from three log files located in subdirectories with indexes 1, 3, and 5.
Extracts relevant data from JSON and writes it to CSV files in the script's directory.
"""

import json
import csv

options = ["1", "3", "5"]

for option in options:
    file_path =f'exit_max_pred_delay_0_{option}'
    file_name =  f'exit_max_pred_delay_0_{option}'
    file_extension = "txt"
    csv_column_names = ["Camera ID", "Timestamp", "Plate Height", "Plate Width", "Plate Read", "Score", "Dscore"]
    csv_file_path = f'{file_name}.csv'

    with open(f'{file_path}/{file_name}.{file_extension}', 'r') as f, open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_column_names)

        for line in f.readlines():
            try:
                json_object = json.loads(line)
                json_line = json_object['data']
                camera_id = json_line['camera_id']
                timestamp = json_line['timestamp']
                results = json_line['results'][0]
                box = results['box']
                height = int(box['xmin']) + int(box['xmax'])
                width = int(box['ymin']) + int(box['ymax'])
                plate = results['plate']
                score = results['score']
                dscore = results['dscore']
                csv_writer.writerow([camera_id, timestamp, height, width, plate, score, dscore])

            except ValueError:
                print("not json line")