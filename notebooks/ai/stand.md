# Stand

[TOC]

## OS
```bash
# lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.1 LTS
Release:	20.04
Codename:	focal
```

## NVidia Card
```bash
# nvidia-settings -q gpus

1 GPU on pc.local:1

    [0] pc.local:1[gpu:0] (GeForce RTX 2070 SUPER)

      Has the following names:
        GPU-0
        GPU-0bd29d23-96ae-efb5-c3cd-b19975a65806
```

## NVidia Driver
```bash
# apt-cache policy nvidia-driver-435
nvidia-driver-435:
  Installed: 435.21-0ubuntu7
  Candidate: 435.21-0ubuntu7
  Version table:
 *** 435.21-0ubuntu7 500
        500 http://ru.archive.ubuntu.com/ubuntu focal/restricted amd64 Packages
        100 /var/lib/dpkg/status
```

## CUDA
```bash
# apt-cache policy nvidia-cuda-toolkit
nvidia-cuda-toolkit:
  Installed: 10.1.243-3
  Candidate: 10.1.243-3
  Version table:
 *** 10.1.243-3 500
        500 http://ru.archive.ubuntu.com/ubuntu focal/multiverse amd64 Packages
        100 /var/lib/dpkg/status
```

## Python
```bash
# python3 --version
Python 3.8.2
```

## Python libs
```bash
#pip3 list
Package                 Version             
----------------------- --------------------
absl-py                 0.9.0               
apturl                  0.5.2               
asn1crypto              0.24.0              
astunparse              1.6.3               
bcrypt                  3.1.7               
blinker                 1.4                 
Brlapi                  0.7.0               
cachetools              4.1.0               
certifi                 2019.11.28          
chardet                 3.0.4               
Click                   7.0                 
colorama                0.4.3               
command-not-found       0.3                 
cryptography            2.8                 
cupshelpers             1.0                 
dbus-python             1.2.16              
defer                   1.0.6               
distro                  1.4.0               
distro-info             0.23ubuntu1         
duplicity               0.8.12.0            
entrypoints             0.3                 
fasteners               0.14.1              
future                  0.18.2              
gast                    0.3.3               
google-auth             1.14.2              
google-auth-oauthlib    0.4.1               
google-pasta            0.2.0               
grpcio                  1.28.1              
h5py                    2.10.0              
httplib2                0.14.0              
idna                    2.8                 
Keras-Preprocessing     1.1.0               
keyring                 18.0.1              
keyrings.alt            3.4.0               
language-selector       0.1                 
launchpadlib            1.10.13             
lazr.restfulclient      0.14.2              
lazr.uri                1.0.3               
lockfile                0.12.2              
louis                   3.12.0              
macaroonbakery          1.3.1               
Mako                    1.1.0               
Markdown                3.2.1               
MarkupSafe              1.1.0               
monotonic               1.5                 
netifaces               0.10.4              
numpy                   1.18.4              
oauth                   1.0.1               
oauthlib                3.1.0               
olefile                 0.46                
opt-einsum              3.2.1               
paramiko                2.6.0               
pexpect                 4.6.0               
Pillow                  7.0.0               
pip                     20.0.2              
protobuf                3.11.3              
pyasn1                  0.4.8               
pyasn1-modules          0.2.8               
pycairo                 1.16.2              
pycrypto                2.6.1               
pycups                  1.9.73              
PyGObject               3.36.0              
PyJWT                   1.7.1               
pymacaroons             0.13.0              
PyNaCl                  1.3.0               
pyRFC3339               1.1                 
python-apt              2.0.0+ubuntu0.20.4.1
python-dateutil         2.7.3               
python-debian           0.1.36ubuntu1       
pytz                    2019.3              
pyxdg                   0.26                
PyYAML                  5.3.1               
reportlab               3.5.34              
requests                2.22.0              
requests-oauthlib       1.3.0               
requests-unixsocket     0.2.0               
rsa                     4.0                 
scipy                   1.4.1               
screen-resolution-extra 0.0.0               
SecretStorage           2.3.1               
setuptools              45.2.0              
simplejson              3.16.0              
six                     1.14.0              
ssh-import-id           5.10                
system-service          0.3                 
systemd-python          234                 
tensorboard             2.2.1               
tensorboard-plugin-wit  1.6.0.post3         
tensorflow              2.2.0rc4            
tensorflow-estimator    2.2.0               
termcolor               1.1.0               
ubuntu-advantage-tools  20.3                
ubuntu-drivers-common   0.0.0               
ufw                     0.36                
unattended-upgrades     0.1                 
urllib3                 1.25.8              
usb-creator             0.3.7               
vboxapi                 1.0                 
wadllib                 1.3.3               
Werkzeug                1.0.1               
wheel                   0.34.2              
wrapt                   1.12.1              
xkit                    0.0.0               
zope.interface          4.7.1               
```