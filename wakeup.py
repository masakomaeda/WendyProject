#!/usr/bin/env python3
import pexpect
import requests
import os
import speak

homeAddr = os.environ['HOME']

p = pexpect.spawn("/bin/bash")
p.sendline(f"julius -C {homeAddr}/WendyProject/wendydict/wendystart.conf -module")
#p.sendline("julius -C ~/julius/dictation-kit/main.jconf -C ~/julius/dictation-kit/am-dnn.jconf -dnnconf ~/julius/dictation-kit/julius.dnnconf -demo")

print("hello")
print("please speak something...")

output = ""

while True:
  p.expect("<<< please speak >>>", timeout=120)

  output = str(p.before.decode())
  print(output)

  if 'おきて' in output:
    print("wakeup")
    p.terminate()  
    p.expect(pexpect.EOF)

    # おしゃべりしようよ(^_^)
    import speak

    p = pexpect.spawn("/bin/bash")
    p.sendline(f"julius -C {homeAddr}/WendyProject/wendydict/wendystart.conf -module")

  elif 'おやすみ' in output:
    print("goodnight"")
    break

  else:
    pass

p.terminate()  
p.expect(pexpect.EOF)

##シャットダウンしたい