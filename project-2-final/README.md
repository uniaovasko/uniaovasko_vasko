# Apresentação da Entrega Final do Projeto

## Motivação e Contexto

> O tema do projeto foi definido como “O que as pessoas comem ao redor do mundo”. A ideia para o projeto surgiu de uma análise do sistema de comida a quilo brasileiro, em que uma mesma fileira de pratos possuem alimentos de receitas de origens diversas, como o spaghetti italiano ao lado do sushi japonês que por sua vez está ao lado do kibe, que possui origens no Oriente Médio. Diante tal situação, chegamos a diversas perguntas como “o quão semelhante pode ser uma refeição entre as diversas regiões do mundo?” e “como essa diversidade de pratos molda a dieta macromolecular de cada povo?”.

## Slides

### Apresentação Prévia
> https://github.com/uniaovasko/uniaovasko_vasko/blob/main/project-2-final/slides/Projeto%20Parte%201.pdf

### Apresentação Final
> https://github.com/uniaovasko/uniaovasko_vasko/blob/main/project-2-final/slides/Projeto%20Parte%20Final.pdf

## Modelo Conceitual

> <img src="assets\modelo_conceitual_atualizado.drawio (1).png" width="400px" height="auto">

## Modelos Lógicos

* Modelo lógico relacional
~~~
IngredienteComposto(_ID_, Nome)
IngredienteSimples(_ID_, Nome, Grupo, Subgrupo)
Receita(_ID_, Nome, Regiao)
CompostoQuimico(_ID_, Nome)
Macronutriente(_ID_, Nome)
Contem(Receita_ID, Ingrediente_ID, Volume, Unidades, Massa)
	Receita_ID chave estrangeira -> Receita(ID)
	Ingrediente_ID chave estrangeira -> Ingrediente(Nome)
Constitui(_IngrdienteS_ID_, _CQ_ID_, QuantidadeGrama)
	IngredienteS_ID chave estrangeira -> IngredienteSimples(ID)
	CQ_ID chave estrangeira -> CompostoQuimico(ID)
Define(_IngredienteS_ID_, _Macro_ID_, QuantidadeGrama)
	Ingrediente_ID chave estrangeira -> IngredienteSimples(ID)
	Macro_ID chave estrangeira -> Macronutriente(ID)
Compoe(_Ingrediente1_ID_, _Ingrediente2_ID_)
	Ingrediente1_ID chave estrangeira -> Ingrediente(ID)
	Ingrediente2_ID chave estrangeira -> Ingrediente(ID)
~~~
* Modelo lógico de grafos
~~~
Ingredientes-Simples(_id_, nome, grupo, subgrupo)
Composicao-Quimica(_nome_)
Macronutrientes(_nome_)
Receita(_id_, nome, regiao)
Ingrediente-Composto(_id_, nome)
Define(_idis_, _nome-macro_, quantidade-grama)
	idis chave estrangeira -> Ingredientes-Simples(id)
	nome-macro chave estrangeira -> macronutrientes(nome)
Constitui(_idis_, _nomecq_, quantidade-grama)
	idis chave estrangeira -> Ingredientes-Simples(id)
	nomecq chave estrangeira -> Composicao-Quimica(nome)
Compoe(_idis_, _idic_)
	idis chave estrangeira -> Ingredientes-Simples(id)
	idic chave estrangeira -> Ingrediente-Composto(id)
Contems(_idrec_, _idis_)
	idirec chave estrangeira -> Receita(id)
	idis chave estrangeira -> Ingredientes-Simples(id)
Contemc(_IDrec_, _IDic_)
	idirec chave estrangeira -> Receita(id)
	idic chave estrangeira -> Ingrediente-Composto(id)
~~~
<!-- > ![Modelo Lógico de Grafos](assets/modelo-logico-grafos.jpeg) -->
> <img src="assets/modelo-logico-grafos.jpeg" width="400px" height="auto">

## Dataset Publicado
> Se ao tratar e integrar os dados originais foram produzidas novas bases relacionais ou de grafos, elencar essas bases.

título do arquivo/base | link | breve descrição
----- | ----- | -----
Densidade e peso unitário dos ingredientes | https://github.com/uniaovasko/uniaovasko_vasko/blob/main/project-2-final/data/processed/densidades.csv | Arquivo contendo as densidades e pesos médios coletados de diversas fontes para uso no projeto. Referencia id e nome do FooDB.
-|-|-
Receitas e Nutrição por Região | https://github.com/uniaovasko/uniaovasko_vasko/blob/main/project-2-final/ | Conjunto de arquivos permitindo análise nutricional e relacional entre regiões, suas receitas e seus respectivos ingredientes.


## Bases de Dados

título da base | link | breve descrição
----- | ----- | -----
`FooDB` | `https://foodb.ca` | `FooDB representa uma ampla e abrangente fonte de informações sobre alimentos, abordando detalhes relacionados à química dos alimentos, sua composição de ingredientes e os diversos nutrientes que contêm.`
`CulinaryDB` | `https://cosylab.iiitd.edu.in/culinarydb/` | `CulinaryDB é um extenso depósito de informações sobre pratos culinários e seus componentes. Dentro deste vasto banco de dados, encontram-se mais de 40 mil receitas, cada uma com detalhes que incluem sua região de procedência, dentre as 20 regiões catalogadas, assim como o nome e a lista completa de ingredientes utilizados.`

## Detalhamento do Projeto

* Eliminação das colunas que não serão importantes na análise, para facilitar a pesquisa e melhorar a visualização dos dados. [limpar.py](src/limpar.py)
~~~python
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
~~~

~~~python
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
~~~

~~~python
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
~~~

* Extração e filtragem de ingredientes, suas quantidades e suas respectivas unidades de medidas utilizando regex. [regex.py](src/limpar.py)
~~~python
    with open('data/external/04_Recipe-Ingredients_Aliases.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        array = []
        for row in csv_reader:
            array.append(row[1])

    input_strings = array[1:]
    result = test_strings(input_strings)
    #...
    regex = re.compile(r'((\d+/\d+)|(\d)+(\s\d+/\d+)?) (teaspoons?|tablespoons?|pounds?|cups?|\((\d+(\.\d+)?) (ounces?)\))?')
~~~

~~~python
with open('data/external/04_Recipe-Ingredients_Aliases.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	array = []
	for row in csv_reader:
	    array.append(row[1])

    input_strings = array[1:]
    result = test_strings(input_strings)
#...
regex = re.compile(r'((\d+/\d+)|(\d)+(\s\d+/\d+)?) (teaspoons?|tablespoons?|pounds?|cups?|\((\d+(\.\d+)?) (ounces?)\))?')
~~~


* Integração dos dados de um dataset com o outro usando um algoritmo de Hamming, na qual calcula a pontuação de correspondência para duas strings de dados. [ligador.py](src/limpar.py)

~~~python
def checar_par(ing_cdb, ing_fdb, sem_par: dict[str, str], pares, cdb_nome='Aliased Ingredient Name', cdb_id='Entity ID') -> bool:
    if (s := hamming.normalized_similarity(ing_cdb[cdb_nome].lower(), ing_fdb["name"].lower())) >= 0.85:
        sem_par.pop(ing_cdb[cdb_id], None)
        if ing_cdb[cdb_id] in pares.keys():
            print(f"{ing_cdb[cdb_id], ing_cdb[cdb_nome]} de {pares[ing_cdb[cdb_id]]} para {(ing_cdb[cdb_id], ing_fdb['name'])}")
        pares[ing_cdb[cdb_id]] = (ing_cdb[cdb_nome], ing_fdb['id'], ing_fdb["name"], ing_fdb["food_group"], ing_fdb["food_subgroup"])
        return True
    return False
~~~

> Aqui devem ser apresentadas as operações de construção do dataset:
* extração de dados de fontes não estruturadas como, por exemplo, páginas Web
* agregação de dados fragmentados obtidos a partir de API
* integração de dados de múltiplas fontes
* tratamento de dados
* transformação de dados para facilitar análise e pesquisa

Link Para Notebook Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/uniaovasko/uniaovasko_vasko/HEAD)

## Evolução do Projeto
> Esse projeto se iniciou com as escolhas dos datasets que faziam sentido para as análises e pesquisas que queríamos desenvolver, com base nisso foram escolhidas as base de dados FoodDB e CulinaryDB. Na primeira versão os projeto foi apresentada uma modelagem conceitual e lógica baseado na perspectiva inicial de como seria desenvolver e aplicar as ferramentas necessárias para fazer as análises. Para a segunda versão do modelo lógico e conceitual foram feitas algumas poucas modificações que foram percebidas ao longo do desdobramento do projeto. No desenvolvimento da atividade, à princípio, tivemos dificuldades para fazer a filtragem e processamento dos elementos nas bases de dados, como por exemplo os ingredientes da base do CulinaryDB não seguiam um padrão de escrita, alguns ingredientes vinham acompanhado de quantidades e unidades de medidas, já outros não tinham essa configuração. Esse problema foi resolvido utilizando a ferramenta regex, além disso foi criada outro arquivo para armazena todas as informações de forma estruturada para serem usadas na análise. Outro entrave que tivemos no projeto foi fazer o "match" com as informações que tinhámos da base CulinaryDB com a base FoodDB em decorrência da diferença estrutural das informações entre elas, levando isso em consideração foram feitas várias consultas e buscas para superar esse obstáculo, a melhor ferramenta que encontrada foi o algoritmo chamado de Distância de Hamming. Esse algoritmo calcula uma pontuação de correspondência para duas strings de dados computando o número de posições as quais os caracteres diferem entre as strings de dados, para string de comprimento diferente, cada caractere adicional na string mais longa é contado como uma diferença entre as strings. Com esse método obtivemos uma bom percentual de match entre os ingredientes das duas bases mencionadas acima, porém alguns ingredientes obtiveram uma baixa pontuação no confronto dos dados, então tivemos que fazer o match manualmente com os ingredientes que sobraram da base CulinaryDB.

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

### Perguntas/Análise com Resposta Implementada

#### Pergunta/Análise 1
> * Quais as estruturas bioquímicas mais frequentes em cada região?
>   
>   * Por meio do CulinaryDB é possível identificar as receitas de cada região e seus ingredientes. Com esses ingredientes, por meio do FooDB será identificado as estruturas bioquímicas mais frequentes de cada região. Essa pergunta é importante pois a bioquímica dos alimentos é uma importante ferramenta para estudo para saúde pública, pois identifica estruturas que são mais comuns e mais raras para os diferentes povos do mundo.

<img src="assets\TOP3MAISFREQUENTES.png" width="400px" height="auto">

#### Pergunta/Análise 2
> * Quais regiões possuem receitas com ingredientes majoritariamente vegetais?
>   
>   * Mantendo o mesmo modelo da pergunta 1, com os ingredientes de cada receita é possível identificar os subgrupos a qual pertencem. Assim é possível analisar como cada região se relaciona com as produções alimentícias locais.

<img src="assets\PORCENTAGEM VEGETAIS.png" width="400px" height="auto">

#### Pergunta/Análise 3
> * Quais regiões possuem a maior média de gorduras por receita?
>   
>   * Utilizando os valores nutricionais de cada ingrediente, fornecido pelo FooDB, é possível identificar a proporção de gordura contida na receita. Com essa informação será possível estabelecer uma média de lipídios em cada região. É uma pergunta importante visto que na atualidade a obesidade é um grande problema.

<img src="assets\MÉDIA GORDURA.png" width="400px" height="auto">

### Perguntas/Análise Propostas mas Não Implementadas

#### Pergunta/Análise 1
> * Existem similaridades entre as receitas das mais diversas regiões do globo?
>   
>   * Por meio de comparação entre os ingredientes e a estrutura deles nas diversas receitas é possível pesquisar receitas que se assemelham em regiões distintas. É uma pergunta bem interessante para se estudar movimentos migratórios e rotas de comércio que ocorreram no passado.

#### Pergunta/Análise 2
> * Quais regiões com maior diversidade de subgrupos alimentícios?
>   
>   * Com a análise de cada ingrediente é possível identificar a diversidade de grupos e subgrupos alimentares. É uma pergunta de importância geopolítica visto que a baixa diversidade de alimentos de algumas regiões pode estar relacionada a adversidades climáticas ou políticas.

#### Pergunta/Análise 3
> * Quais as combinações de ingredientes mais frequentes em cada região?
>   
>   * Podemos simplesmente contar a frequência de cada combinação de ingredientes em todas as receitas de uma determinada região. Isso nos ajuda a compreender a cultura alimentar de cada região, destacando os ingredientes que são mais tradicionalmente combinados em pratos locais, e possivelmente auxiliar no desenvolvimento de novas receitas condizentes com o cardápio local

### Análises do modelo de grafos
No modelo de grafos, criamos uma rede de ingredientes através de uma projeção nas receitas em que estes aparecem juntos, e utilizamos o cypher para explorar essa rede. Uma limitação, porém, foi a memória do ambiente online, assim, utilizamos apenas as receitas da região "USA" para as análises

#### Análise 1
> * O que ingredientes considerados "hubs" têm em comum?
>   
>   * Pudemos contabilizar o grau de cada nó, isto é, quantas arestas se ligam a ele, e assim rankear os top 20 hubs com mais conexões da nossa base se dados. Inicialmente, a resposta nos pareceu muito óbvia, pois ingredientes auxiliares como sal e óleo de cozinha dominavam o ranking. Portanto decidimos filtrar os ingredientes do grupo "Baking goods", e geramos a seguinte imagem. Podemos notar que uma característica em comum dos ingredientes hubs é que todos são considerados mais "suaves" em seus respectivos grupos, até mesmo as pimentas que aparecem
<img src="assets\TOP 20 HUBS SEM BAKING GOODS.jpeg" width="400px" height="auto">

#### Análise 2
> * Distância grande entre entre dois ingredientes implica em baixa compatibilidade/disponibilidade na mesma região?
>   
>   * Inicialmente nossa ideia era utilizar algoritmos de calculo de distância para calcular as maiores possíveis em nossa rede, porém, o ambiente online cypher não possuia algoritmos muito eficientes para isso, e acabamos utilizando uma implementação de dijkstra presente no amibnete, porém, mesmo com o número reduzido de nós, nossa querry excedeu o tempo de execução limite e falhou
