class User:
    def __init__(self, id, name):
        self.id= id
        self.name= name
        self.following= 0
        self.follower= 0

    def follow(self, user):
        self.following+= 1
        user.follower+= 1

user_1= User("1921870042", "Saifur")
user_2= User("2222302030", "Arifa")

user_1.follow(user_2)
user_1.follow(user_2)

print(user_1.following)


