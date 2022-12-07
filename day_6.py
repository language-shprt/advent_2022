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