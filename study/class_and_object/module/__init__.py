from study.class_and_object.module import test_module as test
import pprint
import os

print(test)
# __name__属性值为__main__
# __main__是主模块，一个程序只有一个主模块
print(test.__name__)
print(__name__)

pprint.pp(os.environ['path'])
