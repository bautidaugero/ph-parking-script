# Agregar comparacion entre 2 

def validate_accounts(accounts_list):
    '''Valida que la lista de cuentas tenga el formato correcto'''

    if not accounts_list:
        return False, "La lista de cuentas está vacía"
    
    if len(accounts_list) == 0:
        return False, "La lista de cuentas está vacía"
    
    return True, f"Se encontraron {len(accounts_list)} cuentas válidas"