class Post:
    num = 0
    post = input("Share your thoughts here!")
    history = {}
    def __init__(self,post,num,history):
        self.post = post
        self.num = num
        self.history = history

    def __str__(self):
        num=+1
        # save post 
        # put post text and a post number in a array or tupple

