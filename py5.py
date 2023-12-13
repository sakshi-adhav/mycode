def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def display_top_five(arr):
    print("Top five scores:")
    for i in range(-1, -6, -1):
        print(arr[i])

# Main program
def main():
    
    second_year_percentages = [75.2, 88.7, 82.5, 91.0, 79.3, 94.8, 86.5, 90.2, 78.9, 83.4]


    print("Original Scores:", second_year_percentages)


    insertion_sort_percentages = second_year_percentages.copy()
    insertion_sort(insertion_sort_percentages)
    print("Scores after Insertion Sort:", insertion_sort_percentages)


    shell_sort_percentages = second_year_percentages.copy()
    shell_sort(shell_sort_percentages)
    print("Scores after Shell Sort:", shell_sort_percentages)

    # Display top five scores
    display_top_five(shell_sort_percentages)
main()
