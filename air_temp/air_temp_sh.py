import csv
import pyexcel as pe

# Paths
input_ods_file = '/home/stefan/Desktop/atlas-klime-pa/dataset/dataset.ods'
output_csv_file = '/home/stefan/Desktop/atlas-klime-pa/air_temp/air_temp_sh.csv'

# Load the ODS file
sheet = pe.get_sheet(file_name=input_ods_file)

# Define the range to extract
start_row = 544  # 0-based index for row 545
end_row = 5028
cols_to_extract = [0, 4, 5, 6]  # 0-based index for columns A, E, F, G

# Read header row from A2:D2
header_row = sheet.row[1]  # 0-based index for row 2
headers = [header_row[i] for i in cols_to_extract]

# Prepare to write to CSV
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Date/Time', 'avg', 'max', 'min'])

    # Iterate over rows in the specified range
    for row in sheet.row[start_row:end_row]:
        row_data = [row[col] for col in cols_to_extract]
        writer.writerow(row_data)

print(f"Data extracted and saved to {output_csv_file}")

