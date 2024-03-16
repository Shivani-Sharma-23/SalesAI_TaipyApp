import random
import pandas as pd

data = pd.read_csv('DataSet\Diwali Sales Data.csv', encoding= 'latin1')


# Overlayed chart
def chart(occu):
   Occupation = data[data['Occupation'] == occu]
   chart_data= {"States": Occupation['State'].to_list(),"Zone": Occupation['Zone'].to_list(),"Product_cat": Occupation['Product_Category'].to_list(),}
   return chart_data, ["States", "Zone", "Product_cat"], {"stackgroup": "first_group"}

#Pie chart
def PieChart(states):
   States = data[data['State'] == states]
   Order = States.groupby('Occupation')['Orders'].sum().reset_index()
   pie_data= {"values": Order['Orders'].to_list(),"labels": Order['Occupation'].to_list()}
   return pie_data

# bar graph
def BarGraph():
   grouped_data = data.groupby('Occupation', as_index=False).agg({
       'Orders': 'sum'
   })

   layout = {
       "title": 'Total Orders per Occupation',
       "xaxis": dict(title='Occupation'),
       "yaxis": dict(title='Orders'),
       "barmode": 'group'
   }
   return grouped_data, layout

#BubbleChart
def BubbleChart():
    # Grouping data by Age and calculating total Orders and Amount for each Age group
    Age_Group = data.groupby('Age').agg({
        'Orders': 'sum',
        'Amount': 'sum'
    }).reset_index()
    
    # Prepare data for the bubble chart
    bubble_data = {
        "x": Age_Group['Age'],  # X-axis: Age
        "y": Age_Group['Amount'],  # Y-axis: Amount
        "text": Age_Group['Age'],  # Text for hover-over
    }
    
    # Bubble size representing the number of Orders
    size = Age_Group['Orders']
    
    # Marker settings for the bubble chart
    marker = {
        "size": size,  # Bubble size
        "color": Age_Group['Orders'],  # Color based on number of Orders
        "colorscale": "plasma",  # Color scale
    }
    
    # Design settings for the bubble chart
    design = {
        "title": 'Bubble Chart: Sales by Age',
        "xaxis": {"title": 'Age'},  # X-axis label
        "yaxis": {"title": 'Amount'},  # Y-axis label
    }
    
    return bubble_data, marker, design

# TreeMap
def TreeMap():
    zone_orders = data.groupby('Zone')['Orders'].sum().reset_index()
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
        state_orders = data[data['Zone'] == zone_name].groupby('State')['Orders'].sum().reset_index()
        for _, state_row in state_orders.iterrows():
            state_name = state_row['State']
            labels.append(state_name)
            parents.append(zone_name)
            values.append(state_row['Orders'])
    tree_data = {"label": labels, "parents": parents, "values": values}
    design = {"title": "Zones and States by Total Orders"}
    return tree_data, design
