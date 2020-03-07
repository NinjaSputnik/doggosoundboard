import pygame.mixer         # Module for loading and playing sounds
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
import logging
import threading
import concurrent.futures


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)

# TODO: Test that pygame.mixer is available and initialized


# Create sound objects
sndA = pygame.mixer.Sound("buzzer.wav")
sndB = pygame.mixer.Sound("clap.wav")
sndC = pygame.mixer.Sound("text.wav")


# Create channel objecs
# pygame.mixer.set_num_channels
soundChannelA = pygame.mixer.Channel(1) 
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)
soundChannelD = pygame.mixer.Channel(4)

# def playSound(sound):
#     # pygame.mixer.find_channel
#     print("Hello Sound")

print("Sampler Ready.")

while True:
   try:
      if (GPIO.input(23) == True):
         soundChannelA.play(sndA)
         # TODO: Pause channel for a while so sound
         #dosent play immidiately if button is held in
      if (GPIO.input(24) == True):
         soundChannelB.play(sndB)
      if (GPIO.input(25) == True):
          soundChannelC.play(sndC)
      print(GPIO.input(23))
      print(GPIO.input(24))
      print(GPIO.input(25))
      sleep(0.1)
   except KeyboardInterrupt:
      exit()
