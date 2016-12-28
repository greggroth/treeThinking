require 'spec_helper'

describe TreeThinking::BinaryTree do
  subject(:tree) { TreeThinking::BinaryTreeFactory.from_yaml('./spec/fixtures/simple_tree.yaml') }

  describe '#call' do
    it 'returns a probablity from an answer vector' do
      expect(tree.call([1, 0])).to eq(0.1)
      expect(tree.call([1, 1])).to eq(0.8)
    end
  end
end
