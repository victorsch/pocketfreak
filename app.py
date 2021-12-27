from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder

Builder.load_string('''

<ExampleRV>:

    viewclass: 'SelectableProgram'
    
    RecycleBoxLayout:
    
        size_hint_y: None
        
        height: self.minimum_height
        
        orientation: 'vertical'

<SelectableProgram>:
    orientation: "vertical"
    Label:
        text: root.program_name
        color: 0, 0, 0, 1
    Button:
        text: "Press Me"
        on_release: root.run_docker_command()
''')


class SelectableProgram(Button):
    program_name = ""
    command = ""
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)

    def run_docker_command():
        print("command run")

selectable_programs = []

program1 = SelectableProgram()
program1.program_name = "Gobuster"

program2 = SelectableProgram()
program2.program_name = "Bettercap"

program3 = SelectableProgram()
program3.program_name = "Aircrack Suite"

program4 = SelectableProgram()
program4.program_name = "WaybackUrls"

selectable_programs.append(program1)

selectable_programs.append(program2)

selectable_programs.append(program3)

selectable_programs.append(program4)

class ExampleRV(RecycleView):
    def __init__(self, **kwargs):
        super(ExampleRV, self).__init__(**kwargs)
        self.data = [{'text': str(x.program_name)} for x in selectable_programs]

class FirstKivy(App):
    def build(self):
        return ExampleRV()




FirstKivy().run()
