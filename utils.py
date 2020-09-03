
def get_bin(x, n=0):
    """
    Get the binary representation of x.

    Parameters
    ----------
    x : int
    n : int
        Minimum number of digits. If x needs less digits in binary, the rest
        is filled with zeros.

    Returns
    -------
    str
    """

    return format(x, 'b').zfill(n)

def list2int(x):
    """
    Converts a binary list to number
    """

    return int("".join(str(i) for i in x), 2)


def int2list(x, n=0):
    """
    Convert a number to binary list
    """

    x = get_bin(x,n)
    return [int(s) for s in x]
