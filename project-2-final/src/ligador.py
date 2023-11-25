import csv
from textdistance import hamming

def checar_par(ing_cdb, ing_fdb, sem_par: dict[str, str], pares) -> bool:
    if (s := hamming.normalized_similarity(ing_cdb['Aliased Ingredient Name'].lower(), ing_fdb["name"].lower())) >= 0.85:
        sem_par.pop(ing_cdb["Entity ID"], None)
        if ing_cdb['Entity ID'] in pares.keys():
            print(f"{ing_cdb['Entity ID'], ing_cdb['Aliased Ingredient Name']} de {pares[ing_cdb['Entity ID']]} para {(ing_cdb['Entity ID'], ing_fdb['name'])}")
        pares[ing_cdb["Entity ID"]] = (ing_cdb['Aliased Ingredient Name'], ing_fdb['id'], ing_fdb["name"], ing_fdb["food_group"], ing_fdb["food_subgroup"])
        return True
    return False

def ligar_ingredientes():
    with(open("data/external/02_Ingredients.csv") as ing_cdb_f,
         open("data/external/Food.csv") as ing_fdb_f):
        reader_cdb = list(csv.DictReader(ing_cdb_f))
        reader_fdb = list(csv.DictReader(ing_fdb_f))
        sem_par = dict()
        pares = dict()
        for ing_cdb in reader_cdb:
            sem_par[ing_cdb["Entity ID"]] = ing_cdb["Aliased Ingredient Name"]
            for ing_fdb in reader_fdb:
                nome_cdb = ing_cdb["Aliased Ingredient Name"].lower()
                nome_fdb = ing_fdb["name"].lower()
                if not checar_par(ing_cdb, ing_fdb, sem_par, pares):
                    alt_list = ing_cdb["Ingredient Synonyms"].split("; ")
                    novos = []
                    for x in alt_list:
                        if x.find("-") > -1:
                            novos.append(x.replace("-", " "))
                        if x.find("=") > -1:
                            novos.append(x.replace("=", " "))
                            novos.append(x.replace("=", ""))
                        if x.find("#") > -1:
                            novos.append(x.removeprefix("#").removesuffix("#"))
                    alt_list.extend(novos)
                    for x in alt_list:
                        if checar_par(ing_cdb, ing_fdb, sem_par, pares):
                            break
                            
        print("Quantidade sem par:", len(sem_par))
        #print(pares)
        with open("data/interim/ingredientes.csv", "w") as out:
            csv_writer = csv.writer(out)
            csv_writer.writerow(["id_cdb", "nome_cdb", "id_fdb", "nome_cdb", "grupo", "subgrupo"])
            for (id_cdb, (nome_cdb, id_fdb, nome_fdb, grupo, subgrupo)) in pares.items():
                csv_writer.writerow([id_cdb, nome_cdb, id_fdb, nome_fdb, grupo, subgrupo])
        with open("data/interim/ingredientes_sem_nome.csv", "w") as out:
            csv_writer = csv.writer(out)
            csv_writer.writerow(["id_cdb", "nome_cdb", "id_fdb", "nome_fdb"])
            for (id_cdb, nome_cdb) in sem_par.items():
                csv_writer.writerow([id_cdb, nome_cdb])


if __name__ == "__main__":
    ligar_ingredientes()