import tensorflow as tf

def session_demo():
    tf.compat.v1.disable_eager_execution()  # 保证sess.run()能够正常运行
    a = tf.constant(1, name='a')
    b = tf.constant(4, name='b')
    print("a：\n", a)
    print("b：\n", b)
    c = tf.add(a, b, name='c')
    print("c：\n", c)
    # 查看默认图
    # 方法1：调用方法
    default_g = tf.compat.v1.get_default_graph()
    print("default_g:\n", default_g)

    # 方法2：查看属性
    print("a的图属性：\n", a.graph)
    print("b的图属性：\n", b.graph)
    print("c的图属性：\n", c.graph)
    print('-' * 30)

    with tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(allow_soft_placement=True,
                                                              log_device_placement=True)) as sess:
        # sess= tf.compat.v1.Session()#版本2.0的函数
        c_value = sess.run(c)
        abc = sess.run([a, b, c])
        a_t, b_t, c_t = sess.run([a, b, c])
        print("abc:\n", abc)
        print("abc:\n", a_t, b_t, c_t)
        print(a.eval())
        print("c_value.eval()：\n", c.eval())
        print("c_value：\n", c_value)
        print("sess的图属性：", sess.graph)
        # 1) 将图写入本地生成events文件
        tf.compat.v1.summary.FileWriter("./tmp/summary", graph=sess.graph)
    return None

def session_run_demo():
    """
    会话的run方法
    :return:
    """
    # 定义占位符
    tf.compat.v1.disable_eager_execution()
    a = tf.compat.v1.placeholder(tf.float32)
    b = tf.compat.v1.placeholder(tf.float32)
    sum_ab = tf.add(a, b)
    print("a:\n", a)
    print("b:\n", b)
    print("sum_ab:\n", sum_ab)
    with tf.compat.v1.Session() as sess:
        print("占位符的结果：\n", sess.run(sum_ab, feed_dict={a: 3.0, b: 4.0}))
if __name__ == '__main__':
    session_demo()
    # session_run_demo()