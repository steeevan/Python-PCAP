class Animal:
    def __init__(self) -> None:
        print("Animal Object Created")
        my_animal = ""

    def set_animal(self, myAnim):
        self.my_animal = myAnim
    def get_animal(self):
        return self.my_animal