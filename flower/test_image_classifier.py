import tensorflow as tf
import numpy as np


tf.app.flags.DEFINE_string('model_dir','frozen_vgg_16.pb','Path for graph directory containing pb file')
FLAGS = tf.app.flags.FLAGS

def create_graph():
  """Creates a graph from saved GraphDef file and returns a saver."""
  # Creates graph from saved graph_def.pb.
  print FLAGS.model_dir
  with tf.gfile.FastGFile('vgg_frozen.pb', 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')


def main(_):
    print("Testing Image Classifier")
    model_fn = 'frozen_vgg_16fc8squeezed_summaryop.pb'
    graph = tf.Graph()
    sess = tf.InteractiveSession(graph=graph)
    with tf.gfile.FastGFile(model_fn, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    #create_graph()
    layers = [op.name for op in graph.get_operations() if op.type == 'Conv2D' and 'vgg_16/' in op.name]
    feature_nums = [int(graph.get_tensor_by_name(name + ':0').get_shape()[-1]) for name in layers]
    print('Number of layers', len(layers))
    print('Total number of feature channels:', sum(feature_nums))

    #for op in graph.get_operations():
    #   print(op.name + "   type:  " + op.type)
    for name in layers:
        print name



if __name__=='__main__':
    tf.app.run()