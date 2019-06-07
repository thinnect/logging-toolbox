# `logging-toolbox`

[![Build Status](https://travis-ci.com/thinnect/logging-toolbox.svg?branch=master)](https://travis-ci.com/thinnect/logging-toolbox)

The `logging-toolbox` module contains useful functions to help the user
with logging recurring things like command-line arguments and dependencies
on startup.

## Usage

### Logging program arguments and dependencies

Suppose we have a Python program that has the dependencies `dep1` and `dep2`,
and takes the command-line arguments `--server-url`, `--one-argument` and
`--some-hex-value`. We'll assume the module the program is a part of is
called `simple_program`. Upon startup, we can log the versions of our
dependencies and all arguments.

```python
from .utils import get_args, setup_logging

from logging_toolbox.startup import startup_log
from logging_toolbox.utils import clean_url


if __name__ == '__main__':
    arguments = get_args()
    setup_logging()

    startup_log(arguments,
                critical_modules=['simple_program', 'dep1', 'dep2'],
                cleaners={'server_url': clean_url,
                          'some_hex_value': '0x{:04X}'.format})
```

This should log something like:

```text
=================CONFIG=================
----------------Versions----------------
simple_program : UNKNOWN
dep1           : 0.3.2.dev23
dep2           : 1.0.1
---------------Arguments----------------
one_argument   : argument value
server_url     : https://user:******@server/
some_hex_value : 0x02FF
=======================================
```
