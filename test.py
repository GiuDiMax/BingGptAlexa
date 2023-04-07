import re

string = """
I 12 apostoli erano i discepoli che Gesù scelse e chiamò a sé per diffondere il suo messaggio nel mondo. I loro nomi erano: Pietro, Giovanni, Giacomo il maggiore, Andrea, Filippo, Tommaso, Bartolomeo, Matteo, Giacomo il minore, Simone lo Zelota, Giuda Taddeo e **Mattia**[^1^] [^2^] [^4^]. Mattia fu scelto dopo la morte di Gesù per sostituire Giuda Iscariota, che lo tradì[^2^] [^4^]. Gli apostoli seguirono Gesù durante la sua vita terrena e furono testimoni della sua passione, morte e resurrezione[^2^] [^3^]. Dopo la Pentecoste, gli apostoli si dedicarono alla predicazione del Vangelo e alla fondazione della Chiesa cristiana[^3^] [^4^].
"""

string = re.sub("\[\^[[0-9]+\^\]", "", string).replace("  ", " ").replace(" .", ".").replace(" ,", ",")
print(string)
