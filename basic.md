---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"tags": []}

# Introduction to PyShop

+++

SHOP has oringally been run as a batch process where the user defines a model and input data through one or several files, and the exectuion process is specified by a command file. Similarly, the results are dumped as a set of output files. A more modern and flexible approach is to run SHOP through an API. An API (application programming interface) enables interaction with SHOP through programming code instead of only fixed predefined inputs, and this approach has several benefits such as:
- SHOP can interact with other applications in the scheduling toolchain instead without using input and output files.
- The optimization process may follow programmatic rules, for example, to decide how many types of interation to execute based on results and execution time of previous iterations.
- Input and outputs are using the pandas library that has a wide support for different input/output sources and formats.

However, the SHOP-API is written in C and only permits setting and getting primitive datatypes such as numbers, strings and arrays of number or strings. Therefore, setting timeseries and curves requires multiple API-calls. PyShop is a wrapper written in Python that lifts the primitive C-API to a high-level API using pandas to represent timeseries and curves, and offers model exploration and auto-completion in a pythonic way.

+++

## Installing PyShop
This course will use SINTEF Energy's vlab for the PyShop exercises. For local installation, please follow the guidelines provided at the SHOP portal: https://shop.sintef.energy/news/pyshop-becomes-an-official-python-package/

+++

## Getting started
PyShop uses pandas, that is an open source library for managing data-structures, for managing timeseries and curves. We will therefore, as shown in the first codeline below, import pandas and refer to it as pd for convenience. To start a ShopSession, we will also import the ShopSession class from PyShop. This class enables us to create new instances of SHOP that are populated with data and optimized. The corrector is a set of functions that must be imported for this course to check your answers.

```{code-cell} ipython3
import pandas as pd
from pyshop import ShopSession
from corrector.corrector import *
```

To instantiate a new `ShopSession`, we simply call the class by appending the parantheses and name the session `shop`. The `ShopSession` constructor may receive several optional arguments like `ShopSession(license_path='c:/my license path')` but these are not required when running in the vlab.

```{code-cell} ipython3
shop = ShopSession()
```

### Setting the time horizon
The time horizon, start and end time of the optimization, must be defined before adding any data. Our optimization starts at the time given by the `starttime` variable.

Complete the code:
- create a new `Timestamp` named `endtime` 2 days later than `starttime`.
- fill in the missing argument to `set_time_resolution`.
- execute the code.

```{code-cell} ipython3
starttime = pd.Timestamp('2022-01-01')
endtime = pd.Timestamp('2022-01-03')
shop.set_time_resolution(starttime=starttime, endtime=endtime, timeunit='hour')
```

```{code-cell} ipython3
---
jupyter:
  source_hidden: true
tags: []
---
button, output = generate_button(shop, check_time_resolution)
display(button, output)
```

+++ {"tags": []}

### Setting the time resolution (optional)
The `set_time_resolution` function also specified the `timeunit` as `'hour'`. SHOP formulates an optimization model with discrete time steps. The default step size is given by the time unit. We can also use timeunit `'minutes'` and set the `timeresolution` to 60 as shown in the example below which is equivalent with hourly resolution. The `timeresolution` argument also enables variable step size in the model, for example, smaller step size in the first hours.

```{code-cell} ipython3
shop.set_time_resolution(starttime=starttime, endtime=endtime, timeunit='minute', timeresolution=pd.Series([60], index=[starttime]))
```

### Creating objects
A SHOP model comprises multiple objects, both physical objects in the watercourse like reservoirs, plants and generators as well as abstract objects like markets. SHOP can list all available object types as shown below. For detailed information about the object types, we refer to the documentation.

```{code-cell} ipython3
rsv1 = shop.model.reservoir.add_object('Rsv1')
```

Complete the code below to create a minimal working example:
- create a `plant` named `'Plant1'`
- create a `generator` named `'Plant1_G1'`

```{code-cell} ipython3
plant1 = shop.model.plant.add_object(___)
___
```

```{code-cell} ipython3
---
jupyter:
  source_hidden: true
tags: []
---
button, output = generate_button(shop, check_plant_and_generator_added)
display(button, output)
```

```{code-cell} ipython3

```
