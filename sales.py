from taipy.gui import Gui,navigate
import openai
import os
import sys
from web_pages.calc.calc import calc_ui
from web_pages.dashboard.dashboard import dashboard_ui
from web_pages.intro.intro import intro_ui
from web_pages.crypto.crypto import *
from web_pages.calc.calc import *


no_logo = ""

def to_SalesAI(state):
    state.name =  "New Chat"
    navigate(state, "Dashboard")

# setting page navigation function
def to_Crypto(state):
    state.name =  "New Chat"
    navigate(state, "CryptoMate")


my_theme = {
    "palette": {
    "background": {"default": "#31363F"},
    "primary": {"main": "#9CAFAA"} 
    },
}

pages = {
    "AboutUs":intro_ui,
    "Calculator":calc_ui,
    "Dashboard":dashboard_ui,
    "CryptoMate": crypto_ui,
}

if __name__ == "__main__":
    df_selection = filter(symbol, name)  
    total_market_cap = int(df_selection["Market Cap"].sum())
    page = crypto_ui.replace("<|{int(df_selection['Market Cap'].sum())}|>", f"<|{total_market_cap}|>")

    Gui(pages=pages).run(
        title="SalesCrypto",
        image = ("calculator1.png", "Chatbot.png", "Dashboard.png","salescycle.png"),
        use_reloader=True,
        theme=my_theme,
        watermark=no_logo,
    )


    