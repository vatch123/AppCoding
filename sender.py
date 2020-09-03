"""
BTP Project - App Coding
"""

from math import comb
import random
from utils import int2list, list2int

class Sender():

    def __init__(self, messages, delay_tolerance):
        self.feedback = None
        self.feedback_packet = None
        self.messages_list = messages
        self.sent_list = [False] * len(messages)
        self.delay_tolerance = delay_tolerance
    
    def send_packet(self, packet_number, size):
        """
        size: No. of 8 bit messages that can be in a packet
        """

        packet = [self.messages_list[packet_number]]
        packet_header = [packet_number]

        if self.feedback_packet is packet_number - 1:
            oldest_undelivered = int(self.feedback[1:9], 2)
            num_missing = int(self.feedback[9:], 2)
            if oldest_undelivered < packet_number:
                packet.append(self.messages_list[oldest_undelivered])
                packet_header.append(oldest_undelivered)
                if num_missing > 1:
                    if packet_number - oldest_undelivered <= size - 1:
                        for i in range(oldest_undelivered + 1, oldest_undelivered + num_missing):
                            packet.append(self.messages_list[i])
                            packet_header.append(i)
                    elif packet_number - oldest_undelivered > size - 1 and num_missing == packet_number - oldest_undelivered:
                        for i in range(oldest_undelivered + 1, oldest_undelivered + size - 1):
                            packet.append(self.messages_list[i])
                            packet_header.append(i)
                    elif packet_number - oldest_undelivered > size - 1 and 1 < num_missing < packet_number - oldest_undelivered:
                        interest_list = self.messages_list[oldest_undelivered + 1:packet_number]
                        for _ in range(size - 2):
                            coded_message, coding_list = self.code(interest_list, packet_number, oldest_undelivered, num_missing)
                            packet.append(coded_message)
                            packet_header.append(coding_list)
        else:

            # TODO: Decide what to do first when no feedback is present
            if self.feedback:
                oldest_undelivered = int(self.feedback[1:9], 2)
            else:
                oldest_undelivered = 0
            z = min(packet_number - oldest_undelivered, self.delay_tolerance)

            # TODO: Check for reversal here
            interest_list = self.messages_list[packet_number - z:packet_number]
            if z < size-1:
                for pack in interest_list:
                    packet.append(pack)
            else:
                for _ in range(size-1):
                    coded_message, coding_list = self.code(interest_list=interest_list, oldest_undelivered=oldest_undelivered,
                                                            packet_number=packet_number, distribution='uniform')
                    packet.append(coded_message)
                    packet_header.append(coding_list)
        
        return (packet_header, packet)


    def code(self, interest_list=None, packet_number=None, oldest_undelivered=None, num_missing=None, distribution=None):

        if distribution == 'uniform':
            z = min(packet_number - oldest_undelivered, self.delay_tolerance)
            coding_degree = random.randint(1,z)
            base_index = packet_number - z

        else:
            probs = [(num_missing - 1) * comb(packet_number - oldest_undelivered - num_missing, d - 1) /
                        comb(packet_number - oldest_undelivered - 1, d) for d in range(1, packet_number - oldest_undelivered)]
            coding_degree = probs.index(max(probs))
            base_index = oldest_undelivered + 1

        coded_message = int('000000000', 2)
        coding_list = []
        for _ in range(coding_degree):
            idx = random.randint(0,len(interest_list)-1)
            coded_message = coded_message ^ list2int(interest_list[idx])
            coding_list.append(base_index + idx)
        
        coded_message = int2list(coded_message, 8)
        
        return (coded_message, coding_list)

    
    def store_feedback(self, packet_number, feedback):
        self.feedback = feedback
        self.feedback_packet = packet_number
    

