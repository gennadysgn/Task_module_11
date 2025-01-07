import inspect


def introspection_info(obj):
    dict_info = {'type': type(obj).__name__,
                 'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
                 'methods': [meth for meth in dir(obj) if callable(getattr(obj, meth))],
                 'module': inspect.getmodule(introspection_info)
                 }
    return dict_info


number_info = introspection_info(42)
print(number_info)


