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
    erasure_prob = 0.5,
    erasure_prob2 = 0.4,
    erasure_prob_feedback = 0.4
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
        p_i_h, p_i = transmitter.send_packet(i, size)
        
        # Channel erasure
        if channel_erasure_model == 'Bernouli':
            lost = bernouli_erasure(erasure_prob)
        elif channel_erasure_model == 'Gilbert-Elliot':
            previous_status = gateway.received_packet_list[i-1] if i>=0 else False
            lost = gilbert_elliot_erasure( previous_status, erasure_prob, erasure_prob2)

        # Receiver's side
        gateway.update_packet_reception(i, lost)

        if not lost:
            gateway.receive_packet(p_i_h, p_i, size)
        
        if i % feedback_interval==0:
            feedback = gateway.send_feedback(i, delay_tolerance)
            
            if feedback:
                lost = bernouli_erasure(erasure_prob_feedback)
                if not lost:
                    transmitter.store_feedback(i, feedback)
        

    # Analysis
    reception_rate = sum(gateway.received_messages_list) /  number
    unreceived = number - sum(gateway.received_messages_list)
    dfr = unreceived/number

    print("Channel Erasure: ", channel_erasure_model)
    print("Erasure probability: ", erasure_prob)
    print("Number of messages: ", number)
    print("Delay Tolerance: ", delay_tolerance)
    print("Reception Rate: ", reception_rate)
    print("Number of unreceived packets: ", unreceived)
    print("Delivery Failure Rate: ", dfr)

    return dfr


if __name__=="__main__":
    system()
