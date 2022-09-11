﻿import unittest
import os
import sys

from PIL import Image
import pytest
import shutil

sys.path.append("sources")
from sources import File

#setup

@pytest.fixture
def setup() :
    try :
        shutil.rmtree("test")
    except :
        pass
    os.mkdir("test")
    File.SaveFile(os.getcwd() + "\\test\\test.txt", "test")
    yield
    shutil.rmtree("test")

def test_ShowFileDialog(setup) :
    File.ShowFileDialog() == os.getcwd() + "\\test\\test.txt"

def test_ShowSaveFileDialog(setup) :
    assert File.ShowSaveFileDialog() == os.getcwd() + "\\test\\test.txt"