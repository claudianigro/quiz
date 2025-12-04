def estrai_index(content:str) -> int:
    return content.index("$")

def estrai_domanda(content:str, index:int) -> str:
    return content[0:index]

def estrai_risposta(content:str, index:int) -> str:
    return content(index+1)

def est

def main():
    domande_list: list[str] = []
    qa : dict[str,str] = {
        "domanda" : None, "risposta" : None
    }

with open("domande.txt", "r") as f:
    for i in f:
        domande_liste.append(i.strip())