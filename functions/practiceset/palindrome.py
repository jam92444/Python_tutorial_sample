def reverse_string(word):#word=pop
    return word[::-1];#pop

def palindrome(word):#word=pop
    string = word; #string = "pop"
    reversed_string = reverse_string(string)  # Correctly call the function to reverse the word
#reversed_string = pop
    #if pop == pop:
    if string == reversed_string:  # Compare the word and its reversed version
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"

word = input("Enter the word: ")#pop
isPalindrome = palindrome(word); #ispalindrome = "pop is a palindrome"
print(isPalindrome)
