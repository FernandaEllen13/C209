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

Nessa técnica, começamos com uma imagem de origem e uma imagem menor, que é o template que você está procurando na imagem maior. Coloque o canto superior esquerdo do template na posição inicial na imagem de origem.

Para cada pixel no template e na região correspondente da imagem de origem, calcule a diferença absoluta entre os valores de intensidade dos pixels.
A diferença absoluta é simplesmente a diferença entre os valores dos pixels, sem considerar a direção (sinal). Some todas as diferenças absolutas calculadas. Isso cria uma única medida que representa a dissimilaridade ou o "erro" entre o template e a região da imagem de origem. Desloque o template para a próxima posição na imagem de origem e repita o processo de cálculo da SAD.

A posição onde a SAD é mínima indica a melhor correspondência entre o template e a região da imagem de origem.

###### TESTE 1:

<img src="/Testes/Figure_1.png">

###### TESTE 2:

<img src="/Testes/Figure_2.png">

###### TESTE 3:

<img src="/Testes/Figure_3.png">

#### CONCLUSÃO
O Template Matching tem suas vantagens e desvantagens, e a eficácia da técnica depende muito do contexto da aplicação. Vamos dar uma olhada:

Vantagens:

Simplicidade:

É fácil de entender e implementar, o que o torna acessível para aplicações simples.
Computacionalmente Eficiente:

Para imagens pequenas e templates simples, o Template Matching pode ser computacionalmente eficiente.
Desvantagens:

Sensibilidade a Variações:

É sensível a variações de iluminação, rotação e escala. Pequenas mudanças podem afetar significativamente a correspondência.
Limitado a Padrões Simples:

Funciona melhor para padrões simples e pode ter dificuldades com variações complexas.
Não Robusto:

Pode não ser robusto o suficiente para ambientes onde as condições variam muito.
Melhorias Possíveis:

Normalização de Intensidade:

Normalizar a intensidade dos pixels pode tornar o método mais robusto a variações de iluminação.
Uso de Outros Métodos:

Combinação com métodos de pré-processamento, como filtragem ou extração de características, pode melhorar a robustez.
Incorporação de Informações Contextuais:

Adição de informações contextuais pode melhorar a precisão, como considerar padrões ao redor do template.
Utilização de Técnicas Avançadas:

Métodos mais avançados, como técnicas baseadas em aprendizado de máquina, podem ser aplicados para melhorar a capacidade de generalização.
Viabilidade com Outras Técnicas:

Sim, é frequentemente viável e até recomendado combinar o Template Matching com outras técnicas. Por exemplo, você pode usar detecção de características para pré-processar a imagem e, em seguida, aplicar Template Matching para refinamento.
Em resumo, o Template Matching é uma ferramenta valiosa em contextos específicos, mas suas limitações podem ser superadas com a combinação inteligente de técnicas adicionais.

#### REFERÊNCIAS
1. [https://community.revelo.com.br/reconhecimento-de-padroes-em-visao-computacional-para-identificacao-de-imagem-via-template-matching/]
2. [https://www.ppgee.ufmg.br/defesas/1244M.PDF]
3. [https://medium.com/geekculture/image-template-matching-methods-with-python-using-opencv-cd7fac319a2d]
4. [https://stackoverflow.com/questions/12715673/numpy-template-matching-using-matrix-multiplications]
5. [http://www.lps.usp.br/hae/apostila/tmatch-ead.pdf]
6. [https://docplayer.com.br/86843068-Explicacao-simplificada-de-template-matching-casamento-de-mascara-ou-casamento-de-modelo.html]



