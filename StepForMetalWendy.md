# Wendyと遊ぼう

### <Step.1>　Raspberry pi の準備
- raspberry pi ImagerでSDカードにOSを準備する

- raspberry pi 本体にSDを差し込む
    
    
- 初期設定を行う  
    ```
    % sudo raspi-config
    ```
「4 Localisation Options」⇒ I1 Change Localeで「ja_JP.UTF-8 UTF-8」　⇒Configuring locals　⇒　C.UTF-8（ja_JP.UTF-8を選ぶとHDMIで繋いだ時に文字化けする）  
「4 Localisation Options」⇒I2 Change Timezoneで「Asia」⇒「Tokyo」  
「4 Localisation Options」⇒I3 Change Keyboard Layoutで「Generic 105-key (Intl) PC」⇒「Japanese」  
Configuring keyboard-configurationでは、「 The default for the keyboard layout」を、「Configuring keyboard-configration」では、「No compose key」を選ぶ。  
「4 Localisation Options」⇒ I4 Change Wi-fi Countryで「JP Japan」    
「5 Interfaces Option」⇒「P1 Camera」を有効（enabled） 
「5 Interfaces Option」⇒「P2 SSH」を有効（enabled）  
ここまで終わったらFinishとして、  
Would you like to reboot now? で「Yes」で再起動  

- ソフトウェアのアップデート  
    ```
    % sudo apt update
    % sudo apt upgrade
    ```
