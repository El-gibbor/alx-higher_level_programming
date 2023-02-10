"""a module for appending"""


def append_write(filename="", text=""):
    """appends str at the end of a text file and 
        return the number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
