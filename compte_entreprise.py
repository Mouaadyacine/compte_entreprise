class Composition:
    def _init_(self, produit, quantite):
        self._produit = produit
        self._quantite = quantite

    @property
    def produit(self):
        return self._produit

    @property
    def quantite(self):
        return self._quantite


class Produit:
    def _init_(self, nom, code):
        self._nom = nom
        self._code = code

    @property
    def nom(self):
        return self._nom

    @property
    def code(self):
        return self._code

    def _str_(self):
        return f"Produit {self.nom} ayant pour code {self.code}"

    def getProcHT(self):
        pass


class ProduitElementaire(Produit):
    def _init_(self, nom, code, pricht):
        super()._init_(nom, code)
        self._pricht = pricht

    @property
    def pricht(self):
        return self._pricht

    def getProcHT(self):
        return self.pricht


class ProduitCompose(Produit):
    TVA = 18 / 100

    def _init_(self, nom, code, franchfabrication, Cenas):
        super()._init_(nom, code)
        self._franchfabrication = franchfabrication
        self._Cenas = Cenas

    @property
    def franchfabrication(self):
        return self._franchfabrication

    @property
    def Cenas(self):
        return self._Cenas

    def getProcHT(self):
        prix_ht = 0
        for cama in self._Cenas:
            prix_ht += cama.produit.getProcHT() * cama.quantite
        prix_ht /= (1 + self.IVA)
        return prix_ht

    def _str_(self):
        return super()._str_() + f" avec une valeur de {self.getProcHT()} euros"
