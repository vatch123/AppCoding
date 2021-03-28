"""
This module contains various functions related to the receiver
"""

from utils import get_bin, list2int, int2list

class Receiver():

    """
    This class forms the basic structure of the receiver object
    """

    def __init__(self, num_messages):
        """
        It intializes the receiver's state as empty (no message has been received)

        Parameters
        ----------
        num_messages : `int`
            Number of messages the receiver is expected to receive
        """

        self.received_messages_list = [False] * num_messages
        self.messages_list = [[]] * num_messages
        self.received_packet_list = [False] * num_messages
    

    def update_packet_reception(self, packet_number, received):
        """
        Updates the reception of the `packet_number` packet in the receiver's
        memory

        Parameters
        ----------
        packet_number : `int`
            The packet number whose is reception state is being stored
        received : `bool`
            whether the packet was received or not
        """
        self.received_packet_list[packet_number] = received

    
    def receive_packet(self, packet_header, packet, size):
        """
        Receive a packet and split it into its constituent symbols
        
        Parameters
        ----------
        packet_header : `list` or `int`
            stores information about the constituent symbols whether coded or not and with
            what symbols
        packet : `list`
            actual contents of the packet
        size : `int`
            Number of symbols in the packet
        """

        for packet_number, message in zip(packet_header, packet):
            if type(packet_number) is list:
                self.decode(packet_number, message)
            else:
                self.messages_list[packet_number] = message
                self.received_messages_list[packet_number] = True 

    
    def decode(self, coding_list, coded_message):
        """
        Decodes a coded symbol

        Parameters
        ----------
        coding_list : `list`
            List of symbols which has been coded together
        coded_message : `list`
            The actual message
        """

        ans = 0
        for idx in coding_list:
            ans += self.received_messages_list[idx]

        if ans == len(coding_list):
            # print('All packets are already present')
            pass
        elif ans < len(coding_list) - 1:
            # print('Decoding cannot be done as more than one messages are missing')
            pass
        else:
            coded_message = list2int(coded_message)
            for idx in coding_list:
                if self.received_messages_list[idx]:
                    coded_message = coded_message ^ list2int(self.messages_list[idx])
                else:
                    decoded_idx = idx
            
            self.messages_list[decoded_idx] = int2list(coded_message, 8)
            self.received_messages_list[decoded_idx] = True


    def send_feedback(self, packet_number, delay_tolerance):
        """
        Generate feedback for the sender

        Parameters
        ----------
        packet_number : `int`
            The current packet number received
        delay_tolerance : `int`
            The delay tolerance
        
        Returns
        -------
        `list`
            The feedback for the sender
        """
        # Interval of interest starting position
        lower = max(0, packet_number - delay_tolerance + 1)
        
        try:
            index = packet_number - self.received_messages_list.index(False, lower, packet_number+1)
            num_unreceived = (packet_number + 1 - lower) - sum(self.received_messages_list[lower:packet_number+1]) 
        except ValueError as _:
            index = 0
            num_unreceived = 0

        feedback = str(int(self.received_messages_list[packet_number])) + get_bin(index, 8) + get_bin(num_unreceived, 8)
        return feedback

