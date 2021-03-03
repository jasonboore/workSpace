import tensorflow as tf


def tensorflow_demo():
    """
    Tensorflow的基本结构
    :return:
    """
    tf.compat.v1.disable_eager_execution()#保证sess.run()能够正常运行
    a = tf.constant(1)
    b = tf.constant(4)
    c = a + b
    # 开启会话
    with tf.compat.v1.Session() as sess:
        # sess= tf.compat.v1.Session()#版本2.0的函数
        print(sess.run(c))
    return None

if  __name__ == "__main__":
    tensorflow_demo()