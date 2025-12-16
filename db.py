import pyodbc

DB_CONFIG = {
    "driver": "ODBC Driver 18 for SQL Server",
    "server": "localhost\\SQLEXPRESS",
    "database": "myERP_prod",
    "username": "myERPuser",
    "password": "9myAdminErp23",
    "trust_server_certificate": "yes"
}

def get_connection():
    conn_str = (
        f"DRIVER={{{DB_CONFIG['driver']}}};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['username']};"
        f"PWD={DB_CONFIG['password']};"
        f"TrustServerCertificate={DB_CONFIG['trust_server_certificate']};"
    )
    return pyodbc.connect(conn_str)