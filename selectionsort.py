from sortable import Sortable 

class SelectionSort (Sortable) :

    @staticmethod
    def sort (tosort : list) :
        '''
        Docstring to finish.
        '''
        lst = tosort.copy()
        n = len(lst)

        for i in range(n-1) :
            #   Select first element as minimum
            min_i = i
            #   Compare with all other elements (to the right of the minimum)
            for j in range(i+1, n):
                if lst[j] < lst[min_i]:
                    min_i = j # update location of new minimum

            # if a new minimum has been found, we want to swap it with the old one
            if min_i != i :
                lst[i], lst[min_i] = lst[min_i], lst[i]

        return lst