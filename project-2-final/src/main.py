import csv
import textdistance
from limpar import *
from ligador import ligar_ingredientes, ligar_ingredientes_compostos, finalizar_ligacao, ligar_ingrediente_receita

def main():
    limpa_compound()
    limpa_nutrient()
    limpa_receita()
    
    ligar_ingredientes()
    ligar_ingredientes_compostos()
    finalizar_ligacao()
    ligar_ingrediente_receita()
    




if __name__ == "__main__":
    main()
    
