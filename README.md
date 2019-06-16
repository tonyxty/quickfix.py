# quickfix.py

[![image](https://img.shields.io/pypi/v/quickfix-py.svg)](https://pypi.python.org/pypi/quickfix-py)
[![image](https://img.shields.io/travis/tonyxty/quickfix.py.svg)](https://travis-ci.org/tonyxty/quickfix.py)
[![Documentation
Status](https://readthedocs.org/projects/quickfix-py/badge/?version=latest)](https://quickfix-py.readthedocs.io/en/latest/?badge=latest)

Run a Python script and format the exception traceback as Vim quickfix.

-   Free software: MIT license

-   Documentation: <https://quickfix-py.readthedocs.io>.

## Installation

    pip install --user quickfix-py

or using [pipx](https://pipxproject.github.io/pipx)

    pipx install --spec git+https://github.com/tonyxty/quickfix.py quickfix-py

## Usage

    quickfix.py foobar.py foo bar

runs `foobar.py` with command line arguments `foo bar` under
supervision. Once an exception is raised, *quickfix.py* prints the stack
traceback in Vim quickfix format, one frame per line.

`docs/vimrc_example` provides an example `vimrc` configuration.

Currently only works for Python 3.x.

### Command line options

-   By default, only those frames that are in "user" scripts are
    printed, standard library calls are skipped. `--all` enables
    printing all frames.
-   By default, *quickfix.py* catches `Exception`s, but not
    `KeyboardInterrupt`. `--interrupt` enables catching \^C, thereby
    allowing conveniently locating an infinite loop.

### thef\_\_k mode

*quickfix.py* also supports "thefuck" mode, inspired by
[nvbn/thefuck](https://github.com/nvbn/thefuck). When `--fuck` option is
given or the script is run as "thefuck.py", it outputs a line of command
that opens `sensible-editor` at the location of exception. See
`docs/bashrc_example` for idiomatic usages.

## Credits

Authored by [Tony Beta Lambda](https://github.com/tonyxty/quickfix.py). This
package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[ashwinvis/cookiecutter-pypackage](https://github.com/ashwinvis/cookiecutter-pypackage)
project template.
