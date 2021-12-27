from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
import os

Config.set('kivy', 'keyboard_mode', 'systemandmulti')

def striplines(lines):
    return [l.strip('\n') for l in lines]

def cmdOutputLines(cmd):
    return striplines(os.popen(cmd).readlines())

class MainWindow(Screen):
    pass

class GobusterWindow(Screen):
    pass

class NmapWindow(Screen):
    host = ""
    ports = ""
    command = "docker run instrumentisto/nmap -sC -sV -Pn "
    command_output = StringProperty()
    def launch_docker(self):
        print("Running command")
        new_command = self.command + self.host.text
        print(new_command)
        output = cmdOutputLines(new_command)
        for line in output:
            offset = 80
            if (len(line) > offset):
                line = line[:offset] + "\n" + line[offset:]
            self.command_output += line + "\n"
        print(self.command_output)
    pass


class WindowManager(ScreenManager):
    pass

class MenuButton(Button):
    pass


kv = Builder.load_file("screens.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
