from taipy.gui import Gui
from web_pages.calc.calc import calc_ui
from web_pages.dashboard.dashboard import dashboard_ui
from web_pages.intro.intro import intro_ui
from web_pages.bot.bot import bot_ui
pages = {
    "/":" <|toggle|theme|> <|navbar|>",
    "AboutUs":intro_ui,
    "Calculator":calc_ui,
    "Dashboard":dashboard_ui,
    "SalesBot":bot_ui
}

if __name__ == "__main__":
    Gui(pages=pages).run(
        title="SalesAI",
        favicon="logo.png",
        image = ("calculator1.png", "Chatbot.png", "Dashboard.png","salescycle.png"),
        use_reloader=True
    )