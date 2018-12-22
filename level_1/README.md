# Step 0: Install tools

For both macOS and Windows - follow the instructions [here](https://github.com/Codexpanse/workshops/blob/master/level_1/steps.md).

# Step 1: Internet vs Web

- The Internet is the network of networks ([wiki](https://en.wikipedia.org/wiki/Internet)
- The web is the est of apps that use the Internet for communication
- This communication often uses [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol), a special language for communication (do not confuse with a programming language)

- web clients send HTTP requests to web servers
- web servers send HTTP responses back

![](https://i.imgur.com/1uarUI0.png)
**[⬇ Download this PDF cheatsheet an HTTP ⬇](https://rakhim.org/ce/HTTP_notes_diagram_1.pdf)**

# Step 2: Netcat client

## Make a HTTP request via netcat.

### Windows
1. Run `cmder` installed in the previous step.

### macOS
1. Launch `Terminal.app`

### Make a connection
Type:

```
nc 127.0.0.1 8080
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

# Step 4: Create a simple HTTP server

Even a simple HTTP server, which consists of just 4 lines of code, is a pretty complex program. Each line includes tens and tens of different concepts.

One way to go — a classic, “proper” way — is to start with the basics of Python and make our way up the ladder of difficulty. We’d need to learn about variables, modules, importing, TCP, handlers, with-statements and command line arguments. It’s quite a list, and each concept requires you to at least gave some idea about a dozen more. It’ll take us a few days or even weeks!

Another way to go is to just give you those 4 lines to copy and paste and hope it works. You’ll have no idea what’s happening, but the HTTP server will probably be launched successfully.

I believe there’s the third way. I will indeed give you 4 lines of code to copy and paste. But this is a loan, not a gift. You’ll have to pay back!

In the next workshops we will look back and cover the missing parts. I call this a “learning credit card”. We’ll always jump ahead and do something cool, but then at some point we’ll come back and “pay the debt”. As long as we’re disciplines and don’t take too many “knowledge loans”, we’ll be fine and it’ll be fun!

Here is the code:

```python
import http.server
import socketserver

host = "localhost"
port = 8080

server = socketserver.TCPServer((host, port), http.server.SimpleHTTPRequestHandler)

print("Server started...")
server.serve_forever()
```
        
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

Now you repeat the HTTP request using the netcat app. You should see a response.
