score1 = 85
score2 = 92

score = [85, 92]
score = [85.5, 92.5, "Any", True]
print(score[2]) # Result is Any
print(score[-1]) # Result is True
print(score[0:2]) # after the dot is minus

# List - data collection that can be sorted and mutable

# Add Element
score.append("Try") # Added to the last section
print(score)

score.insert(-1, 10)
print(score)

del score[1]
print(score)

try_pop = score.pop()
print(score)
print(try_pop)

scores = [1, 5, 3, 4, 8, 90]
scores.sort(reverse=False) # if empty, then is reverse
print(scores)

print(len(scores)) # amount

# Tuple - sorted data collection but immutable

lat = (-6.1, 3.4)
print(lat[1])

# Dictionary - key-value data collection
student = {
    'name' : "James", # double or single quote free
    'age' : 50,
    'height' : 170,
    'graduated' : True
}

print(student['height'])
print(f"Student height: {student['height']} cm")

student['weight'] = 65.7
print(student['weight'])

print(student)

students = {
    'name' : ["James", "Josh"],
    'age' : [50, 40],
    'height' : [170, 200],
    'graduated' : [True, False]
}
print(students['name'])

student1 = {
    'name' : 'asep',
    'age' : 80
}

student1['name'] = 'leon'
print(student1['name'])

del student1['age']
print(student1)

print('age' in student1)