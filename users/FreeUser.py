from .User import User

class FreeUser(User):
    def __init__(self, Name, Email, Drivers_liscence):
        super().__init__(Name, Email, Drivers_liscence)

    def add_a_post(self):
        if len(self.posts) < 2:
            id=len(self.posts)+1
            user_title = input("Please enter the title of your post:\n")
            user_body = input("Please enter the content of your post:\n")
            self.posts.append({"id":id,"title":user_title,"content":user_body})
            self.User_posts.append({"id":id,"title":user_title,"content":user_body})
        else:
            print("You have already made 2 out of 2 of your free posts. Please upgrade to Premium.")