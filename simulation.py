"""
BTP Project - App Coding
Simulation Code
"""

import matplotlib.pyplot as plt
from system import system
import sys

def run_simulations():

    """
    Simulation 1:
        Constants:
            size = 2
            erasure_prob_feedback = 0.75    TODO: Check with the simulation in paper. This
                                                  should be different I guess
            other parameters = default
        
        Sweep Over:
            "Packet Sucess Probability"
            For Gilbert-Elliot: erasure_prob and erasure_prob2 = erasure_prob - 0.1

    """
    erasures = [i/50 for i in range(51)]
    packet_success = [1 - i/50 for i in range(51)]
    dfr = []
    for erasure_prob in erasures:
        dfr.append(system(
            length = 8,
            number = 10000,
            size = 2,
            delay_tolerance = 16,
            feedback_interval = 20,
            channel_erasure_model = 'Gilbert-Elliot',
            erasure_prob = erasure_prob,
            erasure_prob2 = max(0, erasure_prob - 0.1),
            erasure_prob_feedback = 0.4
        ))

    plt.plot(packet_success, dfr)
    plt.show()


if __name__=='__main__':
    sys.stdout = open('./logs/simulation_results.txt', 'w')
    run_simulations()
    sys.stdout.close()
