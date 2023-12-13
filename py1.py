def get(n):
    marks = []
    for i in range(n):
        mark = float(input("Enter the marks of student " + str(i + 1) + ": "))
        marks.append(mark)
    return marks


def avg(marks):
    total, count = sum(marks), len(marks)
    return total / count if count != 0 else 0


def high_low(marks):
    highest = lowest = marks[0] if marks else None
    for mark in marks[1:]:
        if mark > highest:
            highest = mark
        elif mark < lowest:
            lowest = mark
    return highest, lowest


def count_absent(marks):
    return marks.count(0)


def highest_frequency(marks):
    frequency_dict = {}
    highest_frequency_mark = None
    highest_frequency = 0

    for mark in marks:
        frequency_dict[mark] = frequency_dict.get(mark, 0) + 1
        if frequency_dict[mark] > highest_frequency:
            highest_frequency = frequency_dict[mark]
            highest_frequency_mark = mark

    return highest_frequency_mark


def main():
    n = int(input("Enter the number of students: "))
    student_marks = get(n)

    # a) Compute average score
    average_score = avg(student_marks)
    print("Average score of the class:", average_score)

    # b) Find highest and lowest score
    highest, lowest = high_low(student_marks)
    print("Highest score in the class:", highest)
    print("Lowest score in the class:", lowest)

    # c) Count of students who were absent for the test
    absent_count = count_absent(student_marks)
    print("Number of students absent for the test:", absent_count)

    # d) Display mark with the highest frequency
    highest_frequency_mark = highest_frequency(student_marks)
    print("Mark with the highest frequency:", highest_frequency_mark)

main()
