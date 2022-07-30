step_count = int(input())
lst = []
x_offset = 0
y_offset = 0
compass = 'север', 'юг', 'запад', 'восток'
for i in range(step_count):
    lst.append(input().split())

for direction in lst:
    if direction[0] in compass:
         match direction[0]:
            case 'север':
                y_offset += int(direction[1])
            case 'юг':
                y_offset -= int(direction[1])
            case 'запад':
                x_offset -= int(direction[1])
            case 'восток':
                x_offset += int(direction[1])
    else:
        print('Wrong direction')

print(x_offset, y_offset, sep=' ')