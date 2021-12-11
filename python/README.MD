# Setup Python on Ubuntu

## Goal

To setup python environment on Ubuntu.

## Prerequisites

* ubuntu
* github account

## Install

### Install Conda

```
# 1. install curl
sudo apt-get install curl


# 2. install conda 
cd /tmp
curl –O https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh

bash Anaconda3-2020.02-Linux-x86_64.sh
```

### Create Conda Environment
```
# 1. create envionrment 
conda create --name r-lab-minecraft python=3.7

# 2. activate environment
conda activate r-lab-minecraft

# 3. install packages
pip install -r requirements.txt
```

### Install Code

```
# 1. prepare

sudo apt update
sudo apt install software-properties-common apt-transport-https wget

# 2. install key
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -

# 3. enable repo
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

# 4. install 
sudo apt install code
```


Start vscode and install python extensions:

python extension
* select python interpreter (r-lab-micrsoft)

IntelliJ IDEA Key Bindings



### Fork and Clone Repo 

Fork this repo: https://github.com/miharothl/lab-minecraft


Clone the repo
```
cd ~
mkdir scm
cd scm
git clone https://github.com/<your_user>/lab-minecraft
```
