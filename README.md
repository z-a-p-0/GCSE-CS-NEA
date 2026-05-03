# Rolling Dice Game

This was my GCSE Computer Science Non-Exam Assessment, made before all these AIs were taking over the coding world.

## Requirements to Run

Uses Python 3.9.6 and Pygame 2.5.1

All the code is in the .py file

Needs a .txt file called "ZAP.txt" in the same folder for the local leaderboard.
This name can be changed if you want to for some reason on lines 2614 and 2642

Modules imported: random, time, pygame, math

## Features

Dice are proper cubes rendered as their 8 vertices and lines drawn between them where needed, with the visible faces having their pits on.

Local multiplayer (2 players) with a leaderboard stored in ZAP.txt

Login stage with login details in lines 13-24

The sybmols, letters, numbers, etc is all hard-coded in with the specific way all of this is stored visible in lines 48-662

The dice work by having a random start orientation then  being rolled and whichever face is on the top is then the actual number used.

A tutorial is available, as well as credits and different theme colours

## Rounds & Scoring

There are 5 rounds
Each round each player rolls 2 dice

The sum of the points on the dice is added to your score
If the sum is even you get a bonus 10 points
If the sum is odd you lose 5 points

If you roll a double you get a bonus roll

After 5 rounds the person with the highest score wins

If there's a draw the players both roll an extra die and the greatest roll wins (keep rollign until a greatest roll emerges)

(We didn't get to choose the game design here)

## Creator Notes

Was definitely enjoyable and an experience to code.
Could've done something basic and text based, but there's no fun in that.

The rendering of the dice as cubes with pits on and all of that logic and implementation was definitely one of the more difficut parts, but I'd say it was worth it.

Hope you enjoy seeing it just as much!
