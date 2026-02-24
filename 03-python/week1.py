name = "Jessica"
age = 20
# age = 23
score = 9.5

print(name)
print(age)
print(score)

print(type(name)) # string is text
print(type(score)) # float is decimal

print(len(name)) # length (including "" = 0)
print(type(age)) # int is integer

number_a = 10
number_b = 7

print(number_a > number_b)
print(number_a < number_b)
print(number_a == number_b) # == is comparison

# converting data type
# int,float,str,bool
age_float = float(age)
print(age_float)
print(type(age_float))

print(str(score))
score_str = str(score)
print(type(score_str))

# arithmetic operators
print(5+5, 10-5)
print(10/5)
print(12//5) #floor division

print(10%3) # modulo, remainder after division
print(5**2) # exponent

# string operations
print(name[0]) # J
print(name[-1]) # a is last in the name
print(name[1:4]) # ess
print(name[1:]) # essica
print(name[:6]) # Jessic

print("Hello!", name)
print(f"Hello! {name}")

# comparison operators

age1 = 20
has_id1 = True
age2 = 17
has_id2 = False

print(age1 >= 17 and has_id1)
print(age2 >= 17 or has_id2)
print(not has_id1) # opposite of the value

names = str(input("what is your name? "))
print(f"hi! {names}")

age3 = int(input("what is your age? "))
print(f"your age is {age3}")