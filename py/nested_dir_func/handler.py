import lib1
import lib2


def handler(ctx, event):
    a = lib1.A()
    b = lib2.B()
    return "OK"
