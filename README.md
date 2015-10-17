# quickfix.py
Run a Python script and format the exception traceback as Vim quickfix

## Usage
    quickfix.py foobar.py foo bar
runs `foobar.py` with command line arguments `foo bar` under supervision.  Once an exception is raised, *quickfix.py* prints the stack traceback in Vim quickfix format, one frame per line.

Currently only works for Python 3.x.

### Command line options
* By default, only those frames that are in "user" scripts are printed, standard library calls are skipped.  `--all` enables printing all frames.
* By default, *quickfix.py* catches `Exception`s, but not `KeyboardInterrupt`.  `--interrupt` enables catching ^C, thereby allowing conveniently locating an infinite loop.

### thef__k mode
*quickfix.py* also supports "thefuck" mode, inspired by [nvbn/thefuck](https://github.com/nvbn/thefuck).  When `--fuck` option is given or the script is run as "thefuck.py", it outputs a line of command that opens `sensible-editor` at the location of exception.  See `bashrc` for idiomatic usages.
