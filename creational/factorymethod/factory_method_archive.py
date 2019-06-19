#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""factory_method_archive.py"""

import os
from zipfile import ZipFile
import tarfile

class BaseArchive(object):
    EXTENSION = None
    def __init__(self, location_path, files_to_pack):
        self.location_path = location_path
        self.files_to_pack = files_to_pack
    def generate(self): raise NotImplementedError()
    @classmethod
    def check_extenstion(cls, extension):
        return extension == cls.EXTENSION

class ZIPArchive(BaseArchive):
    EXTENSION = '.zip'
    def generate(self):
        with ZipFile('{}{}'.format(self.location_path, self.EXTENSION), 'w') as zip_file:
            for file_ in self.files_to_pack:
                zip_file.write(file_)

class TARArchive(BaseArchive):
    EXTENSION = '.tar'
    def generate(self):
        with tarfile.open('{}{}'.format(self.location_path, self.EXTENSION), 'w') as tar_file:
            for file_ in self.files_to_pack:
                tar_file.add(file_)

class ArchiveManager(object):
    ARCHIVE_ENGINES = [ZIPArchive, TARArchive]
    def __init__(self, location_path, files_to_pack):
        self.location_path = location_path
        self.extension = os.path.splitext(location_path)[-1]
        self.files_to_pack = files_to_pack
        self.archive_engine = self.choose_archive_engine()
    def choose_archive_engine(self):
        for engine in self.ARCHIVE_ENGINES:
            if engine.check_extenstion(self.extension):
                return engine(self.location_path, self.files_to_pack)
    def create_archive(self):
        self.archive_engine.generate()

if __name__ == '__main__':
    zip_manager = ArchiveManager(os.path.join(os.getcwd(), 'init.zip'), ['__init__.py'])
    tar_manager = ArchiveManager(os.path.join(os.getcwd(), 'init.tar'), ['__init__.py'])
    zip_manager.create_archive()
    tar_manager.create_archive()
