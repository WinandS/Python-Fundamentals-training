import importlib
import inspect


def build_test_skeleton(input_file, output_file):
    module = input_file[:input_file.index(".py")]
    mod = importlib.import_module(module)
    dir_list = inspect.getmembers(mod, inspect.isfunction)

    with open(output_file, 'w+') as outf:
        outf.writelines(["import unittest\n", "import {module}\n".format(module=module), "\n",
                         "class Test_{module_name}(unittest.TestCase):\n".format(module_name=module)])
        for el in dir_list:
            outf.writelines(["\tdef test_{function_name}(self):\n".format(function_name=el),
                             "\t\tself.assetTrue(False)\n"])
        outf.write("unittest.main()\n")

build_test_skeleton("temperature.py", "temperature_test_gen.py")
