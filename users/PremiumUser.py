from .User import User

class PremiumUser(User):
    def __init__(self, name, email, drivers_liscence):
        super().__init__(name, email, drivers_liscence)