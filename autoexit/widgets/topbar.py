from textual.containers import Container
from textual.app import ComposeResult
from textual.widgets import Label

class TopBar(Container):
    def __init__(self, app_name:str="unknown", app_version:str="", system:str="", help:str=""):
        super().__init__()

        self.left = Label(f"{app_name} {app_version}", id="topbar-left")
        self.middle = Label(system, id="topbar-middle")
        self.right = Label(help, id="topbar-right")
        
    def compose(self) -> ComposeResult:
        yield self.left
        yield self.middle
        yield self.right
        