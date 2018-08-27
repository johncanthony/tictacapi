from redisco import models


class Foo(models.Model):
    name = models.Attribute()
    title = models.Attribute()

class FooControler():

    def __init__(self,foo_obj):
        self.foo = foo_obj

    def test(self):
        print self.foo.name


name_shiz = "glep"

class Bar(models.Model):
    name = models.Attribute(default=name_shiz)
    foo = models.ReferenceField(Foo)


class BarController():

    def __init__(self,bar_obj):
        self.bar = bar_obj

    def update_name(self, new_name):
        self.bar.foo.name=str(new_name)
        self.bar.foo.save()

if __name__ == "__main__":
    title = "[test]"
    name = "tasty"

    a = Foo(name=name, title=title)
        
    a.is_valid()
    a.save()
    

    b = Bar(foo=a)
    b.save()
    
    testy = Bar.objects.filter(name=name_shiz)[0]
    print(testy.foo.name)


    bc = BarController(b)
    bc.update_name("wheat")

    testy = Bar.objects.filter(foo=a)[0]
    print(testy.foo.name)

   



