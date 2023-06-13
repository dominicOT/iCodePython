def reverse_string(input_str: str) -> str:
    
    """
    Program to reverse letters in a string
   
   >>> reverse_letters('The quick brown fox jumped over the lazy dog.')
    'ehT kciuq nworb xof depmuj revo eht yzal .god'
    
   >>> reverse_letters("I code Python")
    'I edoc nohtyP'
    """
    return " ".join([word[::-1] for word in input_str.split()])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
