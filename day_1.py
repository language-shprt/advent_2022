"""
Find the Elf carrying the most Calories. 
How many total Calories is that Elf carrying?
"""

# Part 1
with open('day_1_input.txt', encoding='utf-8') as input_data:
    calories_list = input_data.readlines()

calories_list = [item.replace('\n','') for  item in calories_list]

def summing_up_calories(list_of_calories):
    sum_calories = []
    sum_calories_elf = 0
    for item in calories_list:
        if item == '':
            sum_calories.append(sum_calories_elf)
            sum_calories_elf = 0
        else:
            sum_calories_elf = sum_calories_elf + int(item)
    sum_calories.append(sum_calories_elf)
    return(sum_calories)

def finding_elf_with_max_calories(list_of_sums):
    max_calories = list_of_sums[0]
    elf_with_max_calories = 0
    for i in range(len(list_of_sums)):
        if list_of_sums[i] > max_calories:
            max_calories = list_of_sums[i]
            elf_with_max_calories = i
    print(f'The Elf carrying the most Calories in Elf number {i + 1}.')
    return max_calories

total_of_calories_each_elf = summing_up_calories(calories_list)
print(finding_elf_with_max_calories(total_of_calories_each_elf))

# Part 2
"""
Find the top three Elves carrying the most Calories. 
How many Calories are those Elves carrying in total?
"""

def sorting_elves_by_colories(total_of_calories_each_elf):
    if len(total_of_calories_each_elf) < 2:
        return total_of_calories_each_elf
    else:
        pivot = total_of_calories_each_elf[0]
        colories_less_pivot = [item for item in total_of_calories_each_elf[1:] if item < pivot]
        colories_greater_pivot = [item for item in total_of_calories_each_elf[1:] if item >= pivot]
        return sorting_elves_by_colories(colories_less_pivot) + [pivot] + sorting_elves_by_colories(colories_greater_pivot)

def summing_up_top_three(sorted_list):
    sum_calories_top_three = sorted_list[-1] + sorted_list[-2] + sorted_list[-3]
    return sum_calories_top_three

print(summing_up_top_three(sorting_elves_by_colories(total_of_calories_each_elf)))

# Part 2, simpler solution

def finding_three_elves_with_max_calories(array):
    max_1 = 0
    max_2 = 0
    max_3 = 0
    for i in range(len(array)):
        if array[i] >= max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = array[i]
        elif array[i] >= max_2:
            max_3 = max_2
            max_2 = array[i]
        elif array[i] >= max_3:
            max_3 = array[i]
    top_three = [max_1, max_2, max_3]
    sum_top_three = max_1 + max_2 + max_3
    return sum_top_three

print(finding_three_elves_with_max_calories(total_of_calories_each_elf))