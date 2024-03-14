from taipy.gui import Gui

from web_pages.dashboard.dashboard import dashboard_ui
from web_pages.intro.intro import intro_ui
pages = {
    "intro":intro_ui,
    "dashboard": dashboard_ui
}

if __name__ == "__main__":
    Gui(pages=pages).run(
        title="SalesAI",
        use_reloader=True
    )