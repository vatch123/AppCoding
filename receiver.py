"""
BTP Project - App Coding
"""

from utils import get_bin

class Receiver():

    def __init__(self, num_messages):
        self.received_messages_list = [False] * num_messages
        self.messages_list = [[]] * num_messages
        self.received_packet_list = [False] * num_messages
    

    def update_packet_reception(self, packet_number, status):
        self.received_packet_list[packet_number] = status

    
    def receive_packet(self, packet, packet_number, size):
        # Currently assuming only non-coded packets are being received
        for i in range(size):
            if (packet_number - i) >=0:
                self.messages_list[packet_number - i] = packet[i]
                self.received_messages_list[packet_number - i] = True
    
    def decode(self):
        pass


    def send_feedback(self, packet_number, delay_tolerance):
        # Interval of interest starting position
        lower = max(0, packet_number - delay_tolerance)
        
        try:
            index = self.received_messages_list.index(False, lower, packet_number + 1)
            num_unreceived = (delay_tolerance + 1) - sum(self.received_messages_list[lower:packet_number+1]) 
        except ValueError as _:
            index = None
        
        if index:
            feedback = str(int(self.received_messages_list[packet_number])) + get_bin(index, 8) + get_bin(num_unreceived, 8)
            return feedback
        else:
            return False


