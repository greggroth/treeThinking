require 'spec_helper'

describe TreeThinking::BinaryTreeFactory do
  describe '::from_yaml' do
    it 'create a BinaryTree from a YAML file' do
      tree = described_class.from_yaml('./spec/fixtures/simple_tree.yaml')
      expect(tree).to be_kind_of(TreeThinking::BinaryTree)
    end
  end
end

