# Wendyと遊ぼう

### <Step.1>　Raspberry pi の準備
- raspberry pi ImagerでSDカードにOSを準備する

- raspberry pi 本体にSDを差し込む
    
    
- 初期設定を行う  
    ```
    % sudo raspi-config
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
    % sudo apt update
    % sudo apt upgrade
    ```
