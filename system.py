"""
BTP project - Application Layer Coding
"""

# Import necessary modules
import sender
import receiver
import random
from channel_erasure import bernouli_erasure, gilbert_elliot_erasure
import argparse

def system(
    length = 8,
    number = 10000,
    size = 4,
    delay_tolerance = 16,
    feedback_interval = 1,
    channel_erasure_model = 'Gilbert-Elliot',
    Pbg = 0.5,
    Pgb = 0.4,
    erasure_prob_feedback = 0.4,
    scheme = 'ICC'
):
    """
    length: 8 bit message
    number: No. of messages
    size: No. of messages in a packet
    delay_tolerance: No. of previous packets of interest at the current moment
    feedback_interval: Feedback sent after every these many packets
    channel_erasure_model: Type of channel erasure
    Pbg: Probability of transition from bad to good
    Pgb: Probability of transition from good to bad
    erasure_prob_feedback: Feedback erasure probability
    """

    # Placeholder for all packets
    messages = [[random.randint(0,1) for _ in range(length)]] * number

    # Create a sender
    transmitter = sender.Sender(messages, delay_tolerance)

    # Creating a receiver
    gateway = receiver.Receiver(number)

    # Transmission
    for i in range(number):
        # Senders' side
        p_i_h, p_i = transmitter.send_packet(i, size, scheme)
        
        # Channel erasure
        if channel_erasure_model == 'Bernouli':
            lost = bernouli_erasure(Pbg)
        elif channel_erasure_model == 'Gilbert-Elliot':
            previous_status = gateway.received_packet_list[i-1] if i>=0 else True
            lost = gilbert_elliot_erasure(previous_status, Pbg, Pgb)

        # Receiver's side
        gateway.update_packet_reception(i, lost)

        if not lost:
            gateway.receive_packet(p_i_h, p_i, size)
        
            # The feedback is sent for each received packet
            if i % feedback_interval==0:
                # TODO: If none of the last packets are missing what to do
                feedback = gateway.send_feedback(i, delay_tolerance)

                if feedback:
                    lost = bernouli_erasure(erasure_prob_feedback)
                    if not lost:
                        transmitter.store_feedback(i, feedback)
        

    # Analysis
    reception_rate = sum(gateway.received_messages_list) /  number
    unreceived = number - sum(gateway.received_messages_list)
    dfr = unreceived/number

    print("********")

    print("Channel Erasure: ", channel_erasure_model)
    if channel_erasure_model=='Gilbert-Elliot':
        print("Probability bad to good: ", Pbg)
        print('Probability good to bad: ', Pgb)
    elif channel_erasure_model=='Bernouli':
        print('Erasure Probability: ', Pbg)
    print("Number of messages: ", number)
    print("Delay Tolerance: ", delay_tolerance)
    print("Reception Rate: ", reception_rate)
    print("Number of unreceived packets: ", unreceived)
    print("Delivery Failure Rate: ", dfr)

    print("********")

    return dfr


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', help='Length of one message in binary', type=int, default=8)
    parser.add_argument('-n', '--number', help='Number of messages to transmit', type=int, default=10000)
    parser.add_argument('-c', '--channel', help='The channel erasure model', choices=['Bernouli', 'Gilbert-Elliot'], type=str, default='Bernouli')
    parser.add_argument('-s', '--size', help='Size of the packet', type=int, default=4)
    parser.add_argument('-d', '--delay_tolerance', help='Delay Tolerance', type=int, default=16)
    parser.add_argument('-pbg', '--pbg', help='Channel Erasure Probability for Bernouli or Probability of good to bad transition in Gilbert Elliot', type=float, default=0.5)
    parser.add_argument('-pgb', '--pgb', help='Probability of bad to good transition in Gilbert Elliot', type=float, default=0.4)
    parser.add_argument('-f', '--feedback_erasure', help='Feedback erasure probability', type=float, default=0.4)
    parser.add_argument('-i', '--feedback_interval', help='The interval of sending feedback', type=int, default=1)
    parser.add_argument('--scheme', help='The coding scheme to use', choices=['ICC', 'repetition'], type=str, default='ICC')
    args = parser.parse_args()

    system(
        length = args.length,
        number = args.number,
        size = args.size,
        delay_tolerance = args.delay_tolerance,
        feedback_interval = args.feedback_interval,
        channel_erasure_model = args.channel,
        Pbg = args.pbg,
        Pgb = args.pgb,
        erasure_prob_feedback = args.feedback_erasure,
        scheme = args.scheme
    )

