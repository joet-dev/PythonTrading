
from textual.widgets import Button, Placeholder
from textual.screen import Screen
from textual.app import ComposeResult
from traders.service import APIService
import secret as secret
from traders.alphavantage import AlphaVantageService, AVFunction



class DashboardView(Screen):
    def __init__(self, api_service:APIService): 
        super().__init__() 
        if api_service == APIService.ALPHA_VANTAGE:
            self.service = AlphaVantageService(secret.ALPHA_VANTAGE_API_KEY)

    def compose(self) -> ComposeResult:
        yield Placeholder("Dashboard Screen")