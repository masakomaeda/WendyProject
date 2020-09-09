# WendyProject
小さいウエンディを動かそう


 - サーバーの動かし方
 
   % julius -C fast.jconf -module




sudo apt-get install build-essential zlib1g-dev libsdl2-dev libasound2-dev -y
% git clone https://github.com/julius-speech/julius.git
% cd julius
% ./configure --enable-words-int
% make -j4
make install

sudo apt-get install git-lfs 

git lfs clone https://github.com/julius-speech/dictation-kit.git


usbマイクのセッティング

https://www.pc-koubou.jp/magazine/19743


sudo apt-get install alsa-utils sox libsox-fmt-all  -y

cd juius/diction-kit



以下でPython 3用のpipをインストールできた。

$ sudo apt-get install python3-pip



標準入出力について

ass1_bestは、中間認識結果で、最終的な結果としてはsentence1に表示

<<< please speak >>>をまつ


標準入出力について
pexpectをpip
