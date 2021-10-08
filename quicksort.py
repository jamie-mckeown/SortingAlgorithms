from sortable import Sortable

class QuickSort (Sortable) :
    
    @staticmethod
    def sort (tosort : list) :
        '''
        Docstring to finish.
        '''

        #   method will operate recursively so needs a termination case - we are splitting lists apart, so we terminate when our list is a single element.
        if len(tosort) < 2:
            return tosort
        elif len(tosort) == 2: # not entirely sure this case is necessary but we move!
            if tosort[1] <= tosort[0]:
                return [tosort[1], tosort[0]]

        #   Set variables
        lst = tosort.copy()
        n = len(lst)
        
        #   Select a pivot to compare all other elements to; make left and right for smaller or equal to and greater than pivot, respectively.
        pivot = lst.pop()
        left = list()
        rght = list()

        #   Go through remaining elements of lst, compare to pivot and relocate accordingly.
        for num in lst :
            left.append(num) if (num <= pivot) else rght.append(num)

        return QuickSort.sort(left) + [pivot] + QuickSort.sort(rght)