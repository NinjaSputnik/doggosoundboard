import pygame.mixer         # Module for loading and playing sounds
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
import logging
import threading
import concurrent.futures
from gpiozero import Button    # from some tutorial online

# CONS with this structure of the code
# The counter that decides the delay of when to replay the sound depends on how many times the while loop executes
# Especially if there is no "sleep" in the while loop, this will become very hardware dependent.



# Try this: 
# sndA = pygame.mixer.Sound("buzzer.wav")
# btn_sndA = Button(4)     # 4 is from a tutorial, maybe this indicates the gpio?
# btn_sndA.when_pressed = sndA.play


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)

# TODO: check that pygame.mixer is available and initialized


# Create sound objects
sndA = pygame.mixer.Sound("buzzer.wav")
sndB = pygame.mixer.Sound("clap.wav")
sndC = pygame.mixer.Sound("text.wav")


# Create channel objecs
# One for each sound or just 3 channels because not more than three sounds should be allowed to play at the same time?
# pygame.mixer.set_num_channels
soundChannelA = pygame.mixer.Channel(1) 
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)
soundChannelD = pygame.mixer.Channel(4)

# def playSound(sound):
#     # pygame.mixer.find_channel
#     print("Hello Sound")

print("Sampler Ready.")

# TODO
# instead of while loop, try to just have the program listening for buttonpress (even listener)
statusA_prev = False
statusB_prev = False
statusC_prev = False

counterA = 0
counterB = 0
counterC = 0

while True:       
   try:
      # Fetch status of th buttons
      statusA = GPIO.input(23)
      statusB = GPIO.input(24)
      statusC = GPIO.input(25)

      # For debugging purposes
      print(GPIO.input(23))
      print(GPIO.input(24))
      print(GPIO.input(25))

      # Check if a button has been pressed
      # aka its status has gone from False to True
      if (statusA == True):
         if (statusA_prev == False):
            soundChannelA.play(sndA)
      # If the button has been pressed for a long time, play the sound again
      elif ((statusA == False) and (counterA == 1000)):
         soundChannelA.play(sndA)
         counterA = 0
      elif ((statusA == False) and (statusA_prev == False)):
         counterA = counterA + 1 

      if (statusB == True):
         if (statusB_prev == False):
            soundChannelB.play(sndB)
      elif ((statusB == False) and (counterB == 1000)):
         soundChannelB.play(sndB)
         counterB = 0
      elif ((statusB == False) and (statusB_prev == False)):
         counterB = counterB + 1 

      if (statusC == True):
         if (statusC_prev == False):
            soundChannelC.play(sndC)
      # If the button has been pressed for a long time, play the sound again
      elif ((statusC == False) and (counterC == 1000)):
         soundChannelC.play(sndC)
         counterC = 0
      elif ((statusC == False) and (statusC_prev == False)):
         counterC = counterC + 1 
      

      # Store current status as prev status for the next iteration of the loop
      statusA_prev = statusA
      statusB_prev = statusB
      statusC_prev = statusC



      # Sleep or no sleep?
      # If too long sleep, risk of a button going True and then False quickly after, and the True will be missed by the program
      # A low risk though since dogs tend to stand/put their weight on the button
      sleep(0.1)
      
   except KeyboardInterrupt:
      exit()
