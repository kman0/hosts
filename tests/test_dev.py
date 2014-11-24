__author__ = 'M'

from hosts import Hosts

hosts_file_1 = """
# comment
   # comment with space before

# line after blank line
100.1.1.1 hundred-one-one-one
100.1.1.2 hundred-one-one-two
100.1.1.1 hundred-one-one-one
100.1.1.10 hundred-one-one-ten

"""

hosts_file_path = 'k:/hosts'
with open(hosts_file_path, 'w') as fpw:
   fpw.write(hosts_file_1)

obj = Hosts(hosts_path=hosts_file_path)
print(obj._lines)
obj.save()

