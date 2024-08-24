import csv
import pyexcel as pe

# Paths
input_ods_file = '/home/stefan/Desktop/atlas-klime-pa/dataset/dataset.ods'
output_csv_file = '/home/stefan/Desktop/atlas-klime-pa/precipitation/precipitation.csv'

# Load the ODS file
sheet = pe.get_sheet(file_name=input_ods_file)

# Define the range to extract
start_data_row = 2  # 0-based index for row 3
end_data_row = 5027  # 0-based index for row 5028
col_for_date_time = 0  # 0-based index for column A
col_for_sum = 22       # 0-based index for column W

# Read header row from A2 and W2
header_date_time = sheet.cell_value(1, col_for_date_time)  # Value at A2
header_sum = sheet.cell_value(1, col_for_sum)              # Value at W2

# Prepare to write to CSV
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Date/Time', 'sum'])

    # Iterate over rows in the specified range
    for i in range(start_data_row, end_data_row + 1):
        date_time_value = sheet.cell_value(i, col_for_date_time)
        sum_value = sheet.cell_value(i, col_for_sum)
        writer.writerow([date_time_value, sum_value])

print(f"Data extracted and saved to {output_csv_file}")

