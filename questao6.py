convidados = ["Luciano", "João", "Manoel", "Adeilto", "Thales"]

convite = "Olá {}, você está convidado para um jantar em minha casa no próximo sábado."

for convidado in convidados:
 print(convite.format(convidado))

 desistentes = ["Luciano", "Adeilto"]
 print("\nInfelizmente, {} não poderão comparecer.\n".format(desistentes))

convidados.remove("Luciano")
convidados.remove("Adeilto")
convidados.append("Ana")

for convidado in convidados:
     print(convite.format(convidado))