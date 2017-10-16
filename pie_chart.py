import sys
sys.path.insert(0, '/anaconda/lib/python3.6/site-packages')

import pandas as pd #dataframe package
import numpy as np #Python number processor
import matplotlib.pyplot as plt # for plotting
import seaborn as sns # for plotting and styling
df = pd.read_csv('fake_database.csv')
import matplotlib.pyplot as plt

#pie chart
def pie_chart():
    
    group_by_name = df.groupby(['User Name']).sum().loc["Ayo"]
    
    #expense category and amount per person
    category = group_by_name.index.tolist()
    amount = group_by_name.tolist()
    
    #make pie chart
    labels = category
    sizes = amount
    explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) 

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
    
