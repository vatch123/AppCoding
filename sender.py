"""
BTP Project - App Coding
"""

class Sender():

    def __init__(self, messages):
        self.feedback_list = []
        self.messages_list = messages
        self.sent_list = [False] * len(messages)
    
    def send_packet(self, packet_number, size):
        """
        size: No. of 8 bit messages that can be in a packet
        """

        # Currently sending the last "size" messages
        # TODO: Deal with feedback and coding

        packet = []

        for i in range(size):
            if(packet_number-i)>=0:
                packet.append(self.messages_list[packet_number - i])
                self.sent_list[packet_number - i] = True
        
        return packet
    
    def store_feedback(self, feedback):
        self.feedback_list.append(feedback)
    

    def code(self):
        pass

