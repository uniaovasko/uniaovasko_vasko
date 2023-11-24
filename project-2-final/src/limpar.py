import csv

def limpa_compound():
    with open('data/external/01_Recipe_Details.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open('data/processed/01_Recipe_Details.csv', mode='w') as new_csv_file:
            csv_writer = csv.writer(new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                csv_writer.writerow([row[0], row[2]])

    #checando os prieiros 10 elementos do novo arquivo
    # with open('data/processed/Compound.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     for i in range(10):
    #         print(next(csv_reader))
    
def limpa_nutrient():
    with open('data/external/Nutrient.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open('data/processed/Nutrient.csv', mode='w') as new_csv_file:
            csv_writer = csv.writer(new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                csv_writer.writerow([row[0], row[2]])

    #checando os prieiros 10 elementos do novo arquivo
    # with open('data/processed/Nutrient.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     for i in range(10):
    #         print(next(csv_reader))
    
def limpa_receita():
    with open('data/external/Nutrient.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open('data/processed/Nutrient.csv', mode='w') as new_csv_file:
            csv_writer = csv.writer(new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                csv_writer.writerow([row[0], row[1], row[3]])

    #checando os prieiros 10 elementos do novo arquivo
    # with open('data/processed/Nutrient.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     for i in range(10):
    #         print(next(csv_reader))