from textual.app import App
from pages import WelcomeView, DashboardView
import secret as secret
from textual import on, work


class Stocker(App):
    @work
    async def on_mount(self) -> None:
        self.screen.styles.background = "#23232b"

        api_service = await self.push_screen_wait(WelcomeView())

        self.push_screen(DashboardView(api_service=api_service))
        

if __name__ == "__main__":
    app:App = Stocker()
    app.run(inline=False)