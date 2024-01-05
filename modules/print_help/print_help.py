def print_help(object, filename):
    """
    Prints the help() and dir() text of a python object to a text file
    in the same directory.
    
    If the file does not yet exist, it will be created.  If the file already exists, the output will be appended to the end of the file.
    
    Example usage:
    
        #saves output of the dir and help functions for ph to help.txt:
    
        from print_help import print_help as ph
        ph(ph, "help.txt")

    """

    import contextlib

    with open(filename, "a") as f:
        f.write(f"Output of dir() command for {str(object)}:\n")
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

        f.write(f"\n\nOutput of help() command for {str(object)}:\n")
        try:
            with contextlib.redirect_stdout(f):
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
