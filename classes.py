class Utilisateur:
    def __init__(self, nom : str, prenom : str) -> None:
        self.nom = nom
        self.prenom = prenom

    def presentation(self) -> None:
        return f"bonjour je suis {self.prenom} {self.nom}"
    def getInfo(self):
        return (self.nom, self.prenom, self.presentation())

class Admin(Utilisateur):
    def __init__(self, age,nom,prenom) -> None:
       super().__init__(nom,prenom)
       self.age = age
    def peutimport(self):
        pass

user = Utilisateur("Arnaud","Basile")
print(user.presentation())
print(user.getInfo())
