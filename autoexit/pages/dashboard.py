

from widgets import TopBar

from textual.screen import Screen
from textual.app import ComposeResult
from traders.service import APIService
from textual.widgets import Footer
from traders.alphavantage import AlphaVantageService
from obj.config import AutoExitConfig

class DashboardView(Screen):
    def __init__(self, config:AutoExitConfig) -> None: 
        super().__init__() 
    
        self.config = config

        if self.config.api_service == APIService.ALPHA_VANTAGE:
            self.service = AlphaVantageService(self.config.api_key)

    def compose(self) -> ComposeResult:
        yield TopBar(self.config.package_name, self.config.version, self.config.api_service.value, "click [bold red]?[/bold red] for help")
        yield Footer()
