import csv
import os
import pathlib


# Generic path generation
root_file = pathlib.Path(__file__).parent.resolve()
csv_path = os.path.join(root_file, "csv_files", "small.csv")

with open(csv_path, "r", newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")

    for row in reader:
        print(row)


# Generic path generation
root_file = pathlib.Path(__file__).parent.resolve()
csv_path = os.path.join(root_file, "csv_files", "test.csv")

with open(csv_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_MINIMAL)

    new_row1 = ["Colonne 1", "Colonne 2", "Colonne 3"]
    writer.writerow(new_row1)
    new_row2 = [1, 2, 3]
    writer.writerow(new_row2)
    new_row3 = [4, 5, 6]
    writer.writerow(new_row3)

    # Add several lines in one line
    writer.writerows([new_row1, new_row2, new_row3])

