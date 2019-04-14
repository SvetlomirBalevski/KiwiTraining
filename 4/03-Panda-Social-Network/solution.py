# # Panda
#
# For our social network, we are going to need a `Panda` class which behaves like that:
#
# ```python
# ivo = Panda("Ivo", "ivo@pandamail.com", "male")
#
# ivo.name() == "Ivo" # True
# ivo.email() == "ivo@pandamail.com"  # True
# ivo.gender() == "male" # True
# ivo.isMale() == True # True
# ivo.isFemale() == False # True
# ```
#
# The `Panda` class also should be possible to:
#
# * Be turned into a string
# * Be hashed and used as a key in a dictionary (`__eq__` and `__hash__`)
# * Make sure that the email is a valid email!
#
# Two `Panda` instances are equal if they have matching `name`, `email` and `gender` attributes.

import re


class Panda:
    def __init__(self, name, email, gender):
        self._name = name
        self._email = email
        self._gender = gender

        email_match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

        if email_match == None:
            raise ValueError('Wrong email')

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

    def isMale(self):
        if self._gender == "male":
            return True
        else:
            return False

    def isFemale(self):
        result = self.isMale()
        return not result

    def __eq__(self, other):
        if self.gender() == other.gender() and self.name() == other.name() and self.email() == other.email():
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.name(),self.email(),self.gender()))

    def __str__(self):
        return f"This is {self.name()}, with email of {self.email()} and gender {self.gender()}"

# # SocialNetwork
#
# Now it is time for our social network!
#
# Implement a class, called `PandaSocialNetwork`, which has the following public methods:
#
# * `add_panda(panda)` - this method adds a panda to the social network. The panda has 0 friends for now.
# If the panda is already in the network, raise a `PandaAlreadyThere` error.
# * `has_panda(panda)` - returns `True` or `False` if the panda is in the network or not.
# * `make_friends(panda1, panda2)` - makes the two pandas friends. Raise `PandasAlreadyFriends` if they are already friends.
# The friendship is two-ways - `panda1` is a friend with `panda2` and `panda2` is a friend with `panda1`.
# If `panda1` or `panda2` are not members of the network, add them!
# * `are_friends(panda1, panda2)` - returns `True` if the pandas are friends. Otherwise, `False`
# * `friends_of(panda)` - returns a list of `Panda` with the friends of the given panda.
# Returns `False` if the panda is not a member of the network.

class PandaSocialNetwork:

    def __init__(self):
        self.members = []
        self.list_of_friendships = {}

    def add_panda(self,panda):
        if self.has_panda(panda):
            raise ValueError("PandaAlreadyThere")

        else:
            self.members.append(panda)

    def has_panda(self,panda):
        if panda in self.members:
            return True
        else:
            return False

    def make_friends(self,panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
            self.list_of_friendships.update({panda1 : []})
        if not self.has_panda(panda2):
            self.add_panda(panda2)
            self.list_of_friendships.update({panda2: []})
        if panda2 in self.list_of_friendships[panda1]:
            raise ValueError ("PandasAlreadyFriends")
        else:
            self.list_of_friendships[panda1].append(panda2)
            self.list_of_friendships[panda2].append(panda1)
    def are_friends(self,panda1, panda2):
        if panda2 in self.list_of_friendships[panda1]:
            return True
        else:
            return False

    def friends_of(self,panda):
        if panda not in self.list_of_friendships:
            return False
        return self.list_of_friendships[panda]

