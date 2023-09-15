# Modelo para Apresentação do Projeto 1 - Modelo Conceitual e Lógico

## Slides da Apresentação
> Coloque aqui o link para o PDF da apresentação

## Motivação e Contexto

> O tema do projeto foi definido como “O que as pessoas comem ao redor do mundo”. A ideia para o projeto surgiu de uma análise do sistema de comida a quilo brasileiro, em que uma mesma fileira de pratos possuem alimentos de receitas de origens diversas, como o spaghetti italiano ao lado do sushi japonês que por sua vez está ao lado do kibe, que possui origens no Oriente Médio. Diante tal situação, chegamos a diversas perguntas como “o quão semelhante pode ser uma refeição entre as diversas regiões do mundo?” e “como essa diversidade de pratos molda a dieta macromolecular de cada povo?”.


## Bases de Dados
> Elencar as bases de dados fonte utilizadas no projeto.

título da base | link | breve descrição
----- | ----- | -----
`FooDB` | `https://foodb.ca` | `FooDB representa uma ampla e abrangente fonte de informações sobre alimentos, abordando detalhes relacionados à química dos alimentos, sua composição de ingredientes e os diversos nutrientes que contêm.`
`CulinaryDB` | `https://cosylab.iiitd.edu.in/culinarydb/` | `CulinaryDB é um extenso depósito de informações sobre pratos culinários e seus componentes. Dentro deste vasto banco de dados, encontram-se mais de 40 mil receitas, cada uma com detalhes que incluem sua região de procedência, dentre as 20 regiões catalogadas, assim como o nome e a lista completa de ingredientes utilizados.`

## Modelo Conceitual

> Coloque aqui a imagem do modelo conceitual em ER ou UML, como o exemplo a seguir:
> ![ER Taxi](images/er-taxi.png)

## Modelos Lógicos

> Coloque aqui o modelo lógico relacional dos bancos de dados relacionados ao modelos conceitual. Sugere-se o formato a seguir.

> Exemplo de modelo lógico relacional
~~~
PESSOA(_Código_, Nome, Telefone)
ARMÁRIO(_Código_, Tamanho, Ocupante)
  Ocupante chave estrangeira -> PESSOA(Código)
~~~

## Perguntas de Pesquisa/Análise

> Liste aqui as perguntas de pesquisa/análise. Nem todas as perguntas precisam de implementação associada. É possível haver perguntas em que a solução é apenas descrita para demonstrar o potencial da base. Abaixo são ilustradas três perguntas, mas pode ser um número maior a critério da equipe.

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
>   * Explicação em linhas gerais de como a base pode ser usada para responder esta pergunta e a sua relevância.

#### Pergunta/Análise 2
> * Quais regiões com maior diversidade de subgrupos alimentícios?
>   
>   * Explicação em linhas gerais de como a base pode ser usada para responder esta pergunta e a sua relevância.

#### Pergunta/Análise 3
> * Pergunta 3
>   
>   * Explicação em linhas gerais de como a base pode ser usada para responder esta pergunta e a sua relevância.
