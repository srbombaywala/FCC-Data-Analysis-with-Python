import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter('Year','CSIRO Adjusted Sea Level',data=df)
    # plt.xlim(1880,2050)
    # plt.ylim(-2,14)
        # Create first line of best fit
    first_line = linregress(df.Year,df['CSIRO Adjusted Sea Level'])
    x_line = np.arange(df['Year'].min(),2051,1)
    first_line_plot = first_line.slope*x_line + first_line.intercept
    plt.plot(x_line, first_line_plot)
        # Create second line of best fit
    df_second = df[df['Year']>=2000]
    # df_second.head()
    second_line = linregress(df_second.Year, df_second['CSIRO Adjusted Sea Level'])
    xs_line = np.arange(df_second['Year'].min(),2051,1)
    second_line_plot = second_line.slope*xs_line + second_line.intercept
    plt.plot(xs_line, second_line_plot)

        # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel("Year")
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()