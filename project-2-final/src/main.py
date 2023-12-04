from limpar import *
from ligador import ligar_ingredientes, ligar_ingredientes_compostos, finalizar_ligacao, ligar_ingrediente_receita

def main():
    limpa_compound()
    print("limpa_compound")
    limpa_nutrient()
    print("limpa_nutrient")
    limpa_receita()
    print("limpa_nutrient")
    
    ligar_ingredientes()
    print("ligar_ingredientes")
    ligar_ingredientes_compostos()
    print("ligar_ingredientes_compostos")
    finalizar_ligacao()
    print("finalizar_ligacao")
    ligar_ingrediente_receita()
    print("ligar_ingrediente_receita")

    limpa_content()
    print("limpa_content")
    limpa_ingrediente()
    print("limpa_ingrediente")
    




if __name__ == "__main__":
    main()
    
