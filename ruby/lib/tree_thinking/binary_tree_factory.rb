require 'yaml'

module TreeThinking
  class BinaryTreeFactory
    attr_reader :tree

    def self.from_yaml(path)
      new(YAML.load(File.read(path))).build!
    end

    def initialize(tree)
      @tree = tree
    end

    def build!
      btree = BinaryTree.new(name: tree['class_name'])
      btree.tree = nodify(tree['tree'])
      btree
    end

    private

    def nodify(attrs)
      BinaryTree::Node.new(
        attrs['feature_idx'],
        attrs['op'],
        attrs['thr'],
        attrs['prob'],
        Hash[attrs.fetch('results', {}).map do |return_val, child_node|
          [return_val, nodify(child_node)]
        end]
      )
    end
  end
end
