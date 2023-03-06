# Projekt "onboard CC100 programming" ET'23

## Teilnehmer

- Nele Stocksmeyer <nele.stocksmeyer@wago.com>
- Bekim Imrihor <bekim.imrihor@wago.com>
- Tobias Pape <tobias.pape@wago.com>
- Tobias Schäkel <tobias.schaekel@wago.com>
- Mattis Schrade <mattis.schrade@wago.com>
- Konrad Holsmölle <konrad.holsmoelle@wago.com>
- Bjarne Zaremba <bjarne.zaremba@wago.com>
- Danny Meihoefer <danny.meihoefer@wago.com>
- Sascha Hahn <sascha.hahn@wago.com>

### Raspberry Pi

##### Downloads

- [*Windows Disk-Imager*](https://sourceforge.net/projects/win32diskimager/)

- [*Image-Download*](https://www.raspberrypi.com/software/operating-systems/)

- [*Treiber für das 5" Touchdisplay*](https://joyiteurope-my.sharepoint.com/personal/onedrive_joyiteurope_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fonedrive%5Fjoyiteurope%5Fonmicrosoft%5Fcom%2FDocuments%2F5display%2FLCD%2Dshow%2Dmaster%2Ezip&parent=%2Fpersonal%2Fonedrive%5Fjoyiteurope%5Fonmicrosoft%5Fcom%2FDocuments%2F5display&ga=1)


##### Anleitungen

Treiber-Installation:
``` bash
cd Downloads
unzip LCD-show-master.zip
cd LCD-show-master/
sudo bash ./LCD5-show
```

``` bash
pip install CC100IO
```

### CC100
- [Docker installieren](https://github.com/WAGO/docker-ipk)
- [Python3 ipk downloaden](https://github.com/WAGO/cc100-howtos/blob/main/HowTo_AddPython3/packages/python3_3.7.6_armhf.ipk)
IPK-Datei wie die Docker-IPK im WBM installieren
- Docker Container von DockerHub laden <br>
`docker pull bzporta/pipdocker:1.0`
- vscpy.sh ausführen
