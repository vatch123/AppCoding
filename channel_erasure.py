"""
This module contains various channel erasure models
"""


import numpy as np

def bernouli_erasure(success_prob):
    """
    It simulates a bernouli erasure channel

    Parameters
    ----------
    success_prob : `float`
        Probability that the message will be sucessfully delivered
    
    Returns
    -------
    `bool`
        Whether the current packet will be delivered or not

    """
    
    x = np.random.uniform(0,1)
    return True if x < success_prob else False


def gilbert_elliot_erasure(previous_status, Pbg, Pgb):
    """
    Simulates a Gilbert-Elliot channel as a two state markov chain

    Parameters
    ----------
    previous_state : `bool`
        Whether the previous message was delivered or not
    Pbg : `float`
        Probability of state transition from bad to good
    Pgb : `float`
        Probability of state transition from good to bad

    Returns
    -------
    `bool`
        Whether the current packet will be delivered or not
    """

    # Check if packet_number-1 was lost
    if not previous_status:
        x = np.random.uniform(0,1)
        return True if x < Pbg else False
    
    else:
        x = np.random.uniform(0,1)
        return True if x < 1 - Pgb else False

