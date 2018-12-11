# Links

## Telnet on Windows:

[Enable telnet in Windows 10](https://social.technet.microsoft.com/wiki/contents/articles/38433.windows-10-enabling-telnet-client.aspx?Redirected=true)

1. Type Windows Key + R to open the Run command dialog. 
2. Type cmd and hit the Enter key.
3. Type `telnet` and hit Enter to access the Telnet Client.

## Python

- [Download Python](https://www.python.org/downloads/) (get version 3.7.1 or higher)
- [VS Code](https://www.python.org/downloads/) (code and text editor)

## Python Flask framework

- [Flask](http://flask.pocoo.org)
- [Flask Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/)

## More in-depth stuff

- [venv - Creation of virtual environments](https://docs.python.org/3/library/venv.html)
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Learn Python in Y minutes](https://learnxinyminutes.com/docs/python/)

# Workshop plan

## Part 1: Theory

1.  Internet vs Web
2.  Clients and servers
3.  HTTP
4.  Quiz
    1.  Web without the internet?
    2.  Do you **need** to know everything about the internet?
    3.  Internet, not the web: wifi router, satellite, google chrome


## Part 2: Request, building a client (18:00 - 18:15)

1.  HTTP request
    1.  Restaurant analogy
    2.  Request example
2.  Terminal 101
    1.  Enable in Windows
    2.  Try telnet, fail


## Part 3: Response, building a server (18:15 - 18:45)

1.  Install Python <https://www.python.org/downloads/>
    1.  3.7.x, add PATH
    2.  Windows: `python`, macOS: `python3`
2.  Install VS Code

    import http.server
    import socketserver
    
    with socketserver.TCPServer(("", 8080), http.server.SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()

1.  Create HTML.
    1.  Basic HTML and CSS


## Part 4: Back to the client

1.  Make request again
2.  Get HTML
3.  Save and open


## Part 5: Flask


### Basic Python

    
    # numbers
    2 + 3
    
    # print
    print("Something")
    
    # if
    cloudy = True
    if cloudy:
        print("Take umbrella!")
    else:
        print("Relax")
    
    # strings as variables
    cloudy = True
    message_1 = "Take umbrella!"
    message_2 = "Relax!"
    
    if cloudy:
        print(message_1)
    else:
        print(message_2)
    
    # concat (glue)
    name = "Jake"
    print(message_1 + name)
    
    # input
    name = input("What's your name? ")
    print(message_1 + name)
    
    # functions
    def report_weather(name, cloudy):
        if cloudy:
            print("Take umbrella, " + name + "!")
        else:
            print("Relax, " + name + ".")


### Venv

    python3 -m venv path/to/venv/folder


### Pip

    mkdir myprojec
    cd myproject
    python3 -m venv venv

*nix:

    . venv/bin/activate

Windows:

    venv\Scripts\activate

Install flask:

    pip install Flask


### Flask Basics

    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

Running:

    export FLASK_APP=hello.py
    flask run

On Windows cmd:

    C:\path\to\app>set FLASK_APP=hello.py

On Windows PowerShell:

    PS C:\path\to\app> $env:FLASK_APP = "hello.py"


### Flask routing

    @app.route('/')
    def index():
        return 'Index Page'
    
    @app.route('/hello')
    def hello():
        return 'Hello, World'


### Variables in routing

    @app.route('/user/<username>')
    def show_user_profile(username):
        return 'User %s' % username



