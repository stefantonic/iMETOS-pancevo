import pandas as pd
import plotly.express as px

# Step 1: Load the data from the CSV file
file_path = '/home/stefan/Desktop/atlas-klime-pa/air_temp/combined.csv'
df = pd.read_csv(file_path)

# Convert 'Date/Time' to datetime if it's not already
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Step 2: Filter and calculate the frequency of temperatures

# For max temperatures above 0
df_max_above_0 = df[df['max'] > 0]
frequency_max_df = df_max_above_0.groupby(['Date/Time', 'max']).size().reset_index(name='count')
frequency_max_df['temperature_type'] = 'max'

# For min temperatures below 0
df_min_below_0 = df[df['min'] < 0]
frequency_min_df = df_min_below_0.groupby(['Date/Time', 'min']).size().reset_index(name='count')
frequency_min_df.rename(columns={'min': 'max'}, inplace=True)  # Rename 'min' to 'max' for merging
frequency_min_df['temperature_type'] = 'min'

# Combine the dataframes for both max and min temperatures
combined_df = pd.concat([frequency_max_df, frequency_min_df])

# Step 3: Plot the data using Plotly
fig = px.density_heatmap(
    combined_df,
    x='Date/Time',
    y='max',
    z='count',
    color_continuous_scale='sunset',  # Change color scale to Turbo
    labels={'Date/Time': 'Date/Time', 'max': 'Temperature (°C)', 'count': 'Frequency'},
    text_auto=True,  # Add text annotations
    facet_col='temperature_type',  # Create separate plots for 'max' and 'min'
    facet_col_wrap=1  # Wrap facets into columns (one column here)
)

# Customize the layout for better appearance
fig.update_layout(
    title={
        'text': ('Ponavljanje zabelezenih vrednosti temperatura na osnovu istih/priblizno slicnih pojava tokom cele godine (jan-dec)\n'
                 'u opsegu 0-40°C.<br> Skala temperature i njihovo merenje progresuje za +5°C(max) ili -5°C(min) za svaku godinu 2010-2024;'),
        'x': 0.5,  # Center the title horizontally
        'xanchor': 'center',  # Center align the title
        'y': 0.95,  # Move the title slightly higher (adjust as needed)
        'yanchor': 'top',  # Anchor the title at the top
        'font': {'size': 16, 'family': 'Ubuntu'}  # Set font size and family for the title
    },
    xaxis_title='Date/Time',
    yaxis_title='Temperature (°C)',
    coloraxis_colorbar_title='Frequency',
    xaxis={'tickangle': -45},  # Rotate x-axis labels for better readability
    yaxis={'title_standoff': 10},  # Add some space between the y-axis title and the axis (default value)
    coloraxis_colorbar={'title_font_size': 16},  # Set font size for the colorbar title
    font={'size': 13, 'family': 'Ubuntu'},  # Set font size and family for axis labels and tick labels
    margin={'l': 60, 'r': 20, 't': 120, 'b': 60}  # Increase top margin to provide additional space for the title
)

# Step 4: Save the plot as a high-resolution PNG file
fig.write_image(
    '/home/stefan/Desktop/atlas-klime-pa/air_temp/test_comparison.png', 
    width=1920,  # Width of the image in pixels
    height=1080   # Height of the image in pixels
)

# Optional: Show the plot
fig.show()

# Calculate and output occurrences to a file
frequency_max_count = df_max_above_0.shape[0]  # Number of occurrences for max > 0
frequency_min_count = df_min_below_0.shape[0]  # Number of occurrences for min < 0

# Summarize the frequencies in a grid-like system
summary_df = pd.DataFrame({
    'Temperature Type': ['Max Above 0°C', 'Min Below 0°C'],
    'Total Count': [frequency_max_count, frequency_min_count]
})

# Save the summary to a text file
with open('/home/stefan/Desktop/atlas-klime-pa/air_temp/zero.txt', 'w') as f:
    f.write("Summary of frequencies:\n")
    for index, row in summary_df.iterrows():
        f.write(f"{row['Temperature Type']}: {row['Total Count']}\n")

    # Step 5: Calculate yearly sum of frequencies and their differences
    df['Year'] = df['Date/Time'].dt.year

    # For max temperatures above 0
    yearly_max_freq = frequency_max_df.groupby(frequency_max_df['Date/Time'].dt.year)['count'].sum().reset_index(name='total_count')
    yearly_max_freq = yearly_max_freq.sort_values(by='Date/Time')
    
    # For min temperatures below 0
    yearly_min_freq = frequency_min_df.groupby(frequency_min_df['Date/Time'].dt.year)['count'].sum().reset_index(name='total_count')
    yearly_min_freq = yearly_min_freq.sort_values(by='Date/Time')
    
    # Calculate differences
    yearly_max_freq['difference'] = yearly_max_freq['total_count'].diff().abs()
    yearly_min_freq['difference'] = yearly_min_freq['total_count'].diff().abs()

    # Output results for each year
    f.write("\nYearly Frequencies and Absolute Differences:\n")
    
    f.write("\nMax Temperatures Above 0°C:\n")
    for index, row in yearly_max_freq.iterrows():
        year = row['Date/Time']
        total_count = row['total_count']
        diff = row['difference'] if pd.notna(row['difference']) else 'N/A'
        f.write(f"Year: {year}, Total Count: {total_count}, Absolute Difference: {diff}\n")
    
    f.write("\nMin Temperatures Below 0°C:\n")
    for index, row in yearly_min_freq.iterrows():
        year = row['Date/Time']
        total_count = row['total_count']
        diff = row['difference'] if pd.notna(row['difference']) else 'N/A'
        f.write(f"Year: {year}, Total Count: {total_count}, Absolute Difference: {diff}\n")

    # Step 6: Sort and display frequencies for 2010 from lowest to highest
    df_2010 = df[df['Date/Time'].dt.year == 2010]
    
    # For max temperatures above 0 in 2010
    freq_2010_max = df_2010[df_2010['max'] > 0].groupby('max').size().reset_index(name='count').sort_values(by='count')
    
    # For min temperatures below 0 in 2010
    freq_2010_min = df_2010[df_2010['min'] < 0].groupby('min').size().reset_index(name='count').rename(columns={'min': 'max'}).sort_values(by='count')

    # Output sorted results for 2010
    f.write("\nFrequencies for 2010 (Sorted from Lowest to Highest):\n")
    
    f.write("\nMax Temperatures Above 0°C:\n")
    for index, row in freq_2010_max.iterrows():
        f.write(f"Temperature: {row['max']}, Count: {row['count']}\n")
    
    f.write("\nMin Temperatures Below 0°C:\n")
    for index, row in freq_2010_min.iterrows():
        f.write(f"Temperature: {row['max']}, Count: {row['count']}\n")
    
    # Save temperatures that occurred more than once
    f.write("\nMax Temperatures Above 0°C that occurred more than once:\n")
    max_temp_above_0 = frequency_max_df[frequency_max_df['count'] > 1]
    for index, row in max_temp_above_0.iterrows():
        f.write(f"Temperature: {row['max']}, Count: {row['count']}\n")
    
    f.write("\nMin Temperatures Below 0°C that occurred more than once:\n")
    min_temp_below_0 = frequency_min_df[frequency_min_df['count'] > 1]
    for index, row in min_temp_below_0.iterrows():
        f.write(f"Temperature: {row['max']}, Count: {row['count']}\n")
    
    # Overall temperature ranges (not including counts but showing min and max)
    f.write("\nOverall Temperature Ranges:\n")
    f.write(f"Max temperatures above 0°C - Lowest: {df_max_above_0['max'].min()}, Highest: {df_max_above_0['max'].max()}\n")
    f.write(f"Min temperatures below 0°C - Lowest: {df_min_below_0['max'].min()}, Highest: {df_min_below_0['max'].max()}\n")

