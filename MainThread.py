#!/usr/bin python3
import pexpect
import request
import os

homeAddr = os.environ['HOME']

p = pexpect.spawn("/bin/bash")
p.sendline(f"julius -C {homeAddr}/WendyProject/myDict/wendy-speak.conf -demo")
#p.sendline("julius -C ~/julius/dictation-kit/main.jconf -C ~/julius/dictation-kit/am-dnn.jconf -dnnconf ~/julius/dictation-kit/julius.dnnconf -demo")

print("hello")
print("please speak something...")

output = ""
cnt = 0
while True:
  p.expect("<<< please speak >>>", timeout=120)

  output = str(p.before.decode())
  print(output)

  if 'おはよう' in output:
    print("sleepy")
    url = 'http://localhost/io-api/templates/wings/action/sleepy'
    response = requests.get(url)
  elif 'まさお' in output:
    print("delight")

    url = 'http://localhost/io-api/templates/wings/action/delight/0'
    response = requests.get(url)
  elif 'きつね' in output:
    print("delight")

    url = 'http://localhost/io-api/templates/wings/action/delight/0'
    response = requests.get(url)

  elif 'みぎ' in output:
    print("right")
  elif 'ひだり' in output:
    print("left")
  elif 'とまれ' in output:
    print("stop")
    
  elif 'さようなら' in output:
    break

    
print("by!")
p.terminate()
p.expect(pexpect.EOF)
