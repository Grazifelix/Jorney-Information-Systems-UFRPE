#23/12/20
#Geometria do táxi: Distancia entre dois pontos num plano cartesiano
#formula: Dt(A,B)=|X2-X1|+|Y2-Y1|



def GeoTaxi(x1,y1,x2,y2):
    D = abs((x2-x1))+abs((y2-y1))
    return D


while True:
    dist = input()
    if dist:
        dist = dist.split()
        print(GeoTaxi(int(dist[0]), int(dist[1]), int(dist[2]), int(dist[3])))
    else:
        print("Ocorreu um erro.")
        break
