# -*- coding: utf-8 -*-
import re
def ventana(seq, k):
    if k<=0:
        return []
    it = iter(seq)
    buf = []
    for x in it:
        buf.append(x)
        if len(buf)==k:
            yield tuple(buf)
            buf.pop(0)

