import nmap

def run_nmap(ip, ports, arguments, sudo):
    scanner = nmap.PortScanner()
    scanner.scan(ip, ports, arguments)

    for host in scanner.all_hosts():
        print("Host: ", host)
        for proto in scanner[host].all_protocols():
            lport = scanner[host][proto].keys()
            for port in lport:
                print("   Port: ", port)
                print("   Name: ", scanner[host][proto][port]['name'])
                print("   State: ", scanner[host][proto][port]['state'])
                print("   Version: ", scanner[host][proto][port]['version'])
                if 'product' in scanner[host][proto][port]:
                    print("   Product: ", scanner[host][proto][port]['product'])
                if 'extrainfo' in scanner[host][proto][port]:
                    print("   Extra Info: ", scanner[host][proto][port]['extrainfo'])

if __name__ == "__main__":
    ip = input("Ingrese la IP a escanear: ").strip()
    ports = input("Ingrese los puertos a escanear (por ejemplo, '80,443'): ").strip()
    arguments = input("Ingrese los argumentos adicionales de Nmap (opcional): ").strip()
    sudo_input = input("¿Desea ejecutar el comando como super usuario? (s/n): ").strip().lower()

    sudo = sudo_input == 's'

    run_nmap(ip, ports, arguments, sudo)
