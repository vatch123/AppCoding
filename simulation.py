"""
BTP Project - App Coding
Simulation Code
"""

import matplotlib.pyplot as plt
from system import system
import sys
import argparse

num = 5 # Number of simulations currently in the system

def run_simulations(simulation='all'):

    length = 8
    number = 10000
    delay_tolerance = 16
    feedback_interval = 1

    if simulation == 'all':
        for i in range(1, num+1):
            run_simulations(str(i))

    elif simulation == '1':
        """
        Simulation 1:
            Constants:
                size = 2
                erasure_prob_feedback = 0.75    TODO: Check with the simulation in paper. This
                                                    should be different I guess
                other parameters = default
            
            Sweep Over:
                "Packet Sucess Probability"

        """
        print("###################################################")
        print("Simulation 1: DFR vs Packet Delivery Probability (Bernouli) (Size = 2, Feedback Erasure = 0.75)")
        print("###################################################")
        erasures = [i/50 for i in range(51)]
        packet_success = [1 - i/50 for i in range(51)]
        dfr_icc = []
        for erasure_prob in erasures:
            dfr_icc.append(system(
                length = length,
                number = number,
                size = 2,
                delay_tolerance = delay_tolerance,
                feedback_interval = feedback_interval,
                channel_erasure_model = 'Bernouli',
                Pbg = erasure_prob,
                erasure_prob_feedback = 0.75,
                scheme='ICC'
            ))
        
        dfr_rr = []
        for erasure_prob in erasures:
            dfr_rr.append(system(
                length = length,
                number = number,
                size = 2,
                delay_tolerance = delay_tolerance,
                feedback_interval = feedback_interval,
                channel_erasure_model = 'Bernouli',
                Pbg = erasure_prob,
                erasure_prob_feedback = 0.75,
                scheme='repetition'
            ))

        plt.figure()
        plt.title("Simulation 1: DFR vs Packet Delivery Probability (Bernouli) (Size = 2, Feedback Erasure = 0.75)", fontsize=12)
        plt.plot(packet_success, dfr_icc, label='Windowed Coding')
        plt.plot(packet_success, dfr_rr, label='Repetition Redundancy')
        plt.xlabel('Packet Delivery Probability')
        plt.ylabel('Delivery Failure Rate')
        plt.yscale('log')
        plt.grid()
        plt.tight_layout()
        plt.legend(loc='upper right')

        print("###################################################")

    elif simulation == '2':
        """
        Simulation 2:
            Constants:
                size = 3
                erasure_prob_feedback = 0.25    TODO: Check with the simulation in paper. This
                                                    should be different I guess
                other parameters = default
            
            Sweep Over:
                "Packet Sucess Probability"

        """
        print("###################################################")
        print("Simulation 2: DFR vs Packet Delivery Probability (Bernouli) (Size = 3, Feedback Erasure = 0.25)")
        print("###################################################")
        erasures = [i/50 for i in range(51)]
        packet_success = [1 - i/50 for i in range(51)]
        dfr_icc = []
        for erasure_prob in erasures:
            dfr_icc.append(system(
                length = length,
                number = number,
                size = 3,
                delay_tolerance = delay_tolerance,
                feedback_interval = feedback_interval,
                channel_erasure_model = 'Bernouli',
                Pbg = erasure_prob,
                erasure_prob_feedback = 0.25,
                scheme='ICC'
            ))

        dfr_rr = []
        for erasure_prob in erasures:
            dfr_rr.append(system(
                length = length,
                number = number,
                size = 3,
                delay_tolerance = delay_tolerance,
                feedback_interval = feedback_interval,
                channel_erasure_model = 'Bernouli',
                Pbg = erasure_prob,
                erasure_prob_feedback = 0.25,
                scheme='repetition'
            ))

        plt.figure()
        plt.title("Simulation 2: DFR vs Packet Delivery Probability (Bernouli) (Size = 3, Feedback Erasure = 0.25)", fontsize=12)
        plt.plot(packet_success, dfr_icc, label='Windowed Coding')
        plt.plot(packet_success, dfr_rr, label='Repetition Redundancy')
        plt.xlabel('Packet Delivery Probability')
        plt.ylabel('Delivery Failure Rate')
        plt.yscale('log')
        plt.grid()
        plt.tight_layout()
        plt.legend(loc='upper right')

        print("###################################################")

    elif simulation == '3':
        
        """
        Simulation 3:
            Constants:
                size = 3
                erasure_prob = 0.4    TODO: Check with the simulation in paper. This
                                                    should be different I guess
                other parameters = default
            
            Sweep Over:
                "Feedback Reception Probability"

        """
        print("###################################################")
        print("Simulation 3: DFR vs Feedback Reception Probability (Bernouli) (Size = 4, Erasure = 0.4)")
        print("###################################################")

        # TODO: the probability of feedback in paper and for our case is different
        # as our feedback itself is intermittent. So for some packets the probability of 
        # feedback is 0, but for the paper it some fixed number. Our feedback erasure probability
        # is the probability with which feedback is lost if sent.
        feedback_erasure = [i/50 for i in range(51)]
        feedback_success = [1 - i/50 for i in range(51)]
        dfr_icc = []
        for erasure_prob in feedback_erasure:
            dfr_icc.append(system(
                length = length,
                number = number,
                size = 4,
                delay_tolerance = delay_tolerance,
                feedback_interval = feedback_interval,
                channel_erasure_model = 'Bernouli',
                Pbg = 0.4,
                erasure_prob_feedback = erasure_prob,
                scheme='ICC'
            ))

        dfr_rr = []
        for erasure_prob in feedback_erasure:
            dfr_rr.append(system(
                length = length,
                number = number,
                size = 4,
                delay_tolerance = delay_tolerance,
                feedback_interval = feedback_interval,
                channel_erasure_model = 'Bernouli',
                Pbg = 0.4,
                erasure_prob_feedback = erasure_prob,
                scheme='repetition'
            ))

        plt.figure()
        plt.title("Simulation 3: DFR vs Feedback Reception Probability (Bernouli) (Size = 4, Erasure = 0.4)", fontsize=12)
        plt.plot(feedback_success, dfr_icc, label='Windowed Coding')
        plt.plot(feedback_success, dfr_rr, label='Repetition Redundancy')
        plt.xlabel('Feedback Reception Probability')
        plt.ylabel('Delivery Failure Rate')
        plt.yscale('log')
        plt.grid()
        plt.tight_layout()
        plt.legend(loc='upper right')

        print("###################################################")
    
    elif simulation == '4':
        """
        Simulation 4:
            Constants:
                Pgb = 0.2
                other parameters = default
            
            Sweep Over:
                Pbg

        """
        print("###################################################")
        print("Simulation 4: DFR vs Pbg (Gilbert-Elliot) (Size = 3, Feedback Erasure = 0.7)")
        print("###################################################")
        erasures = [i/50 for i in range(51)]
        packet_success = [1 - i/50 for i in range(51)]
        dfr_icc = []
        for erasure_prob in erasures:
            dfr_icc.append(system(
                length = length,
                number = number,
                size = 3,
                delay_tolerance = delay_tolerance,
                feedback_interval = feedback_interval,
                channel_erasure_model = 'Gilbert-Elliot',
                Pbg = erasure_prob,
                Pgb = 0.2,
                erasure_prob_feedback = 0.7,
                scheme='ICC'
            ))

        dfr_rr = []
        for erasure_prob in erasures:
            dfr_rr.append(system(
                length = length,
                number = number,
                size = 3,
                delay_tolerance = delay_tolerance,
                feedback_interval = feedback_interval,
                channel_erasure_model = 'Gilbert-Elliot',
                Pbg = erasure_prob,
                Pgb = 0.2,
                erasure_prob_feedback = 0.7,
                scheme='repetition'
            ))

        plt.figure()
        plt.title("Simulation 4: DFR vs Pbg (Gilbert-Elliot) (Size = 3, Feedback Erasure = 0.7)", fontsize=12)
        plt.plot(packet_success, dfr_icc, label='Windowed Coding')
        plt.plot(packet_success, dfr_rr, label='Repetition Redundancy')
        plt.xlabel('Probability bad to good')
        plt.ylabel('Delivery Failure Rate')
        plt.yscale('log')
        plt.grid()
        plt.tight_layout()
        plt.legend(loc='upper right')

        print("###################################################")
    
    elif simulation == '5':
        """
        Simulation 5:
            Constants:
                Pgb = 0.3
                Pbg = 0.6
                feedback_erasure = 0.5
                other parameters = default
            
            Sweep Over:
                delay_tolerance

        """
        print("###################################################")
        print("Simulation 5: DFR vs Delay Tolerance")
        print("###################################################")
        delays_list = [i for i in range(4,19)]
        dfr_icc = []
        for delay in delays_list:
            dfr_icc.append(system(
                length = length,
                number = number,
                size = 3,
                delay_tolerance = delay,
                feedback_interval = feedback_interval,
                channel_erasure_model = 'Gilbert-Elliot',
                Pbg = 0.6,
                Pgb = 0.3,
                erasure_prob_feedback = 0.5,
                scheme='ICC'
            ))

        dfr_rr = []
        for delay in delays_list:
            dfr_rr.append(system(
                length = length,
                number = number,
                size = 3,
                delay_tolerance = delay,
                feedback_interval = feedback_interval,
                channel_erasure_model = 'Gilbert-Elliot',
                Pbg = 0.6,
                Pgb = 0.3,
                erasure_prob_feedback = 0.5,
                scheme='repetition'
            ))

        plt.figure()
        plt.title("Simulation 5: DFR vs Delay Tolerance (Size = 3, Feedback Erasure = 0.5)", fontsize=12)
        plt.plot(delays_list, dfr_icc, label='Windowed Coding')
        plt.plot(delays_list, dfr_rr, label='Repetition Redundancy')
        plt.xlabel('Delay Tolerance')
        plt.ylabel('Delivery Failure Rate')
        plt.yscale('log')
        plt.grid()
        plt.tight_layout()
        plt.legend(loc='upper right')

        print("###################################################")
    



if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", help="Run the particular simulation")
    args = parser.parse_args()
    if not args.number:
        args.number = 'all'
    sys.stdout = open('./logs/simulation_'+ args.number +'_results.txt', 'w')
    run_simulations(args.number)
    plt.show()
    sys.stdout.close()
