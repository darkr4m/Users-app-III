"""
user posts - list of dictionaries
    Post - 
        id
            unique, incrementing
        title
        body
        author
    Methods -
        create_post -
            append post to list of posts
            append post to list of user's posts
        delete_post -
            delete post from list of posts
                check if post exists by id
            delete post from list of user's posts
                check if post exists by id
        all_posts
            see all posts
        all_my_posts
            see all of this users posts

"""

# your improved User class goes here
class User:
    # List of all posts
    posts = []

    """
    Attributes:
        Name: - string - Name of the user
        Email: - string - The user's email address
        Drivers_lisence - string - The user's drivers lisence number
        User_posts - list - List of posts the user has made
    """
    def __init__(self,Name,Email,Drivers_liscence):
        self._Name = Name
        self._Email = Email
        self._Drivers_liscence = Drivers_liscence
        self._User_posts = []
#class mathods

# GETTERS AND SETTERS
    @property
    def Name(self):
        return self._Name
    @Name.setter
    def Name(self, name):
        self._Name = name

    @property
    def Email(self):
        return self._Email
    @Email.setter
    def Email(self, email):
        self._Email = email

    @property
    def Drivers_liscence(self):
        return self._Drivers_liscence
    @Drivers_liscence.setter
    def Drivers_liscence(self, dl):
        self._Drivers_liscence = dl

    @property
    def User_posts(self):
        return self.User_posts
    @User_posts.setter
    def User_posts(self, post):
        self._User_posts.append(post)

# #dunders
#     def __str__(self):
#         pass

#instance methods

user = User("Max","email","47832HD2")

