import dns.resolver
target = str(input("Enter Domain Name / IP For Target >> "))
record_types = ["A", "AAAA","MX", "SOA","SRV", "CNAME"]



for type in record_types:
    d = dns.resolver.query(target,type, raise_on_no_answer=False)
    if d.rrset is not None:
        print(d.rrset)
