from __future__ import absolute_import
from erlpack import pack


def test_float():
    assert pack(2.5) == b'\x83F@\x04\x00\x00\x00\x00\x00\x00'
    assert pack(51512123841234.31423412341435123412341342) == b'\x83FB\xc7l\xcc\xeb\xedi('
