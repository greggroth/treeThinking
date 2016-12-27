'''
treeThinking module https://github.com/BBischof/treeThinking
originally based on http://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html
'''

import numpy as np
import random

def writeTreeYaml(tree, feature_list, label):
    n_nodes = tree.tree_.node_count
    children_left = tree.tree_.children_left
    children_right = tree.tree_.children_right
    feature = tree.tree_.feature
    threshold = tree.tree_.threshold
    value = tree.tree_.value
    '''We will write the YAML line by line as we walk the tree.'''
    out = ("---\n")
    out += ("- " + "class_name: '%s'\n" % label)
    out += ("  " + "features:\n")
    for f in feature_list:
      out += ("    - " + "'%s'\n" % f)
    out += ("  " + "tree:\n")
    node_depth = np.zeros(shape=n_nodes)
    is_leaves = np.zeros(shape=n_nodes, dtype=bool)
    stack = [(0, -1)]  # seed is the root node id and its parent depth
    while len(stack) > 0:
        node_id, parent_depth = stack.pop()
        node_depth[node_id] = parent_depth + 1
        if (children_left[node_id] != children_right[node_id]):
            stack.append((children_left[node_id], parent_depth + 1))
            stack.append((children_right[node_id], parent_depth + 1))
        else:
            is_leaves[node_id] = True
    for i in range(n_nodes):
        if i in children_left:
            out += ("%strue_tree: \n" % ((node_depth[i]+1) * "  "))
        if i in children_right:
            out += ("%sfalse_tree: \n" % ((node_depth[i]+1) * "  "))
        if is_leaves[i]:
            out += ("%sprob: %s\n" % ((node_depth[i]+2) * "  ", ((value[i][0][1]/(value[i][0][1]+value[i][0][0])))))
        else:
            out += ("%sidx: %s\n" % ((node_depth[i]+2) * "  ",feature[i]))
            out += ("%sthr: %s\n" % ((node_depth[i]+2) * "  ",threshold[i]))
    return out

def yamlSwitch(vector, ytree, label):
    if 'idx' in ytree.keys() and 'thr' in ytree.keys():
        if 'op' not in ytree.keys():
            if vector[ytree['idx']] <= ytree['thr']:
                return yamlSwitch(vector,ytree['false_tree'], label)
            else:
                return yamlSwitch(vector,ytree['true_tree'], label)
        else:
            ops = {"<=": (lambda x,y: x<=y),
                   ">=": (lambda x,y: x>=y),
                   "<": (lambda x,y: x<y),
                   ">": (lambda x,y: x>y),
                   "=": (lambda x,y: x==y),
                   "!=": (lambda x,y: x!=y),
                   "<>": (lambda x,y: x!=y)}
            if ytree['op'] in ops.keys():
              if ops[ytree['op']](vector[ytree['idx']], ytree['thr']):
                  return yamlSwitch(vector,ytree['false_tree'], label)
              else:
                  return yamlSwitch(vector,ytree['true_tree'], label)
            else:
                raise ValueError('Unallowed operator')
    elif 'prob' in ytree.keys():
        x = 1 if random.random() <= ytree['prob'] else 0
        return (label, x)
    else:
        raise ValueError('YAML tree inappropriate format')

