# -*- coding: utf-8 -*-
import argparse
import os
import sys
from os.path import isdir, join

import pytest


def list_dirs(path):
    """列出path目录下的文件夹"""
    ret = []
    for ele in os.listdir(path):
        p = ele if path == "." else join(path, ele)
        if isdir(p) and not ele.startswith(".") and not ele.startswith("_"):
            ret.append(p)
    return ret


def ignores(parent, *sub):
    """生成需要忽略的目录"""
    len_max = max([len(su) for su in sub])  # 路径深度
    for i in range(len_max):
        dirs_v2 = set()  # 当前层级下的路径集合
        remove_list = set()  # 需要移出的路径
        for su in sub:
            if i + 1 <= len(su):
                dirs_v2 = dirs_v2 | set(list_dirs(join(parent, *su[:i])))
                remove_list.add(join(parent, *su[:i + 1]))
        for remove_path in remove_list:
            try:
                dirs_v2.remove(remove_path)
            except KeyError as e:
                raise KeyError("check your path: %s" % e)
        yield dirs_v2


def dpath_to_lists(dpath):
    """将目录字符串转换成list对象"""
    return list(map(lambda s: s.strip().strip("/").split("/"), dpath.split(",")))


parser = argparse.ArgumentParser()
# parser.add_argument("--env",
#                     dest="env",
#                     action="store",
#                     default='',
#                     type=str,
#                     help="用于指定不同的测试环境")
# parser.add_argument("--suites",
#                     dest="suites",
#                     action="store",
#                     type=str,
#                     help="用于指定执行哪些目录下的用例（可包含子目录），多个目录用`,`分割, eg: --suites app,infrastructure")
# parser.add_argument("--ignores",
#                     dest="ignores",
#                     action="store",
#                     default="wish_bottle",
#                     type=str,
#                     help="用于指定忽略哪些目录下的用例，多个目录用`,`分割, eg: --ignores app_room,web_room")
# parser.add_argument("--tag",
#                     dest="tag",
#                     action="store",
#                     type=str,
#                     help='要执行的用例标签，eg: --tag "smoke and FAT8"')

args, other_args = parser.parse_known_args()

if args.tag:
    sys.argv.append('-m ' + args.tag)

# if args.env != config.env:  # 设置测试环境
#     config.env = config.global_env = args.env

sys.argv = [sys.argv[0]]
sys.argv.extend(other_args)

if args.suites:
    data = dpath_to_lists(args.suites)
    for ds in ignores("cases", *dpath_to_lists(args.suites)):
        for d in ds:
            opt = "--ignore={}".format(d)
            sys.argv.append(opt)

if args.ignores:
    for d in args.ignores.split(","):
        opt = "--ignore=cases/{}".format(d)
        sys.argv.append(opt)

# sys.argv.append("cases")
pytest.main()
