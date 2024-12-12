import random

rooms = []
total_rooms = 5
rooms = [random.choice(['clean','dirt']) for _ in range(total_rooms)]
# for _ in range(total_rooms):
#     rooms.append(random.choice(['clean', 'dirt']))
    # rooms.append('dirt')
vacuum_at = def_room = random.randint(1, total_rooms - 1)
to_clean = len(rooms)
print('vacuum at: %s \t starting room: %s \t room left to clean; %s' % (vacuum_at, def_room, to_clean))
print('rooms state:', rooms, '\n')


def room_state(room_no):
    return rooms[room_no]


def clean_room(room_no):
    if rooms[room_no] == 'dirt':
        rooms[room_no] = 'clean'


def move_forward():
    global vacuum_at
    vacuum_at += 1


def move_back():
    global vacuum_at
    vacuum_at -= 1


def display():
    print(rooms)


all_room_clean = False
while not all_room_clean:
    # print('vacuum at : %s  state: %s ' % (vacuum_at, room_state(vacuum_at)))
    if vacuum_at <= len(rooms) - 1:
        if room_state(vacuum_at) == 'dirt':
            clean_room(vacuum_at)
        to_clean -= 1  # if dirt -> cleaned;  if not skipped task is decremented
        print('cleaning:', end=' ')
        # display()

        if to_clean > def_room:  # vacuum moves within the limited room
            move_forward()
        elif to_clean <= def_room:
            while vacuum_at > def_room:  # returning after cleaning nth room
                move_back()
                print('vacuum at : %s  state %s ' % (vacuum_at, room_state(vacuum_at)))
            if to_clean > 0:  # room left to clean at left
                move_back()
            else:
                while vacuum_at < def_room:  # towards where it began to work
                    move_forward()
                    print('vacuum at : %s  state %s ' % (vacuum_at, room_state(vacuum_at)))
                if vacuum_at == def_room:  # after cleaning all room returned to starting room
                    all_room_clean = True
                    print('\nFinished cleaning: Returned to the room where it started')

print(rooms)

'''
The vacuum can start in any room and begins cleaning from the rightmost room.
Once it finishes cleaning the nth room, it traces back to the initial room without cleaning. 
After reaching the initial room, it starts cleaning towards the 0th room.
Once the vacuum finishes its cleaning job, it returns to the room where it initially started.
'''
