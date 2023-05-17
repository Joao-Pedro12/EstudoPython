import csv


with open ('filmes.csv', 'r', encoding='utf-8')as arquivo:
    filme_visto = csv.reader(arquivo, delimiter=',')
    
    vizu = 2
    maisvisto = ""

    for linha in filme_visto:
        vizumax = linha[2]
        filmemax = int(linha[8])
    if int(vizumax) > vizu:
        vizu = int(vizumax)
        maisvisto = int(linha[8])
        print("O filme mais visto é:", filmemaisvisto)
        print("Número de visualizações:", vizu)



            
        
        