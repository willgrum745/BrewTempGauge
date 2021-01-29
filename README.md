# BrewTempGauge

## JUST TEST CODE AT THE MOMENT NO ACTUAL USE YET

## Goal
The goal of this project is to create a GUI that integrates with Raspberry Pi in order to controll the temperature of fermentation for brewing.

## Hardware
* Raspberry Pi
* 4 Relay Module 
* Grove Controller
* Grove ADS Module for Pi
* 3.5 LCD Touch Screen for Pi

## To Do
* Make function so I can reuse increase/decrease command that will change parent without being a single global variable
* Pretify Code
* Full Screen
* GPIO control
  * Thermistor will attach to ADS module
  * Relay module will attach to GPIO pins 20+
  * When temp raises above set value turn relay on for that gauge
  * Turn on pump relay if any of the other relays are activated
* "Real time" updates on temp

## Schematic/Wiring Guide (TBD)
