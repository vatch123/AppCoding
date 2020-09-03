"""
BTP project - Application Layer Coding
"""

# Import necessary modules
import sender
import receiver
import random
from channel_erasure import bernouli_erasure, gilbert_elliot_erasure

# Creating a set of messages
length = 8   # 8 bit message
number = 10000  # No. of messages
size = 4 # No. of messages in a packet
delay_tolerance = 16 # No. of previous packets of interest at the current moment
feedback_interval = 20 # Feedback sent after every 20 packets

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
    # lost = bernouli_erasure(0.4)
    previous_status = gateway.received_packet_list[i-1] if i>=0 else False
    lost = gilbert_elliot_erasure( previous_status, 0.5, 0.4)

    # Receiver's side
    gateway.update_packet_reception(i, lost)

    if not lost:
        gateway.receive_packet(p_i_h, p_i, size)
    
    if i % feedback_interval==0:
        feedback = gateway.send_feedback(i, delay_tolerance)
        
        if feedback:
            lost = bernouli_erasure(0.4)
            if not lost:
                transmitter.store_feedback(i, feedback)
    

# Analysis
reception_rate = sum(gateway.received_messages_list) /  number
print(reception_rate)
