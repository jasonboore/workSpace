import tensorflow as tf
import os

def linear_regration():
    tf.compat.v1.disable_eager_execution()
    # 1.准备数据
    with tf.compat.v1.variable_scope("prepare_data"):
        X = tf.compat.v1.random_normal(shape=(1000, 1), name="data")
        y_true = tf.matmul(X, [[0.8]]) + 0.7

    # 2.构造模型
    with tf.compat.v1.variable_scope("create_model"):
        weights = tf.Variable(initial_value=tf.compat.v1.random_normal(shape=(1, 1)), name="Weight")
        bias = tf.Variable(initial_value=tf.compat.v1.random_normal(shape=(1, 1)), name="Bias")
        y_predict = tf.matmul(X, weights) + bias

    # 3.构造误差函数
    with tf.compat.v1.variable_scope("cost_function"):
        error = tf.reduce_mean(tf.square(y_true - y_predict))

    # 4.优化误差
    with tf.compat.v1.variable_scope("optimizer"):
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.01).minimize(error)

    # 2_收集变量
    tf.compat.v1.summary.scalar("error", error)
    tf.compat.v1.summary.histogram("weight", weights)
    tf.compat.v1.summary.histogram("bias", bias)

    # 3_合并变量
    merged = tf.compat.v1.summary.merge_all()

    # 显示初始化变量
    init = tf.compat.v1.global_variables_initializer()

    with tf.compat.v1.Session() as sess:
        # 初始化变量
        sess.run(init)

        # 1_创建事件文件
        file_writer = tf.compat.v1.summary.FileWriter('./tmp/linear', sess.graph)

        # 创建Saver对象
        saver = tf.compat.v1.train.Saver()
        # 查看初始化模型参数后的值
        print("训练前模型参数为：权重{}, 偏置{}, 误差{}".format(weights.eval(), bias.eval(), error.eval()))

        for i in range(1000):
            sess.run(optimizer)
            print("训练后模型参数为：权重{}, 偏置{}, 误差{}".format(weights.eval(), bias.eval(), error.eval()))

            # 运行合并变量操作
            summer = sess.run(merged)
            file_writer.add_summary(summer, i)

            # 保存模型
            if i % 10 == 0:
                saver.save(sess, './tmp/model/my_linear.ckpt')
        # 加载模型
        # if os.path.exists("./tmp/model/checkpoint"):
        #     saver.restore(sess, "./tmp/model/my_linear.ckpt")
        # print("训练后模型参数为：权重{}, 偏置{}, 误差{}".format(weights.eval(), bias.eval(), error.eval()))

    return None


if __name__ == '__main__':
    linear_regration()
