require 'pry'
require './lib/binary_tree_factory'
require './lib/binary_tree'

describe BinaryTreeFactory do
  describe '::from_yaml' do
    it 'create a BinaryTree from a YAML file' do
      tree = described_class.from_yaml('./spec/fixtures/simple_tree.yaml')
      expect(tree).to be_kind_of(BinaryTree)
    end
  end
end

describe BinaryTree do
  subject(:tree) { BinaryTreeFactory.from_yaml('./spec/fixtures/simple_tree.yaml') }

  it 'returns a probablity from an answer vector' do
    expect(tree.call([1, 0])).to eq(0.1)
    expect(tree.call([1, 1])).to eq(0.8)
  end
end
