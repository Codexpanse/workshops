## Make sure you have telnet installed

1.  If you're on Windows, enable telnet by following [the official docs](https://social.technet.microsoft.com/wiki/contents/articles/38433.windows-10-enabling-telnet-client.aspx).
2.  If you're on macOS Sierra or lower, you already have `telnet`. If you're on macOS High Sierra or Mojave (the latest one as of Dec. 2018), you have `nc`, which is a drop-in alternative to `telnet`.

## Make a connection

Launch a terminal:

On Windows:

1.  Press `WinKey+R`
2.  Type `cmd`
3.  Press `Enter`

On macOS:

1.  Launch Spotlight (`Cmd+Space` by default)
2.  Type `Terminal.app`
3.  Press `Enter`

Now, type

    telnet 127.0.0.1 8080

If you're on macOS High Sierra or Mojave, type `nc` instead of `telnet`.

We've put three things separated by spaces:

1.  The name of the app.
2.  First parameter that `telnet` requires: the address of the machine we want to connect to.
3.  Second parameter that `telnet` requires: the port.

`127.0.0.1` is a special IP-address that corresponds to "the same computer". It's like a pointer that always points to itself: if I run a program on my laptop, then `127.0.0.1` means "my laptop". If I run the same program on my mom's PC, `127.0.0.1` will mean "my mom's PC". We use this address here because we will run both the client app and the server app on the same physical computer.

## Make a GET request

```
GET /article.html HTTP/1.1
Host: localhost
```
