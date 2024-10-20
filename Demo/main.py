from kivymd.app import MDApp
from kivy.uix.button import Button 
from kivy.lang import Builder

from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from kivymd.uix.boxlayout import MDBoxLayout


class MyCustomButton(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.font_size = 30 
    def on_text(self,wdt,text):
        if text in '+-x/':
            self.background_color=[0,0,1,1] 
        elif text == '=': 
            self.background_color = [0,1,0,1]
        else:
            self.background_color = [0,1,1,1]

class CalculatorDesign(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = 20

        self.title = Label(text = 'Kivy Calculator',size_hint_y = None)
        self.add_widget(self.title)

        self.entry = TextInput(readonly= True,size_hint_y=None,height=50)
        self.add_widget(self.entry)

        self.grid = GridLayout(cols = 4)
        self.add_widget(self.grid)

        chars = '123+456-789x0./='
        for char in chars:
            b = MyCustomButton(text=char,on_release = lambda x,y=char:self.clicked(y))
            self.grid.add_widget(b)

    def clicked(self,text):
        answer = self.entry.text
        if text == '.' and '.' in answer:  
            return 
        if text in '+-/x':
            if answer.endswith(('+',"-","x","/")):
                self.entry.text = answer[:-1] + text
                return 
            else:
                 self.entry.text += text
                 return
        
        if text == '=':
            result = eval(answer.replace('x','*')) 
            self.entry.text = str(result)
            return
        self.entry.text += text




class MyApp(MDApp):
    def build(self):
        # return Builder.load_file('myapp.kv')  
        return CalculatorDesign()


    
       




if __name__ == '__main__':
    MyApp().run()