'''
A **lambda function** is a small, anonymous function defined with the `lambda` keyword in Python. 

It's often used when you need a short function for a specific purpose and don't want to formally define it using the `def` keyword.

The basic syntax of a lambda function is:

    lambda  arguments: expression
    (keyword)(parameters):(expression)

Where:
    - **arguments** are the parameters passed to the lambda function (just like regular function parameters).
    - **expression** is a single expression that is evaluated and returned when the lambda function is called.
'''

'''
Examples of =Lambda Functions

1. Basic Example
    A simple lambda function that adds two numbers:
'''

# add = lambda x, y: x + y
# sub = lambda x, y: x - y
# print(add(3, 9))  # Output: 12
# print(sub(3, 9))  # Output: -6


# Here, `lambda x, y: x + y` defines a function that takes two arguments `x` and `y` and returns their sum. We then call the lambda function with `3` and `4`, which returns `7`.


'''
2. Using Lambda in `map()`
    The `map()` function applies a given function to all items in an iterable (like a list).
 

    def square(x):
        return x ** 2;
        
    numbers = [1, 2, 3, 4, 5]
    
    squared_numbers = map(square, numbers);
   
    
# Example:'''
# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)  

number = [1,2,3,4,5,6,7,8,9,10];
table = int(input("Enter table: "));
def addItem(x):
    return table
final_table = list(map(addItem,number));
tables = list(map(lambda x,y: x * y,final_table, number))
print(tables)



# Here, the lambda function `lambda x: x * 2` doubles each number in the list `numbers`.

'''
3. Using Lambda in `filter()`
    The `filter()` function filters elements from an iterable based on a condition defined by a function. It returns elements for which the function returns `True`.

# Example:


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
'''

# In this example, `lambda x: x % 2 == 0` filters out only the even numbers from the list.

'''
4. Using Lambda in `sorted()`
    You can use a lambda function to specify a custom sorting order with the `sorted()` function.


# Example:

pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[0])
print(sorted_pairs)  # Output: [(1, 'one'), (2, 'two'), (3, 'three')]

'''
# Here, the lambda function `lambda x: x[0]` sorts the list of tuples based on the first element of each tuple.

'''
5. Lambda with Default Arguments
    You can also provide default values for the arguments in a lambda function.


# Example:

power = lambda x, y=2: x ** y
print(power(3))    # Output: 9 (3^2)
print(power(3, 3)) # Output: 27 (3^3)
'''

# In this example, if the second argument `y` is not provided, it defaults to `2`.

'''
 When to Use Lambda Functions
    - Short and simple functions**: When you need a small function for a brief operation.
    - Anonymous operations**: When you don't need to give a name to the function.
    - Functional programming**: For use in higher-order functions like `map()`, `filter()`, `reduce()`, etc.

However, if the function logic is complex or will be reused multiple times, it's better to use a regular function defined with `def`.

'''

