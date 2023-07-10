# Conda

## Overview

While we will be using a cloud-hosted computing environment during the hackweek
({ref}`event-jupyterhub`), it is often desirable to run Python code on your laptop.
We also want to ensure that hackweek tutorials or other scientific code is
reproducible and can be run on different computers and operating systems.

This lesson takes you through our recommended procedure for managing [Python environments and software](./python) on your personal computer.
We suggest you follow these instructions in advance so that we can help you troubleshoot during the hackweek
and have a fully functioning environment after.

## What is Conda?

[**Conda**](http://conda.pydata.org/docs/) is an **open source `package` and `environment` management system** for installing multiple versions of software packages and their dependencies and switching easily between them. Conda works with many programming languages but is very popular in the Python community. It works on Linux, OS X and Windows.

## Installing Miniconda

[Miniconda](http://conda.pydata.org/miniconda.html) is a command line tool which contains only Python and essential packages.
We recommend installing it because it is the easiest way to use conda for Python environment management without taking up too much space.

### Windows
Click [here](http://conda.pydata.org/miniconda.html) to download the proper installer for your Windows platform (64 bits).
You can still create Python 2 environments using the Python 3 version of Miniconda.

When installing, you will be asked if you wish to make the Anaconda Python your default Python for Windows.
If you do not have any other installation that is a good option.
If you want to keep multiple versions of Python on your machine (e.g. ESRI-supplied Python or 64 bit versions of Anaconda), then don't select the option to modify your path or modify your windows registry settings.

### Linux and OS X
You may follow manual steps from [here](http://conda.pydata.org/miniconda.html) similar to the instructions on Windows (see above).
Alternatively, you can execute these commands on a terminal shell (in this case, the bash shell):

```bash
# For MacOSX
url=https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
# For Linux
url=https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
wget $url -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
conda update conda --yes
```

## Installing Anaconda Instead (Optional)

!!! note "If you don't want all of Anaconda"
	If you don't have time or disk space for the entire distribution do not install Anaconda.
	Install only [Miniconda](http://conda.pydata.org/miniconda.html), a bootstrap version of Anaconda, which contains only Python, essential packages, and conda. We will provide an environment file to install all the packages necessary for the hackweek.*

[Anaconda](https://www.anaconda.com/distribution/) is a data science platform that comes with a lot of packages.
At its core, Anaconda uses the conda package management system.

The list of packages included can be found [*here*](https://docs.anaconda.com/anaconda/packages/pkg-docs).

1. To install Anaconda, please click on the link below for your operating system, and follow the instructions on the [site](https://www.anaconda.com/download/).
2. Once the Anaconda installation step is finished run `python` in the command line to test if Anaconda is installed correctly.
**Note: For windows, please use the Anaconda prompt as the command line. It should be installed with your installation of Anaconda**.
If Anaconda is installed correctly, you should have this prompt, which emphasizes **Anaconda**:

```bash
$ python
Python 3.7.3|Anaconda custom (x86_64)| (default, Mar 27 2019, 22:11:17)
...
```

```{note}
Anaconda (on Linux) expects you to work in the `bash` shell.
If this is not already your default shell, you need to set it to be with:
``` bash
chsh -s /bin/bash
```

You can also run an instance of bash from the command line before issuing "Conda" commands (`/bin/bash` or where it is located on your system).
```