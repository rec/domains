import os, sys


path = '/net/u/1/j/jongiles/scripts/domains/names'
TEST_STRINGS = 'Name server', 'name server', 'Name Server'
active_domains = []

def is_active_line(line):
    """Return true if the line of the file indicates that the domain is active.
    """
    return any(ts in line.decode() for ts in TEST_STRINGS)

def is_active_domain(f):
    return any(is_active_line(line) for line in open(f, 'rb'))

def is_ns_in_domain(f):
    return [line for line in open(f, 'rb') if is_active_line(line)]


directory = [os.path.join(path, f) for f in os.listdir(path)]
domainfiles = [f for f in directory if os.path.isfile(f)]
inactive_domains = [f.replace( path+'/', '') for f in domainfiles if not is_active_domain(f)]
active_domains = [f.replace( path+'/', '') for f in domainfiles if is_active_domain(f)]
name_servers = [f for f in active_domains if is_ns_in_domain(os.path.join(path, f))]
print("This is a list of inactive domains")
print(inactive_domains)
print("This is a list of active domains")
print(active_domains)
print("A list of nameservers")
print(name_servers)
