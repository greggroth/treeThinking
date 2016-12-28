# The Ruby Gem

The ruby gem currently supports loading and applying a YAML decision tree.  The
following example is from the tests and shows how a YAML fixture file is parsed
into a `BinaryTree` object:

```ruby
tree = TreeThinking::BinaryTreeFactory.from_yaml('./spec/fixtures/simple_tree.yaml')
```

This tree can then be used to get a probability from an answer vector:

```ruby
tree.call([1, 0])
#> 0.1
```

In this case, the answer vector is `[1,0]`, however another approach that can
be used is a `Struct` where the attribute order matches the order of the
features in the decision tree.  For example:

```ruby
Answer = Struct.new(:likes_ice_cream, :likes_chocolate)
answer_vector = Answer.new(1,0)
tree.call(answer_vector)
#> 0.1
```
