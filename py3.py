def main():
    acl_numero = int(input("Introduzca el número de ACL IPv4: "))
    if 1 <= acl_numero <= 99 or 1300 <= acl_numero <= 1999:
        print("Es una ACL Estándar.")
    elif 100 <= acl_numero <= 199 or 2000 <= acl_numero <= 2699:
        print("Es una ACL Extendida.")
    else:
        print("El número no corresponde a una lista de acceso válida.")

if __name__ == "__main__":
    main()