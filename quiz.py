def valida_scelta(scelta:str) -> bool:
    """Questa funzione controlla l'input dell'utente"""
    scelta_tmp = scelta.upper()
    if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp =="D":
        return True
    else:
        return False


def mostra_domanda() -> None:
    """Questa funzione restituisce la domanda e le opzioni della risposta"""
    print("""Chi parteciperà a Sanremo 2026?" \
    
    A. Nayt
    B. La Nina
    C. Nilla Pizzi 
    D. Rocco Papaleo
    """)

def raccogli_risposta() -> str:
    """Questa funzione prende input dell'utente"""
    return input("Inserisci la tua scelta: ")

risposta_da_validare : str = raccogli_risposta()
risposta_validata : bool = valida_scelta(risposta_da_validare)

print(risposta_validata)