import sys


def mostra_domanda(domanda: str) -> None:
    print(domanda)

def valida_scelta(scelta:str) -> bool:
    """Questa funzione controlla l'input dell'utente"""
    scelta_tmp = scelta.upper()
    if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp =="D":
        return True
    else:
        return False

def raccogli_risposta() -> str:
    """Questa funzione prende input dell'utente"""
    return input("Inserisci la tua scelta: ")

def leggi_file(file_path : str) -> str:
        with open(file_path, "r") as file:
            content = file.read()
        return content

def estrai_index(content:str) -> int:
    return content.index("£")

def estrai_domanda(content: str, index : int) -> str:
    return content[0:index]
  
def estrai_risposta(content: str, index : int) -> str:
    return content[index+1:]
     

def is_risposta_esatta(scelta:str, risposta_esatta : str) -> str:
    if scelta.upper() == risposta_esatta:
        return True
    else:
        return False

def genera_feedback(is_corretta : bool) -> str:
    """Questa funzione controlla se la risposta è giusta"""
    if is_corretta == True:
        return "Hai indovinato!"
    else:
        return "Non hai indovinato!"
    

def mostra_feedback(messaggio : str) -> None:
    simbolo : str = "*"*30
    print(f"""
{simbolo}
{messaggio}
{simbolo}"""  )

def main():
    domande_list :list[str]= []
    qa : dict[str, str] = {
        "domanda": None,
        "risposta" : None
    }
    with open("domande_risposte/domande.txt", "r") as file:
        for i in file:
            domande_list.append(i.strip())
    
    content: str = leggi_file(f"domande_risposte/{domande_list[1]}")
    index : int = estrai_index(content)
    qa["domanda"] : str = estrai_domanda(content, index)
    qa["risposta"] : str = estrai_risposta(content, index)
    print(qa)
    """
    file_path : str = sys.argv[1]
    content : str  = leggi_file(file_path)
    index : int = estrai_index(content)
    domanda : str = estrai_domanda(content, index)
    risposta : str = estrai_risposta(content, index)
    is_risposta_corretta: bool = False
    while True:
        mostra_domanda(domanda)
        risposta_da_validare : str = raccogli_risposta()
        risposta_validata : bool = valida_scelta(risposta_da_validare)
        feedback : str = ""

        if risposta_validata == True:
            is_risposta_corretta = is_risposta_esatta(risposta_da_validare, risposta)
            feedback = genera_feedback(is_risposta_corretta)
        else:
            feedback = "Inserisci solo opzioni valide!"
            
        mostra_feedback(feedback)
        if is_risposta_corretta == True:
            break 
"""

main()