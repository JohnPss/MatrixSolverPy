with open("matriz.txt", "r") as arquivo:
    primeira_linha = arquivo.readline().strip()
    linhas, colunas = map(int, primeira_linha.split())

    matriz = []
    for _ in range(linhas):
        linha = arquivo.readline().strip()
        matriz.append(linha[:colunas])

def andar_pela_matriz(matriz, linhas, colunas):
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == ' ':
                x, y = i, j
                break

    def pode_andar(x, y):
        return 0 <= x < linhas and 0 <= y < colunas and matriz[x][y] == '-'

    while True:
        for dx, dy in movimentos:
            novo_x, novo_y = x + dx, y + dy
            if pode_andar(novo_x, novo_y):
                matriz[x] = matriz[x][:y] + ' ' + matriz[x][y+1:]
                x, y = novo_x, novo_y
                matriz[x] = matriz[x][:y] + ' ' + matriz[x][y+1:]
                for linha in matriz:
                    print(linha)
                print()
                break
        else:
            break

andar_pela_matriz(matriz, linhas, colunas)

print("Dimensões da matriz:", linhas, "x", colunas)
print("Matriz:")
for linha in matriz:
    print(linha)
