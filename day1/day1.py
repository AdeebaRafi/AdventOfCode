def load():
    # Load data
    with open("input.txt", "r") as f:
        data = f.readlines()

    # Process data
    list_1, list_2 = zip(*(line.split() for line in data))
    list_1 = [int(n) for n in list_1]
    list_2 = [int(n) for n in list_2]
    return list_1, list_2


def part_1(list_1, list_2):
    list_1_sorted = sorted(list_1)
    list_2_sorted = sorted(list_2)

    # Calculate distances
    distances = sum([abs(a - b) for a, b in zip(list_1_sorted, list_2_sorted)])
    return distances


def part_2(list_1, list_2):
    from collections import Counter

    list_2_counts = Counter(list_2)

    # Loop over each number in the first list and calculate the similarity
    # score. Note a Counter object returns 0 if the key doesn't exist.
    return sum([n * list_2_counts[n] for n in list_1])


if __name__ == "__main__":
    list_1, list_2 = load()
    star_1_answer = part_1(list_1, list_2)
    print(f"Star 1 answer: {star_1_answer}")
    star_2_answer = part_2(list_1, list_2)
    print(f"Star 2 answer: {star_2_answer}")