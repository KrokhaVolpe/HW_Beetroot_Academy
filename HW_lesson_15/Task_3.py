#Task 3
"""
TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
 
The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.

CHANNELS = ["BBC", "Discovery", "TV1000"]

 class TVController:

pass

 controller = TVController(CHANNELS)

controller.first_channel() == "BBC"

controller.last_channel() == "TV1000"

controller.turn_channel(1) == "BBC"

controller.next_channel() == "Discovery"

controller.previous_channel() == "BBC"

controller.current_channel() == "BBC"

controller.exists(4) == "No"

controller.exists("BBC") == "Yes"
"""

class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.current_channels_index = 0

    def first_channel(self):
        self.current_channels_index = 0
        return  self.current_channel()

    def last_channel(self):
        self.current_channels_index = len(self.channels) - 1 
        return self.channels[- 1]

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
             self.current_channels_index = N - 1
        return  self.current_channel()

    def next_channel(self):
       self.current_channels_index = (self.current_channels_index + 1) % len(self.channels)
       return self.current_channel()

    def previous_channel(self):
        self.current_channels_index = (self.current_channels_index - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_channels_index]

    def exists(self, N_or_name):
        if isinstance(N_or_name, int):
            return "Yes" if 1 <= N_or_name <= len(self.channels) else "No"
        elif isinstance (N_or_name, str):
            return "Yes" if N_or_name in self.channels else "No"
        else:
            return "No"
        
        

    
CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print(controller.first_channel() == "BBC")
print(controller.last_channel() == "TV1000")
print(controller.turn_channel(1) == "BBC")
print(controller.next_channel() == "Discovery")
print(controller.previous_channel() == "BBC")
print(controller.current_channel() == "BBC")
print(controller.exists(4) == "No")
print(controller.exists("BBC") == "Yes")
