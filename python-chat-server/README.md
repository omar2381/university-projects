# Python Chat Room

A multi-user chat room built directly on TCP sockets: a threaded server and a Tkinter desktop client, with no networking libraries beyond the Python standard library.

University coursework on networking.

## Features

- The server handles each connected client on its own thread and broadcasts messages to everyone.
- Join and leave announcements.
- Chat commands:

| Command | Action |
|---|---|
| `/help` | List the commands |
| `/list` | Show who is connected |
| `/msg` | Send a private message to one user |
| `/namech` | Change your display name |
| `/q` | Leave the chat |
| `/end` | Shut the server down for everyone |

- Every message and command is written to `server.log`.
- The client reports bad arguments, unreachable hosts and invalid ports instead of crashing.

## Running it

Start the server on a port, then start one client per user in separate terminals:

```bash
python server.py 5000
python client.py alice 127.0.0.1 5000
python client.py bob 127.0.0.1 5000
```

The client takes `<name> <host> <port>`. The server listens on `127.0.0.1`, so all clients need to be on the same machine unless you change the bind address in `server.py`.

## Tech

Python, `socket`, `threading`, Tkinter
