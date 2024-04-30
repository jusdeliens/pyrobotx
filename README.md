# PyRobotX
Control the sensors and actuators of a physical robot called [Ova](https://jusdeliens.com/ova) 🤖

## ⚙️ Setup

1. Clone this repo
2. Update all submodules recursively
```
git submodule update --init --recursive
```
3. pip install all deps in [the requirement list](requirements.txt)
```
pip install --no-cache-dir -r requirements.txt
```
4. Add a .env file in the root project directory, containing the following credentials. If you don't have any credentials, feel free [to contact us](https://jusdeliens.com/contact) to join the adventure 🚀
```.env
# The name of your player or your robot ID as str
ROBOTID         = ...
# The name of the arena to join as str
ARENA           = ...
# The broker user name provided by a Jusdeliens administrator as str
USERNAME        = ...
# The broker user password as str
PASSWORD        = ...
# The broker ip address or dns as str
BROKERADDRESS   = ...
# The broker port as int 
BROKERPORT      = ...
# Verbosity level as int from 0:no log, to 4: full debug logs
VERBOSITY       = ... 
```
5. Then run the main.py with python interpretor (⚠️ at least version 3.9)
```
python main.py
```

## 🎮 How to play ?

You don't have an Ova bot ? Get one [by clicking here](https://jusdeliens.com/ova).

Then fetch all instructions to program your robot 👉 [on our tutorial here](https://tutos.jusdeliens.com/index.php/2023/01/17/onboarding/)

## 🧑‍💻 Author
Designed with 💖 by [Jusdeliens Inc.](https://jusdeliens.com)

## ⚖️ License
Under CC BY-NC 4.0 licence 
👉 https://creativecommons.org/licenses/by-nc/4.0/deed.en