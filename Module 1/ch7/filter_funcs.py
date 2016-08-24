def filter_ints(v):
    return [num for num in v if is_positive(num)]

def is_positive(n):
    return n > 0


if __name__ == "__main__":
    print(filter_ints([3, -4, 0, 5, 8]))  # [3, 5, 8]
