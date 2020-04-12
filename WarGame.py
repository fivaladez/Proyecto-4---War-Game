""""
The first two operations should signal an error if they contradict your former
knowledge. The two relations “friends” (denoted by ∼) and “enemies” (denoted by
∗) have the following properties:
∼ is an equivalence relation: i.e.,
    1.If x ∼ y and y ∼ z, then x ∼z (The friends of my friends are my friends as well.)
    2.If x ∼ y, then y ∼ x (Friendship is mutual.)
    3.x ∼ x (Everyone is a friend of himself.)
∗ is symmetric and inflexible:
    1. If x ∗ y then y ∗ x (Hatred is mutual.) 
    2. Not x ∗ x (Nobody is an enemy of himself.) 
    3. If x ∗ y and y ∗ z then x ∼ z (A common enemy makes two people friends.)
    4. If x ∼ y and y ∗ z then x ∗ z (An enemy of a friend is an enemy.)
Operations setFriends(x,y) and setEnemies(x,y) must preserve these properties.
"""
from os import system, name
from time import sleep


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

class WarGame:
    """Class for solving project WarGame"""
    people_list = set()
    country_A = set()
    country_B = set()
    # Use a set to avoid duplicated elements

    def setFriends(self, x, y):
        # Check if they are enemies
        if (x in self.country_A and y in self.country_B) or (x in self.country_B and y in self.country_A):
            return -1
        else:
            if x in self.country_A:
                self.country_A.add(y)
            elif x in self.country_B:
                self.country_B.add(y)
            elif y in self.country_A:
                self.country_A.add(x)
            elif y in self.country_B:
                self.country_B.add(x)
            else:
                self.country_A.add(x)
                self.country_A.add(y)

    def setEnemies(self, x, y):
        # Check if they are friends
        if (x in self.country_A and y in self.country_A) or (x in self.country_B and y in self.country_B):
            return -1
        else:
            if x in self.country_A:
                self.country_B.add(y)
            elif x in self.country_B:
                self.country_A.add(y)
            elif y in self.country_A:
                self.country_B.add(x)
            elif y in self.country_B:
                self.country_A.add(x)
            else:
                self.country_A.add(x)
                self.country_B.add(y)

    def areFriends(self, x, y):
        # 1.If x ∼ y and y ∼ z, then x ∼ z (The friends of my friends are my friends as well.)
        # 2.If x ∼ y, then y ∼ x (Friendship is mutual.)
        # 3.x ∼ x (Everyone is a friend of himself.)
        if (x in self.country_A and y in self.country_A) or (x in self.country_B and y in self.country_B):
            return 1
        else:
            return 0

    def areEnemies(self, x, y):
        # 1. If x ∗ y then y ∗ x (Hatred is mutual.) 
        # 2. Not x ∗ x (Nobody is an enemy of himself.) 
        # 3. If x ∗ y and y ∗ z then x ∼ z (A common enemy makes two people friends.)
        # 4. If x ∼ y and y ∗ z then x ∗ z (An enemy of a friend is an enemy.)
        if (x in self.country_A and y in self.country_B) or (x in self.country_B and y in self.country_A):
            return 1
        else:
            return 0

    def execute(self, number_of_people, operation_lists):
        """"All the control for class WarGame is executed here"""
        clear()
        self.people_list = {n for n in range(number_of_people)}
        print(" --------------- --------------- ")
        print("| Sample Input  | Sample Output |")
        print(" --------------- --------------- ")
        print("| {}            |               |".format(n))
        for operation_list in operation_lists:
            c, x, y = operation_list[0], operation_list[1], operation_list[2]
            result = "Invalid"
            if c == 1:
                result = self.setFriends(x, y)
            elif c == 2:
                result = self.setEnemies(x, y)
            elif c == 3:
                result = self.areFriends(x, y)
            elif c == 4:
                result = self.areEnemies(x, y)
            else:
                pass

            if result is not None:
                if result == -1: # Remove an space for the - in result
                    print("| {}     | {}            |".format(operation_list, result))
                elif result == "Invalid":
                    print("| {}     |  {}      |".format(operation_list, result))
                else: # Add an extra space
                    print("| {}     |  {}            |".format(operation_list, result))
            else:
                print("| {}     |               |".format(operation_list))

        print(" --------------- --------------- \n")
        print("People list {}\nCountry A {}\nCountry B {}".format(self.people_list, self.country_A, self.country_B))


if __name__ == "__main__":
    # The first line contains a single integer, n, the number of people.
    n = int(input())
    data = list()
    while True:
        # Each subsequent line contains a triple of integers, c x y, where c is the code of the operation,
        # c=1 setFriends, c=2 setEnemies, c=3 areFriends, c=4 areEnemies
        data_package = [int(element) for element in input().split()]
        if len(data_package) != 3:
            print("Invalid data {}".format(data_package))
            continue
        else:
            data.append(data_package)

        if [0, 0, 0] in data:
            # data.remove([0, 0, 0])
            break

    war_game = WarGame()
    sleep(2)
    war_game.execute(n, data)
