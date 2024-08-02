class Human:
    def __init__(self) -> None:
        self.my_name = ""
        print("Human was born")

    def set_name(self,name):
        self.my_name = name
        print("Name set~")
    
    def get_name(self):
        return self.my_name