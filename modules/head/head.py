def head(text, lines=5):
    """
    Prints the first 5 lines of text.  
    Configure number of lines by providing the optional lines parameter
    
    Example usage code for running this on a text file in the same
    local directory:
    
    from head import head
    f = open("textfilehere.txt", "r")
    text = f.readlines()
    f.close()
    
    head(text)      # returns first 5 lines
    head(text, 53)  # returns first 53 lines
    """
    i = 0
    for line in text:
        print(line)
        i += 1

        if i >= lines:
            break
