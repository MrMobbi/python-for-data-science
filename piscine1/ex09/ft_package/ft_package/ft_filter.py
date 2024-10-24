

def ft_filter(string, nbr):
    """
    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    """
    list = string.split(' ')
    return_list = [item for item in list if
                   (lambda item: len(item) > nbr)(item)]
    return return_list
