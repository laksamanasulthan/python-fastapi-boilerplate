#Road Detection Project (FastAPI-Python)


###Requirement 
- Python 3.12 Installation
```bash
sudo apt update && sudo apt upgrade -y

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update

apt list | grep python3.12

sudo apt install python3.12

python3.12 --version
```
- Python 3.12 virtual environment
```bash
sudo apt install python3.12-venv
```


###Installation Process
- Clone this repository

```bash 
git clone https://github.com/laksamanasulthan/road-detection-backend-fastapi.git

```

- Create virtual environment for Isolating dependencies
```bash 
python3.12 -m venv venv
```

- Start Virtual Environment 
```bash
source venv/bin/activate
```
- Download dependency all dependecies 
```bash 
pip install -r dependencies.txt
```
- Create .env in your project root, and change their respective value with your own development server

- Start your project with 
```bash
fastapi dev main.py
```
- This will automatically start your project and doing automigration for database

- Done