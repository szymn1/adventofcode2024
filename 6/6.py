import numpy as np


class Guard:
    def __init__(self, curr_pos, facing):
        self.pos = [curr_pos[0], curr_pos[1]]
        self.dir = facing
        self.in_room = True

    def advance(self):
        if self.dir == '^':
            self.pos[0] -= 1
        elif self.dir == 'v':
            self.pos[0] += 1
        elif self.dir == '>':
            self.pos[1] += 1
        elif self.dir == '<':
            self.pos[1] -= 1

    def rotate(self, corner_list):
        corner_list.append(((self.pos[0], self.pos[1]), self.dir))
        if self.dir == '^':
            self.dir = '>'
        elif self.dir == '>':
            self.dir = 'v'
        elif self.dir == 'v':
            self.dir = '<'
        elif self.dir == '<':
            self.dir = '^'

    def check_fwd(self, room_map):
        fwd = calc_fwd_pos(self.dir, self.pos)

        if fwd[0] >= len(room_map) or fwd[1] >= len(room_map[0]) or fwd[0] < 0 or fwd[1] < 0:
            self.in_room = False
            return True
        elif str(room_map[fwd[0]][fwd[1]]) != '#':
            return True
        else:
            return False

    def action(self, room_map, corner_list):
        if self.check_fwd(room_map):
            self.advance()
        else:
            self.rotate(corner_list)


def calc_fwd_pos(face, position):
    fwd = ()
    if face == '^':
        fwd = (position[0] - 1, position[1])
    elif face == 'v':
        fwd = (position[0] + 1, position[1])
    elif face == '>':
        fwd = (position[0], position[1] + 1)
    elif face == '<':
        fwd = (position[0], position[1] - 1)
    return fwd


with open('input', 'r') as f:
    room = np.array([list(line.strip('\n')) for line in f])

starting_point = np.where(room == '^')
guard = Guard([starting_point[0][0], starting_point[1][0]], '^')


counter = 0
visited = []
corners = []
loop_spots = []
while guard.in_room:
    visited.append((guard.pos[0], guard.pos[1], guard.dir))
    guard.action(room, corners)
    if len(corners) >= 3:
        if guard.pos[0] == corners[-3][0][0]:
            loop_spots.append(calc_fwd_pos(guard.dir, (guard.pos[0], guard.pos[1])))
        elif guard.pos[1] == corners[-3][0][1]:
            loop_spots.append(calc_fwd_pos(guard.dir, (guard.pos[0], guard.pos[1])))

    counter += 1
    if counter == 50000:
        print('ERR!')
        break

unique = []
for pos in visited:
    room[pos[0], pos[1]] = 'X'
    if (pos[0], pos[1]) not in unique:
        unique.append((pos[0], pos[1]))


print(f'Unique visited spots: {len(unique)}')


with open('output', 'w') as f:
    for line in room:
        f.write(''.join(char for char in line) + '\n')


with open('input', 'r') as f:
    room = np.array([list(line.strip('\n')) for line in f])


loops = 0
for j, pos in enumerate(unique[1:]):
    counter = 0
    new_visited = []
    corners = []
    new_room = np.copy(room)
    new_room[pos[0], pos[1]] = '#'
    guard.pos = [starting_point[0][0], starting_point[1][0]]
    guard.in_room = True
    guard.dir = '^'
    while guard.in_room:
        new_visited.append((guard.pos[0], guard.pos[1], guard.dir))
        guard.action(new_room, corners)
        if (guard.pos[0], guard.pos[1], guard.dir) in new_visited:
            loops += 1
            room[pos[0], pos[1]] = 'O'
            break
        counter += 1
        if counter == 17000:
            print('ERR!')
            break


with open('output1', 'w') as f:
    for line in room:
        f.write(''.join(char for char in line) + '\n')

print(f'LOOPS: {loops}')
