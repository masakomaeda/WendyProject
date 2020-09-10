# Wendyと遊ぼう

### <Step.1>　Raspberry pi の準備
- raspberry pi ImagerでSDカードにOSを準備する

- raspberry pi 本体にSDを差し込む
    
    
- 初期設定を行う  
    % sudo raspi-config nonint do_wifi_country JP  
    % sudo raspi-config nonint do_change_timezone Asia/Tokyo  
    % sudo raspi-config nonint do_change_locale ja_JP.UTF-8
    
    
- ネットワークの設定を行う  
    % sudo nano /etc/wpa_supplicant/wpa_supplicant.conf  
    
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev  
    update_config=1  
    country=JP  
    network={  
    ssid="ssid"  
    psk="password"  
    }
