def process_accounts_list(accounts_text):
    '''Procesa la lista de comitentes y
    devuelve una lista limpia'''

    if not accounts_text:
        return []
    
    accounts = []
    lines = accounts_text.split('\n')

    for line in lines:
        #Dividir cada linea por comas
        line_accounts = line.split(',')
        for account in line_accounts:
            # Limpiar espacios y caracteres especiales
            clean_account = account.strip()
            if clean_account and clean_account.isdigit():
                accounts.append(clean_account)
    return accounts

def validate_accounts(accounts_list):
    '''Valida que la lista de cuentas tenga el formato correcto'''

    if not accounts_list:
        return False, "La lista de cuentas está vacía"
    
    if len(accounts_list) == 0:
        return False, "La lista de cuentas está vacía"
    
    return True, f"Se encontraron {len(accounts_list)} cuentas válidas"