"""Aula 05 - Listas, fatiamento, métodos de lista e tuplas."""

# ---------- Variáveis e f-string ----------
nome = "Carlos"
idade = 34
print(f"{nome} tem {idade} anos de idade!")

# ---------- Listas e índices ----------
numeros = [56, 35, 67, 89, 225]
print(numeros[0])

aluno = ["Carlos", 34, 7.85, 999, 20, 69, 777]
print(aluno[2])

# ---------- Fatiamento: [inicio : fim : passo] ----------
print(aluno[0:])     # todos
print(aluno[::-1])   # invertida
print(aluno[1:4:2])  # do índice 1 ao 3, de 2 em 2
print(aluno[3:])     # do índice 3 até o fim
print(aluno[::2])    # elementos alternados

# ---------- Inserção de elementos ----------
equipamento_mota = ["GPS", "luvas", "bota", "intercomunicador"]

equipamento_mota.append("fato de chuva")        # no final
equipamento_mota.insert(0, "Capacete")          # na posição 0 (início)
extras = ["gps de reserva", "câmera de ação"]
equipamento_mota.extend(extras)                 # junta outra lista
print(equipamento_mota)

# ---------- Remoção de elementos ----------
equipamento_mota.remove("GPS")                  # remove pelo valor
ultimo = equipamento_mota.pop()                 # remove e devolve o último
segundo = equipamento_mota.pop(1)               # remove e devolve o índice 1
del equipamento_mota[0]                         # remove pelo índice
print(equipamento_mota, "| removidos:", ultimo, segundo)
equipamento_mota.clear()                        # esvazia a lista
print(equipamento_mota)                         # []

# ---------- Ordenação ----------
notas = [7.5, 30, 9.9, 6.6]

notas.sort()                                    # altera a própria lista (crescente)
print(notas)
notas.sort(reverse=True)                        # decrescente
print(notas)

novas_notas = sorted(notas)                     # devolve nova lista, sem alterar a original
print(novas_notas)

# ---------- Pesquisa ----------
cidades = ["Ipatinga", "Bambui", "Tapirai", "BH"]

print(cidades.index("BH"))                      # posição do elemento
if "Bambui" in cidades:
    print("Bambui está na lista de cidades")

# ---------- Exercício: top 3 altitudes do drone ----------
altitudes = []
print("\n=== Sistema de Registro de Altitudes do Drone ===\n")
for i in range(1, 6):
    altitudes.append(float(input(f"Informe a altitude {i} (m): ")))

altitudes.sort(reverse=True)
print("\nTop 3 maiores altitudes:", altitudes[:3])

# ---------- Tuplas ----------
# Coleção ordenada, indexada e imutável. Definida com () e acessada com [].
# Lista: dados que mudam (clientes, patrimônio investido, marcas).
# Tupla: dados constantes (coordenadas, meses do ano).
coordenada_bh = (-19.92, -43.94)
print(coordenada_bh[0])
