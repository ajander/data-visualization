import os
import pandas as pd
import seaborn as sns

# Set working directory to this script's location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

data = pd.read_csv('formatted_data.csv')
data = data[data.Table == 'Total Number of Searches']

sns.set_theme(style='whitegrid')

# Draw a nested barplot by year and category
g = sns.catplot(
    data=data, kind="bar",
    x="Year", y="Value", hue="Category",
    palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("Year", "Number")
g.legend.set_title("Title")