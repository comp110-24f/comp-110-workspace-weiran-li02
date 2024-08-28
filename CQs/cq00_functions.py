__author__ = "730799401"


def mimic(message: str) -> str:
    """Please type the message you want"""
    return message


def main() -> None:
    """only print the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
