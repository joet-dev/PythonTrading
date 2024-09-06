from textual.app import App
from pages import WelcomeView, DashboardView
import secret as secret
from textual import work
from importlib import metadata
from obj.config import AutoExitConfig
from rich.theme import Theme


try:
    __package_name__ = metadata.metadata('autoexit')["Name"]
    __version__ = metadata.version('autoexit')
except Exception as e:
    print(e)
    __package_name__ = "autoexit"
    __version__ = "N/A"

class AutoExit(App):
    CSS_PATH = "main.tcss"

    def __init__(self) -> None:
        super().__init__() 

        theme = Theme(
            {
                "white": "#e9e9e9",
                "green": "#54efae",
                "yellow": "#f6ff8f",
                "dark_yellow": "#cad45f",
                "red": "#fd8383",
                "purple": "#b565f3",
                "dark_gray": "#969aad",
                "b dark_gray": "b #969aad",
                "highlight": "#91abec",
                "label": "#c5c7d2",
                "b label": "b #c5c7d2",
                "light_blue": "#bbc8e8",
                "b white": "b #e9e9e9",
                "b highlight": "b #91abec",
                "bold red": "b #fd8383",
                "b light_blue": "b #bbc8e8",
                "recording": "#ff5e5e",
                "b recording": "b #ff5e5e",
                "panel_border": "#6171a6",
                "table_border": "#333f62",
            }
        )
        self.console.push_theme(theme)

    @work
    async def on_mount(self) -> None:
        self.screen.styles.background = "#23232b"
        api_service = await self.push_screen_wait(WelcomeView())

        config = AutoExitConfig(api_service, __package_name__, __version__)
        self.push_screen(DashboardView(config))
        

if __name__ == "__main__":
    app:App = AutoExit()
    app.run(inline=False)