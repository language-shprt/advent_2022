"""
After the rearrangement procedure completes, what crate ends up on top of each stack?
"""

piles_of_crates = [['S','L','W'],['J','T','N','Q'],['S','C','H','F','J'],['T','R','M','W','N','G','B'],['T','R','L','S','D','H','Q','B'],['M','J','B','V','F','H','R','L'],['D','W','R','N','J','M'],['B','Z','T','F','H','N','D','J'],['H','L','Q','N','B','F','T']]

with open('day_5_input.txt', encoding='utf-8') as input_data:
    rearranging_procedure = input_data.readlines()

rearranging_procedure = [step.replace('move','').replace('from','').replace('to','').replace('\n','') for step in rearranging_procedure]

for step in rearranging_procedure:
    step = step.split(' ')
    step = [step[1], step[3], step[5]]
    #move 1 from 2 to 1
    number_of_crates = int(step[0])
    from_where = int(step[1])
    to_where = int(step[2])
    for i in range(number_of_crates): # do it how many times
        moving_crate = piles_of_crates[from_where - 1].pop()
        piles_of_crates[to_where - 1].append(moving_crate)

print(piles_of_crates)
top_crates = ''
for pile in piles_of_crates:
    top_crate = pile[-1]
    top_crates = top_crates + top_crate
print(top_crates)