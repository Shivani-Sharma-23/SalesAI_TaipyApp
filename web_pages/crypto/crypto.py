import pandas as pd
from taipy.gui import Gui, notify
import numpy as np
df = pd.read_csv("C:\\Users\\shiva\\Documents\\Python_Mini _project\\SalesAI_TaipyApp\\web_pages\\crypto\\dataset\\Cryptocurrency_Dataset_2023.csv")

df["Price (Intraday)"] = df["Price (Intraday)"].str.replace(",", "").astype(float)

df["Market Cap"] = df["Market Cap"].replace('[^\d.]', '', regex=True).astype(float)

percent_columns = ["% Change"]
for col in percent_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.dropna(inplace=True)

symbols = list(df["Symbol"].unique())
names = list(df["Name"].unique())

layout = {"margin": {"l": 220}}

symbol = []
name = []

crypto_ui = """
<|toggle|theme|>

<|25 75|layout|gap=30px|
<|sidebar|
## **Filter here**{: style="color: #D875C7"}

<|{symbol}|selector|lov={symbols}|multiple|label=Select the Symbol|dropdown|on_change=on_filter|class_name=fullwidth|>
<br/><br/>
<|{name}|selector|lov={names}|multiple|label=Select the Name|dropdown|on_change=on_filter|class_name=fullwidth|>

|>

<main_page|
# 📊 **Cryptocurrency Dashboard**{: style="color: #B7C9F2"}

<|1 1 1|layout|
<total_market_cap|
## **Total Market Cap**{: style="color: #D875C7"}
US $ <|{int(df_selection["Market Cap"].sum())}|>
|total_market_cap>

<average_price|
## **Average Price (Intraday)**{: style="color: #D875C7"}
US $ <|{round(df_selection["Price (Intraday)"].mean(), 2)}|>
|average_price>

<average_change|
## **Average Change**{: style="color: #D875C7"}
<|{round(df_selection["Change"].mean(), 2)}|>%
|average_change>
|>

<br/>

<|Crypto Table|expandable|not expanded|
<|{df_selection}|table|page_size=5|>
|>

<|Crypto Plots|expandable|not expanded|


<|Line Graph|
### **InSights**{: style="color: #ff00ff"}
<|{x_selected}|selector|lov={numeric_columns}|dropdown=True|label=Select X Axis|>
<br/>
<|{y_selected}|selector|lov={numeric_columns}|dropdown=True|label=Select Y Axis|>
<br/>
<|{df_selection}|chart|type=line|properties={properties_line_graph}|rebuild|x={x_selected}|y={y_selected}|height=600px|>
|>
### **Pie Chart Visualisation **{: style="color: #ff00ff"}
<|{df_selection}|chart|type=pie|values=Market Cap|labels=Symbol|>

|>

|main_page>
|>

"""

def filter(symbol, name):
    df_selection = df[
        df["Symbol"].isin(symbol)
        & df["Name"].isin(name)
    ]

    print("Number of rows after filtering:", len(df_selection)) 

    return df_selection

def on_filter(state):
    if len(state.symbol) == 0 or len(state.name) == 0:
        notify(state, "Error", "Ok Ok !! processsing select name also 🤯")
        return
    
    state.df_selection = filter(
        state.symbol, state.name
    )


x_selected = "Price (Intraday)"
y_selected = "Change"
numeric_columns = ["Price (Intraday)", "Change", "% Change", "Market Cap", "Volume in Currency (Since 0:00 UTC)", "Volume in Currency (24Hr)", "Total Volume All Currencies (24Hr)", "Circulating Supply"]



