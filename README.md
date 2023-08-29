<div align="center">

<img src="https://github.com/ramsy0dev/sleuth/blob/957c88186b3e3e1cac164d9488438f0b61de9546/assets/sleuth.png?raw=true" width="400"/>

![Python](https://img.shields.io/badge/python-3.11%2B-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub contributors](https://img.shields.io/github/contributors/ramsy0dev/sleuth?style=for-the-badge)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/ramsy0dev/sleuth?style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/sleuth?style=for-the-badge)

</div>

# Table of content

* [What is Sleuth?](#what-is-sleuth)
* [Prequirements](#prequirements)
* [Installation](#installation)
    * [Pypi](#pypi)
    * [From source](#from-source)
* [Setup](#setup)
* [Help](#help)
* [Contributors](#contributors)
* [License](#license)

# What is Sleuth?

Sleuth is an open source OSINT tool for tracking down IP addresses and gathering information about them. It supports two types of databases (SQLite, PostgreSQL) to save your tracking results and enables you to review them.

# Prerequisites

Before installing Sleuth, make sure you have nmap installed, along with Python version 3.11 or higher. Additionally, you need to create an account on [vpnapi.io](https://vpnapi.io) to obtain an API Key, as you will need it during Sleuth setup.

# Installation

* ## Pypi

```
pip install sleuth
```

* ## From source

You need to clone the repository and build the package using Poetry. If you don't have Poetry installed, you can install it with pip: `pip install poetry`

Full command:

```bash
git clone https://github.com/ramsy0dev/sleuth
cd sleuth
poetry build
pip install sleuth-*.whl
```

# Setup

Now that Sleuth is installed, let's proceed with the setup. To do that, run the setup command:

``` bash
sleuth setup
```

You will be prompted with questions to fill in. The first is your vpnapi.io API Key. Afterward, decide whether to use a database or not. It's recommended to use a database to save tracking results. Sleuth supports two types of databases: SQLite and PostgreSQL. If you choose SQLite, a database file will be created at `~/.config/sleuth/sleuth.db`. If you opt for PostgreSQL, you'll need to provide additional parameters like username, password, host, port, and database name for the connection. If you don't want to host PostgreSQL locally, you can use an external provider like neondb, which offers a great free plan and it's beginner-friendly.

> __Warning__: Do not remove the database at `~/.config/sleuth/sleuth.db`

# Help

``` bash

         ___   _             _    _
        / __> | | ___  _ _ _| |_ | |_
        \__ \ | |/ ._>| | | | |  | . |
        <___/ |_|\___.`___| |_|  |_|_|
                  Made by `ramsy0dev`
     -- Sleuth -- `If it's smart, it's vulnerable`


 Usage: python -m sleuth [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell. [default: None]                   │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or customize the          │
│                                                              installation.                                                                 │
│                                                              [default: None]                                                               │
│ --help                                                       Show this message and exit.                                                   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ search              Search for a target IP in the database                                                                                 │
│ setup               Setup Sleuth's database to use                                                                                         │
│ track               Tracks a given IP address and returns info about it                                                                    │
│ version             Sleuth's current version                                                                                               │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

# Contributors

<!-- A big thank you to the following contributors who have helped improve this project: -->

Your contributions are highly appreciated! Whether it's bug reports, feature suggestions, or direct code contributions, every bit helps make this project better.

If you're interested in contributing, check out the [Contributing Guidelines](CONTRIBUTING.md) to get started.

# License

This project is under the [GPL-3.0](LICENSE) license
