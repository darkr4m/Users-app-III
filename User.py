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
        pass
#class mathods
# GETTERS AND SETTERS

#dunders
    def __str__(self):
        pass

#instance methods

