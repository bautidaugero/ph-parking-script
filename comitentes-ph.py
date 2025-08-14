import pymssql

# Establecer los parámetros de conexión
server = "172.17.15.179"
port = 1433  # Puerto predeterminado de SQL Server
database = "VBolsaNet"
username = "conversiondat"
password = "Pinoteca1972+"

try:
    # Crear la conexión
    conn = pymssql.connect(server=server,
                          port=port,
                          database=database, 
                          user=username,
                          password=password)
    
    # Crear un cursor
    cursor = conn.cursor()
    
    # Ejecutar la consulta
    query = """
    select NumComitente, Descripcion, EsFisico, EstaAnulado 
    from COMITENTES 
    where EsFisico=-1 and EstaAnulado=0 
    order by NumComitente
    """
    
    cursor.execute(query)
    
    # Obtener y mostrar los resultados
    for row in cursor:
        print(f"NumComitente: {row[0]}, Descripcion: {row[1]}, EsFisico: {row[2]}, EstaAnulado: {row[3]}")
    
    # Cerrar cursor y conexión
    cursor.close()
    conn.close()

except pymssql.Error as e:
    print(f"Error al conectar a la base de datos: {e}")
