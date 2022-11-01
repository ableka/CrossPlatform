from MyApplication.model.database import DataBase


class RegistrationFunctional:
    database = DataBase()

    def registration_func(self, username, password, rep_password, manager):
        if username != '' and password != '' and rep_password != '':
            if password == rep_password:
                self.database.new_user(username, password)
                self.database.delete_duplicates()
                manager.current = "log_screen"
            else:
                print("Password doesn't match")
        else:
            print("You didn't fill all of the blanks")
        print(f"Button pressed. {username}, {password}, {rep_password}")
