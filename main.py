import kivy

kivy.require('2.3.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import ScreenManager, Screen

from prompt import Prompt

Builder.load_file('main.kv')


class HomeScreen(Screen):
    def on_button_create(self):
        prompt = Prompt(
            text=self.ids.prompt_start.text,
            weighted=self.ids.checkbox_weighted.active,
            randomize=self.ids.checkbox_randomized.active)
        self.ids.prompt_new.text = prompt.create_prompt()

    def on_button_copy(self):
        Clipboard.copy(self.ids.prompt_new.text)


class SettingsScreen(Screen):
    pass


class MyApp(App):
    def build(self):
        self.title = "SD Prompt Engineering"
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


if __name__ == '__main__':
    MyApp().run()
