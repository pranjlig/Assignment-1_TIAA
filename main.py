# Prime Numbers

def is_prime_no (n):
    for i in range (2, int(n ** 0.5) + 1):
        if (n % i) == 0:
            return False
        return True

def get_prime_list():
    prime_list = []
    for n in range (2, 51):
        if is_prime_no(n):
            prime_list.append(n)
    return prime_list

print(get_prime_list())


# User Input Table

def print_table(n):
    for i in range (1, 11):
        print(n, " * ", i, " = ", n * i)

print_table(int(input("Enter a number: ")))


# Palindrome

def is_palindrome(s):
    if (s == s[ : : -1]):
        print(s, " is a palindrome.")
    else:
        print(s, " is not a palindrome.")

is_palindrome(input("Enter a string: "))


# Reverse a String

def reverse_string(s):
    print("Rever of ", s, " is ", s[ : : -1])

reverse_string(input("Enter a string: "))


