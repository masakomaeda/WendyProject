#!/usr/bin/env python3

import pexpect
import requests
import os
import speak
import socket

print('...starting')

# モジュールモードで起動する
homeAddr = os.environ['HOME']
#p = pexpect.spawn(f"julius -C {homeAddr}/WendyProject/wendydict/wendystart.conf -module")
#p.expect(r".*Module mode ready.*", timeout=120)


host = 'localhost'
port = 10500
datasize = 1024

# Juliusにソケット通信で接続
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

try:
  data = ''
  while True:
    data += str(client.recv(1024).decode('utf-8'))
  
    if '</RECOGOUT>\n.' in data:
      # 出力結果から認識した単語を取り出す
      output = ""
      for line in data.split('\n'):
        index = line.find('WORD="')
        if index != -1:
          output = output +  line[index + 6:line.find('"', index + 6)]
      print('認識結果: ' + output)
      if 'おきて' in output:
        print('wake up')
        print('認識結果: ' + output)
        speak.startverb(client)
      elif 'おやすみ' in output:
        print('see you again!')
#        client.close()
        break
      else:
        pass
      
      data = ""

except KeyboardInterrupt:
  print('finished')
