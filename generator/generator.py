from datetime import date
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('generator', 'templates'))


def generate_class(obj):
    template = env.get_template('class.py')

    context = {}
    context["internal_name"] = obj.internal_name
    context["class_name"] = obj.class_name
    context["field_count"] = len(obj.fields)
    context["fields"] = obj.fields
    return template.render(context)


def generate_epw(objs):
    list_objs = []
    for obj in objs:
        for field in obj.fields:
            if field.is_list:
                list_objs.append(field.internal_name)
    not_list_objs = []
    for obj in objs:
        if obj.internal_name not in list_objs:
            not_list_objs.append(obj)

    template = env.get_template('epw.py')
    context = {}
    classes = []
    for obj in objs:
        classes.append(generate_class(obj))
    context["datadicts"] = classes
    context["generation_date"] = date.today()
    context["objs"] = not_list_objs[:-1]
    return template.render(context)


def generate_testclass(obj, objs):
    _objs = {}
    for o in objs:
        _objs[o.class_name] = o
    template = env.get_template('test_class.py')
    context = {}
    context["obj"] = obj
    context["objs"] = _objs
    return template.render(context)
