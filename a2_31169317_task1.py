"""
Student Name : Sampreeth Amith Kumar
Student ID : 31169317
Start Date : 20/05/2020
Last Modified Date : 07/06/2020
Description : Reads data from a2_sample_set.txt and
            Creates objects for each person provided
            in .txt file and also creates connection
            to individual object, i.e referencing another
            Person object.
"""


class Person:
    """Person's class."""
    def __init__(self, first_name, last_name):
        """Constructor to store the first and last name of
            a Person instance and also friends of instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []

    def add_friend(self, friend_person):
        """Will add friends object to Person instance."""
        self.friends.append(friend_person)

    def get_name(self):
        """Returns a string containing the instance of Person's
            first and last name concatenated together."""
        return self.first_name + " " + self.last_name

    def get_friends(self):
        """Returns a list of Person's objects which are in
            connection with the Instance."""
        return self.friends


"""Reads the data from file a2_sample_set.txt and create objects
        of each person and also create their connections."""
def load_people():

    file = open("a2_sample_set.txt", "r")
    split_lines = file.read().splitlines()
    file.close()

    person_name = []                                                    # stores the name of the person
    person_connection = []                                              # stores the persons connection.
    persons = []                                                        # Objects of the person

    for index in split_lines:
        """Splitting the person name and his/her connections."""
        name_connection = index.split(": ")
        person_name.append(name_connection[0])
        person_connection.append(name_connection[1])

    for index in range(len(person_name)):
        """Splitting the persons first name and his last name."""
        split_name = person_name[index].split(" ")
        f_name = split_name[0]
        lst_name = split_name[1]
        persons.append(Person(f_name, lst_name))                        # Creating Object of the person

    for index in range(len(persons)):
        """Spliting the persons connections."""
        connection_split_list = person_connection[index].split(", ")
        for connection_value in connection_split_list:
            """Comparing each value of connection with person object."""
            for obj_index in range(len(persons)):
                """Getting the name of person object."""
                p_name = persons[obj_index].get_name()
                if connection_value == p_name :
                    """If the connection matches with list of person, Add them to connection."""
                    persons[index].add_friend(persons[obj_index])
    return persons

if __name__ == '__main__':
    people = load_people()


