"""Base class for service plugins - functions should be parameter-less where possible."""
import inspect

class ServiceBase(object):

    # Override iter definition to return all non-private methods.
    def __iter__(self):
        for method in inspect.getmembers(self, predicate=inspect.ismethod):
            if not method[0].startswith('_'):
                yield method
