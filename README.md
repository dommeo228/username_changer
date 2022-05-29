# 🎭 Username Changer

**Username Changer is a script for automatically changing an account's telegram username to a randomly generated username on a schedule.**

🔥 Based on the [pyrogram](https://docs.pyrogram.org/) library (user API)

## Installation

🐍 The script requires python 3.9.0+ to run.

```sh
apt-get update
apt-get install python
apt-get install python3-pip
apt-get install git
```

```sh
git clone https://github.com/dommeo228/username_changer
cd username_changer
```

🔒 Set your telegram app information to .env (get it from [my.telegram.org](https://my.telegram.org))

```sh
nano .env
```

For example

```
API_ID=123456
API_HASH=kj48muxw59ncwm0x34t89qx4nthw43sh
```

After setting the data, press CTRL+S for save and CTRL+X for exit

### 🐳 Docker

🔐 Authorization in your Telegram account to create a session for the docker

```sh
pip3 install -r auth_requirements.txt
python3 auth.py
```

🚀 Start a docker container

```sh
sh docker_install.sh
docker-compose up --build
```

😎 After the container has successfully started and you see "Started." press CTRL+Z to exit the container without stopping it 

### 🐍 Python
```sh
pip3 install -r requirements.txt
python3 main.py
```
