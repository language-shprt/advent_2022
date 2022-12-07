"""
Identify the first position where the four most recently received characters were all different.
How many characters need to be processed before the first start-of-packet marker is detected?
"""
with open('day_6_input.txt', encoding='utf-8') as input_data:
    message = input_data.readlines()[0]

is_marker = False
index_counter = 0

for character in message:
    if is_marker == True:
        break
    else: 
        next_three_symbols_indexes = index_counter + 4
        group_of_four = message[index_counter:next_three_symbols_indexes]
        index_counter += 1
        
        unique_characters = ''
        for character in group_of_four:
            if character in unique_characters:
                # print('not a group of unique characters')
                break
            else:
                unique_characters = unique_characters + character
                if len(unique_characters) == 4:
                    is_marker = True
                    print(group_of_four)
                    print(next_three_symbols_indexes)

# Part 2
"""
A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters.
How many characters need to be processed before the first start-of-message marker is detected?
"""

is_marker = False
index_counter = 0

for character in message:
    if is_marker == True:
        break
    else: 
        next_13_symbols_indexes = index_counter + 14
        group_of_14 = message[index_counter:next_13_symbols_indexes]
        index_counter += 1
        
        unique_characters = ''
        for character in group_of_14:
            if character in unique_characters:
                # print('not a group of unique characters')
                break
            else:
                unique_characters = unique_characters + character
                if len(unique_characters) == 14:
                    is_marker = True
                    print(group_of_14)
                    print(next_13_symbols_indexes)