class User:

    def __init__(self, user_id, user_name):
        """
        Constructs a new user object.
        :rtype: None
        """
        self.user_id = user_id
        self.user_name = user_name
        self.user_followers = 0
        self.user_following = 0
        print('INFO: User constructed')

    def follow_other_user(self, obj_other_user):
        """
        Increase the number of following users and the number of users followed by the other user.
        :param obj_other_user:
        """
        self.user_following += 1
        obj_other_user.user_followers += 1


user_1 = User(user_id='001', user_name='jorge')
print(type(user_1))
print(user_1)
