"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

"""


def solution(string, ending):
    lst1 = []
    lst2 = []
    for i in string:
        lst1.append(i)
    
    for i in ending:
        lst2.append(i)
    if(lst1[len(lst1)-len(lst2):len(lst1)] == lst2):
        return True
    else:
        return False