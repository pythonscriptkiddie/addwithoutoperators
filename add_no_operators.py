'''
Addition without operators: This program obtains two integers from the user
and then adds them together without using operators. This is one of the 'hard'
questions from 'Cracking the Coding Interview' by 
'''

print('Welcome to addition without a plus sign!')
item1 = int(input('Please enter the first number: '))
item2 = int(input('Please eneter the second number: '))

item1_list = []
item2_list = []
total = 0
total_list = []
marker = 'x'
placeholder = 'placeholder'

while len(item1_list) < item1:
    item1_list.append(marker)

while len(item2_list) < item2:
    item2_list.append(marker)

item1_list.insert(1, placeholder)
item1_list.insert(1, placeholder)

for item in range(1, len(item1_list)):
    total_list.append(item1_list.pop())

for item in range(1, len(item2_list)):
    total_list.append(item2_list.pop())

total = len(total_list)

print('The sum of', item1, 'and', item2, 'is', total)
