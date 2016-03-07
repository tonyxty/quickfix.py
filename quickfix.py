#!/usr/bin/env python3
# quickfix.py
# Copyright (C) 2015 Tony Beta Lambda <tonybetalambda@gmail.com>
# This file is licensed under the MIT license.  See LICENSE for more details.

import os
import sys
import functools
from argparse import ArgumentParser
from traceback import print_tb, extract_tb
from contextlib import redirect_stdout


def run(source, filename, catch_interrupt=False):
    try:
        code = compile(source, filename, 'exec')
    except (TypeError, SyntaxError) as e:
        return e, None
    else:
        sys.path.insert(0, os.path.dirname(filename))
        globs = {
            '__file__': filename,
            '__name__': '__main__',
            '__package__': None,
            '__cached__': None,
        }
        exceptions = (Exception, KeyboardInterrupt) if catch_interrupt \
            else Exception
        try:
            exec(code, globs, None)
        except exceptions:
            _, e, tb = sys.exc_info()
            return e, extract_tb(tb)[1:]


def extract_error_location(exc, filename_filter=None):
    e, tb = exc
    if isinstance(e, SyntaxError):
        # yield the line triggering SyntaxError
        yield (e.filename, e.lineno, "{}: {}".format(type(e).__name__, e.msg))
    if tb is not None:
        r = ((filename, lineno, "in function " + fnname)
             for filename, lineno, fnname, text in tb if text is not None)
        if filename_filter is not None:
            r = (_ for _ in r if filename_filter(_[0]))
        r = list(r)

        try:
            filename, lineno, _ = r.pop()
        except IndexError:
            return
        # insert error message to the first returned location
        yield filename, lineno, "{}: {}".format(type(e).__name__, e)
        yield from reversed(r)


# writable by user and directory components do not start with a dot
@functools.lru_cache(maxsize=32)
def is_user_heuristic(filename):
    return os.access(filename, os.W_OK) and \
            not any(s != '.' and s.startswith('.')
                    for s in filename.split(os.sep))


def main():
    parser = ArgumentParser(
            description="run a Python script and format the exception "
                        "traceback as Vim quickfix",
            epilog="Fork me on GitHub: https://github.com/tonyxty/quickfix.py"
            )
    parser.add_argument(
            '-o', '--output',
            help="specify quickfix output file")
    parser.add_argument(
            '-i', '--interrupt', action='store_true',
            help="catch ^C (useful when locating an infinite loop)")
    parser.add_argument(
            '-a', '--all', action='store_true',
            help="print all files instead of just user files")
    parser.add_argument(
            '-f', '--fuck', action='store_true',
            help="print a line of command that opens sensible-editor at the "
            "last error location")

    invocation = sys.argv[0]
    (options, args) = parser.parse_known_args()
    if invocation == "thefuck.py":
        options.fuck = True

    sys.argv[:] = args
    if len(args) > 0 and (args[0] == "python3" or args[0] == "python"):
        filename_index = 1
    else:
        filename_index = 0

    try:
        filename = args[filename_index]
    except IndexError:
        if options.fuck:
            print("#", end=" ")
        print("no file given")
        return 2

    with open(filename, 'rb') as f:
        source = f.read()

    if options.output is not None:
        exc = run(source, filename, options.interrupt)
    else:
        # suppress output of exec'ed script
        with open(os.devnull, 'w') as f:
            with redirect_stdout(f):
                exc = run(source, filename, options.interrupt)

    if exc is not None:
        filename_filter = None if options.all else is_user_heuristic
        err_locs = extract_error_location(exc, filename_filter)
        if options.output is not None:
            outfile = open(options.output, 'w')
        else:
            outfile = sys.stdout

        if options.fuck:
            try:
                filename, lineno, _ = next(err_locs)
            except StopIteration:
                print("# no fuck given", file=outfile)
            print("sensible-editor {} +{}".format(filename, lineno),
                  file=outfile)
        else:
            print("\n".join("\"{}\":{}: {}".format(*loc) for loc in err_locs),
                  file=outfile)

        if outfile is not sys.stdout:
            outfile.close()
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
