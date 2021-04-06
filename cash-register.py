import numpy as np

countries = np.array(["Allemagne ", "Autriche ", "Belgique ", "Bulgarie ", "Chypre ", "Croatie ", "Danemark ", "Espagne ",
	"Estonie ", "Finlande ", "France ", "Grèce ", "Hongrie ", "Irlande ", "Italie ", "Lettonie ",
	"Lituanie ", "Luxembourg ", "Malte ", "Pays-Bas ", "Pologne ", "Portugal ", "République Tchèque ",
	"Roumanie ", "Royaume-Uni ", "Slovaquie ", "Slovénie ", "Suède"])

codes = np.array(["DE", "AT", "BE", "BG", "CY", "HR", "DK", "ES", "EE",
	"FI", "FR", "EL", "HU", "IE", "IT", "LV", "LT", "LU",
	"MT", "NL", "PL", "PT", "CZ", "RO", "GB", "SK", "SI", "SE"])

TVA = np.array([19, 20, 21, 20, 19, 25, 25, 21, 20,
	24, 20, 23, 27, 23, 22, 21, 21, 17,
	18, 21, 23, 23, 21, 24, 20, 22, 20, 25])

for i in range(countries.size):
	print(codes[i] + "\t" + str(TVA[i]) + "%\t" + countries[i])

price = int(input('Prix du produit :'))
qtt = int(input('Quantité de produit :'))
reduction = int(input('Montant de la réduction :'))
totalHT = (price*qtt)-reduction
codePays = input('Code pays :')
for i in range(countries.size):
	if codePays == codes[i]:
		tauxTVA = TVA[i]
totalTVA = (totalHT/100)*tauxTVA

total = totalHT+totalTVA
print(total)