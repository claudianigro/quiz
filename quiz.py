

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

def is_risposta_esatta(scelta:str) -> str:
    if scelta.upper() == "A":
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
    is_risposta_corretta: bool = False
    while True:
        mostra_domanda()
        risposta_da_validare : str = raccogli_risposta()
        risposta_validata : bool = valida_scelta(risposta_da_validare)
        feedback : str = ""

        if risposta_validata == True:
            is_risposta_corretta = is_risposta_esatta(risposta_da_validare)
            feedback = genera_feedback(is_risposta_corretta)
        else:
            feedback = "Inserisci solo opzioni valide!"
            
        mostra_feedback(feedback)
        if is_risposta_corretta == True:
            break 

main()