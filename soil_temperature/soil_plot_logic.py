import pandas as pd
import plotly.express as px

# Step 1: Load the new data from the updated CSV file
file_path = '/home/stefan/Desktop/atlas-klime-pa/soil_temperature/soil_temperature.csv'
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
    color_continuous_scale='brwnyl',  # Change color scale to Sunset
    labels={'Date/Time': 'Date/Time', 'max': 'Temperature (°C)', 'count': 'Frequency'},
    text_auto=True,  # Add text annotations
    facet_col='temperature_type',  # Create separate plots for 'max' and 'min'
    facet_col_wrap=1  # Wrap facets into columns (one column here)
)

# Customize the layout for better appearance
fig.update_layout(
    title={
        'text': ('Ponavljanje zabelezenih vrednosti temperatura ZEMLJE na osnovu istih/priblizno slicnih pojava tokom cele godine (jan-dec)\n'
                 'u opsegu 0-40°C.<br> Skala temperature i njihovo merenje progresuje za +5°C(max) ili -5°C(min) za svaku godinu 2016-2019;'),
        'x': 0.5,  # Center the title horizontally
        'xanchor': 'center',  # Center align the title
        'y': 0.95,  # Move the title slightly higher (adjust as needed)
        'yanchor': 'top',  # Anchor the title at the top
        'font': {'size': 16, 'family': 'Ubuntu'}  # Set font size and family for the title
    },
    xaxis_title='',
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
    '/home/stefan/Desktop/atlas-klime-pa/soil_temperature/soil_temperature.png', 
    width=1920,  # Width of the image in pixels
    height=1080   # Height of the image in pixels
)

# Optional: Show the plot
fig.show()
