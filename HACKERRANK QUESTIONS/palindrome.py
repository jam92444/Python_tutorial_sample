def palindrome(string):
    return string == string[::-1];

string = palindrome("malayalam");
if string:
    print("palindrome");
else:
    print("Not a Palindrome");
    
    
