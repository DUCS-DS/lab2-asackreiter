#Lab 2 
#Author: Artemis Sackreiter

def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    increasing = decreasing = both = True #defines what is true

    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]: #decreasing is monotonic
            decreasing = False
        if lst[i] < lst[i-1]: #increasing is monotonic
            increasing = False
        if lst[i] == lst[i-0]: #constant lst is monotonic
            both = False


    return increasing or decreasing

nums = [1, 2, 2, 3]
print(monotonic(nums)) #True

nums = [5, 4, 3, 2, 2]
print(monotonic(nums)) #True

nums = [1, 3, 2]
print(monotonic(nums)) #False

nums = [2, 2, 2, 2]
print(monotonic(nums)) #True

nums = []
print(monotonic(nums)) #True
