"""
= addx V takes two cycles to complete. ¨
After two cycles, the X register is increased by the value V.
= noop takes one cycle to complete. It has no other effect.

During the first cycle, X is 1.
The signal strength (the cycle number multiplied by the value of the X register).

Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. 
What is the sum of these six signal strengths?
"""

with open('day_10_input.txt', encoding='utf-8') as file_object:
    input_data = file_object.readlines()

input_data = [instruction.replace('\n', '').split(' ') for instruction in input_data]
# print(input_data)

register = 1
cycle = 0

# Part 1

cycle_register = {}
for instruction in input_data:
    if len(instruction) == 1:
        cycle += 1
        if cycle > 1:
            cycle_register[f'{cycle}_in_process'] = cycle_register[f'{cycle-1}_executed']
            cycle_register[f'{cycle}_executed'] = cycle_register[f'{cycle-1}_executed']
        else:
            cycle_register[f'{cycle}_in_process'] = 0
            cycle_register[f'{cycle}_executed'] = register
    else:
        cycle += 1
        if cycle > 1:
            cycle_register[f'{cycle}_in_process'] = cycle_register[f'{cycle-1}_executed']
            cycle_register[f'{cycle}_executed'] = cycle_register[f'{cycle-1}_executed']
            cycle +=1
            cycle_register[f'{cycle}_in_process'] = cycle_register[f'{cycle-1}_executed']
            register = register + int(instruction[1])
            cycle_register[f'{cycle}_executed'] = register
        else:
            cycle_register[f'{cycle}_in_process'] = 0
            cycle_register[f'{cycle}_executed'] = register
            cycle +=1
            cycle_register[f'{cycle}_in_process'] = register
            register = register + int(instruction[1])
            cycle_register[f'{cycle}_executed'] = register


sum_signal_strength = cycle_register['20_in_process']*20 + cycle_register['60_in_process']*60 + cycle_register['100_in_process']*100 + cycle_register['140_in_process']*140 + cycle_register['180_in_process']*180 + cycle_register['220_in_process']*220

print(cycle_register)
print(sum_signal_strength)


# Part 2

"""
The X register controls the horizontal position of a sprite. 
The sprite is 3 pixels wide, and the X register sets the horizontal position of the middle of that sprite.
The pixels on the CRT: 40 wide and 6 high.
The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39.
The CRT draws a single pixel during each cycle.
If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.).

Render the image given by your program. What eight capital letters appear on your CRT?
"""