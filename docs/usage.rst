=====
Usage
=====

To use quickfix.py in a project::

    usage: quickfix.py [-h] [-v] [-V] [-o OUTPUT] [-i] [-a] [-f]

    run a Python script and format the exception traceback as Vim quickfix

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         be more verbose (default: False)
      -V, --version         show program's version number and exit
      -o OUTPUT, --output OUTPUT
                            specify quickfix output file (default: None)
      -i, --interrupt       catch ^C (useful when locating an infinite loop)
                            (default: False)
      -a, --all             print all files instead of just user files (default:
                            False)
      -f, --fuck            print a line of command that opens sensible-editor at
                            the last error location (default: False)

    Fork me on GitHub: https://github.com/tonyxty/quickfix.py
