# treeThinking

```
The free-thinking of one's age is the common sense of the next. -Matthew Arnold
```

`treeThinking` is intended to be a simple tool for converting the output of `sklearn`'s Decision Tree models into something more useful.

## `treeThinking` is not:
- If your intention with DT is to simply build a classifier on your training data, and then run it on your full dataset, you could simply run it against the model that you build.
- If you want to create an API to query the DT for classifing requests, use something like Django or Flask, and build a little API server that uses the model.

## Use cases:

However, you may want to train your model, and then convert that model into something more language agnostic for integration with some other system. Or, simply serialize your model in a nice readable form.

Another interesting use-case is for an evolutiary model, with intermittent backups. This provides a simple serialization that you can dump, and always return to.

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

### Read the YAML

_depends on `YAML` and `random`._

The YAML is a straightforward presentation of the tree with a few convenient structural choices.

```
---
- class_name: str
  features:
    - str
    - str
  tree:
    idx: int
    thr: float
    op: str (opt)
    true_tree:
      idx: int (opt)
      thr: float (opt)
      op: str (opt)
      prob: float (opt)
      true_tree: tree (opt)
      false_tree: tree (opt)
    false_tree:
      idx: int (opt)
      thr: float (opt)
      op: str (opt)
      prob: float (opt)
      true_tree: tree (opt)
      false_tree: tree (opt)
```

Where `class_name` is the name of the class label you're attempting to assign. `idx` refers to the feature index(names are presented in order under the `features` list), `thr` is the break boundary for this decision, `op` is a purely optional parameter that can be specified if you want to use other comperators than `<=`(pandas DTs are always `<=`). `true_tree` is where the function recurses if the comparison is true, likewise for `false_tree`. `prob` is the resulting probability of assigning the class label based on the node's purity.

<!-- Which you could think of as the following decision tree: -->



### Use the YAML

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

The `lorax.ipynb` has a worked example for the Titanic dataset. It is probably the fastest way to see this module in use..

## The name

Not sorry for the bad pun. Am sorry I didn't go with `Lorax`, but copyright, y'know? `¯\_(ツ)_/¯`
