# treeThinking

```
The free-thinking of one's age is the common sense of the next. -Matthew Arnold
```

`treeThinking` was inspired by the desire to convert the output of `sklearn`'s `DecisionTreeClassifier` models into something more useful.

This project and schema emerged from conversations with [@greggroth](https://github.com/greggroth) at [Blue Bottle Coffee](https://github.com/bluebottlecoffee).

## The need for schema

Serializing a decision tree is relatively straightforward, and in fact, extremely ad-hoc. The need for a schema is in anticipation of the integration with other systems. For this reason we outline a general spec which lends itself to customization, but provides a scaffold for the basic logic.

### Reading the YAML

The YAML is a straightforward presentation of the tree with a few convenient structural choices.

```
---
class_name: 'Likes chocolate icecream'
features:
  - name: 'Likes ice cream'
    type: 'binary'
  - name: 'Likes chocolate'
    type: 'binary'
  - name: 'how much do you like ice cream'
    type: 'continuous'
    min: 0
    max: 5
    step: 1
nodes:
  feature_idx: 0
  op: =
  thr: 1
  prob: nil
  results:
    true:
      feature_idx: 1
      op: >
      thr: 0.5
      prob: nil
      results:
        true:
          feature_idx: nil
          op: nil
          thr: nil
          prob: 1
          results: []
        false:
          feature_idx: nil
          op: nil
          thr: nil
          prob: 0
          results: []
    false:
      feature_idx: nil
      op: nil
      thr: nil
      prob: 0
      results: []
```

Which can be seen as a struct:
```
---
class_name: <str>
features:
  - name: <str>
    type: <str> ('opt')('binary', 'continuous')
    min: <float> ('opt')
    max: <float> ('opt')
    step: <float> ('opt')
nodes:
  feature_idx: <int>
  thr: <float>
  op: <str> (opt)
  results:
    true:
      feature_idx: <int> (opt)
      thr: <float> (opt)
      op: <str> (opt)
      prob: <float> (opt)
      results:
        true: <node> (opt)
        false: <node> (opt)
    false:
      feature_idx: <int> (opt)
      thr: <float> (opt)
      op: <str> (opt)
      prob: <float> (opt)
      results:
        true: <node> (opt)
        false: <node> (opt)
```

Noting the optional fields one can create our ice-cream tree a bit less verbosely:
```
---
class_name: 'Likes chocolate icecream'
features:
  - name: 'Likes ice cream'
  - name: 'Likes chocolate'
  - name: 'how much do you like ice cream'
    min: 0
    max: 5
    step: 1
nodes:
  feature_idx: 0
  op: =
  thr: 1
  results:
    true:
      feature_idx: 1
      op: >
      thr: 0.5
      results:
        true:
          prob: 1
        false:
          prob: 0
    false:
      prob: 0
```

Where `class_name` is the name of the class label you're attempting to assign. `feature_idx` refers to the feature index(names are presented in order under the `features` list), `thr` is the break boundary for this decision, `op` is a purely optional parameter that can be specified if you want to use other comperators than `<=`(pandas DTs are always `<=`). Results are a list of nodes, with the defaults being `true` is where the function recurses if the comparison is true, likewise for `false`. `prob` is the resulting probability of assigning the class label based on the node's purity.

## Usage

If you're using `sklearn` and want to output your models, under the Python directory is a module for reading and writing YAML in the above format.

One can also use the above schema as a guideline for writing decision tree logic in an extensible way.

## The name

Not sorry for the bad pun. Am sorry I didn't go with `Lorax`, but copyright, y'know? `¯\_(ツ)_/¯`

## Contributing

Bug reports and pull requests are welcome on GitHub at [https://github.com/bluebottlecoffee/eatl](https://github.com/bluebottlecoffee/eatl). This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org/) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
