import os, sys

MATCH = 'name server'


class Domain:
    def __init__(self, path, name):
        self.name = name
        filename = os.path.join(path, name)
        self.data = [line.decode().strip() for line in open(filename, 'rb')]
        self.active_lines = [i for i in self.data if MATCH in i.lower()]


def report_inactive(domains):
    print('Inactive domains:')
    for k, d in sorted(domains.items()):
        if not d.active_lines:
            print('   ', k)

    print()


def report_active(domains):
    print('Active domains:')
    for k, d in sorted(domains.items()):
        if d.active_lines:
            print('   ', k)
            for line in d.active_lines:
                print('        ', line)
            print()


def print_domains(path='/net/u/1/j/jongiles/scripts/domains/names'):
    domains = {name: Domain(path, name) for name in os.listdir(path)}
    report_inactive(domains)
    report_active(domains)


if __name__ == '__main__':
    print_domains(*sys.argv[1:])
