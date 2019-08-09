def printProps(props, name, var):
    """
    Print the properties of var
    Args:
        props: a tuple of functions to call on var
        name : string to be printed (name of var)
        var  : variable of interest. This can be any type, but currently restricted to function objects without arguments
    Returns: 
        None
    Examples:
        utils.printProps((type, id, callable, len, sys.getrefcount), 'a', a)
    """   
    w = len(max([p.__name__ for p in props], key=len))
    for p in props:
        try:
            print("{:>{width}}({}) : {}".format(p.__name__, name, p(var), width=w))
        except TypeError:
            print("{:>{width}}({}) : {}".format(p.__name__, name, "cannot be called", width=w))
