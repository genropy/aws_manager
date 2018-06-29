#!/usr/bin/python
# -*- coding: UTF-8 -*-

def config(root,application=None):
    aws = root.branch('AWS')
    aws.thpage('ec2_instance',table='aws.ec2_instance')
