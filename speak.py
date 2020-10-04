#!/usr/bin/env python3

import pexpect
import requests
import os
import socket

def startverb(client):
  print("welcome")
  url = "http://localhost:8000/wings/action/delight"
  reponse = requests.get(url)
  datasize = 1024

  # Juliusにソケット通信で接続
  #client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #client.connect((host, port))

  try:
    data = ""

    while True:
      data += str(client.recv(datasize).decode('utf-8'))
    
      if '</RECOGOUT>\n.' in data:
        # 出力結果から認識した単語を取り出す
        output = ""
        for line in data.split('\n'):
          index = line.find('WORD="')
          if index != -1:
            output = output + line[index + 6:line.find('"', index + 6)]
        
        print(output)
        if "さよなら" in output:
          print("by")
          url = 'http://localhost:8000/wings/action/sleepy'
          response = requests.get(url)
          break
        elif "おはよう" in output:
          print("sleepy")
          url = 'http://localhost:8000/wings/action/sleepy'
        elif "まさお" in output:
          print("I love MASAO!")
          url = "http://localhost:8000/wings/action/delight"
        elif "きつね" in output:
          print("uhh... KITUNE!")
          url = "http://localhost:8000/wings/action/delight"
        elif "みぎ" in output:
          print("turn right")
          url = "http://localhost:8000/run/right"
        elif "ひだり" in output:
          print("turn left")
          url = "http://localhost:8000/run/left"
        elif "すすめ" in output:
          print("go straight")
          url = "http://localhost:8000/run/go"
        elif "とまれ" in output:
          print("stop please")
          url = "http://localhost:8000/run/stop"
        else:
          url = ""
          pass

        if "http://" in url:
          response = requests.get(url)

        url = ""    
        data = ""  
      else:
        pass

        
  except KeyboardInterrupt:
    print('finished')

if __name__ == "__main__":
  host = 'localhost' 
  port = 10500

  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((host, port))
  startverb(client)

