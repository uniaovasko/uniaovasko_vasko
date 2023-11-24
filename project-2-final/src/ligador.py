import csv

def main():
    with open("Food.csv") as foodDB:
        csv_reader = csv.reader(foodDB)
        for line in csv_reader:
            print(line[1])
    
main()