def binary_search(arr, target):
    """
    Performs binary search on a sorted list to find the target element.
    
    Args:
        arr (list): A sorted list of elements
        target: The element to search for
    
    Returns:
        int: Index of target if found, otherwise -1
    """
    # Initialize left pointer at the start of the list
    left = 0
    # Initialize right pointer at the end of the list
    right = len(arr) - 1
    
    # Continue searching while left pointer doesn't exceed right pointer
    while left <= right:
        # Calculate the middle index to avoid overflow
        mid = left + (right - left) // 2
        
        # Check if target is at the middle position
        if arr[mid] == target:
            return mid
        
        # If target is smaller, search in the left half
        elif arr[mid] > target:
            right = mid - 1
        
        # If target is larger, search in the right half
        else:
            left = mid + 1
    
    # Target not found in the list
    return -1


def get_user_input():
    """
    Gets dynamic input from the user for binary search.
    """
    arr = list(map(int, input("Enter sorted array elements (space-separated): ").split()))
    target = int(input("Enter target element to search: "))
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("-1")


# Test cases
get_user_input()
if __name__ == "__main__":
    # Test 1: Target found in the middle
    assert binary_search([1, 3, 5, 7, 9, 11], 7) == 3
    
    # Test 2: Target found at the beginning
    assert binary_search([1, 3, 5, 7, 9, 11], 1) == 0
    
    # Test 3: Target found at the end
    assert binary_search([1, 3, 5, 7, 9, 11], 11) == 5
    
    # Test 4: Target not found
    assert binary_search([1, 3, 5, 7, 9, 11], 6) == -1
    
    # Test 5: Empty list
    assert binary_search([], 5) == -1
    
    # Test 6: Single element found
    assert binary_search([5], 5) == 0
    
    # Test 7: Single element not found
    assert binary_search([5], 3) == -1
    