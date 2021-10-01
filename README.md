# Ordenation-Algorithms
<p>Este programa tem como objetivo realizar teste empíricos de algoritmos para seus piores casos e casos aleatorios e armazenar localmente os dados obtidos</p>
<br>
<h2>Algoritmos testados:<h2>
<ul>
    <li>BUBBLE SORT</li>
    <li>MERGE SORT</li>
    <li>COUNTING SORT</li>
</ul>
<h2>Tamanhos de entrada testados:<h2>
<ul>
    <li>10 elementos</li>
    <li>100 elementos</li>
    <li>1000 elementos</li>
    <li>10000 elementos</li>
    <li>20000 elementos</li>
</ul>
<h2>Requisitos:</h2>
<p>Python 3.8 ou superior</p>
<p>Download python: https://www.python.org/downloads/</p>

<br>
<h2>Como executar:</h2>
<p>Para ver dados pré-armazenados:  <strong> python main.py</strong></p>
<p>Para realizar seus próprios teste:  <strong> python __init__.py</strong></p>

<br>
<h1>Pastas:</h1>
<br>

<h2>./modules</h2>
<p>Armazena todos os módulos fundamentais para a execução do programa</p>
<br>

<h2>./results</h2>
<p>Armazena todos os resultados dos testes em 3 pastas nomeadas conforme o algoritmo utilizado para realizar os testes. Embora a cada execução de "__init__.py" sobrescreva seus dadods, é fundamental para o programa.</p>
<br>

<h2>./tests</h2>
<p>Possui o único modulo que realiza os testes e salva os dados obtidos, utlizando módulos da pasta "./modules" </p>

<br>
<h1>Conclusão</h1>
<p>Dos 3 algoritmos testados, bubble sort foi o menos eficiente para tamanhos de entrada muitos elevados, em contrapartida, counting sort mostrou-se muito eficiente para qualquer tamanho de entrada, tendo em vista sua complexidade O(n), ele sempre será mais eficiente que bubble sort e merge sort para qualquer que seja o valor de n. Portanto, conclui-se que, para entradas pequenas, qualquer um dos 3 algoritmos testados será eficiente, porém para entradas demasiadamente grandes, recomenda-se que bubble sort seja descartado.</p>