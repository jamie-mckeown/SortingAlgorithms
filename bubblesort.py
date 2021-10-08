from sortable import Sortable

class BubbleSort (Sortable) :

    @staticmethod
    def sort (tosort : list) :
        '''
        Docstring to finish.
        '''
        n = len(tosort) - 1 # index of the final element in the list
        lst = tosort.copy()
        swaps = True

        #   While the list remains unsorted, we carry out a bubble sort on the list
        while swaps :
            swaps = False
            for i in range(0, n) :
                # compare the ith and i+1th elements
                if lst[i] > lst[i+1] :
                    #   Swap the elements
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    swaps = True
        
        return lst