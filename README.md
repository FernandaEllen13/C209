# C209
Repositório contendo o projeto da matéria de C209 - Computação Gráfica 

## TEMPLATE MATCHING

#### INTEGRANTES:
*Fernanda Ellen de Souza*

*Leonardo dos Santos Ferreira*

#### INTRODUÇÃO
Nosso projeto buscou tratar sobre a técnica de Template Matching, ou casamento de templates, uma abordagem amplamente utilizada para identificar padrões em imagens digitais. O processo de casamento pode ocorrer de duas maneiras: com base nas características específicas do template T ou considerando toda a região do template T para encontrar correspondências em uma imagem analisada A. Em ambas as abordagens, é essencial empregar alguma medida de similaridade.

Diversas métricas são comumente aplicadas, como a soma das diferenças quadradas, soma das diferenças absolutas, correlação e correlação cruzada normalizada (NCC), nas quais o seu valor mínimo ou máximo indicará a região de maior similaridade. É uma técnica bastante pesquisada por cientistas da computação no mundo todo, já que abrange diversos usos em diferentes áreas, desde a área da saúde até a empresarial.

A teoria por trás dele é bastante simples, na verdade. Funciona assim: você tem uma imagem maior, que é sua "imagem de origem", e uma imagem menor, que é seu "modelo" ou "template". O objetivo é encontrar a posição na imagem de origem onde o template se encaixa melhor. O algoritmo percorre a imagem de origem, comparando a semelhança entre o pixel atual e o pixel correspondente no template. Existem diferentes métodos de comparação, como a Soma dos Quadrados das Diferenças (SSD) ou a Correlação Cruzada Normalizada (NCC).

Quando a semelhança atinge um valor máximo ou mínimo (dependendo do método), você identifica a posição onde o template melhor se alinha com a imagem de origem. Isso é ótimo para detecção de padrões simples, mas pode ter problemas com rotação, escala ou variações de iluminação.

Em resumo, o Template Matching é uma técnica básica, mas eficaz, para encontrar padrões em imagens.

#### ALGORITMO
O algoritmo criado para esse projeto teve como objetivo principal simplificar de maneira concisa e didática essa técnica tão famosa, sem usar bibliotecas que possam tornar a solução trivial. Usamos apenas a biblioteca Numpy para trabalhar com arrays, Matplotlib para melhor visualização dos resultados, e PIL para facilitar o processo de entrada da imagem. A métrica escolhida para encontrar semelhanças entre o template e a imagem original foi a Soma das Diferenças Absolutas.

Nessa técnica, começamos com uma imagem de origem e uma imagem menor, que é o template que você está procurando na imagem maior. O template inicia na posição inicial da imagem de origem, e para cada pixel de ambos, calcula-se a diferença absoluta(ou seja, a diferença sem considerar o sinal) entre os valores de intensidade dos pixels. Ao fim, soma-se todas as diferenças absolutas calculadas, criando uma única medida que representa a dissimilaridade entre o template e a região da imagem de origem. Esse processo é repetido até que toda a região da imagem seja rastreada. A região onde a Soma das DIferenças Absolutas é mínima indica a melhor correspondência entre as duas imagens.

###### TESTE 1:

<img src="/Testes/Figure_1.png">

###### TESTE 2:

<img src="/Testes/Figure_2.png">

###### TESTE 3:

<img src="/Testes/Figure_3.png">

#### CONCLUSÃO
Apesar de ser um método bastante difundido na área de processamento de imagens, seus algoritmos e técnicas tem suas vantagens e desvantagens, e sua eficácia está intimamente atralda ao contexto da aplicação. Entre as vantagens, temos sua simplicidade, sendo mais fácil entender e implementar do que outras técnicas dessa área. Além disso, é computacionalmente eficiente, não necessitando de processadores potentes para que seja aplicado.

Já dentre as desvantagens, está sua sensibilidade a variações, como por exemplo iluminação, rotação e escala, com pequenas mudanças afetando significantemente a correspondência. Ademais, encontra-se limitado a padrões simples, podendo ter dificuldades com imagens mais complexas. Essas desvantagens podem ser contornadas fazendo o pré-processamento tanto da imagem quanto do template, como por exemplo normalizar a intensidade do pixel ou utilizar de técnicas como filtragem e extração de caracterísitcas. Há inclusive a possibilidade de utilizar técnicas conjuntas mais avançadas, como as que são baseadas em aprendizado de máquina, as quais podem melhorar a capacidade de generalização do algoritmo. 

Em resumo, o Template Matching é uma ferramenta valiosa em contextos expecíficos, cujas limitações podem ser superadas com a combinação inteligente de técnicas adicionais.



#### REFERÊNCIAS
1. [https://community.revelo.com.br/reconhecimento-de-padroes-em-visao-computacional-para-identificacao-de-imagem-via-template-matching/]
2. [https://www.ppgee.ufmg.br/defesas/1244M.PDF]
3. [https://medium.com/geekculture/image-template-matching-methods-with-python-using-opencv-cd7fac319a2d]
4. [https://stackoverflow.com/questions/12715673/numpy-template-matching-using-matrix-multiplications]
5. [http://www.lps.usp.br/hae/apostila/tmatch-ead.pdf]
6. [https://docplayer.com.br/86843068-Explicacao-simplificada-de-template-matching-casamento-de-mascara-ou-casamento-de-modelo.html]



