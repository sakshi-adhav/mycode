def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def display_top_five(arr):
    print("Top five scores:")
    for i in range(-1, -6, -1):
        print(arr[i])

# Main program
def main():

    first_year_percentages = [85.5, 90.0, 78.3, 92.7, 88.1, 79.5, 94.2, 87.8, 91.5, 83.6]


    print("Original Scores:", first_year_percentages)


    quick_sort_percentages = quick_sort(first_year_percentages)
    print("Scores after Quick Sort:", quick_sort_percentages)


    display_top_five(quick_sort_percentages)
main()
