class matrix_op:

    def add(m1, m2, row, col):
        result = [[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                result[i][j] = m1[i][j] + m2[i][j]
        print(result)

    def sub(m1, m2, row, col):
        result = [[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                result[i][j] = m1[i][j] - m2[i][j]
        print(result)

    def mult(m1, m2, row, col):
        result = [[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                result[i][j] = m1[i][j] * m2[i][j]
        print(result)

    def transpose(m, row, col):
        result = [[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                result[j][i] = m[i][j]
        for i in range(col):
            for j in range(row):
                print(result[i][j], end=" ")
            print()

    def main(self):
        obj=matrix_op();

        m1 = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
        m2 = [[4, 2, 9], [5, 4, 7], [2, 6, 3]]
        m = [[1, 3, 5], [4, 3, 2], [8, 6, 4]]

        row = 3
        col = 3

        print(m1, m2)

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            obj.add(m1, m2, row, col)
        elif choice == 2:
            obj.sub(m1, m2, row, col)
        elif choice == 3:
            obj.mult(m1, m2, row, col)
        elif choice == 4:
            obj.transpose(m, row, col)
        else:
            print("Wrong choice")

    main()




