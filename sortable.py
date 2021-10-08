class Sortable () :
    '''A class to store a list of integers that requires sorting, and provide functionality for sorting the list or sorting other lists.'''

    def __init__ (self, lst) :
        self.list = lst

    @staticmethod
    def sort (self, sortable_list):
        '''Method that takes a sortable list as input and returns the sorted list. Implented using a specfic sorting algorithm in subclasses.'''
        raise NotImplementedError

    def selfsort (self) :
        '''Method to sort the Sortable object.'''
        self.list = self.sort(self.list)