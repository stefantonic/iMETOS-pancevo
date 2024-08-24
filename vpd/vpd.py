import csv
import pyexcel as pe

# Paths
input_ods_file = '/home/stefan/Desktop/atlas-klime-pa/dataset/dataset.ods'
output_csv_file = '/home/stefan/Desktop/atlas-klime-pa/vpd/vpd.csv'

# Load the ODS file
sheet = pe.get_sheet(file_name=input_ods_file)

# Define the range to extract
start_data_row = 2  # 0-based index for row 3
end_data_row = 543
cols_for_data = [0]  # 0-based index for column A
cols_for_extra = [14, 15]  # 0-based index for columns O and P

# Read header row from A2 and O2:P2
header_row_1 = sheet.row[1]  # 0-based index for row 2 (A2)
header_row_2 = sheet.row[15]  # 0-based index for row 2 (O2:P2)
headers = ['Date/Time', 'avg', 'min']

# Prepare to write to CSV
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(headers)

    # Iterate over rows in the specified range
    for i in range(start_data_row, end_data_row):
        date_time_value = sheet.cell_value(i, cols_for_data[0])
        avg_value = sheet.cell_value(i, cols_for_extra[0])
        min_value = sheet.cell_value(i, cols_for_extra[1])
        writer.writerow([date_time_value, avg_value, min_value])

print(f"Data extracted and saved to {output_csv_file}")

