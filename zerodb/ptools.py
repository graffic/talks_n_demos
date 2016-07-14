import sys

def export(the_class):
    setattr(sys.modules["__main__"],the_class.__name__, the_class)
