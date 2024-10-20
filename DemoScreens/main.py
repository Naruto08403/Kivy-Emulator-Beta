from kivymd.app import MDApp
from kivy.lang import Builder


class ProjectApp(MDApp):

    def on_start(self):
        self.loginscreen = Builder.load_file('login.kv')
        self.homescreen = Builder.load_file('home.kv')
        self.signupscreen = Builder.load_file('signup.kv')


        self.root.add_widget(self.loginscreen)
        self.root.add_widget(self.homescreen)
        self.root.add_widget(self.signupscreen)
        

    def login(self):
        username = self.loginscreen.ids.username.text 
        password = self.loginscreen.ids.password.text 
        if username == 'admin' and password == 'admin':
            self.root.current = 'home'
        else:
            self.loginscreen.ids.errorlabel.text = 'Wrong credentials!'


if __name__ == '__main__':
    ProjectApp().run()