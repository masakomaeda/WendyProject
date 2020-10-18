# Wendyと遊ぼう

### <Step.1>　Raspberry pi の準備
- raspberry pi ImagerでSDカードにOSを準備する

- raspberry pi 本体にSDを差し込む
    
    
- 初期設定を行う  
    ```
    $ sudo raspi-config
    ```
    
    - 4 Localisation Options

        |第二メニュー|選択肢|
        |:-|:-|
        |I1 Change Locale|ja_JP.UTF-8 UTF-8 (Configuring locals ⇒ ~~C.UTF-8~~ ja_JP.UTF-8 日本語UTF-8)|
        |I2 Change Timezone|Asia ⇒ Tokyo|
        |I3 Change Keyboard Layout|Generic 105-key (Intl) PC ⇒ キーボード通り （Configuring keyboard-configrationではNo compose key)|
        |I4 Change Wi-fi Country|JP Japan|

    - 5 Interfaces Option  

        |第二メニュー|選択肢|
        |:-|:-|
        |P2 SSH|enabled|

    以上でFinish、再起動（Would you like to reboot now? ⇒「Yes」）  


- ソフトウェアのアップデート  
    ```
    $ sudo apt-get update
    $ sudo apt-get upgrade
    ```

- ネットワーク(Wi-fi)の設定 　バックアップ取ってからだぞ！
    ```
    $ sudo vi /etc/wpa_supplicant/wpa_supplicant.conf
    ```
    
    ```
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=JP
    network={
    ssid="ssid"
    psk="password"
    }
    ```
    
 - Gitがないときはインストールしておく  
    ```
    $ sudo apt-get install git-all -y
    ```

----
### <Step.2>　Juliusのインストール
- オーディオ関係のライブラリーをインストールしておく  
（無くてもJuliusuは入れられるのだが入れた方がいい [公式サイト](http://julius.osdn.jp/juliusbook/ja/desc_install.html) ものと、マイク設定にも使うもの）
    ```
    $ sudo apt-get install alsa-utils sox libsox-fmt-all -y
    ```

- 本体（Gitの[Readme](https://github.com/julius-speech/julius)より）  
    ```
    $ cd /usr/local/src/
    $ sudo apt-get install build-essential zlib1g-dev libsdl2-dev libasound2-dev -y
    $ sudo git clone https://github.com/julius-speech/julius.git
    $ cd julius
    $ sudo ./configure --enable-words-int --with-mictype=alsa
    $ sudo make -j4
    $ sudo make install
    ```
  

### <Step.3>　ディクテーションキットのダウンロード 

- まずは大きいファイルをGIT HUBからゲットするためのツールをインストール  
    ```
    $ sudo apt-get install git-lfs -y
    ```

- 本体（ホームでいいけ？）
    ```
    $ cd ~/ 
    $ mkdir julius/
    $ cd julius 
    $ git lfs clone https://github.com/julius-speech/dictation-kit.git
    ```


### <Step.4>　USBマイクの準備

- マイクをぶっさす

- マイクの感度を上げる(56は入力の感度。0～62の範囲で56=90%。上げすぎると音割れする。)  
  -cの後の0はカード番号。```$ arecord -l```で調べられる（後述）
    ```
    $ amixer sset Mic 50 -c 0
    ```

- juliusが利用するサウンドカードを、juliusが参照する環境変数「AUDIODEV」に指定する
  （起動する度に設定しなくて済むよう「/etc/profile」ファイルに追加する）
    - まずは入力のカードNO,デバイスNOを調べる
        ```
        $ arecord -l
        ```
    - 環境変数を保存する
        ```
        $ sudo vi /etc/profile

        # 0,0の最初の0はカードNO、最後の0はデバイスNO
        export ALSADEV="plughw:0,0"
        ```
    再起動！！！  
    
### <Step.5>　起動チェック
```
$ julius -C ~/julius/dictation-kit/main.jconf -C ~/julius/dictation-kit/am-gmm.jconf -demo
# 精度がいいのはこちら↓ でも遅い
# julius -C ~/julius/dictation-kit/main.jconf -C ~/julius/dictation-kit/am-dnn.jconf -dnnconf ~/julius/dictation-kit/julius.dnnconf -demo
```

### <Step.6>　アプリ実行の準備
- pexpectとrequestsをpipでインストールする
    ```
    $ sudo apt-get install python3-pip -y
    $ python3 -m pip install pexpect requests
    ```

### <Step.6>　自動起動のためサービスに登録
 - julius-for-wendy.service・・・juliusstart.shを実行し、ユリウスをモジュールモードで起動する
 - wendy-speak-module.service・・・wakeup.pyを起動し、wendy目覚めさせるための準備をする
    ```
    sudo cp -p ~/WendyProject/julius-for-wendy.service /etc/systemd/system
    sudo cp -p~/WendyProject/ wendy-speak-module.service /etc/systemd/system
    sudo systemctl daemon-reload
    sudo systemctl start julius-for-wendy.service
    sudo systemctl start wendy-speak-module.service
    sudo systemctl enable julius-for-wendy.service
    sudo systemctl enable wendy-speak-module.service
    ```
  
  -----
  
  以上で再起動することにより、wendyはあなたの声を聞き取ります。
  Good luck!!
