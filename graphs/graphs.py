import random
import pandas as pd

data = pd.read_csv('DataSet\Diwali Sales Data.csv', encoding= 'unicode_escape')



# Overlayed chart
def chart(occu):
   dataframe = data
   Occupation = dataframe[dataframe['Occupation'] == occu]
   chart_data= {"States": Occupation['State'].to_list(),"Zone": Occupation['Zone'].to_list(),"Product_cat": Occupation['Product_Category'].to_list(),}
   return chart_data, ["States", "Zone", "Product_cat"], {"stackgroup": "first_group"}

#Pie chart
def PieChart(states):
   dataframe = data
   States = dataframe[dataframe['State'] == states]
   Order = States.groupby('Occupation')['Orders'].sum().reset_index()
   pie_data= {"values": Order['Orders'].to_list(),"labels": Order['Occupation'].to_list()}
   return pie_data

# bar graph
def BarGraph(occu):
   dataframe = data
   bar_data = dataframe[dataframe['Occupation'] ==occu]
   bar_data = bar_data.reset_index(drop=True)
   bar_data = bar_data.groupby('Occupation')['Orders'].sum().reset_index()
   design = {"title": f'Orders {occu}',"xaxis": dict(title='Occupation'), "yaxis": dict(title='Orders'),"barmode": 'group'}
   return bar_data, design

#BubbleChart
def BubbleChart():
    Occupation_State = data.groupby(['Occupation', 'State']).agg({
        'Orders': 'sum'
    }).reset_index()
    factor = 0.0001
    size = Occupation_State['Orders'] * factor
    bubble_data = {"x": Occupation_State['Occupation'].to_list(),"y": Occupation_State['State'].to_list(),"text": Occupation_State['Occupation'].to_list(),}
    marker = {"size": size.to_list(),"color": Occupation_State['Orders'].to_list(),"colorscale": "plasma",}
    design = {"title": 'Bubble Chart: Orders by Occupation and State',"xaxis": dict(title='Occupation'),"yaxis": dict(title='State'),} 
    return bubble_data, marker, design

# TreeMap
def TreeMap():
    dataframe = data
    zone_orders = dataframe.groupby('Zone')['Orders'].sum().reset_index()
    data_zone = zone_orders.groupby('Zone')['Orders'].sum().reset_index()
    data_zone = data_zone.sort_values(by='Orders', ascending=False)
    labels = []
    parents = []
    values = []
    for index, row in data_zone.iterrows():
        zone_name = row['Zone']
        labels.append(zone_name)
        parents.append("")
        values.append(row['Orders'])
        state_orders = dataframe[dataframe['Zone'] == zone_name].groupby('State')['Orders'].sum().reset_index()
        for _, state_row in state_orders.iterrows():
            state_name = state_row['State']
            labels.append(state_name)
            parents.append(zone_name)
            values.append(state_row['Orders'])
    tree_data = {"label": labels, "parents": parents, "values": values}
    design = {"title": "Zones and States by Total Orders"}
    return tree_data, design
