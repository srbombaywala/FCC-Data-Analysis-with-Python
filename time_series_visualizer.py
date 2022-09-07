import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date']) # read the file and parse the date
df["index"] = df.date # set the index to date

# Clean data
df = df[(df["value"]>df["value"].quantile(0.025)) & (df["value"]<df["value"].quantile(.975))] # only consider the data with value > top 2.5% and less than 97.5%


def draw_line_plot():
    # Draw line plot
    df_line = pd.DataFrame.copy(df)
    fig, ax = plt.subplots(figsize=(7,7))
    plt.plot(df_line['date'],df_line['value'], color="red")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    # plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
        # Copy and modify data for monthly bar plot
    df_bar = pd.DataFrame.copy(df) #make a copy (Deep Copy) of the dataFrame

    # Draw bar plot
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] #Names of the month
    df_bar["Years"] = df_bar['index'].dt.year # add a column indicating years
    df_bar['Months'] = df_bar['index'].dt.month # add a column indicating months
    df_bar['Months'] = df_bar['Months'].apply(lambda data:months[data-1]) # names of the months according to the values. python starts from 0 index thats why -1
    df_bar = pd.DataFrame(df_bar.groupby(['Years','Months'],sort=False)['value'].mean()) # find the mean of the values by grouping year wise monthwise
    df_bar = df_bar.rename(columns={'value':'Average Page Views'}) # rename the column named values (as per the output figure)
    df_bar = df_bar.reset_index() # reset the index
    # df_bar
    fig, ax = plt.subplots(figsize=(7,7))
    sns.barplot(x = 'Years', y = 'Average Page Views', hue = 'Months', data = df_bar, palette = 'tab10', hue_order=months)
    plt.legend(loc='upper left', title="Months")
    plt.xticks(rotation=90, horizontalalignment='center')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_box = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    fig,axes = plt.subplots(1,2, figsize=(15,5))
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    # Draw box plots (using Seaborn)
    df_box = df_box.rename(columns={'value':'Page Views'})
    sns.boxplot(data=df_box, x='Year', y='Page Views', ax = axes[0])
    axes[0].set_yticks([0,20000,40000,60000,80000,100000,120000,140000,160000,180000,200000])
    sns.boxplot(data=df_box, x='Month', y='Page Views', ax = axes[1], order=month_box)
    axes[1].set_yticks([0,20000,40000,60000,80000,100000,120000,140000,160000,180000,200000])
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
