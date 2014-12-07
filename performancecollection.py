import numpy as np
import operator
"""
PerformanceCollection is a dataset to hold system production data.
It is designed to be efficient, both in time and storage space.
"""

class PerformanceCollection(object):

    def __init__(self):
        """
        Creates a dictionary upon instantiation
        """
        self.stor = {}

    def add(self, system):
        """ ADD a system to the collection

        usage:
            system = Performance('Sleepy')
            spc = PerformanceCollection()
            spc.add(system)
        """
        # it should check if it's the proper datatype
        self.stor[system] = system.lifetimeperformance()

    def count(self):
        """
        OUTPUT: the number of Performance objects in the collection
        """
        return len(self.stor)

    def max(self):
        """
        OUTPUT: max lifetimeperformance value within collection
        """
        return max(self.stor.keys())

    def min(self):
        """
        OUTPUT: min lifetimeperformance value within collection
        """
        return min(self.stor.keys())

    def percentile(self, pct):
        """
        Calculate the nth percentile of the data collection

        usage:
        tenthpercentileperformance = spc.percentile(10)
        """
        #check if pct is a digit {1,100}
        return np.percentile(self.stor.values(), pct)

    def top(self, k):
        """
        Return an array of dictionaries of performance
        (lifetimeperformance) and names (systemname) for the top k systems.
        The results should be ordered in descending order.

        usage:
        systemperformance = spc.top(10)

        where systemperformance = [
                {'systemname': 'Sleepy', 'lifetimeperformance': 1.10},
                {'systemname': 'Doc', 'lifetimeperformance': 1.08},
                ...
            ]
        """

        #sort the list by lifetimeperformance and get the kth items
        lis = sorted(self.stor.items(), key=operator.itemgetter(1), reverse=True)[:k]
        top_k_list = []
        for system, LTP in lis:
            top_k_list.append(
                {'systemname': system.name(),
                 'lifetimeperformance': '{:.2f}'.format(LTP)}
            )

        return top_k_list


