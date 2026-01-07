import kivy

kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

from prompt import Prompt

Builder.load_file('main.kv')


class MainWindow(Widget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

    def on_button_create(self):
        prompt = Prompt(
            text=self.ids.prompt_start.text,
            weighted=self.ids.checkbox_weighted.active,
            randomize=self.ids.checkbox_randomized.active)
        self.ids.prompt_new.text = prompt.create_prompt()

    def on_button_copy(self):
        Clipboard.copy(self.ids.prompt_new.text)


class MyApp(App):
    def build(self):
        self.title = "SD Prompt Engineering"
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()
