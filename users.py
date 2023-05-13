# Inserer ce code si votre ordinateur affiche un probleme avec OpenGL
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#__________________________________________________________________

from kaki.app import App
from kivymd.app import MDApp
from kivy.factory import Factory
from kivymd.uix.screen import MDScreen
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import Screen, ScreenManager

screen_helper = """
ScreenManager:
    Connexion:
    Inscription:
    Profil:

<Connexion>:

<Inscription>:

<Profil>:


"""

class Connexion(Screen):
    pass

class Inscription(Screen):
    pass

class Profil(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Connexion(name='connexion'))
sm.add_widget(Inscription(name='inscription'))
sm.add_widget(Profil(name='profil'))

class User(MDApp, App):

    DEBUG = 1

    KV_FILES = {
        os.path.join(os.getcwd(), "connexion.kv"),
        os.path.join(os.getcwd(), "inscription.kv"),
        os.path.join(os.getcwd(), "profil.kv"),
    }
    CLASSES = {
        "Connexion": "users",
        "Inscription": "users",
        "Profil": "users",
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
        ]

    


    def build_app(self, **kwargs):
        self.theme_cls.primary_palette="Orange"
        self.theme_cls.theme_style = "Dark"

        screen = Builder.load_string(screen_helper)
        return screen

        # return Factory.Connexion()


if __name__ == "__main__":
    User().run()