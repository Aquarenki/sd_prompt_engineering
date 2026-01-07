import kivy

kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from prompt import Prompt

class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text='Original prompt'))
        self.prompt_start = TextInput(multiline=True)
        self.add_widget(self.prompt_start)

        self.button_create = Button(text='Create')
        self.button_create.bind(on_press=self.on_button_create)
        self.add_widget(self.button_create)

        self.prompt_new = TextInput(multiline=True)
        self.add_widget(self.prompt_new)

    def on_button_create(self, instance):
        prompt = Prompt(self.prompt_start.text)
        self.prompt_new.text = prompt.create_prompt()


class MyApp(App):
    def build(self):
        self.title = "SD Prompt Engineering"
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()
