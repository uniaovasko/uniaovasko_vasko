import csv
from textdistance import hamming
from volume import test_string

def checar_par(ing_cdb, ing_fdb, sem_par: dict[str, str], pares, cdb_nome='Aliased Ingredient Name', cdb_id='Entity ID') -> bool:
    if (s := hamming.normalized_similarity(ing_cdb[cdb_nome].lower(), ing_fdb["name"].lower())) >= 0.85:
        sem_par.pop(ing_cdb[cdb_id], None)
        if ing_cdb[cdb_id] in pares.keys():
            print(f"{ing_cdb[cdb_id], ing_cdb[cdb_nome]} de {pares[ing_cdb[cdb_id]]} para {(ing_cdb[cdb_id], ing_fdb['name'])}")
        pares[ing_cdb[cdb_id]] = (ing_cdb[cdb_nome], ing_fdb['id'], ing_fdb["name"], ing_fdb["food_group"], ing_fdb["food_subgroup"])
        return True
    return False

def converte_pound(q):
    return q * 453,592

def calc_volume(q, u):
    match u:
        case "teaspoon":
            return q * 4.92892159
        case "tablespoon":
            return q * 14.7867648
        case "cup":
            return q * 250
        case "ounce":
            return q * 30

def ligar_ingredientes():
    with (open("data/external/02_Ingredients.csv") as ing_cdb_f,
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
            csv_writer = csv.writer(out, lineterminator='\n')
            csv_writer.writerow(["id_cdb", "nome_cdb", "id_fdb", "nome_fdb", "grupo", "subgrupo"])
            for (id_cdb, (nome_cdb, id_fdb, nome_fdb, grupo, subgrupo)) in pares.items():
                csv_writer.writerow([id_cdb, nome_cdb, id_fdb, nome_fdb, grupo, subgrupo])
        with open("data/interim/ingredientes_sem_nome.csv", "w") as out:
            csv_writer = csv.writer(out, lineterminator='\n')
            csv_writer.writerow(["id_cdb", "nome_cdb", "id_fdb", "nome_fdb"])
            for (id_cdb, nome_cdb) in sem_par.items():
                csv_writer.writerow([id_cdb, nome_cdb])

def ligar_ingredientes_compostos():
    with (open("data/external/03_Compound_Ingredients.csv") as ing_cdb_f,
          open("data/external/Food.csv") as ing_fdb_f):
        reader_cdb = list(csv.DictReader(ing_cdb_f))
        reader_fdb = list(csv.DictReader(ing_fdb_f))
        sem_par = dict()
        pares = dict()
        for ing_cdb in reader_cdb:
            sem_par[ing_cdb["entity_id"]] = ing_cdb["Compound Ingredient Name"]
            for ing_fdb in reader_fdb:
                nome_cdb = ing_cdb["Compound Ingredient Name"].lower()
                nome_fdb = ing_fdb["name"].lower()
                if not checar_par(ing_cdb, ing_fdb, sem_par, pares, "Compound Ingredient Name", "entity_id"):
                    alt_list = ing_cdb["Compound Ingredient Synonyms"].split("; ")
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
                        if checar_par(ing_cdb, ing_fdb, sem_par, pares, "Compound Ingredient Name", "entity_id"):
                            break
        print("Quantidade sem par:", len(sem_par))
        print(pares)
        with open("data/interim/ingredientes_compostos.csv", "w") as out:
            csv_writer = csv.writer(out, lineterminator='\n')
            csv_writer.writerow(["id_cdb", "nome_cdb", "id_fdb", "nome_fdb", "grupo", "subgrupo"])
            for (id_cdb, (nome_cdb, id_fdb, nome_fdb, grupo, subgrupo)) in pares.items():
                csv_writer.writerow([id_cdb, nome_cdb, id_fdb, nome_fdb, grupo, subgrupo])
        with open("data/interim/ingredientes_compostos_sem_nome.csv", "w") as out:
            csv_writer = csv.writer(out, lineterminator='\n')
            csv_writer.writerow(["id_cdb", "nome_cdb", "id_fdb", "nome_fdb"])
            for (id_cdb, nome_cdb) in sem_par.items():
                csv_writer.writerow([id_cdb, nome_cdb])                                

def finalizar_ligacao():
    with (open("data/interim/ingredientes.csv", 'r')                   as ing_f,
          open("data/interim/ingredientes_manuais.csv", 'r')           as ing_m_f,
          open("data/interim/ingredientes_compostos_manuais.csv", 'r') as ingc_m_f,
          open("data/interim/ingredientes_compostos.csv")              as ingc_f,
          open("data/external/02_Ingredients.csv")                     as ing_orig_f,
          open("data/external/03_Compound_Ingredients.csv")            as ingc_orig_f,
          open("data/interim/ingredientes_final.csv", 'w')             as ing_out,
          open("data/interim/ingredientes_compostos_final.csv", 'w')   as ingc_out,
          open("data/interim/ingredientes_removidos.csv", 'w')         as ing_r_out):
        
        header = ["id_cdb","nome_cdb","id_fdb","nome_fdb","grupo","subgrupo", "aliases"]

        ing_m_reader = csv.DictReader(ing_m_f, lineterminator='\n')
        ingc_m_reader = csv.DictReader(ingc_m_f, lineterminator='\n')
        ingc_reader = csv.DictReader(ingc_f, lineterminator='\n')
        ing_reader = csv.DictReader(ing_f, lineterminator='\n')
        ing_orig_reader = csv.DictReader(ing_orig_f, lineterminator='\n')
        ingc_orig_reader = csv.DictReader(ingc_orig_f, lineterminator='\n')
        ing_writer = csv.DictWriter(ing_out, header, lineterminator='\n')
        ingc_writer = csv.DictWriter(ingc_out, header, lineterminator='\n')
        ing_r_writer = csv.DictWriter(ing_r_out, header, lineterminator='\n')

        ingredientes = { x["Entity ID"]: x for x in ing_orig_reader }
        ingredientes_compostos = { x["entity_id"]: x for x in ingc_orig_reader }

        ing_writer.writeheader()
        ingc_writer.writeheader()
        ing_r_writer.writeheader()

        ing_writer.writerows({**ing, **{"aliases": ingredientes[ing["id_cdb"]]["Ingredient Synonyms"]}}
                              for ing in ing_reader)
        for ing in ing_m_reader:
            if ing["id_fdb"] != "":
                int(ing["id_fdb"])
                ing_writer.writerow({**ing, **{"aliases": ingredientes[ing["id_cdb"]]["Ingredient Synonyms"]}})
            else:
                ing_r_writer.writerow({**ing, **{"aliases": ingredientes[ing["id_cdb"]]["Ingredient Synonyms"]}})
        ing_writer.writerows({**ing, **{"aliases": ingredientes_compostos[ing["id_cdb"]]["Compound Ingredient Synonyms"]}}
                             for ing in ingc_reader)
        for ing in ingc_m_reader:
            if ing["id_fdb"] != "":
                int(ing["id_fdb"])
                ing_writer.writerow({**ing, **{"aliases": ingredientes_compostos[ing["id_cdb"]]["Compound Ingredient Synonyms"]}})
            else:
                ingc_writer.writerow({**ing, **{"aliases": ingredientes_compostos[ing["id_cdb"]]["Compound Ingredient Synonyms"]}})

def ligar_ingrediente_receita():
    with (open("data/interim/ingredientes_final.csv") as ing_f,
          open("data/interim/ingredientes_compostos_final.csv") as ingc_f,
          open("data/processed/receitas.csv") as rec_f,
          open("data/external/04_Recipe-Ingredients_Aliases.csv") as rec_ing_f,
          open("data/processed/ingredientes_receitas.csv", "w") as out_f,
          open("data/interim/ing_rec_removidos.csv", "w") as removidos_f):
        ing_reader = csv.DictReader(ing_f, lineterminator='\n')
        ingc_reader = csv.DictReader(ingc_f, lineterminator='\n')
        rec_reader = csv.DictReader(rec_f, lineterminator='\n')
        rec_ing_reader = csv.DictReader(rec_ing_f, lineterminator='\n')
        out_writer = csv.DictWriter(out_f, fieldnames=["id_ingrediente", "id_receita", "volume", "massa", "unidade", "composto"], lineterminator='\n')
        removidos_writer = csv.DictWriter(removidos_f, fieldnames=["id_ing_cdb","id_receita", "nome"])

        out_writer.writeheader()

        ingredientes = { x["id_cdb"]: x for x in ing_reader }
        ingredientes_compostos = { x["id_cdb"]: x for x in ingc_reader }
        for rec_ing in rec_ing_reader:
            [q, u, *_] = test_string(rec_ing["Original Ingredient Name"]) + ["unit"]
            u = u.removesuffix("s")
            tem_volume = u != "unit" and u != "pound"
            
            if ing := ingredientes.get(rec_ing["Entity ID"], False):
                if tem_volume:
                    out_writer.writerow({
                        "id_ingrediente": ing["id_fdb"],
                        "id_receita": rec_ing["Recipe ID"],
                        "volume": calc_volume(q, u),
                        "composto": 0
                    })
                elif u == "pound":
                    out_writer.writerow({
                        "id_ingrediente": ing["id_fdb"],
                        "id_receita": rec_ing["Recipe ID"],
                        "massa": converte_pound(q),
                        "composto": 0
                    })
                else:
                    out_writer.writerow({
                        "id_ingrediente": ing["id_fdb"],
                        "id_receita": rec_ing["Recipe ID"],
                        "unidade": q,
                        "composto": 0,
                    })
            elif ingc := ingredientes_compostos.get(rec_ing["Entity ID"], False):
                if tem_volume:
                    out_writer.writerow({
                        "id_ingrediente": ingc["id_cdb"],
                        "id_receita": rec_ing["Recipe ID"],
                        "volume": calc_volume(q, u),
                        "composto": 1
                    })
                elif u == "pound":
                    out_writer.writerow({
                        "id_ingrediente": ingc["id_cdb"],
                        "id_receita": rec_ing["Recipe ID"],
                        "volume": converte_pound(q),
                        "composto": 1
                    })
                else:
                    out_writer.writerow({
                        "id_ingrediente": ingc["id_cdb"],
                        "id_receita": rec_ing["Recipe ID"],
                        "unidade": q,
                        "composto": 1,
                    })
            else:
                removidos_writer.writerow({
                    "id_ing_cdb": rec_ing["Entity ID"],
                    "id_receita": rec_ing["Recipe ID"],
                    "nome": rec_ing["Aliased Ingredient Name"]
                })


        
        

if __name__ == "__main__":
    #ligar_ingredientes()
    # ligar_ingredientes_compostos()
    #finalizar_ligacao()
    ligar_ingrediente_receita()