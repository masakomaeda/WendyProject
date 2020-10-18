# Wendyが認識する音声用辞書ファイル群

 - wendystart.conf  
  wendy辞書を使ってjuliusuを起動させるためのconfigファイル
 - wendy.*
  julisuが必要とする辞書ファイル

## 認識できる音声  

 - __おきて__ (delight。待機状態⇒音声認識待ち状態へ。importantなワード)
 - __さようなら__ (sleepy。音声認識待ち状態⇒待機状態へ。importantなワード)
 - __おやすみ__ (待機状態で有効。ラズパイを終わらせる。importantなワード)
 - ウエンディ
 - まさお (delight）
 - きつね (delight）
 - とまれ (stop）
 - ひだり (left)
 - みぎ (right)
 - すすめ (go)
 - さがれ(back)
 - おはよう (sleepy)
 - こんにちは (sleepy)
 - こんばんは (sleepy)
 - さようなら (sleepy)


## 辞書の作り方＜開発用メモ＞  
@@@はすべて同じ名称で統一し、同じ場所に保存する。
 - @@@.yomiを作成後以下を実行すると@@@.phoneファイルが作成され、発音用ローマ字一覧をゲットできる。
   この一覧が不要ならば、これらのファイルおよび以下の実行は不要である。
   ```
    /usr/local/src/julius/gramtools/yomi2voca/yomi2voca.pl /home/pi/WendyProject/wendydict/@@@.yomi > /home/pi/WendyProject/wendydict/@@@.phone
    ```
    
 - 辞書を作るには@@@.vocaおよび@@@.grammarの2ファイルが必要である。
 下記を実行することで辞書ファイルが生成される。
 ```
 sudo /usr/local/src/julius/gramtools/mkdfa/mkdfa.py /home/pi/WendyProject/wendydict/@@@
 ```
