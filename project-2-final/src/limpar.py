import csv

def limpa_compound():
    with open('data/external/Compound.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = ["id", "nome"]
        next(csv_reader, None)
        with open('data/processed/compostos.csv', mode='w') as new_csv_file:
            csv_writer = csv.writer(new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            csv_writer.writerow(header)
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
        header = ["id", "nome"]
        next(csv_reader, None)
        with open('data/processed/nutrientes.csv', mode='w') as new_csv_file:
            csv_writer = csv.writer(new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            csv_writer.writerow(header)
            for row in csv_reader:
                csv_writer.writerow([row[0], row[4]])

    #checando os prieiros 10 elementos do novo arquivo
    # with open('data/processed/Nutrient.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     for i in range(10):
    #         print(next(csv_reader))
    
def limpa_receita():
    with open('data/external/01_Recipe_Details.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = ["id", "titulo", "regiao"]
        next(csv_reader, None)
        with open('data/processed/receitas.csv', mode='w') as new_csv_file:
            csv_writer = csv.writer(new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            csv_writer.writerow(header)
            for row in csv_reader:
                csv_writer.writerow([row[0], row[1], row[3]])

    #checando os prieiros 10 elementos do novo arquivo
    # with open('data/processed/Nutrient.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     for i in range(10):
    #         print(next(csv_reader))

def limpa_content():
    with (open("data/external/Content.csv") as content_f,
          open("data/processed/content_nutrientes.csv", "w") as nutriente_f,
          open("data/processed/content_compostos.csv", "w") as composto_f,
          open("data/interim/ingredientes_final.csv") as ing_f):
        content_reader = csv.DictReader(content_f, lineterminator='\n')
        ing_reader = csv.DictReader(ing_f, lineterminator='\n')
        nutriente_writer = csv.writer(nutriente_f, lineterminator='\n')
        composto_writer = csv.writer(composto_f, lineterminator='\n')

        nutriente_writer.writerow(["id_ingrediente", "id_nutriente", "quantidade"])
        composto_writer.writerow(["id_ingrediente", "id_composto", "quantidade"])

        ingredientes = { x["id_fdb"] for x in ing_reader }
        adicionados: set[tuple[str, str]] = set()
        nones = 0
        zeros = 0
        for content in content_reader:
            if (content["food_id"], content["source_id"]) not in adicionados and content["food_id"] in ingredientes:
                row = [content["food_id"], content["source_id"], content["orig_content"]]
                if content["orig_content"] == "0.0":
                    zeros += 1
                    continue
                elif content["orig_content"] == None or content["orig_content"] == "":
                    nones += 1
                    continue
                adicionados.add((content["food_id"], content["source_id"]))
                if content["source_type"] == "Nutrient":
                    nutriente_writer.writerow(row)
                else:
                    composto_writer.writerow(row)
        print(f"nones: {nones}, zeros: {zeros}")

def match_alias(nome, aliases: list[str]):
    for i in range(len(aliases)):
        alias = aliases[i]
        tem_hifen = alias.find("-") > -1
        tem_igual = alias.find("=") > -1
        tem_hashtag = alias.find("#") > -1
        novo_alias = alias
        if tem_hifen:
            novo_alias = novo_alias.replace("-", " ")
        if tem_hashtag:
            novo_alias = novo_alias.removeprefix("#")
            novo_alias = novo_alias.removesuffix("#")
        if tem_igual:
            aliases.append(novo_alias.replace("=", " "))
            novo_alias = novo_alias.replace("=", "")
        if tem_hashtag or tem_igual or tem_hifen:
            aliases.append(novo_alias)
    return nome in aliases

def limpa_ingrediente():
    with (open("data/interim/ingredientes_final.csv") as ing_f,
          open("data/interim/ingredientes_compostos_final.csv") as ingc_f,
          open("data/external/03_Compound_Ingredients.csv") as ingc_orig_f,
          open("data/processed/ingredientes.csv", "w") as out_f,
          open("data/processed/composicao.csv", "w") as out_comp_f):
        ing_reader = csv.DictReader(ing_f, lineterminator="\n")
        ingc_reader = csv.DictReader(ingc_f, lineterminator="\n")
        ingc_orig_reader = csv.DictReader(ingc_orig_f, lineterminator="\n")
        ing_writer = csv.DictWriter(out_f, ["id", "nome", "grupo", "subgrupo", "densidade", "peso_medio", "composto"], lineterminator="\n")
        comp_writer = csv.DictWriter(out_comp_f, ["id_composto", "id_base"], lineterminator="\n")

        ing_writer.writeheader()
        comp_writer.writeheader()

        ingredientes_fdb: dict[str, dict[str, str]] = {}
        ingredientes_cdb = { x["id_cdb"]: x for x in ing_reader }
        ingredientes_compostos = { x["entity_id"]: x for x in ingc_orig_reader }
        for ing_line in ingredientes_cdb.values():
            if ing_line["id_fdb"] not in ingredientes_fdb.keys():
                ing = {
                    "id": ing_line["id_fdb"],
                    "nome": ing_line["nome_fdb"],
                    "grupo": ing_line["grupo"],
                    "subgrupo": ing_line["subgrupo"],
                    "densidade": 1, #TODO
                    "peso_medio": 1, #TODO
                    "composto": 0,
                }
                ingredientes_fdb[ing["id"]] = ing
                ing_writer.writerow(ing)
        for ingc_line in ingc_reader:
            composicao = ingredientes_compostos[ingc_line["id_cdb"]]["Contituent Ingredients"].split(", ")
            composicao_ids = []
            for c in composicao:
                for ing_line in ingredientes_cdb.values():
                    if match_alias(c, ing_line["aliases"].split("; ")):
                        composicao_ids.append(ing_line["id_fdb"])
                        break
                    



if __name__ == "__main__":
    # limpa_nutrient()
    # limpa_compound()
    # limpa_receita()
    limpa_content()