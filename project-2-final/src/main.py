import csv
import textdistance
from limpar import *
from ligador import ligar_ingredientes, ligar_ingredientes_compostos

def main():
    limpa_compound()
    limpa_nutrient()
    limpa_receita()
    ligar_ingredientes()
    ligar_ingredientes_compostos()
    ligar_ingredientes()
    ligar_ingredientes_compostos()




if __name__ == "__main__":
    main()
    
