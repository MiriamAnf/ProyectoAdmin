from collections import Counter

def only_ip(information):
    with open ("reporter.txt","w") as f:
        for i in information:
            new_file = i[0] + "" + str(i[1]) + "\n"
            f.write(new_file)

with open ("/var/log/nginx/access.log", "r", encoding="utf8") as f:
    counter = Counter()
    while True:
        line = f.readline()
        if not line:
            break
        ip = line.split(" ")[0]
        ip_counter = counter.update({ip: 1})
        sorted_counter = {}
        sorted_ip_counter = sorted(counter, key=counter.get, reverse=True)
        for address in sorted_ip_counter:
            sorted_counter[address] = counter[address]
        information = [(ip_address, ip_counter) for ip_address, ip_counter in sorted_counter.items()]
        only_ip(information)
        
