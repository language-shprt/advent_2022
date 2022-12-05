"""
In how many assignment pairs does one range fully contain the other?
"""

with open('day_4_input.txt', encoding='utf-8') as input_data:
    assignment_pairs = input_data.readlines()

assignment_pairs = [assignment_pair.replace('\n', '').split(',') for assignment_pair in assignment_pairs]

# Part 1

full_overlap_counter = []
overlap_counter = 0
for assignment_pair in assignment_pairs:
    assignment_1_beginning = int(assignment_pair[0].split('-')[0])
    assignment_1_end = int(assignment_pair[0].split('-')[1])
    assignment_2_beginning = int(assignment_pair[1].split('-')[0])
    assignment_2_end = int(assignment_pair[1].split('-')[1])
    assignment_1_full = list(range(assignment_1_beginning, assignment_1_end + 1))
    assignment_2_full = list(range(assignment_2_beginning, assignment_2_end + 1))
    matching_sectors = []
    for sector in assignment_1_full:
        if sector in assignment_2_full:
            matching_sectors.append(sector)
    if len(matching_sectors) > 0:
        overlap_counter += 1
    if matching_sectors == assignment_1_full:
        full_overlap_counter.append(1)
    elif matching_sectors == assignment_2_full:
        full_overlap_counter.append(1)

print(f'In {len(full_overlap_counter)} assignment pairs one range fully contains the other.')

# Part 2

"""
In how many assignment pairs do the ranges overlap?
"""

print(f'In {overlap_counter} assignment pairs the ranges overlap.')