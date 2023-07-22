#First write a "helper" function with two extra parameters
# left, right that ddedscribes the search region as shown below
def findCrossoverIndexHelper(x, y, left, right):
    # Note: Output index i such that 
    #         left <= i <= right
    #         x[i] <= y[i]
    # First, Write down our invariants as assertions here
    assert(len(x) == len(y))
    assert(left >= 0)
    assert(left <= right-1)
    assert(right < len(x))
    # Here is the key property we would like to maintain.
    assert(x[left] > y[left])
    assert(x[right] < y[right])
    
    # your code here
    
    if (left > right):
        return None # Search region is empty , code cannot find any "cross over"points.
    else:
        cross_over = (left + right)//2
        if x[cross_over] >= y[cross_over] and x[cross_over+1] < y[cross_over+1]:
            return cross_over #Bingo -- we found it.
        elif x[cross_over] < y[cross_over]:
            return findCrossoverIndexHelper(x,y,left,cross_over-1)
        elif x[cross_over+1] >= y[cross_over+1]:
            return findCrossoverIndexHelper(x,y,cross_over+1,right)
