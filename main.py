import kivy
from kivy.properties import AliasProperty, ObjectProperty

kivy.require('2.3.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import ScreenManager, Screen

from prompt import Prompt

class HomeScreen(Screen):
    def on_button_clear(self):
        self.ids.prompt_start.text = ''
        self.ids.prompt_new.text = ''

    def on_button_create(self):
        weighted_value = self.manager.get_screen('settings').ids.chk_weighted.active
        randomized_value = self.manager.get_screen('settings').ids.chk_randomized.active
        prompt = Prompt(
            text=self.ids.prompt_start.text,
            weighted=weighted_value,
            randomize=randomized_value)
        self.ids.prompt_new.text = prompt.create_prompt()

    def on_button_copy(self):
        Clipboard.copy(self.ids.prompt_new.text)


class SettingsScreen(Screen):
    chk_weighted = ObjectProperty(None)
    chk_randomized = ObjectProperty(None)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')

class MyApp(App):
    def build(self):
        self.title = "SD Prompt Engineering"
        return kv

if __name__ == '__main__':
    MyApp().run()
