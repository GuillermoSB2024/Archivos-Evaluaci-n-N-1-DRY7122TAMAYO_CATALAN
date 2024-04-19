import ipaddress

def main():
    direccion_red = input("Ingrese la IP de red con su máscara (ej. 192.168.1.0/24): ")
    red = ipaddress.ip_network(direccion_red, strict=False)
    primera_ip_valida = str(red.network_address + 1)
    ultima_ip_valida = str(red.broadcast_address - 1)
    broadcast_ip = str(red.broadcast_address)
    
    print(f"Primera IP válida: {primera_ip_valida}")
    print(f"Última IP válida: {ultima_ip_valida}")
    print(f"IP de broadcast: {broadcast_ip}")
    
    dg = input("¿Cuál dirección del segmento será asignada al DG (IP Default Gateway con máscara)? ")
    
    info_red = {
        "primera_ip_valida": primera_ip_valida,
        "ultima_ip_valida": ultima_ip_valida,
        "broadcast_ip": broadcast_ip,
        "default_gateway": dg
    }
    
    buscar_dg = input("Ingrese la dirección del DG para buscar la información: ")
    if buscar_dg == info_red["default_gateway"]:
        print(f"Información del segmento: {info_red}")
    else:
        print("No se encontró la información para el DG proporcionado.")

if __name__ == "__main__":
    main()