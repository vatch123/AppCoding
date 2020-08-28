"""
BTP Project - App Coding
"""

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

    def send_feedback(self):
        pass

