#/usr/bin/env python

def test_myfind():

    with open('find.out') as f:

        lines = f.readlines()

    assert './files1/lorem2.dat\n' in lines
    assert './files1/lorem3.dat\n' in lines
    assert './files2/lorem2.dat\n' in lines
    assert './files2/lorem3.dat\n' in lines


