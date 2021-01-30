import telnetlib

host = '207.180.200.166'
port = 9660

def getInvCount(arr, n): 
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 

try:
    print('Connecting to',host,port)
    s = telnetlib.Telnet(host,port,30)
    print('Coneected')
except:
    print('Socket Timeout')

o = s.read_until(b"/r/n/r/n#>", 0.6)
print(o.decode())
t = o.decode()[111:].replace('[','').replace(']','').replace('\n','').replace('>','').split(',')
r = str(2 ** len(t) - 1).encode()
print(r)
s.write(r + b'\r\n')

for _ in range(24):
    o = s.read_until(b"/r/n/r/n#>", 0.6)
    print(o.decode())
    t = o.decode().replace('[','').replace(']','').replace('\n','').replace('>','').split(',')
    r = str(2 ** len(t) - 1).encode()
    print(r)
    s.write(r + b'\r\n')

o = s.read_until(b"/r/n/r/n#>", 0.6)
print(o.decode())
t = o.decode()[53:].replace('[','').replace(']','').replace('\n','').replace('>','').split(',')
t = [int(_) for _ in t]
r = str(getInvCount(t, len(t))).encode()
print(r)
s.write(r + b'\r\n')

for _ in range(24):
    o = s.read_until(b"/r/n/r/n#>", 0.6)
    print(o.decode())
    t = o.decode().replace('[','').replace(']','').replace('\n','').replace('>','').split(',')
    t = [int(_) for _ in t]
    r = str(getInvCount(t, len(t))).encode()
    print(r)
    s.write(r + b'\r\n')

o = s.read_until(b"/r/n/r/n#>", 0.6)
print(o.decode())