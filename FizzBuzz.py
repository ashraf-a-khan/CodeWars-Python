"""

Return an array containing the numbers from 1 to N, where N is the parametered value. N will never be less than 1 (in C#, N might be less than 1).

C# ONLY: If N is smaller than or equal to 0, throw an ArgumentOutOfRangeException!
Replace certain values however if any of the following conditions are met:

If the value is a multiple of 3: use the value 'Fizz' instead
If the value is a multiple of 5: use the value 'Buzz' instead
If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead
C# method calling example:

string[] result = FizzBuzz.GetFizzBuzzArray(3); // => [ "1", "2", "Fizz" ]

"""


for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif(i%3 == 0):
        print("Fizz")
    elif(i%5 == 0):
       print("Buzz")
    else:
        print(i)