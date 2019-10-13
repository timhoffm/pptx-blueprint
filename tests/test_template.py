# TODO
from pptx_blueprint import Template
from pathlib import Path
import pytest


@pytest.fixture
def template():
    filename = Path(__file__).absolute().parent / '../data/example01.pptx'
    tpl = Template(filename)
    return tpl


def test_open_template():
    filename = Path(__file__).absolute().parent / '../data/example01.pptx'
    tpl = Template(filename)


def test_open_template_missing():
    filename = Path(__file__).absolute().parent / '../data/non_existing.pptx'
    with pytest.raises(FileNotFoundError):
        tpl = Template(filename)


def test_find_shapes_from_all_slides(template):
    shapes = template._find_shapes('*', 'title')
    assert len(shapes) == 3
    for shape in shapes:
        assert shape.text == "{title}"


def test_find_shapes_from_one_slide(template):
    shapes = template._find_shapes(1, "logo")
    assert len(shapes) == 1
    assert shapes[0].text == '{logo}'


def test_find_shapes_index_out_of_range(template):
    with pytest.raises(IndexError):
        shapes = template._find_shapes(0, 'logo')
