def linear_search(numbers, target):

    comparisons = 0
    for i in range(len(numbers)):
        comparisons += 1
        if numbers[i] == target:
            return i, comparisons
    return None, comparisons


def binary_search(numbers, target):

    comparisons = 0
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if numbers[mid] == target:
            return mid, comparisons
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None, comparisons


if __name__ == "__main__":
    sizes = [10, 100, 1_000, 10_000, 100_000]
    results = []

    for size in sizes:
        numbers = list(range(size))
        target = -1  # value guaranteed not to be in the list

        _, linear_comparisons = linear_search(numbers, target)
        _, binary_comparisons = binary_search(numbers, target)

        results.append((size, linear_comparisons, binary_comparisons))

    print(f"{'Size':>10} | {'Linear':>10} | {'Binary':>10}")
    print("-" * 36)
    for size, lin, bin_ in results:
        print(f"{size:>10} | {lin:>10} | {bin_:>10}")