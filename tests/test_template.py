# TODO
from pptx_blueprint import Template
from pathlib import Path
import pytest


def test_open_template():
	filename = Path(__file__).absolute().parent / '../data/example01.pptx'
	tpl = Template(filename)


def test_open_template_missing():
	filename = Path(__file__).absolute().parent / '../data/non_existing.pptx'
	with pytest.raises(FileNotFoundError):
		tpl = Template(filename)
