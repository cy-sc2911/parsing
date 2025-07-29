# Define the login data as a multi-line string
login_data = """username,ip_address,time_date
tshah,192.168.92.147,15:26:08,2022-05-10
dtanaka,192.168.98.221,9:45:18,2022-05-09
tmtfchcl,192.168.110.131,14:13:41,2022-05-11
daquino,192.168.148.144,12:23:59,2022-05-08
erashay,192.168.170.243,1:45:14,2022-05-11
jlansky,192.168.238.42,1:07:11,2022-05-11
acook,192.168.52.90,9:56:48,2022-05-10
asundara,192.168.58.217,23:17:52,2022-05-12
jclark,192.168.214.49,20:49:00,2022-05-10
cjackson,192.168.247.153,19:36:42,2022-05-12
jclark,192.168.197.247,14:11:04,2022-05-12
apatel,192.168.46.207,17:39:42,2022-05-10
mabadi,192.168.96.244,10:24:43,2022-05-12
iuoluke,192.168.131.147,17:59:00,2022-05-11
abelinas,192.168.60.111,13:37:05,2022-05-10
gesparza,192.168.148.80,6:30:14,2022-05-11
cgriffin,192.168.4.157,23:04:05,2022-05-09
alevitsk,192.168.210.228,8:10:43,2022-05-08
erash,192.168.24.12,11:29:27,2022-05-11
jsoto,192.168.25.60,5:09:21,2022-05-09"""

# Write the data to login.txt
with open('login.txt', 'w') as file:
    file.write(login_data)

import_file = 'login.txt'

with open(import_file, 'r') as file:
    text = file.read()

print(text)
# Text is split into lines
print(text.split('\n'))

# 'a' to append
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"

with open(import_file, 'a') as file:
    file.write("\n" + missing_entry)

with open(import_file, 'r') as file:
    text = file.read()
print(text)

# Creating new entry 'allow_list.txt'
import_file = "allow_list.txt"

ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"

with open(import_file, 'w') as file:
    file.write(ip_addresses)

with open(import_file, 'r') as file:
    text = file.read()
print(text)