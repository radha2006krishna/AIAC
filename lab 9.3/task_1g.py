def sum_even_odd(numbers: list[int]) -> tuple[int, int]:
    """
    Calculate the sum of even and odd numbers in a list.
    Args:
        numbers (list[int]): A list of integers.
    Returns:
        tuple[int, int]: A tuple containing two values:
            - Sum of even numbers.
            - Sum of odd numbers.
    """
    even_sum = sum(n for n in numbers if n % 2 == 0)
    odd_sum = sum(n for n in numbers if n % 2 != 0)
    return even_sum, odd_sum
def main():
    """
    Run an interactive program to calculate even and odd sums.

    This function prompts the user to enter a list of integers separated by spaces,
    computes the sum of even and odd numbers using `sum_even_odd`, and prints the results.
    """
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    even_sum, odd_sum = sum_even_odd(numbers)
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")
if __name__ == "__main__":
    main()
