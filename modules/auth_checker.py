#Verify user credentials against a predefined list.
def verify_credentials(name, password):

    name = name.lower()
    password = int(password)
    for i in range(len(list)):
            if name == list[i]["name"].lower() and password == int(list[i]["pass"]):
                return True
    return False

list = [{"name": "Omar", "pass": "123"}, {"name": "ahmed", "pass": "456"}]