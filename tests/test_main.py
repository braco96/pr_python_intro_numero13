import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_ventana():
    assert list(mod.ventana([1,2,3,4], 3)) == [(1,2,3),(2,3,4)]
    assert list(mod.ventana([1,2], 3)) == []
    assert list(mod.ventana([1,2,3], 0)) == []
