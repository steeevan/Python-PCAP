class User:
    def __init__(self, user_id:str, name:str, email:str, password:str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password        # store hashed password
    
    def display_user_info(self) -> str:
        return f"User {self.name}, (email: {self.email})"
    

if __name__ == "__main__":
    person = User("0001", "Mr.E","mr.E@gmail.com","Mr.Beast")
    print(type(person))
    print(person.display_user_info())