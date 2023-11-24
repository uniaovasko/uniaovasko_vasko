import csv
from textdistance import hamming


def ligar_ingredientes():
    with(open("data/external/02_Ingredients.csv") as ing_cdb_f,
         open("data/external/Food.csv") as ing_fdb_f):
        reader_cdb = list(csv.DictReader(ing_cdb_f))
        reader_fdb = list(csv.DictReader(ing_fdb_f))
        sem_par = set()
        pares = dict()
        for ing_cdb in reader_cdb:
            sem_par.add(ing_cdb["Aliased Ingredient Name"])
            for ing_fdb in reader_fdb:
                nome_cdb = ing_cdb["Aliased Ingredient Name"].lower()
                nome_fdb = ing_fdb["name"].lower()
                if (s := hamming.normalized_similarity(nome_cdb, nome_fdb)) >= 0.85:
                    sem_par.remove(ing_cdb["Aliased Ingredient Name"])
                    if ing_cdb["Aliased Ingredient Name"] in pares.keys():
                        print(f"{ing_cdb['Aliased Ingredient Name']} de {pares[ing_cdb['Aliased Ingredient Name']]} para {ing_fdb['name']}")
                    pares[ing_cdb["Aliased Ingredient Name"]] = ing_fdb["name"]
                else:
                    alt_list = ing_cdb["Ingredient Synonyms"].split("; ")
        print(len(sem_par) ,sem_par)
        with open("data/interim/ingredientes.csv", "w") as out:
            pass



if __name__ == "__main__":
    ligar_ingredientes()