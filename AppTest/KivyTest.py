import kivy
from kivymd.app import MDApp


class FirstApp(kivy.app.App):
    def build(self):
        return kivy.uix.label.Label(text = "Hola Mundo App")
    
FirstApp().run()