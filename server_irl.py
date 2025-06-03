import socket
s = socket.socket()
s.bind(("0.0.0.0", 9999))
s.listen(10)

print("[*] Waiting for connections...")

while True:
    sc, address = s.accept()
    print(f"[+] Connection from: {address}")
    with open('server-copy.txt', 'ab') as f:
        while True:
            data = sc.recv(1024)
            if not data:
                break
            # Print to screen AND write to file
            print(data.decode('utf-8', errors='replace'), end='', flush=True)  # Print to console
            f.write(data)  # Save to file
    print("\n[-] Connection closed.")
    sc.close()