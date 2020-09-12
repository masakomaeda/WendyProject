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
        |I1 Change Locale|ja_JP.UTF-8 UTF-8 (Configuring locals ⇒ C.UTF-8)|
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
    $ sudo apt update
    $ sudo apt upgrade
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
----
以下、Dockerを使用する場合はここでコンテナの準備を行い、Doker内に構築を行う？  
マイクやオーディオ設定は外側にも必要？？未検証  
Gitがないときはインストールしておく  
```$ sudo apt-get install git-all -y```

----
### <Step.2>　Juliusのインストール
- オーディオ関係のライブラリーをインストールしておく  
（無くてもJuliusuは入れられるのだが入れた方がいい [公式サイト](http://julius.osdn.jp/juliusbook/ja/desc_install.html) ものと、マイク設定にも使うもの）
    ```
    $ sudo apt install alsa-utils sox libsox-fmt-all -y
    ```

- 本体（Gitの[Readme](https://github.com/julius-speech/julius)より）  
    ```
    $ cd /usr/local/src/
    $ sudo apt install build-essential zlib1g-dev libsdl2-dev libasound2-dev -y
    $ sudo git clone https://github.com/julius-speech/julius.git
    $ cd julius
    $ sudo ./configure --enable-words-int --with-mictype=alsa
    $ sudo make -j4
    $ sudo make install
    ```
  

### <Step.3>　ディクテーションキットのダウンロード 

- まずは大きいファイルをGIT HUBからゲットするためのツールをインストール  
    ```
    $ sudo apt install git-lfs -y
    ```

- 本体（ホームでいいけ？）
    ```
    $ cd ~/ 
    $ mkdir julius/
    $ cd julius 
    $ git lfs clone https://github.com/julius-speech/dictation-kit.git
    ```


----
以上、Dockerを使用する場合はここまでコンテナの準備を行い、Doker内に構築を行う？  
ここからはマイクの設定、手動で行う

----

### <Step.4>　USBマイクの準備

- マイクをぶっさす



- マイクの感度を上げる(56は入力の感度。0～62の範囲で56=90%。上げすぎると音割れする。)  
  -cの後の0はカード番号。arecord -lで調べられる（後述）
    ```
    $ amixer sset Mic 50 -c 0
    ```

- juliusが参照する環境変数「AUDIODEV」を使ってjuliusが利用するサウンドカードを指定する  
  起動する度に設定しなくて済むよう「/etc/profile」ファイルに追加する
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
$ cd ~/julius/dictation-kit/
$ julius -C main.jconf -C am-gmm.jconf -demo
```

# TODO 以下は編集途中

### <Step.6>　アプリインストール
sudo apt-get install python3-pip  
pexpectをpip。py3用のやつで  
精度がいいのはこっち  
julius -C ~/julius/dictation-kit/main.jconf -C ~/julius/dictation-kit/am-dnn.jconf -dnnconf ~/julius/dictation-kit/julius.dnnconf -demo
