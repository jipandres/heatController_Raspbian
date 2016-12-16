# heatController_Raspbian
Project to control a relay that switchs on/off a cauldron remotely using a Raspberry Pi with Raspbian

## The Cauldron
The cauldron must have support for a relay to switch on/off it.

In my case, I want to control a Domusa BioClass NG (http://www.domusateknik.com/en/products/biomass-boiler/pellet-boilers/bioclass-hm)

# Use Cases

## Check the status of the relay
It must be possible to check remotely using a web page hosted in this system if the cauldron is on/off.

1. End user connects to web page and finds a message with the status.

## Switch On the cauldron
It must be possible to switch on the cauldron remotely using a web page hosted in this system

1. End user connects to web page and finds a button to switch on the cauldron.
2. End user clicks on the button and the relay that enables the cauldron is activated.
3. End user receives confirmation that the order to the cauldron has been correctly executed.

## Switch Off the cauldron
It must be possible to switch off the cauldron remotely using a web page hosted in this system

1. End user connects to web page and finds a button to switch on the cauldron.
2. End user clicks on the button and the relay that enables the cauldron is activated.
3. End user receives confirmation that the order to the cauldron has been correctly executed.

## Configure periods to switch off the cauldron (during nights)
This is an extension of Switch On Use Case.
It allows to configure policies to switch off the cauldron automatically when it is on:
* Switch off during nights
* Switch off based on a weekly schedule 
* Switch off based on a season schedule
* Switch off if the environment temperature is too high for a long period of time

# Platform

Raspberry Pi (v1) with Raspbian Jessie installed and a WiFi dongle. Raspberry Pi v3 includes the WiFi.

A single relay connected to GPIO.

A set of LEDs to see the status.

## Wired connections figure

Insert figure
