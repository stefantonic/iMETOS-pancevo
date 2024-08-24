import csv
import pyexcel as pe

# Paths
input_ods_file = '/home/stefan/Desktop/atlas-klime-pa/dataset/dataset.ods'
output_csv_file = '/home/stefan/Desktop/atlas-klime-pa/air_temp/air_temp_sh.csv'

# Load the ODS file
sheet = pe.get_sheet(file_name=input_ods_file)

# Define the range to extract (A3:D543)
start_row = 2  # 0-based index for row 3
end_row = 543
start_col = 0  # 0-based index for column A
end_col = 4    # 0-based index for column D

# Prepare to write to CSV
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write data from the specified range
    for row in sheet.row[start_row:end_row]:
        row_data = row[start_col:end_col]
        writer.writerow(row_data)

print(f"Data extracted and saved to {output_csv_file}")

