import graphs as grafo
from queue import Queue as que
from graphs import Grafo as Grafo
from dijkstra import dijkstra as dk
from kruskalPrim import KruskalPrim as pk
import random 

grafo = Grafo()
        
grafoMalla30 = Grafo().grafoDorogovtsevMendes(30, False)
for arista in grafoMalla30.aristas:
    arista.distancia = random.randint(0,10000)
krusk = pk.kruskal(grafoMalla30)

grafo.generaGephi(krusk[0], "K-Chico")
print("________________________________________")
kruski = pk.kruskalInv(grafoMalla30)
grafo.generaGephi(kruski[0], "KI-Chico")
print("________________________________________")
prim = pk.prim(grafoMalla30)
#print(prim)
grafo.generaGephi(prim[0],"prim-Chico")

grafoMalla100 = Grafo().grafoDorogovtsevMendes(100, False)
for arista in grafoMalla100.aristas:
    arista.distancia = random.randint(0,10000)
krusk = pk.kruskal(grafoMalla100)

grafo.generaGephi(krusk[0], "K-Mediano")
print("________________________________________")
kruski = pk.kruskalInv(grafoMalla100)
grafo.generaGephi(kruski[0], "KI-Mediano")
print("________________________________________")
prim = pk.prim(grafoMalla100)
#print(prim)
grafo.generaGephi(prim[0],"prim-Mediano")


grafoMalla500 = Grafo().grafoDorogovtsevMendes(500, False)
for arista in grafoMalla500.aristas:
    arista.distancia = random.randint(0,10000)
krusk = pk.kruskal(grafoMalla500)

grafo.generaGephi(krusk[0], "K-Grande")
print("________________________________________")
kruski = pk.kruskalInv(grafoMalla500)
grafo.generaGephi(kruski[0], "KI-Grande")
print("________________________________________")
prim = pk.prim(grafoMalla500)
#print(prim)
grafo.generaGephi(prim[0],"prim-Grande")