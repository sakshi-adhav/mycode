def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def display_top_five(arr):
    print("Top five scores:")
    for i in range(-1, -6, -1):
        print(arr[i])

# Main program
def main():
    # Input: First-year percentages of students
    percentages = [85.5, 90.0, 78.3, 92.7, 88.1, 79.5, 94.2, 87.8, 91.5, 83.6]

    # Display original scores
    print("Original Scores:", percentages)

    # Sorting using selection sort
    selection_sort_percentages = percentages.copy()
    selection_sort(selection_sort_percentages)
    print("Scores after Selection Sort:", selection_sort_percentages)

    # Sorting using bubble sort
    bubble_sort_percentages = percentages.copy()
    bubble_sort(bubble_sort_percentages)
    print("Scores after Bubble Sort:", bubble_sort_percentages)

    # Display top five scores
    display_top_five(selection_sort_percentages)

main()

