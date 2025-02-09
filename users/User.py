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
    @classmethod
    def see_all_posts(cls):
        for post in cls.posts:
            print(f"Title: {post['title']}\nContent: \n{post['content']}")


# GETTERS AND SETTERS
    @property
    def Name(self):
        return self._Name
    @Name.setter
    def Name(self, name):
        if isinstance(name, str):
            self._Name = name
        else:
            print("Name must be a string.")

    @property
    def Email(self):
        return self._Email
    @Email.setter
    def Email(self, email):
        if isinstance(email, str):
            self._Email = email
        else:
            print("Email must be a string.")

    @property
    def Drivers_liscence(self):
        return self._Drivers_liscence
    @Drivers_liscence.setter
    def Drivers_liscence(self, dl):
        if isinstance(dl, str):
            self._Drivers_liscence = dl
        else:
            print("Drivers liscence must be a string.")
            
    @property
    def User_posts(self):
        return self._User_posts
    @User_posts.setter
    def User_posts(self, post):
        self._User_posts.append(post)

#dunders
    def __str__(self):
        return f"{self.Name}, ID Number {self.Drivers_liscence} can be reached by email at {self.Email}."

#instance methods
    def create_a_post(self):
        id=len(self.posts)+1
        user_title = input("Please enter the title of your post:\n")
        user_body = input("Please enter the content of your post:\n")
        self.posts.append({"id":id,"title":user_title,"content":user_body})
        self.User_posts.append({"id":id,"title":user_title,"content":user_body})
    
    def delete_a_post(self):
        id=input("Please enter the ID of the post you would like to delete:\n")
        for i in range(len(self.User_posts)):
            if self.User_posts[i]['id'] == id:
                self.User_posts.pop(i)
        for i in range(len(self.posts)):
            if self.posts[i]['id'] == id:
                self.posts.pop(i)
    
    def see_my_posts(self):
        for post in self.User_posts:
            print(f"Title: {post['title']}\nContent: \n{post['content']}")
