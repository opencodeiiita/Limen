import math
import sys
from sortedcontainers import SortedList
import base64

def base64_to_decimal(rank_base64):
    return (base64.b64decode(rank_base64))

def get_permutation(n, rank):
    if n <= 0:
        raise ValueError("Invalid n: must be greater than 0.")
    if rank <= 0:
        raise ValueError("Invalid rank: must be greater than 0.")

    max_permutations = math.factorial(n)

    # Handle ranks exceeding maximum permutations
    rank = (rank % max_permutations)

    numbers = SortedList(range(1, n + 1))
    permutation = []

    for i in range(n, 0, -1):
        max_permutations = max_permutations // i
        index = (rank - 1) // max_permutations
        rank -= index * max_permutations
        permutation.append(numbers.pop(index))
    return permutation

def isFloat(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def main():
    sys.set_int_max_str_digits(1000000)
    try:
        n = int(input("Enter the value of N: "))
        rank_input = input("Enter the rank (int or decimal or Base64): ")

        if isFloat(rank_input):
            rank = int(float(rank_input))
        else:
            rank = int(base64_to_decimal(rank_input))  # Extract Base64 string

        permutation = get_permutation(n, rank)
        print("Permutation:")
        print(",".join(map(str, permutation)))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
