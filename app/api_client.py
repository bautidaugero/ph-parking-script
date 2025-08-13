import requests
import base64
import sys
import os
import json

# Agregar el directorio del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config

class ApiClient:
    def __init__(self):
        # Usar la configuración directamente sin Flask
        self.base_url = Config.API_BASE_URL
        self.username = Config.API_USERNAME
        self.password = Config.API_PASSWORD
        self.group_id = Config.GROUP_ID
        self.group_name = Config.GROUP_NAME

    def _get_auth_header(self):
        credentials = f"{self.username}:{self.password}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return {'Authorization': f'Basic {encoded_credentials}'}
    
    def get_group_info(self):
        """Obtiene informacion del grupo actual"""
        try:
            url = f"{self.base_url}/accountGroup/{self.group_id}"
            headers = self._get_auth_header()

            response = requests.get(url, headers=headers)
            response.raise_for_status()

            return {
                'success': True,
                'data': response.json()
            }
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': f'Error al obtener informacion del grupo: {str(e)}'
            }
        
    def update_group_accounts(self, accounts_list):
        """Actualiza el grupo con la nueva lista de cuentas"""
        try:
            url = f"{self.base_url}/accountGroup/{self.group_id}"
            headers = self._get_auth_header()
            headers['Content-Type'] = 'application/json'
            
            payload = {
                "name": self.group_name,
                "status": "ENABLED",
                "accounts": accounts_list,
                "configurationDTO": {
                    "factorMargin": 1,
                    "allowsUncoveredOptions": False,
                    "bannedUnderlyings": [],
                    "maxUncoveredBatchs": 1000,
                    "factorForUncoveredSell": 1,
                    "resetCredit": True
                },
                "id": self.group_id
            }
            print(f"🔍 Enviando JSON: {json.dumps(payload, indent=2)}")
            response = requests.put(url, headers=headers, json=payload)
            response.raise_for_status()

            return {
                'success': True,
                'data': response.json()
            }
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': f'Error al actualizar el grupo: {str(e)}'
            }