# Apresentação do Projeto 1 - Modelo Conceitual e Lógico

## Slides da Apresentação
> https://github.com/uniaovasko/uniaovasko_vasko/blob/main/project-1/images/Projeto%20Parte%201-2.pdf

## Motivação e Contexto

> O tema do projeto foi definido como “O que as pessoas comem ao redor do mundo”. A ideia para o projeto surgiu de uma análise do sistema de comida a quilo brasileiro, em que uma mesma fileira de pratos possuem alimentos de receitas de origens diversas, como o spaghetti italiano ao lado do sushi japonês que por sua vez está ao lado do kibe, que possui origens no Oriente Médio. Diante tal situação, chegamos a diversas perguntas como “o quão semelhante pode ser uma refeição entre as diversas regiões do mundo?” e “como essa diversidade de pratos molda a dieta macromolecular de cada povo?”.


## Bases de Dados
> Elencar as bases de dados fonte utilizadas no projeto.

título da base | link | breve descrição
----- | ----- | -----
`FooDB` | `https://foodb.ca` | `FooDB representa uma ampla e abrangente fonte de informações sobre alimentos, abordando detalhes relacionados à química dos alimentos, sua composição de ingredientes e os diversos nutrientes que contêm.`
`CulinaryDB` | `https://cosylab.iiitd.edu.in/culinarydb/` | `CulinaryDB é um extenso depósito de informações sobre pratos culinários e seus componentes. Dentro deste vasto banco de dados, encontram-se mais de 40 mil receitas, cada uma com detalhes que incluem sua região de procedência, dentre as 20 regiões catalogadas, assim como o nome e a lista completa de ingredientes utilizados.`

## Modelo Conceitual

> <img src="images/er_projeto-1.png" width="400px" height="auto">

## Modelos Lógicos

~~~
Ingrediente(Nome, Grupo, Subgrupo)
Receita(ID, Regiao)
Composto(Nome, estrutura)
Macronutriente(Nome)
Contem(Receita_ID, Nome_Ingrediente)
	Receita_ID chave estrangeira -> Receita(ID)
	Nome_Ingrediente chave estrangeira -> Ingrediente(Nome)
Constitui(Nome_Ingrediente, Nome_Composto, Quantidade, Unidade)
	Nome_Ingrediente chave estrangeira -> Ingrediente(Nome)
	Nome_Composto chave estrangeira -> Composto(Nome)
Define(Nome_Ingrediente, Nome_Macronutriente, Quantidade, Unidade)
	Nome_Ingrediente chave estrangeira -> Ingrediente(Nome)
	Nome_Macronutriente chave estrangeira -> Macronutriente(Nome)
~~~

## Perguntas de Pesquisa/Análise

#### Pergunta/Análise 1
> * Quais as estruturas bioquímicas mais frequentes em cada região?
>   
>   * Por meio do CulinaryDB é possível identificar as receitas de cada região e seus ingredientes. Com esses ingredientes, por meio do FooDB será identificado as estruturas bioquímicas mais frequentes de cada região. Essa pergunta é importante pois a bioquímica dos alimentos é uma importante ferramenta para estudo para saúde pública, pois identifica estruturas que são mais comuns e mais raras para os diferentes povos do mundo.

#### Pergunta/Análise 2
> * Quais regiões possuem receitas com ingredientes majoritariamente vegetais?
>   
>   * Mantendo o mesmo modelo da pergunta 1, com os ingredientes de cada receita é possível identificar os subgrupos a qual pertencem. Assim é possível analisar como cada região se relaciona com as produções alimentícias locais.

#### Pergunta/Análise 3
> * Quais regiões possuem a maior média de gorduras por receita?
>   
>   * Utilizando os valores nutricionais de cada ingrediente, fornecido pelo FooDB, é possível identificar a proporção de gordura contida na receita. Com essa informação será possível estabelecer uma média de lipídios em cada região. É uma pergunta importante visto que na atualidade a obesidade é um grande problema.

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
