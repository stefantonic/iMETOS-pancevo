import csv
import pyexcel as pe

# Paths
input_ods_file = '/home/stefan/Desktop/atlas-klime-pa/dataset/dataset.ods'
output_csv_file = '/home/stefan/Desktop/atlas-klime-pa/relative_humidity/humidity_sh.csv'

# Load the ODS file
sheet = pe.get_sheet(file_name=input_ods_file)

# Define the range to extract
start_data_row = 544  # 0-based index for row 545
end_data_row = 5027   # 0-based index for row 5028
col_for_date_time = 0  # 0-based index for column A
col_for_avg = 19       # 0-based index for column T

# Read header row from A2 and T2
header_date_time = sheet.cell_value(1, col_for_date_time)  # Value at A2
header_avg = sheet.cell_value(1, col_for_avg)              # Value at T2

# Prepare to write to CSV
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Date/Time', 'avg'])

    # Iterate over rows in the specified range
    for i in range(start_data_row, end_data_row + 1):
        date_time_value = sheet.cell_value(i, col_for_date_time)
        avg_value = sheet.cell_value(i, col_for_avg)
        writer.writerow([date_time_value, avg_value])

print(f"Data extracted and saved to {output_csv_file}")

