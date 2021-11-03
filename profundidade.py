visited = set()  # manter os nodos visitados
path = list() # o caminho tomado
#criacao de um grafo exemplo
g = {
  '5': ['3', '7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': []
}


def dfs(visited, graph, node, target):
    #se o nodo não foi está dentro do set visited, ele é adicionado ao visited e ao path
    if node not in visited:
        print(node)
        visited.add(node)
        path.append(node)
        #se o nodo é o nodo objetivo, ele retorna o caminho
        if node == target:
            return path
        for neighbour in graph[node]:
            #criaçao de uma variavel temporaria para guardar o caminho encontrado
            temp_path = dfs(visited, graph, neighbour, target)
            #na hora que o caminho até o target é encontrado, entra nesse if que termina a recursão
            if temp_path:
                return temp_path
    return []
# execução teste
print("DFS")
result = dfs(visited, g, '5','2')
print(f"resultado: {result}")
