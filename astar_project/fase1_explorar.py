from mapa import mapa_romenia, heuristica_bucareste

print('Quantidade de cidades no mapa:', len(mapa_romenia))
print('Quantidade de valores de h(n):', len(heuristica_bucareste))

vizinhos_arad = mapa_romenia['Arad']
print()
print('Vizinhos de Arad:', vizinhos_arad)
print('Tipo do valor:', type(vizinhos_arad))

primeira = vizinhos_arad[0]
print()
print('Primeira estrada que sai de Arad:', primeira)
print(' posição [0] -> cidade vizinha:', primeira[0])
print(' posição [1] -> custo em km :', primeira[1])

print()
print('Estradas que saem de Arad:')
for vizinho, custo in mapa_romenia['Arad']:
    print(' Arad ->', vizinho, '=', custo, 'km')
