# Projeto de Matriz em Python

## Descrição
Este projeto foi desenvolvido para a disciplina de Python no CEFET-MG, ministrada pelo professor Guido Pantuza. O programa lê uma matriz de caracteres de um arquivo texto e simula um percurso dentro dessa matriz, marcando o caminho percorrido.

## Funcionalidades
- Lê uma matriz de um arquivo texto
- Identifica uma posição inicial (espaço vazio ' ')
- Percorre a matriz seguindo caminhos demarcados por '-'
- Visualiza a matriz e o caminho percorrido

## Como funciona
O programa lê um arquivo chamado "matriz.txt" que contém:
1. Primeira linha: dimensões da matriz (linhas e colunas)
2. Linhas seguintes: representação visual da matriz usando caracteres

O algoritmo inicia em uma posição vazia (' ') e tenta se mover em quatro direções possíveis (cima, baixo, esquerda, direita), seguindo apenas por células marcadas com '-'. À medida que o percurso é feito, o caminho é marcado.

## Exemplo de entrada (matriz.txt)
```
5 5
#####
#   #
#-###
#---#
#####
```

## Como usar
1. Crie um arquivo chamado "matriz.txt" com a definição da matriz
2. Execute o programa com `python matriz.py`

## Estrutura do código
- Leitura do arquivo e criação da matriz
- Função `andar_pela_matriz` que implementa o algoritmo de percurso
- Apresentação da matriz resultante

## Requisitos
- Python 3.x

## Autor
Desenvolvido por João Siqueira para a disciplina de Python no CEFET-MG.

## Professor
Guido Pantuza
