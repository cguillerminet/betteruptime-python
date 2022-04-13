# betteruptime-python

[![Check](https://github.com/cguillerminet/betteruptime-python/actions/workflows/ci.yml/badge.svg)](https://github.com/cguillerminet/betteruptime-python/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/betteruptime.svg)](https://badge.fury.io/py/betteruptime)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/betteruptime.svg)](https://pypi.python.org/pypi/betteruptime/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

**betteruptime-python** is a [BetterUptime](https://betteruptime.com/) API client for python.

## Installation

The package is published on
[PyPI](https://pypi.org/project/betteruptime/) and can be installed by running:

    pip install betteruptime

## Basic Use

Easily query the BetterUptime API from you Python code.

```python
>>> client = betteruptime.Client(bearer_token='My BetterUptime Bearer Token')
>>> client.monitors.list()
>>> client.monitors.get('123456')
```
