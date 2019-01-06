# CodeStats

Provides in-depth information about the makeup of a project, regardless of language used.

## What?

Ever wonder how much code is contained in your project? Maybe in total or minus whitespace, proceeding indents, etc? CodeStats provides an easy way of finding this information plus a lot more. Right now the following is supported, hopefully more coming later.

* percentages per language. e.g. python 50.2%, C++ 30.3%, C# 19.5%
* Total Lines
* total blank lines
* total lines that have content
* average number of characters per line
* average number of lines per file
* total number of proceeding spaces/indents
* average number of indents per file
* total size of all containing files
* total size without indents
* average file size
* average file size without indents
* a complete rundown of all files searched
* exclusions based on unix wildcards

## Usage

usage: stats.py [-h] [-e EXCLUDES] [-ef EXCLUDE_FILE] [-v] [-dr] dir

Tool to provide detailed summaries of code in a project.

positional arguments:
  dir                   directory to search

optional arguments:
  -h, --help            show this help message and exit
  -e EXCLUDES, --exclude EXCLUDES
                        adds a wildcard exclusion
  -ef EXCLUDE_FILE, --exclude-file EXCLUDE_FILE
                        Path to a file containing a list of excludes to be
                        processed seperated by \n
  -v, --verbose         give args.verbose/more detailed output
  -dr, --disable-rundown
                        excludes an individual rundown of every processed file


For example, running on the [NVDA](http://github.com/nvaccess/nvda) source tree excluding individual file information

```
py -3 stats.py nvda/source --disable-rundown
```

297 files accounted for, with 0 exclusions encountered
python: 99.7%
HTML: 0.03%
windows registry entry: 0.02%
INI: 0.25%
total lines: 84644
number of blank lines: 8106
total lines that have content: 76538
average number of characters per line: 42.62
average number of lines per file: 285.0
total number of proceeding spaces/indents: 167178, making up a total of 163.3KB
average indents per file: 562.89
total size: 3.2MB, 3354444b
total size without indents: 3.0MB, 3187266b
average file size: 11.0KB, 11294.42b
average file size without indents: 10.5KB, 10731.54b

## Installing

You must have a copy of [python 3](https://www.python.org/downloads)
After installation, and assuming environment variables are set correctly, you should be able to call from commandline.

## contributing

If you find an issue or would like to contribute, use the issue tracker or get in contact. I'd prefer issues be opened before pull requests, however.

## Contact

twitter (probably most efficient): cartertemm
email: crtbraille@gmail.com
