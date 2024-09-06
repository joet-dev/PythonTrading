from textual.app import ComposeResult
from traders.service import APIService
from rich.markdown import Markdown
from textual.widgets import Button, Static
from textual.screen import Screen
from textual import on
from textual.containers import Container, Horizontal


WELCOM_MD = """\
# pullback.oi Trader

If you're a driven trader that is ready to automate your strategies this trading bot will help to maximize your returns and free up your time. 

### Integration List 
- **API Connectors**: To date Pullback connects to 3 APIs.
    - Alpha Vantage - Stock Data
"""

class WelcomeView(Screen[APIService]):
    DEFAULT_CSS = """
        Welcome #text {
            margin:  0 1;
        }
        Welcome #system_container {
            align: center bottom;
        }
        Welcome .btn {
            margin: 0 1;
        }
    """

    def compose(self) -> ComposeResult:
        yield Container(Static(Markdown(WELCOM_MD), id="text"), id="md")
        yield Horizontal(
            Button("Alpha Vantage", id="av", classes="btn", variant="success"),
            Button("Polygon", id="pg", classes="btn", variant="success"), 
            Button("Exit", id="exit", classes="btn", variant="error"), 
            id="system_container"
        )

    @on(Button.Pressed, "#av")
    def on_av(self) -> None:
        self.dismiss(APIService.ALPHA_VANTAGE)
   
    @on(Button.Pressed, "#pg")
    def on_pg(self) -> None:
        self.dismiss(APIService.POLYGON)

    def on_close(self) -> None: 
        self.app.exit()
