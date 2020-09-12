#!/usr/bin/env python3
import pexpect

p = pexpect.spawn("/bin/bash")
p.sendline("julius -C ~/julius/dictation-kit/main.jconf -C ~/julius/dictation-kit/am-gmm.jconf -demo")
#p.sendline("julius -C ~/julius/dictation-kit/main.jconf -C ~/julius/dictation-kit/am-dnn.jconf -dnnconf ~/julius/dictation-kit/julius.dnnconf -demo")

print("hello")

output = ""
cnt = 0
while True:
  p.expect("<<< please speak >>>", timeout=120)
#  if cnt == 0:
#    print("welcome")

  output = str(p.before.decode())
  print(output)
    #  if '<<< please speak >>>' in output:
  if 'おはよう' in output:
    print("sleepy")
  elif 'まさお' in output:
    print("happy")
  elif 'きつね' in output:
    print("happy")
  elif 'さようなら' in output:
    break
#    else:
#      print("welcome")
#    output = ""
#  else:
#    output += str(p.readline)
#  cnt += 1
#  if cnt == 33:
#    print(output)

print("終了")
p.terminate()
p.expect(pexpect.EOF)
