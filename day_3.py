"""
Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.

Find the item type that appears in both compartments of each rucksack. 
What is the sum of the priorities of those item types?
"""

# Part 1

priorities_list = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]

with open('day_3_input.txt', encoding='utf-8') as input_data:
    rucksacks_data = input_data.readlines()

rucksacks_data = [items_pair.replace('\n', '') for items_pair in rucksacks_data]

same_items = []
for items_pair in rucksacks_data:
    items_1 = items_pair[:len(items_pair) // 2]
    items_2 = items_pair[len(items_pair) // 2:]
    same_items_temp = []
    for item in items_1:
        if item in items_2 and item not in same_items_temp:
            same_items_temp.append(item)
            same_items = same_items + same_items_temp

sum_of_priorities = 0
for item in same_items:
    prioroty = priorities_list.index(item) + 1
    sum_of_priorities = sum_of_priorities + prioroty
print(f'The sum of the priorities is {sum_of_priorities}.')

# Part 2

"""
Find the item type that corresponds to the badges of each three-Elf group. 
What is the sum of the priorities of those item types?
"""

same_items = []
while rucksacks_data:
    three_rucksacks = rucksacks_data[:3]
    rucksack_1 = three_rucksacks[0]
    rucksack_2 = three_rucksacks[1]
    rucksack_3 = three_rucksacks[2]
    rucksacks_data = rucksacks_data[3:]
    same_items_temp = []
    for item in rucksack_1:
        if item in rucksack_2 and item in rucksack_3 and item not in same_items_temp:
            same_items_temp.append(item)
            same_items = same_items + same_items_temp

sum_of_priorities_2 = 0
for item in same_items:
    prioroty = priorities_list.index(item) + 1
    sum_of_priorities_2 = sum_of_priorities_2 + prioroty
print(f'The sum of the priorities is {sum_of_priorities_2}.')