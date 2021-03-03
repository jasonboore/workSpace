import tensorflow as tf

# 1) 定义命令行参数
tf.compat.v1.disable_eager_execution()
tf.compat.v1.app.flags.DEFINE_integer("max_step", 100, "训练模型的步数")
tf.compat.v1.app.flags.DEFINE_string("model_dir", "Unknown", "模型保存的路径+模型名字")

# 2) 简化变量名
FLAGS = tf.compat.v1.app.flags.FLAGS
def comand_demo():
    """
    命令行参数演示
    :return:
    """
    print("max_step:\n", FLAGS.max_step)
    print("model_dir:\n", FLAGS.model_dir)



def main(argv):
    print(argv)
    return None
if __name__ == '__main__':
    comand_demo()
    tf.compat.v1.app.run()