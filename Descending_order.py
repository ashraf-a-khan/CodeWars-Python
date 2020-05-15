"""
Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

"""



def descending_order(num):
    str_num = str(num)
    my_list = []
    my_list = str_num.split()
    
    my_list2 = []
    for i in my_list[0]:
        my_list2.append(int(i))
    
    my_list2.sort()
    my_list2.reverse()
    
    result = ''
    for element in my_list2:
            result += str(element)

    return int(result)