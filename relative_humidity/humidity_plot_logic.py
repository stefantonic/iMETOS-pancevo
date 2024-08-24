import pandas as pd
import plotly.express as px

# Step 1: Load the data from the new CSV file
file_path = '/home/stefan/Desktop/atlas-klime-pa/relative_humidity/humidity_sh.csv'
df = pd.read_csv(file_path)

# Convert 'Date/Time' to datetime if it's not already
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Step 2: Filter and calculate the frequency of average humidity values

# For average humidity above 0
df_above_0 = df[df['avg'] > 0]
frequency_above_df = df_above_0.groupby(['Date/Time', 'avg']).size().reset_index(name='count')
frequency_above_df['humidity_type'] = '%'

# For average humidity below or equal to 0
df_below_or_equal_0 = df[df['avg'] <= 0]
frequency_below_df = df_below_or_equal_0.groupby(['Date/Time', 'avg']).size().reset_index(name='count')
frequency_below_df.rename(columns={'avg': 'humidity'}, inplace=True)  # Rename 'avg' to 'humidity' for merging
frequency_below_df['Prosecna relativna vlaznost vazduha'] = '%'

# Combine the dataframes for both conditions
combined_df = pd.concat([frequency_above_df, frequency_below_df])

# Step 3: Plot the data using Plotly
fig = px.density_heatmap(
    combined_df,
    x='Date/Time',
    y='avg',
    z='count',
    color_continuous_scale='teal',  # Change color scale to Plasma
    labels={'Date/Time': 'Date/Time', 'avg': 'Average Humidity (%)', 'count': 'Frequency'},
    text_auto=True,  # Add text annotations
    facet_col='humidity_type',  # Create separate plots for 'above_0' and 'below_or_equal_0'
    facet_col_wrap=1  # Wrap facets into columns (one column here)
)

# Customize the layout for better appearance
fig.update_layout(
    title={
        'text': ('Ponavljanje zabelezenih vrednosti PROSEKA vlažnosti vazduha na osnovu istih/priblizno slicnih pojava tokom cele godine(jan-dec)\n'
                 'u opsegu 0-100%.<br> Skala prosecne vlažnosti vazduha i njihovo merenje progresuje za 10% za svaku godinu 2010-2024;'),
        'x': 0.5,  # Center the title horizontally
        'xanchor': 'center',  # Center align the title
        'y': 0.95,  # Move the title slightly higher (adjust as needed)
        'yanchor': 'top',  # Anchor the title at the top
        'font': {'size': 16, 'family': 'Ubuntu'}  # Set font size and family for the title
    },
    xaxis_title='Date/Time',
    yaxis_title='Prosecna relativna vlaznost vazduha (%)',
    coloraxis_colorbar_title='Frequency',
    xaxis={'tickangle': -45},  # Rotate x-axis labels for better readability
    yaxis={'title_standoff': 10},  # Add some space between the y-axis title and the axis (default value)
    coloraxis_colorbar={'title_font_size': 16},  # Set font size for the colorbar title
    font={'size': 13, 'family': 'Ubuntu'},  # Set font size and family for axis labels and tick labels
    margin={'l': 60, 'r': 20, 't': 120, 'b': 60}  # Increase top margin to provide additional space for the title
)

# Step 4: Save the plot as a high-resolution PNG file
fig.write_image(
    '/home/stefan/Desktop/atlas-klime-pa/relative_humidity/test_comparison_humidity.png', 
    width=1920,  # Width of the image in pixels
    height=1080   # Height of the image in pixels
)

# Optional: Show the plot
fig.show()
