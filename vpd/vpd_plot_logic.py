import pandas as pd
import plotly.express as px

# Step 1: Load the data from the CSV file
file_path = '/home/stefan/Desktop/atlas-klime-pa/vpd/vpd.csv'
df = pd.read_csv(file_path)

# Convert 'Date/Time' to datetime if it's not already
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Step 2: Filter and calculate the frequency of average temperatures

# For avg temperatures above 0
df_avg_above_0 = df[df['avg'] > 0]
frequency_avg_df = df_avg_above_0.groupby(['Date/Time', 'avg']).size().reset_index(name='count')
frequency_avg_df['VPD(kPa)'] = 'prosek'

# For avg temperatures below 0
df_avg_below_0 = df[df['avg'] < 0]
frequency_avg_below_df = df_avg_below_0.groupby(['Date/Time', 'avg']).size().reset_index(name='count')
frequency_avg_below_df.rename(columns={'avg': 'temperature'}, inplace=True)  # Rename 'avg' to 'temperature' for merging
frequency_avg_below_df['VPD(kPa)'] = 'prosek'

# Combine the dataframes for both avg temperatures
combined_df = pd.concat([frequency_avg_df, frequency_avg_below_df])

# Step 3: Plot the data using Plotly
fig = px.density_heatmap(
    combined_df,
    x='Date/Time',
    y='avg',  # Use 'avg' for y-axis
    z='count',
    color_continuous_scale='teal',  # Change color scale to Plasma
    labels={'Date/Time': 'Date/Time', 'avg': 'VPD(kPa)', 'count': 'Frequency'},
    text_auto=True,  # Add text annotations
    facet_col='VPD(kPa)',  # Create separate plots for 'avg_above_0' and 'avg_below_0'
    facet_col_wrap=1  # Wrap facets into columns (one column here)
)

# Customize the layout for better appearance
fig.update_layout(
    title={
        'text': ('Ponavljanje zabelezenih vrednosti PROSEKA VPD-a na osnovu istih/priblizno slicnih pojava tokom cele godine(jan-dec)\n'
                 'u rasponu od 0-3.5kPa.<br> Skala vodenog pritiska pare(VPD) i njihovo merenje progresuje za +0.5(kPa) za 2023-2024god;'),
        'x': 0.5,  # Center the title horizontally
        'xanchor': 'center',  # Center align the title
        'y': 0.95,  # Move the title slightly higher (adjust as needed)
        'yanchor': 'top',  # Anchor the title at the top
        'font': {'size': 16, 'family': 'Ubuntu'}  # Set font size and family for the title
    },
    xaxis_title='',
    yaxis_title='Vodeni pritisak pare - VPD(kPa)',
    coloraxis_colorbar_title='Frequency',
    xaxis={'tickangle': -45},  # Rotate x-axis labels for better readability
    yaxis={'title_standoff': 10},  # Add some space between the y-axis title and the axis (default value)
    coloraxis_colorbar={'title_font_size': 16},  # Set font size for the colorbar title
    font={'size': 13, 'family': 'Ubuntu'},  # Set font size and family for axis labels and tick labels
    margin={'l': 60, 'r': 20, 't': 120, 'b': 60}  # Increase top margin to provide additional space for the title
)

# Step 4: Save the plot as a high-resolution PNG file
fig.write_image(
    '/home/stefan/Desktop/atlas-klime-pa/vpd/test_comparison_avg.png', 
    width=1920,  # Width of the image in pixels
    height=1080   # Height of the image in pixels
)

# Optional: Show the plot
fig.show()

# Calculate and output occurrences to a file
frequency_avg_above_0_count = df_avg_above_0.shape[0]  # Number of occurrences for avg > 0
frequency_avg_below_0_count = df_avg_below_0.shape[0]  # Number of occurrences for avg < 0

# Summarize the frequencies in a grid-like system
summary_df = pd.DataFrame({
    'Temperature Type': ['Avg Above 0°C', 'Avg Below 0°C'],
    'Total Count': [frequency_avg_above_0_count, frequency_avg_below_0_count]
})

# Save summary to a CSV file (optional)
summary_df.to_csv('/home/stefan/Desktop/atlas-klime-pa/vpd/summary_avg_temperatures.csv', index=False)
