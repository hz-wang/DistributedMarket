#!/bin/bash

hadoop fs -mkdir /user/root/mnist
hadoop fs -mkdir /user/root/mnist/input
hadoop fs -mkdir /user/root/mnist/input/data
hadoop fs -copyFromLocal mnist/code/ /user/root/mnist/input/
hadoop fs -copyFromLocal mnist/mnist.zip /user/root/mnist/input/data/

hadoop fs -mkdir /user/root/mnist/output