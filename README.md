## CS655 Computer Networks - Mini Project
### Team members 
* Ruizhi Jiang
* Tiancheng Zhu
* Anzhe Meng
* Jiahao Song

## How to run

### Run on our server nodes (team members and administrators only)

#### Web interface

SSH to client node using 
```
ssh [your-username]@pcvm1-39.geni.it.cornell.edu -p 22
```

- Activate virtual environment: under `/users/rzjiang/cs655geni`, type command 

```
. venv/bin/activate
```

- Turn on web interface server: under `/users/rzjiang/cs655geni/webapp`, type command

```
python3 app.py
```

#### Backend server

SSH to server node using

```
ssh [your-username]@pcvm1-40.geni.it.cornell.edu -p 22
```

- Activate virtual environment: under `/users/rzjiang/BackendServer`, type command

```
. venv/bin/activate
```

- Turn on backend server: under `/users/rzjiang/BackendServer/webapp`, type command 

```
python3 backend.py
```

#### Our application

Please visit http://192.122.236.116:5000 after executing scripts on server nodes.

### Run on your own server nodes

#### GENI Configuration

On your local, download the Rspec file from our github:

```
wget https://raw.githubusercontent.com/ztcric/CS655-MiniProject/main/rspec.txt
```

Reserve resources using this downloaded file, **make sure you choose the "Publicly Routable IP" option!**

#### Download scripts and our source code

After setting up server nodes, login in to the home directory, and then

```
wget https://raw.githubusercontent.com/ztcric/CS655-MiniProject/main/scripts/download.sh
wget https://raw.githubusercontent.com/ztcric/CS655-MiniProject/main/scripts/env_setup.sh
```

On both server nodes, run

```
bash download.sh
```

#### Configure virtual environments

On both server nodes, make sure they all have python3 (type `python3` to check). Then, setup your virtual environment

```
python3 -m venv cs655
. cs655/bin/activate
```

Notice you've now entered the virtual environment "cs655", then run

```
bash env_setup.sh
```

#### Web interface

First of all, enter the folder `web-interface`

```
cd CS655-MiniProject-main/web-interface
```

At line 18 in `app.py`, change this line to

```
url = "http://YOUR-OWN-BACKEND-SERVER-IP:5000/predict"
```

Also, at line 9 in `templates/index.html`, change this line to 

```
<form action = "http://YOUR-OWN-WEB-INTERFACE-IP:5000/uploader" method = "POST"
```

Then run

```
python3 app.py
```

#### Backend server

First of all, enter the folder `server-backend`

```
cd CS655-MiniProject-main/server-backend
```

At line 9 in `templates/output.html`, change this line to

```
<form action="http://YOUR-OWN-WEB-INTERFACE-IP:5000/">
```

Then run

```
python3 backend.py
```

#### Our application

Please visit http://YOUR-OWN-WEB-INTERFACE-IP:5000 after executing scripts on server nodes.