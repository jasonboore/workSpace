import tensorflow as tf

"""
张量（n维数组）
"""


def tensor_demo():
    """
    张量的演示
    :return:
    """
    tf.compat.v1.disable_eager_execution()
    tensor1 = tf.constant(4.0)
    tensor2 = tf.constant([1, 2, 3, 4])
    linear_squares = tf.constant([[4], [9], [16], [25]], dtype=tf.int32)
    print("tensor1:\n", tensor1)
    print("tensor2:\n", tensor2)
    print("linear_squares:\n", linear_squares)
    print('-' * 30)
    zeros = tf.zeros(shape=(3, 4))
    print(zeros)
    print('-' * 30)
    ones = tf.ones(shape=(4, 3, 2))
    print(ones)
    print('-' * 30)
    random_normal = tf.compat.v1.random_normal(shape=(2, 3), mean=1.75, stddev=0.2)
    print(random_normal)
    print('-' * 30)

    # 张量的变换
    # 张量类型的修改
    l_cast = tf.cast(linear_squares, dtype=tf.float32)
    print("l_cast:\n", l_cast)
    print('-' * 30)

    # 张量形状的改变
    # 改变/更新静态形状（只有在形状没有完全固定下来的情况下）
    # 没有完全固定下来的静态形状
    a_p = tf.compat.v1.placeholder(tf.float32, shape=[None, None])
    b_p = tf.compat.v1.placeholder(tf.float32, shape=[None, 10])
    c_p = tf.compat.v1.placeholder(tf.float32, shape=[3, 2])
    print("a_p:\n", a_p)
    print("b_p:\n", b_p)
    print("c_p:\n", c_p)
    print('-' * 30)
    # 更新未确定的部分
    a_p.set_shape([2, 3])
    b_p.set_shape([2, 10])
    print("更新形状后的a_p:\n", a_p)
    print("更新形状后的b_p:\n", b_p)
    print('-' * 30)

    # 改变动态形状
    a_p = tf.compat.v1.placeholder(tf.float32, shape=[None, None])
    b_p = tf.compat.v1.placeholder(tf.float32, shape=[None, 10])
    c_p = tf.compat.v1.placeholder(tf.float32, shape=[3, 2])

    a_p_reshape = tf.reshape(a_p, shape=[2, 3, 1])
    print("a_p:\n", a_p)
    print("a_p_reshape:\n", a_p_reshape)
    print('-' * 30)
    # 不能更改原有张量中元素的数量
    # c_p_reshape = tf.reshape(c_p, shape=[3, 3])
    c_p_reshape = tf.reshape(c_p, shape=[2, 3, 1])
    print("c_p:\n", c_p)
    print("c_p_reshape:\n", c_p_reshape)

    zeros = tf.zeros(shape=(3, 4))
    zeros_reshape = tf.reshape(zeros, shape=[2,6])
    print("zeros_reshape:\n", zeros_reshape)
    return None


if __name__ == '__main__':
    tensor_demo()
