---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3.10.2 64-bit
  language: python
  name: python3
---

+++ {"tags": []}

# Introduction to PyShop

+++

SHOP has oringally been run as a batch process where the user defines a model and input data through one or several files, and the exectuion process is specified by a command file. Similarly, the results are dumped as a set of output files. A more modern and flexible approach is to run SHOP through an API. An API (application programming interface) enables interaction with SHOP through programming code instead of only fixed predefined inputs, and this approach has several benefits such as:
- SHOP can interact with other applications in a scheduling toolchain.
- The setup of the optimization process is more flexible and we can program rules for how to execute the iterations.
- Input and outputs are using the [pandas](https://pandas.pydata.org/) library that has a wide support for different input/output sources and formats.

The native SHOP-API is written in C and only permits setting and getting primitive datatypes such as numbers, strings and arrays of number or strings. Therefore, setting timeseries and curves requires multiple API-calls. [pySHOP](https://github.com/sintef-energy/pyshop) is a wrapper written in Python that lifts the primitive C-API to a high-level API using pandas. Therefore, you can interact directly with the model through higher level attributes in Python. Moreover, the Python interface also offers convenient auto-completion when working in notebooks in a "pythonic" way.

+++

## Installing PyShop
This course will use SINTEF Energy's vLab for the pySHOP exercises. For local installation, please follow the guidelines provided at the SHOP portal: https://shop.sintef.energy/news/pyshop-becomes-an-official-python-package/

+++

## External resources
If you have low previous knowledge about programming and Python, we recommend to walk through a beginners guide. The official Python website gives a overview of some of the [available resources](https://wiki.python.org/moin/BeginnersGuide/Programmers) and there are many [Python introduction videos on YouTube](https://www.youtube.com/results?search_query=python+beginner+tutorial).

## Getting started
Python has, due to its simplicity, become on of the most used programming languages. Python has a built-in package manager where more than 200.000 packages can be installed by simply typing `pip install <package name>` in your terminal. This makes Python very well suited for gluing different component in your SHOP testing environment. [pandas](https://pandas.pydata.org/) is an open source library for managing structured data, and is used timeseries and curves in pySHOP. We will therefore, as shown in the first codeline below, import pandas and refer to it as pd for convenience. To start a ShopSession, we will also import the ShopSession class from pySHOP. This class enables us to create new instances of SHOP that are populated with data and optimized. The corrector is a set of functions that must be imported for this course to check your answers.

Run the code below as shown a follow the instructions to build and run your first SHOP model in pySHOP.

```{code-cell} ipython3
import pandas as pd
from pyshop import ShopSession
from corrector.basic import *
```

To instantiate a new `ShopSession`, we simply call the class by appending the parantheses and assign the created session to the variable `shop`.

```{code-cell} ipython3
shop = ShopSession()
```

### Setting the time horizon
The time horizon, start and end time of the optimization, must be defined before adding any data by calling the `set_time_resolution` function as shown in the example below. We create a `Timestamp`, which is a object type in the pandas library and assign it the the variable `starttime`.

#### Exercise
Complete the code by filling the missing `***`:
- create a new `Timestamp` named `endtime` 2 days later than `starttime`.
- fill in the missing argument to `set_time_resolution`.
- execute the code.

```{code-cell} ipython3
starttime = pd.Timestamp('2022-01-01')
endtime = pd.Timestamp('2022-01-03')
shop.set_time_resolution(starttime=starttime, endtime=endtime, timeunit='hour')

check_time_resolution(shop)
```

+++ {"tags": []}

### Setting the time resolution (optional)
The `set_time_resolution` function also specified the `timeunit` as `'hour'`. SHOP formulates an optimization model with discrete time steps. The default step size is given by the time unit. We can also use timeunit `'minutes'` and set the `timeresolution` to 60 as shown in the example below which is equivalent with hourly resolution. The `timeresolution` argument also enables variable step size in the model, for example, smaller step size in the first hours.

```{code-cell} ipython3
shop.set_time_resolution(starttime=starttime, endtime=endtime, timeunit='minute', timeresolution=pd.Series([60], index=[starttime]))
```

### Creating objects
All model building related features are located on the `model` object that is a sub-object of the `ShopSession`. pySHOP offers convenient typing help as shown in the video. Try it yourself below by typing `shop.model.` followed by the `tab` key.

```{code-cell} ipython3
shop.model
```

A SHOP model comprises multiple objects, both physical objects in the watercourse like reservoirs, plants and generators as well as more abstract objects types like markets and discharge_groups. Create a new `reservoir` by executing the code below.

```{code-cell} ipython3
rsv1 = shop.model.reservoir.add_object('Rsv1')
```

#### Excercise
Complete the code below to create a minimal working example:
- create a `plant` named `'Plant1'`
- create a `generator` named `'Plant1_G1'`

```{code-cell} ipython3
# plant1 = shop.model.plant.add_object(___)
# ___

## REMOVE
plant1 = shop.model.plant.add_object('Plant1')
gen1 = shop.model.generator.add_object('Plant1_G1')

check_plant_and_generator_added(shop)
```

### Connecting objects
Model relations are used both to connect the objects in the water course and to group objects logically. Execute the code below to connect your `reservoir` named `Rsv1` to the downstream `plant` named `Plant1`.

```{code-cell} ipython3
rsv1.connect_to(plant1)
```

In the case above, the objects we are connecting are stored in the variables `rsv1` and `plant1` respectively. Alternatively, you can also look up the objects directly in SHOP. The following code lines are all equivalent with the code we just executed:
```python
shop.model.reservoir.Rsv1.connect_to(shop.model.plant.Plant1)
shop.model.reservoir['Rsv1'].connect_to(shop.model.plant['Plant1'])
```

The `['<ObjectName>']` syntax is a alternative to `.<ObjectName>` in situations where the object name contains characters that has a special meaning in Python such as `-()`, or if you are looking up as a part of a for-loop.

+++

#### Exercise
Complete the code below by connecting your `generator` and `plant` with your preferred code syntax.

```{code-cell} ipython3
# ***.connect_to(***)

## REMOVE
shop.model.generator.Plant1_G1.connect_to(plant1)

check_plant_and_generator_connected(shop)
```

### Drawing topology
Once your model is built, you can use the topology builder to visualize it. Exececute the code below to verify that the reservoir and plant has been connected correctly.

```{code-cell} ipython3
shop.model.build_connection_tree()
```

### Setting model attributes
The different objects in SHOP are parameterized through different attributes. You can use pySHOP to view all available attributes for the respective object types. Execute the code below to list all available attribute types for `reservoir`. Repeat for `plant`.

```{code-cell} ipython3
shop.model.reservoir.get_attribute_names()
```

You can also get more detailed info about the respective attributes. Exectue the code below to show information about the `reservoir` attribute `lrl`. To create a minimal running example, we will set the attributes `lrl`, `hrl`, `max_vol`, `vol_head`, `flow_descr` and `inflow`. Check the information for each of these yourself.

```{code-cell} ipython3
shop.model.reservoir.Rsv1.lrl.info()
```

Each attribute is one of the following datatypes: int, int_array, double, double_array, txy (timeseries), xy (table), xy_array (list of tables), string, string_array, sy (table where the first column is a string). We use the `set()` function to set attribute values in SHOP.

#### Exercise
Run the code below to set the reservoir `hrl`. Complete the code and set the values according to the table below:
|Object|Attribute         |Value|
|------|------------------|-----|
|Rsv1  |lrl               |860  |
|Rsv1  |start_head        |900  |
|Rsv1  |energy_value_input|30   |
|Plant1|outlet_line       |670  |

```{code-cell} ipython3
shop.model.reservoir.Rsv1.hrl.set(905)

## REMOVE
shop.model.reservoir.Rsv1.lrl.set(860)
shop.model.reservoir.Rsv1.start_head.set(900)
shop.model.reservoir.Rsv1.energy_value_input.set(30)
shop.model.plant.Plant1.outlet_line.set(670)

check_attribute_values1(shop)
```
