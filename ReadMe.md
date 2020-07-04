# Disease Spreading Simulation

# Background:
In the past, there have been viral disease epidemics which have got out of hand.This project works on simulating the way such diseases spread.

# Source Data
A survey of 200 fake people, all with unique names and also their friends who are in regular contact with them are noted down in a connections.txt file.
Example Interpretaion of source data:
if a person with name Gill Bates has a connection with Jode Killam,Natacha,.....
it is made sure Jode Killam also has Gill Bates in his connection

# How the virus spreads
Each person is assigned a health point which changes over time dependingona person's health.

Division of health Points:
	76 - 100 health points: perfect health, not contagious
	75 health points: Average health, not contagious
	50 - 74 health points: fair health, not contagious
	30 - 49  health points: contagious
	0 - 29  health points: ccontagious

At the end of each day, each peron's immune system will natuarally add 5 points to that person, up to a maximum of 100 health points.

Note:
Maximum health points a person can have is 100 and a minimum is 0.


Meeting probability:
Each day, a person may or may not visit his/her friend. Probability of meeting is calculated based on random number generated.
if random number generated is 1.0, that person will meet each of his/her connections.
if random number generated is 0.0, that person will not meet any of his connection.
if random number generated is 0.33, that person will have a 33.33% chance of meeting his connection.

# Viral load:
The virus spreads when a contagious person passes a viral load to a person they are visiting, or a person who has visited them.

Viral load produced by a contagious person is given by the following formula 

Where 
V = viral load
H = Health points of a person

V = 5 + (((H - 25) ^ 2)/62)

Note: 
A person can be effected by a viral load even if they are already partly sick.


# Effect of Infection:
When a contagious person produces a viral load,every person they meet when visting (or being visited) will be infected by their viral load. If the viral load is small, a person is healthy, the person who is infected might not become sick, and they will qickly recover their health later when they sleep.

The change in health from receiving a viral load from another person is given by the fillowing formula

Where
HPa is ht current health points of the recipient before the viral load hits them
HPb is the new value of perso's health points after receiving the viral load.

HPb = HPa - (0.1 * L) if Hpa <= 29
HPb = HPa - (1.0 * L) if 29 < HPa < 50
HPb = HPa - (2.0 * L) if 50 <= Hpa

# Project was Divided into 3 tasks:

# Task 1:
	Getting a list of people from connection.txt file.
	Building people connection with the list of people provided.

# Task 2:
	Each person in task one is considered as patient
	Initial health points of patient zero is provided by used.
	Check if a person will meet his/her connection, If he meets check if the person is contagious. If he/she is contagious, infect the other person he/she meets
	Simulation should run for number of days provided by the user.
	Each day patient is put to sleep after he has met all his connections.
	Output shows number of people contagious at the end of each day.

# Task 3:
	Data produced from task 2 is used to produce a visual curve that shows number of people contagious at the end of each day.

	
