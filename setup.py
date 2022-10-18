# coding=utf-8
# Copyright 2021 Reranker Author. All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup, find_packages

setup(
    name='RetroMAE',
    version='0.0.1',
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        'torch>=1.6.0',
        'transformers>=4.18.0',
        'datasets==1.18.3',
        'faiss-gpu>=1.6'
    ],
)
