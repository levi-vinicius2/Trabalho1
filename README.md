# README.md

## Descrição do Projeto

O projeto implementa a multiplicação eficiente de dois números inteiros utilizando o Algoritmo de Karatsuba, que melhora a performance da multiplicação em comparação com o método tradicional, reduzindo a complexidade de O(n²) para O(n^1.585).

### Explicação do Algoritmo

O algoritmo de Karatsuba divide os números a serem multiplicados em duas partes, semelhante ao merge sort, multiplicando recursivamente essas partes. Ele realiza três multiplicações em vez de quatro, o que resulta em uma redução no número de operações, otimizando o processo de multiplicação.

Passos do algoritmo:

1. Caso Base: Se qualquer número `x` ou `y` for menor que 10, o algoritmo simplesmente realiza a multiplicação direta entre os dois números.

2. Divisão dos Números: Caso contrário, os números são divididos ao meio em duas partes: uma parte "alta" e uma parte "baixa".

3. Recursão: O algoritmo realiza três multiplicações recursivas:
    - `z0` é o produto das partes baixas de `x` e `y`.
    - `z2` é o produto das partes altas de `x` e `y`.
    - `z1` é o produto da soma das partes altas e baixas de `x` e `y`.

4. Combinação dos Resultados: O produto final é obtido combinando os resultados de `z0`, `z1` e `z2` com os respectivos fatores de potência de 10, de acordo com a posição das partes altas e baixas.

### Lógica do Algoritmo Linha a Linha

- `if x < 10 or y < 10:`  
  Caso base: Se `x` ou `y` for menor que 10, a multiplicação direta é feita.
  
- `n = max(len(str(x)), len(str(y)))`  
  Calcula o número de dígitos do maior número entre `x` e `y`.
  
- `m = n // 2`  
  Determina o ponto de divisão dos números, isto é, o número de dígitos que cada parte (alta e baixa) terá.
  
- `parte_alta1, parte_baixa1 = divmod(x, 10**m)`  
  Divide `x` em duas partes: `parte_alta1` e `parte_baixa1`.

- `parte_alta2, parte_baixa2 = divmod(y, 10**m)`  
  Realiza o mesmo processo para `y`.

- `z0 = karatsuba(parte_baixa1, parte_baixa2)`  
  Multiplica as partes baixas recursivamente.

- `z1 = karatsuba((parte_baixa1 + parte_alta1), (parte_baixa2 + parte_alta2))`  
  Multiplica as somas das partes (alta + baixa).

- `z2 = karatsuba(parte_alta1, parte_alta2)`  
  Multiplica as partes altas recursivamente.

- `return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0`  
  Combina os resultados das multiplicações recursivas e retorna o valor final.

## Como Executar o Projeto

Para rodar o código localmente, siga os passos abaixo:

1. Instale o Python.
2. Abra a pasta em que o código python está.
3. Execute o seguinte comando: python main.py
4. Resultado esperado: 'O resultado de 146123 * 352120 é 51452830760'

   # Relatório Técnico

## 1. Análise da Complexidade Ciclomática

A complexidade ciclomática é uma métrica que quantifica a complexidade do fluxo de controle de um programa. Ela pode ser calculada usando a fórmula:

\[
M = E - N + 2P
\]

Onde:
- E: Número de arestas no grafo de fluxo.
- N: Número de nós no grafo de fluxo.
- P: Número de componentes conexos (em um programa simples, P = 1).

### Fluxo de Controle

O fluxo de controle do algoritmo pode ser modelado como um grafo de fluxo, onde cada "nó" representa uma operação e cada "aresta" representa a transição entre operações.

Para a função `karatsuba(x, y)`:
- Um nó para o caso base, onde `x < 10` ou `y < 10`.
- Três nós para as recursões de `z0`, `z1`, e `z2`.
- Um nó para a combinação final dos resultados.

Número de nós (N) = 5 (inclui o caso base e os três resultados recursivos + o nó final de combinação).  
Número de arestas (E) = 6 (caminhos de execução entre as operações).

Então, a complexidade ciclomática M é:

\[
M = 6 - 5 + 2(1) = 3
\]

## 2. Análise da Complexidade Assintótica

### Complexidade Temporal

A complexidade temporal do algoritmo de Karatsuba pode ser representada pela seguinte recursão:

\[
T(n) = 3T(n/2) + O(n)
\]

A solução dessa recursão, usando o Teorema Mestre, resulta em uma complexidade assintótica de:

\[
T(n) = O(n^{\log_2 3}) \approx O(n^{1.585})
\]

Portanto, o algoritmo tem um tempo de execução mais eficiente em comparação com a multiplicação tradicional de O(n²).

### Complexidade Espacial

A complexidade espacial é determinada pela profundidade da recursão. A profundidade máxima da recursão ocorre quando cada chamada recursiva divide o número pela metade, o que leva a uma complexidade espacial de:

\[
O(\log n)
\]

## 3. Análise de Casos

- Melhor Caso: Quando os números `x` e `y` são pequenos e o algoritmo resolve com multiplicação direta. A complexidade é **O(1)** para números pequenos.
  
- Caso Médio: O algoritmo realiza uma divisão e recursão em vários níveis, mas a complexidade continua sendo **O(n^{1.585})** em média, devido à natureza do algoritmo.

- Pior Caso: Mesmo no pior caso, onde o número de recursões é máximo, a complexidade é O(n^{1.585}).

## Conclusão

O algoritmo de Karatsuba oferece uma maneira eficiente de multiplicar números grandes, superando a multiplicação tradicional em termos de desempenho. A análise mostra que sua complexidade é significativamente melhor para números grandes, especialmente em relação a algoritmos de multiplicação de tempo quadrático.

