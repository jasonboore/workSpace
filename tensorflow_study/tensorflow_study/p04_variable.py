import tensorflow as tf

def variale_demo():
    """
    变量的演示
    :return:
    """
    tf.compat.v1.disable_eager_execution()
    # 创建变量
    # 修改命名空间
    with tf.compat.v1.variable_scope("my_scope"):
        a = tf.Variable(initial_value=50)
        b = tf.Variable(initial_value=40)
    with tf.compat.v1.variable_scope("another_scope"):
        c = tf.add(a, b)
    print("a:\n", a)
    print("b:\n", b)
    print("c:\n", c)

    # 初始化变量
    init = tf.compat.v1.global_variables_initializer()
    # 开启会话
    with tf.compat.v1.Session() as sess:
        # 运行初始化
        sess.run(init)
        a_value, b_value, c_value = sess.run([a, b, c])
        print("a_value:\n", a_value)
        print("b_value:\n", b_value)
        print("c_value:\n", c_value)




    return None

if __name__ == '__main__':
    variale_demo()