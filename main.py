from compte_entreprise import ProduitElementaire,Composition,ProduitCompose

p1 = ProduitElementaire("oil", "1234", 250)
p2 = ProduitElementaire("sucre", "2345", 350)

c1 = Composition(p1, 3)
c2 = Composition(p2, 4)

p3 = ProduitCompose("Plan de cuisine", "3456", 1500, [c1, c2])