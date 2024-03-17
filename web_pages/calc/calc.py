from taipy.gui import Markdown

def add_pro(state):
    if state.no_of_prod != "":
        with open("No_pro.txt", "a") as f:
            f.write(state.no_of_prod)


def generate_amt(state):
    if state.amt_one_pro != "":
        with open("Amt.txt", "a") as f:
            f.write(state.amt_one_pro)

def generate_cst_one(state):
    if state.cost_of_making_one_p != "":
        with open("cost_one.txt", "a") as f:
            f.write(state.cost_of_making_one_p)

def clear_out1(state):
    state.no_of_prod = ""


def clear_out2(state):
    state.amt_one_pro = ""

def clear_out3(state):
    state.cost_of_making_one_p = ""

def calculate(state):
    with open("No_pro.txt", "r") as pro_file:
        prod = pro_file.read().strip()

    with open("Amt.txt", "r") as amt_file:
        amt = amt_file.read().strip()
    
    with open("cost_one.txt", "r") as cost_file:
        cost = cost_file.read().strip()

    sum_all = net_amount(prod, amt, cost)
    return sum_all

def net_amount(prod,amt,cost):
    net_amount = prod*amt - (prod*cost)

    return net_amount


calc_ui = """
<h1><div style="text-align: center;">
<span style="color: #B7C9F2;">SALES CALCULATOR</span>
</div></h1>
<|1 1 1 |layout|
<|card|
<total_Product|
#### **Number of products sold**:
<|{no_of_prod}|number|>
<br/>
<br/>
<|Add|button|on_action=add_pro|>
<|Clear|button|class_name=blueButton|on_action=clear_out1|>
|total_Product>
|>

<|card|
<amount|
####  **Amount of One Product**:
<|{amt_one_pro}|number|>
<br/>
<br/>
<|Add|button|on_action=generate_amt|>
<|Clear|button|class_name=blueButton|on_action=clear_out2|>
|amount>
|>

<|card|
<amount_p|
#### **Cost of making one Product**:
<|{cost_of_making_one_p}|number|>
<br/>
<br/>
<|Add|button|on_action=generate_cst_one|>
<|Clear|button|class_name=blueButton|on_action=clear_out3|>
|amount_p>
|>
|>

<br/>
<|card|
<|text-center |
##**TOTAL SALE:**
<|Calculate|button|on_action=calculate|>
|>
"""