

class LoginFunctional:

    def login_func(self, username, password, realpass, manager):
        if realpass:
            if password == realpass:
                if username == "admin":
                    manager.current = "admin_screen"
                else:
                    print("Successfully logged in")
                    manager.current = "main_screen"
            else:
                print("Password is wrong")
        else:
            print("There's no such user in the system")
