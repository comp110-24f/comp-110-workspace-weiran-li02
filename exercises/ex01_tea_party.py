"""Bringing these function together in a “main planner” function that calls each and produces printed output"""

__author__ = "730799401"


def main_planner(guests: int) -> None:
    """This function is used to add the guests number
    Args:
        guests(int): guests
    Returns:
        None
    """
    print("A Cozy Tea Party for" + " " + str(guests) + " " + "People!")
    print("Tea Bags:" + " " + str(tea_bags(guests)))
    print("Treats:" + " " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """A function to compute the number of tea bags needed based on number of guests"""
    return people * 2


def treats(people: int) -> int:
    """A function to compute the number of treats needed based on the number of teas guests are expecting to drink"""

    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """A function to compute the cost of the tea bags and the treats combined"""
    return tea_count * 0.5 + treat_count * 0.75


"""Making the program runnable and asking a user for input when they run the program"""

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
