## Synopsis

PyPathlen is a script written in Python 2.7.9. It creates a report of all subfolders and files in a given folder
and compares their relative pathlength with 2 tresholds which can be individually set. If the values "AlertAt" and "FailAt"
are exceeded, the flags [ALERT] and [FAIL] are set in the report, respectively.

## Code Example

Example 1: Scan local directory, AlertAt=200 characters, FailAt=255 characters (default)
```
python pathlen.py -p ./
```
Example 2: Scan subdirectory, AlertAt=100 characters, FailAt=200 characters
```
python pathlen.py -p /home/testuser -a 100 -f 200
```
Example 3: Display help
```
python pathlen.py -h
```
## Motivation

Some OS have a maximum pathlength. Exceeding this value may result in error messages or in the worst case 
in shortened filenames.


## Installation

Requirement: Python >=2.7.9

This script can be used "as it is" without any installation.

## Usage
```
python pathlen.py 

-p <dir>...directory (mandatory)
-h.........show help
-a <val>...AlertAt (default=200)
-f <val>...FailAt  (default=255)

```
Please note:

FailAt must be >=AlertAt

Providing a relative directory-path will result in relative values.

## Tests

n/a

## Contributors

Michael Peer, michael@michael-peer.net

## License

GPL

## Last Update of this file

17 Aug 2015

