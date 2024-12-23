#Part 1
# Read the initial arrangement from input.txt
def read_input(file):
    with open(file, 'r') as f:
        return list(map(int, f.readline().strip().split()))

# Function to apply the transformation rules to the stones
def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)
    return new_stones

# Main function to simulate the blinking process
def simulate_blinks(initial_stones, blinks):
    stones = initial_stones
    for _ in range(blinks):
        stones = blink(stones)
    return stones

if __name__ == "__main__":
    # Read the initial arrangement of stones from input.txt
    initial_stones = read_input("input11.txt")

    # Number of blinks to simulate
    blinks = 25

    # Simulate the blinking process
    final_stones = simulate_blinks(initial_stones, blinks)

    # Output the number of stones after 25 blinks
    print("Number of stones after", blinks, "blinks:", len(final_stones))
