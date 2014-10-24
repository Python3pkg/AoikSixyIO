# AoikSixyIO
Make Python string encoding and IO code 2*3 compatible, mess-free, and error-proof.

Tested working with:
- Python: 2.7+, 3.3+

[Package on PyPI](https://pypi.python.org/pypi/AoikSixyIO)

[Best Practices](#best-practices) included

## Contents
- [How to install](#how-to-install)
  - [Install via pip](#install-via-pip)
- [How to use](#how-to-use)
  - [Find the command](#find-the-command)
  - [Run the command](#run-the-command)
- [Best Practices](#best-practices)
- [How to read the funny source code](#how-to-read-the-funny-source-code)

## How to install

### Install via pip
Run
```
pip install AoikSixyIO
```
or
```
pip install git+https://github.com/AoiKuiyuyou/AoikSixyIO
```

## How to use
AoikSixyIO aims to help enforce some of the [best practices](#best-practices) listed below.  
Its usage can be best demostrated by the program **aoiksixyioexp**.

*aoiksixyioexp* takes input data from either stdin, a innput file, or a command argument, then optionally pipes the data to a subprocess, and then outputs the data to either stdout or an output file.

As you might have noticed, *aoiksixyioexp* has covered the most common use cases of string encoding and IO. It relies on AoikSixyIO to make the code 2*3 compatible, mess-free, and error-proof.

### Find the command
After the [installation](#how-to-install), a command named **aoiksixyioexp** should be available on your console.

### Run the command
Show usage: 
```
aoiksixyioexp -h
```

By default, it reads from stdin, and writes to stdout.
```
echo hello | aoiksixyioexp
```

Show debug info.  
You will see the traceback info when an error happens.
```
echo hello | aoiksixyioexp --debug
```

Show encoding info.
```
echo hello | aoiksixyioexp --ei
```

Specify stdin, stdout, and stderr encoding.  
Override env var **PYTHONIOENCODING**.
```
echo hello | aoiksixyioexp --stdioe utf-8
```

Specify stdin encoding.  
Override env var **PYTHONIOENCODING**.
```
echo hello | aoiksixyioexp --stdie utf-8
```

Specify stdout encoding.  
Override env var **PYTHONIOENCODING**.
```
echo hello | aoiksixyioexp --stdoe utf-8
```

Specify stderr encoding.  
Override env var **PYTHONIOENCODING**.
```
echo hello | aoiksixyioexp --stdee utf-8
```

Specify input value from cmd arg, instead of stdin.  
```
aoiksixyioexp --ia hello
```

Specify cmd arg encoding.  
```
aoiksixyioexp --ia hello --cae utf-8
```

Specify filesystem encoding.  
(This argument is unused in the program.)
```
aoiksixyioexp --fse utf-8
```

Specify input file path.  
```
aoiksixyioexp --if input_file.txt
```

Specify input file encoding.
```
aoiksixyioexp --if input_file.txt --ife utf-8
```

Specify output file path.  
```
aoiksixyioexp --of output_file.txt
```

Specify output file encoding.  
```
aoiksixyioexp --of output_file.txt --ofe utf-8
```

Convert invalid characters in output file name to empty.  
```
aoiksixyioexp --of output_file.txt --ofnte
```

Convert invalid characters in output file name to spaces.  
```
aoiksixyioexp --of output_file.txt --ofnts
```

Convert invalid characters in output file name to % notation.  
```
aoiksixyioexp --of output_file.txt --ofntn
```

Run a command in subprocess.  
Send input data to its stdin, get output data from its stdout.
```
echo hello | aoiksixyioexp --sp "grep ll"
```

Specify subproc command separator.
```
echo hello | aoiksixyioexp --sp "grep,ll" --spsep ","
```

Specify subproc command encoding.  
By default utf-8.
```
echo hello | aoiksixyioexp --sp "grep ll" --spce utf-8
```

Specify subproc stdin encoding.  
By default utf-8.
```
echo hello | aoiksixyioexp --sp "grep ll" --spie utf-8
```

Specify subproc stdout encoding.  
By default utf-8.
```
echo hello | aoiksixyioexp --sp "grep ll" --spoe utf-8
```

Specify subproc stderr encoding.  
By default utf-8.
```
echo hello | aoiksixyioexp --sp "grep ll" --spee utf-8
```

## Best Practices
Below are general best practices that I recommend for Python string encoding and IO code.

With the help of AoikSixyIO, some of them can be enforced easier.

### BP-1
Use **utf-8** for source file encoding declaration.

```
# coding: utf-8
```

Example:
- See [here](/src/aoiksixyio/aoiksixyioexp.py#L1).

Exception:
- Legacy code.

### BP-2
Make sure source file is indeed encoded by the encoding declared in source file encoding declaration.

Remember to change the actual file encoding whenever you change the declaration, and vice versa.

### BP-3
Note *source file encoding declaration* only affects how unicode literals (stored as bytes in the source file) are decoded into unicode objects. It does not affect other encoding aspects of a program, such as stdout encoding.  

I've seen some smart IDE that will change running environment's PYTHONIOENCODING according to *source file encoding declaration*. This gives the false perception that *source file encoding declaration* affects IO encodings. In fact it doesn't. This is why a program may work out-of-the-box in the IDE's running environment but crashes in a production environment.

### BP-4
On Py2, reload default encoding to utf-8.

Example:
- See [here](/src/aoiksixyio/aoiksixyioexp.py#L300).

The sole purpose of reloading to utf-8 is to be consistent with Py3's default encoding.

In fact, we are going to **NOT** use default encoding, as much as possible. Because use of default encoding is a sympton of implicit conversion, which is recommended against in [BP-8](#bp-8).

AoikSixyIO has provided a [reload_default_encoding](/src/aoiksixyio/aoiksixyio_.py#L256) function.

### BP-5
Use unicode objects, instead of bytes objects, for string processing. 

Do not mix unicode objects with bytes objects like below, it causes [implicit conversion](#bp-8).
```
u'01'.replace(u'0', '1')
```

AoikSixyIO's many functions enforce this practice by allowing unicode objects only.
Examples:
- [stdout_write](/src/aoiksixyio/aoiksixyio_.py#L294).
- [stdout_print](/src/aoiksixyio/aoiksixyio_.py#L311).
- [stdout_write_fmt](/src/aoiksixyio/aoiksixyio_.py#L333).
- [stdout_print_fmt](/src/aoiksixyio/aoiksixyio_.py#L346).

### BP-6
Use unicode literals e.g. ```u'abc'``` instead of str literals e.g. ```'abc'```.  
Unicode literals e.g. ```u'abc'``` are unicode objects on both Py2 and Py3.  
Str literals e.g. ```'abc'``` are bytes objects on Py2 and unicode objects on Py3.

Example:
- See [here](/src/aoiksixyio/aoiksixyioexp.py#L208).

Exception:
- The **u** prefix has been added to Python 3 since version 3.3.  
  It is invalid syntax on Python 3.0~3.2.  
  If your program needs to support Python 3.0~3.2, use another level of wrapping.

### BP-7
On Py2, wherever str objects (str is bytes on Py2) are expected, do not use unicode objects. Otherwise implicit conversion will be performed.

Example:
- See [here](/src/aoiksixyio/aoiksixyioexp.py#L782).

### BP-8
Understand implicit conversion, to the extent that you choose not to use it at all.

Here is an exmaple to help you understand when implicit conversion happens.  
Assume your source file encoding is utf-8, then
```
# coding: utf-8

utxt = u'你好'

print utxt
```
is equivalent to
```
# coding: utf-8

btxt = '你好'
src_file_encoding = 'utf-8'
utxt = btxt.decode(src_file_encoding)

stdout_implicit_encoding = sys.stdout.encoding or sys.getdefaultencoding()
btxt2 = utxt.encode(stdout_implicit_encoding)
print btxt2
```

Implicit conversion not solves but hides encoding problems.  
Do not rely on implicit conversion to get your program working. 

AoikSixyIO has provided functions for converting between bytes and unicode in your specified encodings. Encodings are specified when [creating an object of class SixyIOObj](/src/aoiksixyio/aoiksixyioexp.py#L342).
Then all the conversion and IO actions you perform via the SixyIOObj object are done in the specified encodings.

Examples:
- [Convert input from command argument](/src/aoiksixyio/aoiksixyioexp.py#L409)
- [Convert input from stdin](/src/aoiksixyio/aoiksixyioexp.py#L479)
- [Convert input from file](/src/aoiksixyio/aoiksixyioexp.py#L447)
- [Convert output to stdout](/src/aoiksixyio/aoiksixyioexp.py#L764)
- [Convert output to file](/src/aoiksixyio/aoiksixyioexp.py#L731)

### BP-9
Do not assume that **sys.stdin.encoding**, **sys.stdout.encoding** and **sys.stderr.encoding** have values. They can be None. For example, on Py2, when stdin is from a pipe, or when stdout and stderr are redirected, their encodings are set to None.

AoikSixyIO has solved this by [maintaining its own set of encoding settings](/src/aoiksixyio/aoiksixyio_.py#L816) and ensure none of them is None.

### BP-10
Do not use **sys.stdin.read**, **sys.stdout.write**, **sys.stderr.write**, and **open** directly.

These IO functions are in bytes mode on Py2 and text mode on Py3.  
It's hard to support both Py2 and Py3 in a clean way.

AoikSixyIO has solved this by providing functions that work on both Py2 and Py3.

Examples:
- [stdin_make_reader](/src/aoiksixyio/aoiksixyio_.py#L1143) and [usage](/src/aoiksixyio/aoiksixyioexp.py#L479)
- [stdout_write](/src/aoiksixyio/aoiksixyio_.py#L294) and [usage](/src/aoiksixyio/aoiksixyioexp.py#L764)
- [stdout_print](/src/aoiksixyio/aoiksixyio_.py#L311)
- [stderr_write_safe](/src/aoiksixyio/aoiksixyio_.py#L1234)
- [stderr_print_safe](/src/aoiksixyio/aoiksixyio_.py#L1241) and [usage](/src/aoiksixyio/aoiksixyioexp.py#L380)
- [stdout_write_fmt](/src/aoiksixyio/aoiksixyio_.py#L333)
- [stdout_print_fmt](/src/aoiksixyio/aoiksixyio_.py#L346)
- [stderr_write_fmt_safe](/src/aoiksixyio/aoiksixyio_.py#L1262) and [usage](/src/aoiksixyio/aoiksixyioexp.py#L618)
- [stderr_print_fmt_safe](/src/aoiksixyio/aoiksixyio_.py#L1269) and [usage](/src/aoiksixyio/aoiksixyioexp.py#L412)
- [open_in](/src/aoiksixyio/aoiksixyio_.py#L1374) and [usage](/src/aoiksixyio/aoiksixyioexp.py#L447)
- [open_out](/src/aoiksixyio/aoiksixyio_.py#L1381) and [usage](/src/aoiksixyio/aoiksixyioexp.py#L731)

### BP-11
Choose good default values for encoding settings.

Note *default value* here means the value you use if the user does not specify one explicitly via environment variable (e.g. PYTHONIOENCODING) or command arguments. It is not same as Python's default encoding.

The ultimate goal of good default values is that they work out-of-the-box (e.g. no garbled characters) in as many use cases as possible, without extra tweaking by user.

Due to the variety in use cases, however, there is no universal solution for deciding default values. Below is the how AoikSixyIO decides:
- Stdin encoding: [SixyIO.STDEE](/src/aoiksixyio/aoiksixyio_.py#L74) and [SixyIOObj.stdee](/src/aoiksixyio/aoiksixyio_.py#L907)
- Stdout encoding: [SixyIO.STDOE](/src/aoiksixyio/aoiksixyio_.py#L82) and [SixyIOObj.stdoe](/src/aoiksixyio/aoiksixyio_.py#L885)
- Stderr encoding: [SixyIO.STDEE](/src/aoiksixyio/aoiksixyio_.py#L91) and [SixyIOObj.stdee](/src/aoiksixyio/aoiksixyio_.py#L862)
- Command argument encoding: [SixyIO.CAE](/src/aoiksixyio/aoiksixyio_.py#L97) and [SixyIOObj.cae](/src/aoiksixyio/aoiksixyio_.py#L929)
- Filesystem encoding: [SixyIO.FSE](/src/aoiksixyio/aoiksixyio_.py#L102) and [SixyIOObj.fse](/src/aoiksixyio/aoiksixyio_.py#L951)
- Input file encoding: [SixyIO.IFE](/src/aoiksixyio/aoiksixyio_.py#L106) and [SixyIOObj.ife](/src/aoiksixyio/aoiksixyio_.py#L973)
- Output file encoding: [SixyIO.OFE](/src/aoiksixyio/aoiksixyio_.py#L110) and [SixyIOObj.ofe](/src/aoiksixyio/aoiksixyio_.py#L994)
- Subproc command encoding: [SixyIO.SPCE](/src/aoiksixyio/aoiksixyio_.py#L114) and [SixyIOObj.spce](/src/aoiksixyio/aoiksixyio_.py#L1016)
- Subproc stdin encoding: [SixyIO.SPIE](/src/aoiksixyio/aoiksixyio_.py#L118) and [SixyIOObj.spie](/src/aoiksixyio/aoiksixyio_.py#L1038)
- Subproc stdout encoding: [SixyIO.SPOE](/src/aoiksixyio/aoiksixyio_.py#L122) and [SixyIOObj.spoe](/src/aoiksixyio/aoiksixyio_.py#L1060)
- Subproc stderr encoding: [SixyIO.SPEE](/src/aoiksixyio/aoiksixyio_.py#L126) and [SixyIOObj.spee](/src/aoiksixyio/aoiksixyio_.py#L1082)

### BP-12
Provide command arguments for encoding settings (listed in [BP-10](#bp-10)), in case the default values you choose do not work well.

Depending on your program's use cases, you might provide all of them or leave out some.

### BP-13
Check for invalid encoding settings from PYTHONIOENCODING and command arguments.

Example:
- See [here](/src/aoiksixyio/aoiksixyio_.py#L869).

### BP-14
Decode command argument values to unicode before use.  
Argument values from *argparse* are unicode on Py3 but are bytes on Py2.

AoikSixyIO has provided function [cae_to_u](/src/aoiksixyio/aoiksixyio_.py#L1290).

Example:
- See [here](/src/aoiksixyio/aoiksixyioexp.py#L409).

### BP-15
Provide separate command arguments for standard io encodings and file io encodings. Do not assume they are the same. Standard io are usually for prompt messages, correct encoding of which varies with running environments. File io are usually for data, correct encoding of which varies with use cases.

### BP-16
Convert a filesystem path to unicode, before pass it to a library function like **open**. Library functions are usually smart enough to encode unicode to bytes with proper encoding (supposedly using ```sys.getfilesystemencoding()```).  

Example:
- See [here](/src/aoiksixyio/aoiksixyioexp.py#L430).

If the path is obtained from command argument, see also [BP-13](#bp-13).

### BP-17
Subprocess' command and arguments, its stdin, stdout, and stderr are all in bytes.

Convert command and arguments to bytes before creating the subprocess object  
Example:
- See [here](/src/aoiksixyio/aoiksixyioexp.py#L527).

Convert unicode to bytes before sending input data to its stdin.  
Example:
- See [here](/src/aoiksixyio/aoiksixyioexp.py#L556).

Convert bytes to unicode after reading output data from stdout and stderr.  
Example:
- See [here](/src/aoiksixyio/aoiksixyioexp.py#L637) and [here](/src/aoiksixyio/aoiksixyioexp.py#L599).

As stated in [BP-11](#bp-11), provide command arguments for tweaking in case default values not work well.

### BP-18
Wherever there are encoding or decoding performed, there are chances of errors.

Errors are unavoidable because:
- Default values will not work in all cases.
- User may specify a wrong encoding.
- Many encodings, unlike utf-8, are unable to encode all unicode characters.

To make your program robust, your code must be prepared for errors.

In general, there are two strategies for handling errors:

1. If an error is critical, abort with user friendly error message.  
  Example: [Call unsafe function, catch errors, print message, and exit](/src/aoiksixyio/aoiksixyioexp.py#L430)
2. If an error is non-critical, tolerate.  
  Example: [Call safe function, transforming unencodable characters into something encodable](/src/aoiksixyio/aoiksixyioexp.py#L433)

## How to read the funny source code
For developers interested in reading the source code,  
Here is a flowchart ([.png](/doc/dev/aoiksixyioexp.png?raw=true), [.svg](/doc/dev/aoiksixyioexp.svg?raw=true), or [.graphml](/doc/dev/aoiksixyioexp.graphml?raw=true)) that has recorded key steps of the program **aoiksixyioexp**.  
![Image](/doc/dev/aoiksixyioexp.png?raw=true)

The flowchart is produced using free graph editor [yEd](http://www.yworks.com/en/products_yed_download.html).

If you want to copy the text in the graph, it's recommended to download the [.svg](/doc/dev/aoiksixyioexp.svg?raw=true) file and open it locally in your browser. (For security reason, Github has disabled rendering of SVG images on the page.)

The meaning of the shapes in the flowchart should be straightforward.  
One thing worth mentioning is isosceles trapezium means sub-steps.

The most useful feature of the flowchart is, for each step in it,
there is a 7-character ID.  
This ID can be used to locate (by text searching) the code that implements a step.  
This mechanism has two merits:

1. It has provided **precise** (locating precision is line-level)
  and **fast** (text searching is fast) mapping from doc to code, which is
  very handy for non-trivial project.

  Without it you have to rely on developers' memory to recall the code locations (*Will you recall them after several months, precise and fast?*).

2. It has provided **precise** (unique ID) and **concise** (7-character long) names
  for each steps of a program, which is very handy for communicating between
  members of a development team.

  Without it describing some steps of a program between team members tends to be unclear.
