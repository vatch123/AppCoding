"""
BTP project - Application Layer Coding
"""

# Import necessary modules
import numpy as np
import sender
import receiver
from channel_erasure import bernouli_erasure, gilbert_elliot_erasure

# Creating a set of messages
length = 8   # 8 bit message
number = 10000  # No. of messages
size = 4 # No. of messages in a packet

# Placeholder for all packets
messages = [np.zeros((length, 1))] * number

# Create a sender
transmitter = sender.Sender(messages)

# Creating a receiver
gateway = receiver.Receiver(number)

# Transmission
for i in range(number):
    # Senders' side
    p_i = transmitter.send_packet(i, size)
    
    # Channel erasure
    # lost = bernouli_erasure(0.4)
    previous_status = gateway.received_packet_list[i-1] if i>=0 else False
    lost = gilbert_elliot_erasure( previous_status, 0.5, 0.4)

    gateway.update_packet_reception(i, lost)

    if not lost:
        gateway.receive_packet(p_i, i, size)
    

# Analysis
reception_rate = np.sum(gateway.received_messages_list) /  number
print(reception_rate)
