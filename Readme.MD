# URL Shortener Application

## Local Run

### Docker install

- Install [docker](https://docs.docker.com/get-docker/)
- Make sure it is integrated with [wsl](https://docs.docker.com/desktop/windows/wsl/) if you use windows and wsl
- Open console and start `docker-compose` application with PostgreSQL database:
    ```
    > docker-compose up -d
    ```
- Wait until docker images are fully provisioned
- Test connection to `pgadmin` utility : http://localhost:5050
- Login to `pgadmin` - creds can be found in `docker-compose.yml`
- Connect to server using next information:
    - host : evaluate from the script below
    - port : 54320
    - login : user
    - password : admin
- Create new database using context menu with the name `url_db`

### Evaluate WSL host IP address

Script to get IP address of WSL:
In wsl console:

```
cat /etc/resolv.conf | grep nameserver | cut -d " " -f2
```

### Run python app

- Create virtual environment and activate it
    ```python
    > python -m venv venv
    > source venv/bin/activate
    ```
- install all dependencies:
    ```
    (venv) pip install -r requirements.txt
    ```    
- cd to backend directory
    ```shell
    (venv) > cd backend
    ```
- run Flask application:
    ```python
    (venv) ..backend > python app.py
    or
    python main:app --reload
    ```
You should have something similar to this:
```shell
* Serving Flask app 'app'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Try test http requests

- go to `url.http` at the `httpcalls` directory

- send a test `post request` and get response with a short line 
