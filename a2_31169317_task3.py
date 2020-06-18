"""
Student Name : Sampreeth Amith Kumar
Student ID : 31169317
Start Date : 20/05/2020
Last Modified Date : 07/06/2020
Description : Visual curve simulation
              Generates a graph showing how the disease
              has spread. Data is taken from the
              a2_31169317_task2.

Brief understanding: As the probability of meeting is
                    randomly generated number. So each time
                    the prediction may be different from the previous
                    result.
"""
from a2_31169317_task2 import *
from matplotlib import pyplot as plt

"""Visualizing the spread of virus."""
def visual_curve(days, meeting_probability, patient_zero_health):

    run_case = run_simulation(days,meeting_probability,patient_zero_health)     # Data is given to run_simulation()

    list_days = []
    for index in range(days):
        """Number of days stored in a list."""
        list_days.append(index)

    """Plot a graph using pyplot in matplotlib module."""
    plt.plot(list_days,run_case,label = 'Virus Spread')
    plt.xlabel('Days')                                                          # Labeling x axis
    plt.ylabel('Count')                                                         # Labeling y axis
    plt.title('Visualise The Virus Spread')                                     # Adding title to the graph
    plt.legend()                                                                # Adding legend to graph
    plt.show()                                                                  # Shows the plot.


if __name__ == '__main__':
    visual_curve(30,0.6,25)


