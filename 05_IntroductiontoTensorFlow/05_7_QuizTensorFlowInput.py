# Solution is available in the other "solution.py" tab
import tensorflow as tf


def run():
    output = None
    x = tf.placeholder(tf.int32)
    # y = tf.placeholder(tf.int32)
    # z = tf.placeholder(tf.float32)
    with tf.Session() as sess:
        # TODO: Feed the x tensor 123
        output = sess.run(x, feed_dict={x: 123})
        # print output
    return output
