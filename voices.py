import random
import time

# Define a list of possible voice messages
voice_messages = ["You're worthless", "No one loves you", "They're watching you", "Kill yourself", "You're a failure", "You're going to die"]

# Define the frequency of voice messages in seconds
frequency = 10

# Define the number of voice messages to play
num_messages = 5

# Define a function to simulate the experience of hearing voices
def simulate_voices():
    for i in range(num_messages):
        message = random.choice(voice_messages)
        print("Voice message: " + message)
        time.sleep(frequency)

# Call the function to start the simulation
simulate_voices()