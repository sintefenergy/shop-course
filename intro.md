
# Introduction to pySHOP
SHOP has oringally been run as a batch process where the user defines a model and input data through one or several files, and the exectuion process is specified by a command file. Similarly, the results are dumped as a set of output files. A more modern and flexible approach is to run SHOP through an API. An API (application programming interface) enables interaction with SHOP through programming code instead of only fixed predefined inputs, and this approach has several benefits such as:
- SHOP can interact with other applications in a scheduling toolchain.
- The setup of the optimization process is more flexible and we can program rules for how to execute the iterations.
- Input and outputs are using the [pandas](https://pandas.pydata.org/) library that has a wide support for different input/output sources and formats.

The native SHOP-API is written in C and only permits setting and getting primitive datatypes such as numbers, strings and arrays of number or strings. Therefore, setting timeseries and curves requires multiple API-calls. [pySHOP](https://github.com/sintef-energy/pyshop) is a wrapper written in Python that lifts the primitive C-API to a high-level API using pandas. Therefore, you can interact directly with the model through higher level attributes in Python. Moreover, the Python interface also offers convenient auto-completion when working in notebooks in a "pythonic" way.

## Installing PyShop
This course will use SINTEF Energy's vLab for the pySHOP exercises. For local installation, please follow the guidelines provided at the SHOP portal: https://shop.sintef.energy/news/pyshop-becomes-an-official-python-package/


## External resources
If you have low previous knowledge about programming and Python, we recommend to walk through a beginners guide. The official Python website gives a overview of some of the [available resources](https://wiki.python.org/moin/BeginnersGuide/Programmers) and there are many [Python introduction videos on YouTube](https://www.youtube.com/results?search_query=python+beginner+tutorial).

## Getting started
Python has, due to its simplicity, become on of the most used programming languages. Python has a built-in package manager where more than 200.000 packages can be installed by simply typing `pip install <package name>` in your terminal. This makes Python very well suited for gluing different component in your SHOP testing environment. [pandas](https://pandas.pydata.org/) is an open source library for managing structured data, and is used timeseries and curves in pySHOP. 

This course gives a introduction to the basic building blocks for pySHOP and will show you some of the powerfull features in scripting SHOP from Python. The course is divided into the following sections:
- [Time interval and resolution](time)
- [Objects](objects)
- [Attributes](attributes)
- [Relations](relations)
- [Commands](commands)