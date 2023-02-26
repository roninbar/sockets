# Exercise

1. Add command line arguments to the server:
   - `--host` or `-H`: IP address or hostname to bind to.
   - `--port` or `-p`: port to bind to.
   
    If the `--port` option is not given, check an environment variable named `PORT` and read the port from it.
    If the `PORT` variable is not defined either, use a hard-coded default port number of 3000.
2. Add a command line argument to the *client*:
   - `--text` or `-t`: text to send to the server (instead of using `input()`).
3. Add a command line argument to the *client*:
   - `--file`, `-f`: filename to send to the server.
   This option and the previous one (`-t`) are mutually exclusive. If both options are given, raise an error and quit.