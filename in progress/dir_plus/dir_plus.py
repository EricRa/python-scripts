# trying to build on an answer from this stack exchange post:
# https://stackoverflow.com/questions/73416935/methods-and-objects-in-python-using-dir-method

# Attempting to standardize this a bit in its own module

def dir_plus(object):
    """
    Returns the contents of the built-in dir() function, but with attributes
    separated into callable and non-callable groups.  This is an attempt to
    make it easier to separate non-callable attributes of an object from it's
    callable methods.
    """

    try:
        dir_items = dir(object)
    except TypeError as t_error:
        print(f"There was an error: {t_error}.")
        print("Please make sure you are calling dir() on a python object")
    except Exception as e:
        print(f"There was an error: {e}.  \n Please try again.")

    attributes = [item for item in dir_items \
      if not callable(getattr(dir_items, item))]
    methods = [item for item in dir_items \
      if callable(getattr(dir_items, item))]

    print(dir_items) #DEBUG
    print(type(dir_items)) #DEBUG

    print(f"Callables: {methods} \n")
    print(f"Non-Callables:  {attributes} \n")

            
