from sortable import Sortable

class MergeSort (Sortable) :

    @staticmethod
    def sort (tosort : list) :
        '''
        Docstring to finish.
        '''
        #   Recursion base case - the input list is length 1
        if len(tosort) < 2 :
            return tosort

        #   Split the list into 2 and apply recursion
        n = len(tosort)
        mid = n // 2
        left, right = tosort[0:mid], tosort[mid:n]
        left, right = MergeSort.sort(left), MergeSort.sort(right)
        
        #   Compare elements on the left with elements on the right, and move the smallest into the output list each time
        output = list()
        i, j = 0, 0 # index for left and right resp.
        
        while i < len(left) and j < len(right) :
            if left[i] < right[j]:
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1

        #   Add the remaining elements to the output in order
        while i < len(left) :
            output.append(left[i])
            i += 1
        while j < len(right) :
            output.append(right[j])
            j += 1

        return output

        