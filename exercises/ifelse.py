def less_than_10(num: int) -> None:
    """tell us if num<10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("small number")
    else:
        print("big number")
    print("this is the end of the funciton")


def assignment(date: float, duedate: float) -> None:
    if duedate - date <= 0.1:
        print("work")
    else:
        print("not work")


def wake_up(alarm: bool) -> str:
    """return a message based on if alarm is going off"""
    if alarm is True:
        return "Wake up! Go to comp110"
    else:
        return "Keep sleeping, you deserve it."


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match"
    else:
        return "no match"


less_than_10(num=7)


def get_weather_report() -> str:
    """docstring."""
    weather :str= input("what is the weather?")
    if weather == "cold" or weather == "wind":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather
