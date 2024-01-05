def print_help(object, filename):
    """
    Prints the help() and dir() text of a python object to a text file
    in the same directory.
    """

    with open(filename, "w") as f:
        f.write("Output of dir() command:")
        try:
            f.write(str(dir(object)) + "\n")
            print("Dir() command was successfully run and added to file.")
        except ValueError as ve:
            print(
                f"There was a value error: {ve}.  Please ensure that a "
                + "valid Python object is provided."
            )
        except Exception as e:
            print(
                f"There was an error: {e}.  Please ensure that a valid "
                + "Python object is provided."
            )

        f.write("\n\nOutput of help() command")
        try:
            f.write(str(help(object)) + "\n")
            print("Help() command was successfully run and added to file.")
        except ValueError as ve:
            print(
                f"There was a value error: {ve}.  Please ensure that a "
                + "valid Python object is provided."
            )
        except Exception as e:
            print(
                f"There was an error: {e}.  Please ensure that a valid "
                + "Python object is provided."
            )
