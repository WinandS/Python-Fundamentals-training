import re
import importlib

def build_test_skeleton(input_file, output_file):
    module = input_file[:input_file.index(".py")]
    mod=importlib.import_module(module)
    # print(mod)
    pattern = re.compile("__.+__")
    dir_list = list(dir(mod))
    # print(dir_list)

    with open(output_file, 'w+') as outf:
        outf.writelines(["import unittest\n", "import {module}\n".format(module=module), "\n",
                        "class Test_{module_name}(unittest.TestCase):\n".format(module_name=module)])
        for el in dir_list:
            if not pattern.match(el):
                outf.writelines(["\tdef test_{function_name}(self):\n".format(function_name=el),
                                "\t\tself.assetTrue(False)\n"])
        outf.write("unittest.main()\n")

build_test_skeleton("temperature.py", "temperature_test_gen.py")
