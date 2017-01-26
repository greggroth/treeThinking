require 'spec_helper'

describe TreeThinking::BinaryTree do
  subject(:tree) { TreeThinking::BinaryTreeFactory.from_yaml('./spec/fixtures/simple_tree.yaml') }

  describe '#call' do
    it 'returns a probablity from an answer vector' do
      expect(tree.call([1, 0])).to eq(0.1)
      expect(tree.call([1, 1])).to eq(0.8)
    end
  end

  context 'with a tree with key indicies' do
    subject(:tree) { TreeThinking::BinaryTreeFactory.from_yaml('./spec/fixtures/key_tree.yaml') }

    describe '#call' do
      it 'returns a probablity from an answer vector' do
        expect(tree.call({'likes_ice_cream' => 1, 'likes_chocolate' => 0})).to eq(0.1)
        expect(tree.call({'likes_ice_cream' => 1, 'likes_chocolate' => 1})).to eq(0.8)
      end
    end
  end
end
