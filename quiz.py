

def mostra_domanda() -> None:
    """Questa funzione restituisce la domanda e le opzioni della risposta"""
    print("""Chi parteciperà a Sanremo 2026?" \
    
    A. Nayt
    B. La Nina
    C. Nilla Pizzi 
    D. Rocco Papaleo
    """)

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


def genera_feedback(scelta:str) -> str:
    """Questa funzione controlla se la risposta è giusta"""
    if scelta.upper() == "A":
        return "Hai indovinato!"
    else:
        return "Non hai indovinato!"
    


def mostra_feedback(messaggio : str) -> None:
    simbolo : str = "*"*30
    print(f"""
{simbolo}
{messaggio}
{simbolo}"""  )


risposta_da_validare : str = raccogli_risposta()
risposta_validata : bool = valida_scelta(risposta_da_validare)
feedback : str = ""

if risposta_validata == True:
    feedback = genera_feedback(risposta_da_validare)
else:
    feedback = "Inserisce solo  la risposta tra le opzioni elencate: "

mostra_feedback(feedback)    