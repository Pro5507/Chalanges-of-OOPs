class a():
    def __init__(self, a):
        self.a= a
    def __it__(self, other):
        if self.a<other.a:
            return "ob1<ob2"
        else:
            return "ob2<ob1"
ob1= a(2)
ob2= a(5)
print(ob1.a, ob2.a)
print(ob1<ob2)