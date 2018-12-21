class Kakatua:

    # class attribute
    species = "burung"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
kiki = Kakatua("kiki", 10)
wiki = Kakatua("Wiki", 15)

# access the class attributes
print("Kiki adalah{}".format(kiki.__class__.species))
print("Wiki juga {}".format(wiki.__class__.species))

# access the instance attributes
print("{} ialah {} tahun".format( kiki.name, kiki.age))
print("{} ialah {} tahun".format( wiki.name, wiki.age))
