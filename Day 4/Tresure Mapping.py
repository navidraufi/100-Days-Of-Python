
print("Where do you want to put the tresure?")

first_row= ["O","O","O"]
second_row= ["O","O","O"]
third_row= ["O","O","O"]
print(f"{first_row}\n{second_row}\n{third_row}")

row = input("Row? ")
column = input("Column? ")

combined = [first_row,second_row,third_row]

row_num = int(row)
column_num = int(column) -1


if row_num == 1:
    first_row.pop(column_num)
    first_row.insert(column_num,"X")
    print(f"{first_row}\n{second_row}\n{third_row}")
elif row_num == 2:
    second_row.pop(column_num)
    second_row.insert(column_num,"X")
    print(f"{first_row}\n{second_row}\n{third_row}")
elif row_num == 3:
    third_row.pop(column_num)
    third_row.insert(column_num,"X")
    print(f"{first_row}\n{second_row}\n{third_row}")

