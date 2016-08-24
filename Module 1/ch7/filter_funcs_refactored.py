def filter_ints(v):
    v = [num for num in v if num != 0]  # 1
    return [num for num in v if is_positive(num)]

def is_positive(n):
    return n > 0


if __name__ == "__main__":
    print(filter_ints([3, -4, 0, 5, 8]))  # [3, 5, 8]
