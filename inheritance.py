
class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        print("Child Constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.toys = toys

    def info(self):
        Parent.show_info(self)


will_smith = Parent("Smith", "brown")
jaden_smith = Child("Smith", "Dark Brown", 5)

jaden_smith.info()
