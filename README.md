## CS655 Computer Networks - Mini Project
### Team members 
* Ruizhi Jiang
* Tiancheng Zhu
* Anzhe Meng
* Jiahao Song

## How to run: (group members and administrators only)

### Web interface:

SSH to client node using 
```
ssh username@pcvm1-39.geni.it.cornell.edu -p 22
```

- Activate virtual environment: under `/users/rzjiang/cs655geni`, type command 

```
. venv/bin/activate
```

- Turn on web interface server: under `/users/rzjiang/cs655geni/webapp`, type command

```
python3 app.py
```

### Backend server:

SSH to server node using

```
ssh username@pcvm1-40.geni.it.cornell.edu -p 22
```

- Activate virtual environment: under `/users/rzjiang/BackendServer` - type command

```
. venv/bin/activate
```

- Turn on backend server: under `/users/rzjiang/BackendServer/webapp`, type command 

```
python3 backend.py
```
