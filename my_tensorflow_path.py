# tensorflowライブラリのパスを出力
import os
import inspect
import tensorflow

print(os.path.dirname(inspect.getfile(tensorflow)))