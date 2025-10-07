from GUI import GUI
import flet
import random

class App:
    def __init__(self):
        self.gui = None
        self.history = None

    def roll(self, e):
        result = random.randint(1, 100)
        self.history.controls.append(flet.Text(f"Rolled: {result}"))
        self.gui.page.update()

    def run(self):
        def main(page: flet.Page):
            self.gui = GUI(page)
            self.history = flet.Column()
            self.gui.page.add(
                flet.ElevatedButton("Roll", on_click=self.roll),
                self.history
            )
        flet.app(target=main)
