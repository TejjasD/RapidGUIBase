class passwordManager:

    def __init__(self):
        pass

    def authenticateUser(self, userID, password):
        if userID == 'guest' and password == 'guest':
            return True
        else:
            return False