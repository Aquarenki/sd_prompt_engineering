import kivy

kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

from prompt import Prompt

Builder.load_file('main.kv')


class MainWindow(Widget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

    def on_button_create(self):
        prompt = Prompt(self.ids.prompt_start.text)
        self.ids.prompt_new.text = prompt.create_prompt()


class MyApp(App):
    def build(self):
        self.title = "SD Prompt Engineering"
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()
