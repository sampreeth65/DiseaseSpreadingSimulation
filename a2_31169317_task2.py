"""
Student Name : Sampreeth Amith Kumar
Student ID : 31169317
Start Date : 20/05/2020
Last Modified Date : 07/06/2020
Description : Simulating disease spread
             Meeting probability of a connection is
             first found, if the person meets his connection
             and if either of them is contagious, disease will spread
             to the other person.
"""
from a2_31169317_task1 import *
from random import random


class Patient(Person):
    """Patient class Inheriting Person class."""
    def __init__(self, first_name, last_name, health):
        """Constructor to store the first name,last name
            and health of a patient instance."""
        super(Patient, self).__init__(first_name, last_name)
        if health < 0:
            """Health points should not go below zero."""
            self.health = 0
        elif health > 100:
            """Health points can't be more than 100."""
            self.health = 100
        else:
            self.health = health

    def get_health(self):
        """Returns the health of the patient instance."""
        return round(self.health)

    def set_health(self, new_health):
        """Sets the health of the patient instance."""
        if new_health < 0:
            """Health points can't be below zero."""
            self.health = 0
        elif new_health > 100:
            """Health points can't be above 100."""
            self.health = 100
        else:
            self.health = new_health

    def is_contagious(self):
        """Returns boolean true when a patient is contagious."""
        if self.health >= 0 and self.health <= 49:
            return True
        elif self.health >= 50 and self.health <= 100:
            return False

    def infect(self, viral_load):
        """If a patient is contagious, He/she will infect when
            he meets someone."""
        if self.health <= 29:
            self.health = self.health - (0.1 * viral_load)
        elif self.health > 29 and self.health < 50:
            self.health = self.health - (1.0 * viral_load)
        elif self.health > 50:
            self.health = self.health - (2.0 * viral_load)

    def sleep(self):
        """Patient is put to sleep after each day."""
        self.health += 5
        if self.health > 100:
            self.health = 100


def run_simulation(days, meeting_probability, patient_zero_health):
    """All the patients initial health is set to 75, as provided,
        and health of patient at index zero is set by the argument
        patient_zero_health."""
    patient = load_patients(75)
    patient[0].set_health(patient_zero_health)
    each_day_effected_stats = []

    for index in range(days):
        """Each day simulation."""
        for patient_index in range(len(patient)):
            """Simulation through list of patients."""
            friends_list = patient[patient_index].get_friends()
            for friend_index in friends_list:
                """Simulation for each person in connetion with the friend."""
                probability_of_meeting = random()
                if probability_of_meeting < meeting_probability:
                    """Probability of meeting is compared with entered probability."""
                    if friend_index.is_contagious():
                        """If friend is contagious, he will spread the infection to patient."""
                        friend_viral_load = 5 + (((friend_index.get_health() - 25) ** 2) / 62)
                        patient[patient_index].infect(friend_viral_load)
                    elif patient[patient_index].is_contagious():
                        """Else if patient is contagious, he will spread the infection to his friend."""
                        patient_viral_load = 5 + (((patient[patient_index].get_health() - 25) ** 2) / 62)
                        friend_index.infect(patient_viral_load)

        day_patients_effected = 0
        for patient_index in patient:
            """Loop to put all the persons to sleep and
                also to count the contagious people in a given day."""
            if patient_index.is_contagious():
                """If patient is contagious, Number of 
                    patients effected is incremented."""
                day_patients_effected += 1
            patient_index.sleep()                                       # Each patient is put to sleep at end of day.
        each_day_effected_stats.append(day_patients_effected)           # list of each day stats are stored in a list.

    return each_day_effected_stats


"""Reads the data from file a2_sample_set.txt and create objects
        of each person and also create their connections."""
def load_patients(initial_health):

    file = open("a2_sample_set.txt", "r")
    split_lines = file.read().splitlines()
    file.close()

    person_name = []                                                    # stores the name of the person
    person_connection = []                                              # stores the persons connection.
    patient = []                                                        # Objects of the person

    for index in split_lines:
        """Splitting the person name and his/her connections."""
        name_connection = index.split(": ")
        person_name.append(name_connection[0])
        person_connection.append(name_connection[1])

    for index in range(len(person_name)):
        """Spliting the persons first name and his last name."""
        split_name = person_name[index].split(" ")
        f_name = split_name[0]
        lst_name = split_name[1]
        patient.append(Patient(f_name, lst_name, initial_health))       # Creating Object of the person

    for index in range(len(patient)):
        """Spliting the persons connections."""
        connection_split_list = person_connection[index].split(", ")
        for connection_value in connection_split_list:
            """Comparing each value of connection with person object."""
            for obj_index in range(len(patient)):
                """Getting the name of person object."""
                p_name = patient[obj_index].get_name()
                if connection_value == p_name:
                    """If the connection matches with list of person, Add them to connection."""
                    patient[index].add_friend(patient[obj_index])
    return patient


if __name__ == '__main__':
    test = run_simulation(60,0.25,49)
