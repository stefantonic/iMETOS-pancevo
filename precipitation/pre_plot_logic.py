import pandas as pd
import plotly.express as px

# Step 1: Load the data from the CSV file
file_path = '/home/stefan/Desktop/atlas-klime-pa/precipitation/precipitation.csv'
df = pd.read_csv(file_path)

# Convert 'Date/Time' to datetime if it's not already
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Step 2: Filter and calculate the frequency of sum values greater than 1
df_filtered = df[df['sum'] > 1]  # Include only rows where 'sum' > 1

# Calculate frequency of 'sum' values
frequency_df = df_filtered.groupby(['Date/Time', 'sum']).size().reset_index(name='count')

# Add humidity_type column
frequency_df['kolicina padavina'] = 'mm'

# Step 3: Plot the data using Plotly
fig = px.density_heatmap(
    frequency_df,
    x='Date/Time',
    y='sum',
    z='count',
    color_continuous_scale='teal',  # Change color scale to Teal
    range_color=[1, 70],  # Set the color scale range from 1 to 70
    labels={'Date/Time': 'Date/Time', 'sum': 'Sum of Humidity (%)', 'count': 'Frequency'},
    text_auto=True,  # Add text annotations
    facet_col='kolicina padavina',  # Use 'humidity_type' for facets (even if there is only one type here)
    facet_col_wrap=1  # Wrap facets into columns (one column here)
)

# Customize the layout for better appearance
fig.update_layout(
    title={
        'text': ('Ponavljanje zabelezenih vrednosti KOLICINE padavina na osnovu istih/priblizno slicnih pojava tokom cele godine(jan-dec)\n'
                 'u opsegu 0-70mm.<br> Skala kolicine padavina i njihovo merenje progresuje za +5mm za svaku godinu 2010-2024;'),
        'x': 0.5,  # Center the title horizontally
        'xanchor': 'center',  # Center align the title
        'y': 0.95,  # Move the title slightly higher (adjust as needed)
        'yanchor': 'top',  # Anchor the title at the top
        'font': {'size': 16, 'family': 'Ubuntu'}  # Set font size and family for the title
    },
    xaxis_title='Date/Time',
    yaxis_title='Kolicina padavina (mm)',
    coloraxis_colorbar_title='Frequency',
    xaxis={'tickangle': -45},  # Rotate x-axis labels for better readability
    yaxis={'title_standoff': 10},  # Add some space between the y-axis title and the axis
    coloraxis_colorbar={'title_font_size': 16},  # Set font size for the colorbar title
    font={'size': 13, 'family': 'Ubuntu'},  # Set font size and family for axis labels and tick labels
    margin={'l': 60, 'r': 20, 't': 120, 'b': 60}  # Increase top margin to provide additional space for the title
)

# Customize the y-axis scale
fig.update_yaxes(
    title='Sum of Humidity (%)',  # Set y-axis title
    range=[0, 100],  # Set y-axis range, adjust as necessary
    dtick=10,  # Set y-axis tick interval
    showgrid=True,  # Show grid lines
    zeroline=False  # Hide zero line if desired
)

# Step 4: Save the plot as a high-resolution PNG file
fig.write_image(
    '/home/stefan/Desktop/atlas-klime-pa/precipitation/test_precipitation_sum.png', 
    width=1920,  # Width of the image in pixels
    height=1080   # Height of the image in pixels
)

# Optional: Show the plot
fig.show()

