# C209
Repositório contendo o projeto da matéria de C209 - Computação Gráfica 

## TEMPLATE MATCHING

#### INTRODUÇÃO
Nosso projeto buscou tratar sobre a técnica de Template Matching, ou casamento de templates, uma abordagem amplamente utilizada para identificar padrões em imagens digitais. O processo de casamento pode ocorrer de duas maneiras: com base nas características específicas do template T ou considerando toda a região do template T para encontrar correspondências em uma imagem analisada A. Em ambas as abordagens, é essencial empregar alguma medida de similaridade.

Diversas métricas são comumente aplicadas, como a soma das diferenças quadradas, soma das diferenças absolutas, correlação e correlação cruzada normalizada (NCC), nas quais o seu valor mínimo ou máximo indicará a região de maior similaridade. É uma técnica bastante pesquisada por cientistas da computação no mundo todo, já que abrange diversos usos em diferentes áreas, desde a área da saúde até a empresarial.

A teoria por trás dele é bastante simples, na verdade. Funciona assim: você tem uma imagem maior, que é sua "imagem de origem", e uma imagem menor, que é seu "modelo" ou "template". O objetivo é encontrar a posição na imagem de origem onde o template se encaixa melhor. O algoritmo percorre a imagem de origem, comparando a semelhança entre o pixel atual e o pixel correspondente no template. Existem diferentes métodos de comparação, como a Soma dos Quadrados das Diferenças (SSD) ou a Correlação Cruzada Normalizada (NCC).

Quando a semelhança atinge um valor máximo ou mínimo (dependendo do método), você identifica a posição onde o template melhor se alinha com a imagem de origem. Isso é ótimo para detecção de padrões simples, mas pode ter problemas com rotação, escala ou variações de iluminação.

Em resumo, o Template Matching é uma técnica básica, mas eficaz, para encontrar padrões em imagens.

#### ALGORITMO
O algoritmo criado para esse projeto teve como objetivo principal simplificar de maneira concisa e didática essa técnica tão famosa, sem usar bibliotecas que possam tornar a solução trivial. Usamos apenas a biblioteca Numpy para trabalhar com arrays, Matplotlib para melhor visualização dos resultados, e PIL para facilitar o processo de entrada da imagem. A métrica escolhida para encontrar semelhanças entre o template e a imagem original foi a Soma das Diferenças Absolutas.

Nessa técnica, começamos com uma imagem de origem e uma imagem menor, que é o template que você está procurando na imagem maior. Coloque o canto superior esquerdo do template na posição inicial na imagem de origem.

Para cada pixel no template e na região correspondente da imagem de origem, calcule a diferença absoluta entre os valores de intensidade dos pixels.
A diferença absoluta é simplesmente a diferença entre os valores dos pixels, sem considerar a direção (sinal). Some todas as diferenças absolutas calculadas. Isso cria uma única medida que representa a dissimilaridade ou o "erro" entre o template e a região da imagem de origem. Desloque o template para a próxima posição na imagem de origem e repita o processo de cálculo da SAD.

A posição onde a SAD é mínima indica a melhor correspondência entre o template e a região da imagem de origem.

###### TESTE 1:

<img src="/C209/Testes/Figure_1.jpg">

###### TESTE 2:

<img src="/C209/Testes/Figure_2.jpg">

###### TESTE 3:

<img src="/Testes/Figure_3.jpg">



