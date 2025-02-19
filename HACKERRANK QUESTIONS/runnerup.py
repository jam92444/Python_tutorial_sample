'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Sample input: 
5
2 3 6 6 5

Sample output:
5
'''

#taking the number of score
n = int(input()); 

#getting the list of score
#   input() gets the string "10 20 30 40".
#   .split() converts it into the list ["10", "20", "30", "40"].
#   map(int, ...) converts each string into an integer, producing an iterator of integers: map(int, ["10", "20", "30", "40"]) gives an iterator that will generate the values 10, 20, 30, 40 one by one.
#   arr is assigned this iterator.

arr = map(int, input().split());

#using sorted method making in ascending order and then type casting the list into the sets so all duplicated are removed and then reversing the set to make highest first then the other the second index value will be the final runnerup
runner = sorted(set(arr),reverse=True)
#printing the runnerup
print(runner[1])