# Built by Tejas Deolasee

#########################################################################################

class passwordManager:

    def __init__(self):
        pass

#########################################################################################

    def authenticateUser(self, userID, password):
        return True
        if userID == 'guest' and password == 'guest':
            return True
        else:
            return False

#########################################################################################
