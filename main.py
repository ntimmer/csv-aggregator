import csv
import pprint
import itertools

DELIMITER=';'

def read_dataset(filename):
    result = []

    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=DELIMITER)
        columns = reader.__next__()
        
        for row in reader:
            entry = {}
            for i, col_val in enumerate(row):
                entry[columns[i].strip()] = col_val
            result.append(entry)

    return result


def extract_all_column_names(dataset):
    column_names = set()
    for entry in dataset:
        column_names.update(entry.keys())
    return column_names


def update_entry_with_missing_columns(entry, column_names):
    for col in column_names:
        if not col in entry:
            entry[col] = ""


def write_dataset(dataset):
    columns = sorted(dataset[0].keys())
    with open('result.csv', 'w') as f:
        writer = csv.writer(f, delimiter=DELIMITER)
        writer.writerow(columns)
        for entry in dataset:
            writer.writerow([entry[col] for col in columns])    


def main(amount_of_datasets):
    datasets = []
    for i in range(1, amount_of_datasets+1):
        datasets.append(read_dataset(f"dataset_{i}.csv"))
    dataset = [item for sublist in datasets for item in sublist]

    column_names = extract_all_column_names(dataset)
    print(f"Found {len(column_names)} columns in datasets.")
    print(f"Found {len(dataset)} entries in datasets.")
    
    for entry in dataset:
        update_entry_with_missing_columns(entry, column_names)
    
    write_dataset(dataset)


main(6)