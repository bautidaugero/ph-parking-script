'''Script para procesar comitentes desde base de datos y actualizar grupo PH Parking'''


import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

sys.stdout = open("log.txt", "a", encoding="utf-8")

from app.api_client import ApiClient
from app.utils import validate_accounts


def get_accounts_from_database():
    """
    Funcion para obtener comitentes desde la base de datos
    (Aca venis vos Axel)
    """
    print("🔍 Obteniendo comitentes desde la base de datos...")

    cuentas_ejemplo = [
        "1008",
        "1007",
        "10084",
        "1111"
    ]
    print(f"✅ Se encontraron {len(cuentas_ejemplo)} comitentes en la base de datos")
    return cuentas_ejemplo

def main():
    """
    Funcion principal
    """
    print("🚗 PH Parking - Procesamiento de Comitentes")
    print("=" * 50)
    print(f"⏰ Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    try:
        
        print()
        
        # 1. Obtener informacion actual del grupo
        print("🔍 Obteniendo informacion actual del grupo...")
        api_client = ApiClient()
        current_info = api_client.get_group_info()

        if current_info['success']:
            current_accounts = current_info['data']['accounts']
            print(f"✅ Grupo actual: {current_info['data']['name']}")
            print(f"✅ Cuentas actuales: {len(current_accounts)}")
            print(f"✅ Lista actual: {current_accounts}")
        else:
            print(f"❌ Error al obtener informacion del grupo: {current_info['error']}")
            return
        print()

        # 2. Obtener comitentes desde la base de datos
        new_accounts = get_accounts_from_database()

        if not new_accounts:
            print("❌ No se encontraron comitentes en la base de datos")
            return
        
        print(f"📋 Comitentes obtenidos: {new_accounts}")
        print()

        # 3. Validar las cuentas
        print("🔍 Validando comitentes...")
        is_valid, message = validate_accounts(new_accounts)
        
        if not is_valid:
            print(f"❌ Error de validación: {message}")
            return
        
        print(f"✅ Validación exitosa: {message}")
        print()

        # 4. Actualizar el grupo
        print("🔄 Actualizando grupo con nuevos comitentes...")
        result = api_client.update_group_accounts(new_accounts)

        if result['success']:
            print("✅ Grupo actualizado exitosamente!")
            print(f"📊 Comitentes procesados: {len(new_accounts)}")
            print(f"📋 Lista final: {new_accounts}")
        else:
            print(f"❌ Error al actualizar grupo: {result['error']}")
            return
        
        print()
        print("🎉 Proceso completado exitosamente!")

    except Exception as e:
        print(f"❌ Error inesperado: {str(e)}")
        return
    
    finally:
        print()
        print(f"⏰ Fin: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)

if __name__ == "__main__":
    main()