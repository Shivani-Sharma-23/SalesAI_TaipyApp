import pandas as pd
from taipy.gui import Markdown
from graphs.graphs import chart, PieChart, BarGraph, BubbleChart, TreeMap

data = pd.read_csv('DataSet\Diwali Sales Data.csv', encoding= 'unicode_escape')


def on_change_Occu(state):
    state.bar_data, state.bar_design = BarGraph(state.occu)

    state.pie_data = PieChart(state.occu)

    state.Orders = Stats(state.occu)



def Stats(occus: str):
    occupation_data = data[data['Occupation'] == occus]
    Orders = str(occupation_data['Orders'].sum())
    return Orders


occupation = data['Occupation'].unique().tolist()
state  = data['State'].unique().tolist()

occu= occupation[0]
states = state[0]

Orders = Stats(occu)

bar_data, bar_design = BarGraph(occu)
overlay_data, y_labels, options = chart(occu)
pie_data = PieChart(states)
bubble_data, bubble_marker, bubble_design = BubbleChart()
tree_data =TreeMap()

dashboard_ui = Markdown("pages/dashboard/dashboard_ui.md")