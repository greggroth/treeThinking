# The Python module

The original motivation of `treeThinking` was motivated by the process of converting the output of `sklearn`'s `DecisionTreeClassifier` into something that I could simply build into some other logic. Alas, there isn't a convenient way to serialize this(don't say `dot`, that's not what I mean). This grew into the parent directory, i.e. specifying a YAML format that is language agnostic, extensible, yadda-yadda, with heavy input from [@greggroth](https://github.com/greggroth).

That YAML format is the real contribution, but for the purpose of solving the original problem, here is a Python module!

## `treeThinking` is not:
- If your intention with DT is to simply build a classifier on your training data, and then run it on your full dataset, you could simply run it against the model that you build.
- If you want to create an API to query the DT for classifing requests, use something like Django or Flask, and build a little API server that uses the model.

## Use cases:

However, you may want to train your model, and then convert that model into something more language agnostic for integration with some other system. Or, simply serialize your model in a nice readable form.

Another interesting use-case is for an evolutionary model, with intermittent backups. This provides a simple serialization that you can dump, and always return to.

## How to use:

### Write the YAML

_depends on `numpy`._

`treeThinking` is a Python module to walk the DT and write a YAML file.

```
from treeThinking import writeTreeYaml
```

and then call it as such

```
writeTreeYaml(tree, feature_list, label)
```

which will return a string that you'll write to a YAML file. Note that `YAML` is not required for the writing at all.

### Use the YAML

_depends on `YAML` and `random`._

The intention of treeThinking is not to write modules in various languages to read these YAMLs. But who am I kidding, somebody has to start somewhere. Here is a really basic example of how one can use these YAML trees.

```
from treeThinking import yamlSwitch
```

and then call it as such

```
yamlSwitch(vector, ytree, label)
```

which will output a binary determined by walking the tree. I encourage you to peek at this function to see the workings here.

## Examples:

The `lorax.ipynb` has a worked example for the Titanic dataset. It is probably the fastest way to see this module in use.

## Contributing

It would be nice to extend this module to handle multi-label classification. Also welcome to improvements to this module which I designed to be simple.
