import csv

def main():
    with (
        open("data/external/01_Recipe_Details.csv") as freceitas_meta,
        open("data/processed/receitas.csv", "w") as freceitas_meta_out,
        open("data/external/02_Ingredients.csv") as fingredientes,
        open("data/external/03_Compound_Ingredients.csv") as fcompostos,
        open("data/external/04_Recipe-Ingredients_Aliases.csv") as freceitas_def,
        open("data/external/FoodDensityDB.csv") as fdensidades,
    ):
       reader_receitas_meta = csv.DictReader(freceitas_meta, lineterminator="\n")
       writer_receitas_meta = csv.DictWriter()
       





if __name__ == "__main__":
    main()
