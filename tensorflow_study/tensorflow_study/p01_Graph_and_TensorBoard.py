import tensorflow as tf

def graph_demo():
    """
    图的演示
    :return:
    """
    tf.compat.v1.disable_eager_execution()#保证sess.run()能够正常运行
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

    with tf.compat.v1.Session() as sess:
        # sess= tf.compat.v1.Session()#版本2.0的函数
        c_value = sess.run(c)
        print(a.eval())
        print("c_value.eval()：\n", c.eval())
        print("c_value：\n", c_value)
        print("sess的图属性：", sess.graph)
        # 1) 将图写入本地生成events文件
        tf.compat.v1.summary.FileWriter("./tmp/summary", graph=sess.graph)

        ## 在命令行中输入
        ## tensorboard --logdir="./tmp/summary"
        ## 然后打开浏览器


    # 自定义图
    new_g = tf.Graph()
    # 在自己的图中定义数据和操作
    with new_g.as_default():
        a_new = tf.constant(20)
        b_new = tf.constant(30)
        c_new = a_new + b_new
        print("c_new:\n", c_new)
        print("a_new：\n", a_new)
        print("b_new：\n", b_new)
        print("c_new：\n", c_new)
        print("a_new的图属性：\n", a_new.graph)
        print("b_new的图属性：\n", b_new.graph)
        print("c_new的图属性：\n", c_new.graph)
    # 开启new_g的会话
    with tf.compat.v1.Session(graph=new_g) as sess:
        # sess= tf.compat.v1.Session()#版本2.0的函数
        c_new_value = sess.run(c_new)
        print("c_new_value的图属性：\n", c_new_value)
        print("sess的图属性：", sess.graph)
        print('-' * 30)

    # 操作
    # 常量操作
    con_a = tf.constant(3.0)
    con_b = tf.constant(4.0)
    # 加法操作
    sum_c = tf.add(con_a, con_b)

    print("打印con_a:\n", con_a)
    print("打印con_b:\n", con_b)
    print("打印sum_c:\n", sum_c)

    return None


if __name__ == "__main__":
    graph_demo()
