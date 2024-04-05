def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("First line\n")
            file.write("Second line\n")
            file.write("Third line\n")
    except IOError as e:
        print("Error creating file:", e)
    else:
        print("File created successfully")


def read_and_display_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Contents of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission to access this file is denied!")
    except Exception as e:
        print("An error occured while reading the file:", e)


def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Fourth line\n")
            file.write("Fifth line\n")
            file.write("Sixth line\n")
    except IOError as e:
        print("Error appending to file:", e)
    else:
        print("Content appended to file successfully!")


if __name__ == "__main__":
    create_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()
