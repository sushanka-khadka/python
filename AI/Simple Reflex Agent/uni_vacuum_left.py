class VacuumCleaner:
    def __init__(self, size):
        # Initialize the room with all positions dirty and set the initial position to 0
        self.room = ["dirty"] * size
        self.position = size -1

    def get_position(self):
        # Return the current position of the vacuum cleaner
        return self.position

    def get_state(self, i):
        # Return the state (dirty/clean) of the room at position i
        return self.room[i]

    def update_room(self):
        # Clean the room at the current position if it is dirty
        if self.room[self.position] == "dirty":
            self.room[self.position] = "clean"
            print("Vacuum cleaner cleaned the room.")
        else:
            print("The room is already clean.")

    def move(self, direction):
        # Move the vacuum cleaner left or right based on the direction
        if direction == -1 and self.position > 0:
            self.position -= 1
            print("Vacuum cleaner moved left.")
        elif direction == 1 and self.position < len(self.room) - 1:
            self.position += 1
            print("Vacuum cleaner moved right.")
        else:
            print("Vacuum cleaner cannot move further in this direction.")

def main():
    # Create a vacuum cleaner for a room of size 5
    vc = VacuumCleaner(1000)
    direction = -1  # Start by moving to the right

    while True:
        # Get the state of the current position
        state = vc.get_state(vc.get_position())

        # If the current position is dirty, clean it
        if state == "dirty":
            vc.update_room()

        # Move in the current direction
        vc.move(direction)

        # Check if we need to change direction
        if vc.get_position() == 0:
            direction = 1  # Change direction to right if at the leftmost position
        elif vc.get_position() == len(vc.room) - 1:
            direction = -1  # Change direction to left if at the rightmost position

        # Check if all rooms are clean
        print('vacuum at : ', vc.get_position())
        if all(vc.get_state(i) == "clean" for i in range(len(vc.room))):
            break

    # Print message when all rooms are clean
    print("All rooms are clean.")

if __name__ == "__main__":
    main()
