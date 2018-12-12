# Step 1: Internet vs Web

- The Internet is the network of networks ([wiki](https://en.wikipedia.org/wiki/Internet)
- The web is the est of apps that use the Internet for communication
- This communication often uses [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol), a special language for communication (do not confuse with a programming language)

- web clients send HTTP requests to web servers
- web servers send HTTP responses back

![](https://i.imgur.com/1uarUI0.png)
**[⬇ Download this PDF cheatsheet an HTTP ⬇](https://rakhim.org/ce/HTTP_notes_diagram_1.pdf)**

# Step 2: Telnet client

## Telnet on Windows:

1. [Enable telnet in Windows 10](https://social.technet.microsoft.com/wiki/contents/articles/38433.windows-10-enabling-telnet-client.aspx?Redirected=true)

## Telnet on Mac:

Macs have telnet built in, so nothing to install here.

## Make a HTTP request via telnet

### Windows
1. Type Windows Key + R to open the Run command dialog. 
2. Type cmd and hit the Enter key.

### macOS
1. Launch `Terminal.app`

### Make a connection
Type:

```
telnet localhost 8080
Host: localhost
```

Hit `Enter` twice in the end.

![](https://i.imgur.com/b8ANTXs.png)
**[⬇ Download this PDF cheatsheet an HTTP ⬇](https://rakhim.org/ce/HTTP_notes_diagram_2.pdf)**

(If you're on macOS High Sierra or Mojave, type `nc` instead of `telnet`.)

# Step 3: Basics of Python

Try out Python on [https://repl.it](https://repl.it). Login and choose "Python". Enter code in the right pane, hit `Run`.

```python

# numbers
2 + 3

# print something onto the screen
print("Something")

# True, False and conditions
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

# concatenation (glue)
name = "Jake"
print(message_1 + name)

# input
name = input("What's your name? ")
print(message_1 + name)
```

## Download tools

- [Download Python interpreter](https://www.python.org/downloads/) (get version 3.7.1 or higher)
- [VS Code editor](https://www.python.org/downloads/) (code and text editor)



# Step 4: Create a simple HTTP server

Even a simple HTTP server, which consists of just 4 lines of code, is a pretty complex program. Each line includes tens and tens of different concepts.

One way to go — a classic, “proper” way — is to start with the basics of Python and make our way up the ladder of difficulty. We’d need to learn about variables, modules, importing, TCP, handlers, with-statements and command line arguments. It’s quite a list, and each concept requires you to at least gave some idea about a dozen more. It’ll take us a few days or even weeks!

Another way to go is to just give you those 4 lines to copy and paste and hope it works. You’ll have no idea what’s happening, but the HTTP server will probably be launched successfully.

I believe there’s the third way. I will indeed give you 4 lines of code to copy and paste. But this is a loan, not a gift. You’ll have to pay back!

In the next workshops we will look back and cover the missing parts. I call this a “learning credit card”. We’ll always jump ahead and do something cool, but then at some point we’ll come back and “pay the debt”. As long as we’re disciplines and don’t take too many “knowledge loans”, we’ll be fine and it’ll be fun!

Here is the code:

    import http.server
    import socketserver
    
    with socketserver.TCPServer(("", 8080), http.server.SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()
        
Save this file as `server.py` in a folder called `server` on your Desktop, navigate to that folder in the Terminal:

### Windows
Assuming your folder is saved on the Desktop, in the Terminal type `cd C:\Users\YOUR_USERNAME\Desktop\server` 

Don’t forget to change `YOUR_USERNAME` to your actual username.

### macOS

Assuming your folder is saved on the Desktop, type `cd /Users/YOUR_USERNAME/Desktop/server` in the Terminal.

## Then run the server

### Windows

```
py server.py
```

### macOS

```
python3 server.py
```

# Step 5: Back to the client

Now you repeat the HTTP request using the telnet app. You should see a response.