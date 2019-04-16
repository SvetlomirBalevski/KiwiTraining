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
        self._gender = gender

        email_match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

        if email_match == None:
            raise ValueError('Wrong email')

        self._email = email

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

    def isMale(self):
        return self._gender == "male"

    def isFemale(self):
        return not self.isMale()

    def __eq__(self, other):
        return self.gender() == other.gender() and self.name() == other.name() and self.email() == other.email()


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
        self.list_of_friendships = {}

    def add_panda(self,panda):
        if self.has_panda(panda):
            raise ValueError("PandaAlreadyThere")

        else:
            self.list_of_friendships.update({panda : []})

    def has_panda(self,panda):
        return panda in self.list_of_friendships

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
        return panda2 in self.list_of_friendships[panda1]

    def friends_of(self, panda):
        if panda not in self.list_of_friendships:
            return False
        return self.list_of_friendships[panda]

# # Extra homework
#
# * `connection_level(panda1, panda2)` - returns the connection level between `panda1` and `panda2`.
#    If they are friends, the level is 1. Otherwise, count the number of friends you need to go
#   through from `panda1` in order to get to `panda2`.
#   If they are not connected at all, return -1!
#   Return `False` if one of the pandas are not member of the network.
# * `are_connected(panda1, panda2)` - return `True` if the pandas are connected somehow, between friends, or `False` otherwise.
# * `how_many_gender_in_network(level, panda, gender)` - returns the number of pandas with `gender` (male of female) that
#   are in the network of `panda`, while counting `level` levels deep.
#   If level == 2, we will have to look in all friends of `panda` and all of their friends too...

    def connection_level(self, panda1, panda2, origin_panda1 = Panda("", "mmm@mmm.mmm", "")):

        if not (self.has_panda(panda1) and self.has_panda(panda2)):
            return False

        if self.are_friends(panda1, panda2):
            return 1
        else:
            for panda in self.friends_of(panda1):
                if panda != origin_panda1:
                    return 1 + self.connection_level(panda,panda2,panda1)
            return -1

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1,panda2) > 0:
            return True


    def how_many_gender_in_network(self, level, panda, gender, counted_pandas=None):

        counted_pandas = [] if counted_pandas is None else counted_pandas

        number_of_genders = 0
        counted_pandas.append(panda)

        for single_panda in self.friends_of(panda):
            if single_panda not in counted_pandas:
                if single_panda.gender() == gender:
                    number_of_genders += 1

                if level > 1:
                    number_of_genders += self.how_many_gender_in_network(level-1, single_panda, gender, counted_pandas)


        return number_of_genders




