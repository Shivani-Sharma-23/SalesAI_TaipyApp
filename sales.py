from taipy.gui import Gui, Markdown, State, notify
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
state = list(df["State"].unique())
occu = list(df["Occupation"].unique())
layout = {"margin": {"l": 220}}
df["Orders"].unique()
df["Age Group"].unique()
states = []
occus = []

page = """
<|toggle|theme|>

<|text-center |
# **SALESAI   🤖**{: style="color: #51829B"}
>
<hr/>
### **SALES CALCULATOR**{: style="color: #AD88C6"}
<|1 1 1 |layout|
<total_Product|
#### **Number of products sold**:
<|{number_of_products_sold}|number|>
|total_Product>

<amount|
####  **Amount of One Product**:
<|{amount_of_one_product}|number|>
|amount>

<amount_p|
#### **Cost of making one Product**:
<|{Cost_of}|number|>
|amount_p>
|>
<br/>
<|Calculate|button|on_action=button_pressed|>
<|text-center |
##**TOTAL SALE:**
Rs. 51,000
>
<br/>
<hr/>
## **DATA ANALYSIS**{: style="color: #AD88C6"}
<|{data}|chart|mode=lines|x=Date|y[1]=State|y[2]=Min|y[3]=Max|line[1]=dash|color[2]=blue|color[3]=red|>

<|1 1 1 1|layout|
<total_amount|
#### **AMOUNT**:
Rs. <|{int(df['Amount'].sum())}|>
|total_amount>

<orders|
####  **Orders count**:
<|{int(df['Orders'].sum())}|> units
|orders>

<age|
#### **Age Group**:
<|{int(df['Age Group'].count())}|>
|age>

<user|
#### **No of **Users:
<|{int(df['User_ID'].count())}|> User
|user>
|>
<br/>
<hr/>
## **DO DATA ANALYSIS BY APPLYING FILTERS**{: style="color: #AD88C6"}
<|20 80|layout|gap=30px|
<|sidebar|
## **Apply Filter:** {: style="color: #51829B"}

<|{states}|selector|lov={state}|multiple|label=STATE|dropdown|on_change=on_filter|class_name=fullwidth|>
<br/>
<|{occus}|selector|lov={occu}|multiple|label=OCCUPATION|dropdown|on_change=on_filter|class_name=fullwidth|>

|>

<main_page|

<|1 1 1 1|layout|
<total_amount|
#### **AMOUNT**:
Rs. <|{int(df['Amount'].sum())}|>
|total_amount>

<orders|
####  **Orders count**:
<|{int(df['Orders'].sum())}|> units
|orders>

<age|
#### **Age Group**:
0-17 
<br/>
26-35
|age>

<user|
#### **No of **Users:
<|{int(df['User_ID'].count())}|> User
|user>
|>
<br/>

<|DIWALI SALES|expandable|not expanded|
<|{df}|table|page_size=5|>
|>
|main_page>
|>
"""

def button_pressed(state):
    state.scenario.number_of_products_sold.submit(wait=True)
    state.scenario.amount_of_one_product.submit(wait=True)
    state.scenario.Cost_of.submit(wait=True)
    t = number_of_products_sold * amount_of_one_product - Cost_of * number_of_products_sold
    state.t = scenario.t.read()

if __name__ == "__main__":
    df2 = filter(states, occus) 
    total_market_cap = int(df["Amount"].sum())
    page = page.replace("<|{int(df2['Amount'].sum())}|>", f"<|{total_market_cap}|>")
    
Gui(page).run(margin="0em", title="Sales Dashboard")