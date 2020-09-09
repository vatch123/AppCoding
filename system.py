"""
BTP project - Application Layer Coding
"""

# Import necessary modules
import sender
import receiver
import random
from channel_erasure import bernouli_erasure, gilbert_elliot_erasure

def system(
    length = 8,
    number = 10000,
    size = 4,
    delay_tolerance = 16,
    feedback_interval = 20,
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
    erasure_prob: Probabiltiy of packet lost in Bernouli/Gilbert
    erasure_prob2: Second probability in Gilbert
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
            previous_status = gateway.received_packet_list[i-1] if i>=0 else False
            lost = gilbert_elliot_erasure( previous_status, Pbg, Pgb)

        # Receiver's side
        gateway.update_packet_reception(i, lost)

        if not lost:
            gateway.receive_packet(p_i_h, p_i, size)
        
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
    system(channel_erasure_model='Bernouli')
