#! /usr/bin/env python

import Gen.caffe_pb2 as pb2
import google.protobuf.text_format as pb2_text
import sys

class ParameterTypeException(Exception): pass

def binary_to_text(binary_file, text_file, parameter_type):
    if (parameter_type == "Net"):
        msg = pb2.NetParameter()
    elif (parameter_type == "Solver"):
      msg = pb2.SolverParameter()
    else:
        raise ParameterTypeException("Unexpected Parameter Type: " + parameter_type)

    with open(binary_file) as f:
        msg.ParseFromString(f.read())

    with open(text_file, "w") as f:
        f.write(pb2_text.MessageToString(msg))

if __name__ == "__main__":
    binary_file = sys.argv[1]
    text_file = sys.argv[2]
    try:
      parameter_type = sys.argv[3]
    except IndexError:
      parameter_type = "Net"
    binary_to_text(binary_file, text_file, parameter_type)
