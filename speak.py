#!/usr/bin/env python3
import pexpect
import requests
import os

homeAddr = os.environ['HOME']

p = pexpect.spawn("/bin/bash")
p.sendline(f"julius -C {homeAddr}/WendyProject/wendydict/wendystart.conf -demo")
#p.sendline("julius -C ~/julius/dictation-kit/main.jconf -C ~/julius/dictation-kit/am-dnn.jconf -dnnconf ~/julius/dictation-kit/julius.dnnconf -demo")

print("hello")
print("please speak something...")

output = ""
cnt = 0
while True:
  p.expect("<<< please speak >>>", timeout=120)

  output = str(p.before.decode())
  print(output)
  url = ''
  if 'おはよう' in output:
    print("sleepy->")
    print(output)
    print("sleepy<-")
    url = 'http://localhost:8000/wings/action/sleepy'
  elif 'まさお' in output:
    print("delight")
    url = 'http://localhost:8000/wings/action/delight/0'
  elif 'きつね' in output:
    print("delight")
    url = 'http://localhost:8000/wings/action/delight/0'
  elif 'すすめ' in output:
    print("go")
    url = 'http://localhost:8000/run/go'
  elif 'みぎ' in output:
    print("right")
    url = 'http://localhost:8000/run/right'
  elif 'ひだり' in output:
    print("left")
    url = 'http://localhost:8000/run/left'
  elif 'とまれ' in output:
    print("stop")  
    url = 'http://localhost:8000/run/stop'
  elif 'さようなら' in output:
    print("by!")
    break
  else:
    url = ''
    pass

  if 'http://' in url:
    response = requests.get(url)  

p.terminate()  
p.expect(pexpect.EOF)
