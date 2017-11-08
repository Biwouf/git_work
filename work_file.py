#! /usr/bin/env python3
# coding: utf-8

#Script qui parse un petit fichier CSV

import numpy as np
import pandas as panda
import matplotlib as mpl 
mpl.use('TkAgg')
import matplotlib.pyplot as plt

races = panda.read_csv('triathlon.csv', sep=',')
distances = races['Distance'].dropna().unique()
#print(distances)

#Afficher les distances uniquement XXL
long_races = races.Nom[races["Distance"] == "XXL"]
#print(long_races)


#Fonction qui prend un fichier en paramètre
def get_data(file_to_analyze, separator):
	data = panda.read_csv(file_to_analyze, separator)
	return data

def search_for_equal_distance(data, data_to_compare, value_to_match):
	display = data.Nom[data[data_to_compare] == value_to_match]
	print(display)

class Distance():
	def __init__(self, name):
		self.name = name

	def get_data(self, file):
		self.data = panda.read_csv(file, ",")

	def split_by_distance(self):
		data = self.data

		xs = data[data.Distance == "XS"]
		s = data[data.Distance == "S"]
		m = data[data.Distance == "M"]
		l = data[data.Distance == "L"]
		xl = data[data.Distance == "XL"]
		xxl = data[data.Distance == "XXL"]

		counts = [len(xs), len(s), len(m), len(l), len(xl), len(xxl)]
		counts = np.array(counts)
		races_total = counts.sum() 				#On fait la somme des nombres de la liste.
		proportions = counts / races_total

		#print(races_total)
		#print(proportions)

		labels = ["XS ({})".format(counts[0]),
					"S ({})".format(counts[1]),
					"M ({})".format(counts[2]),
					"L ({})".format(counts[3]),
					"XL ({})".format(counts[4]),
					"XXL ({})".format(counts[5])]

		#TODO => Connecter les % avec les distances
		fig, ax = plt.subplots()
		ax.pie(proportions,
				labels=labels,
				autopct='%1.1f p.')
		plt.title("Répartition des triathlons par distance")
		ax.axis('equal')
		plt.show()


def main():
	races = Distance('All races')
	races.get_data('triathlon.csv')
	print(long_races)
	races.split_by_distance()

#def main():
#	search_for_equal_distance(analyze('triathlon.csv', ','),
#								'Distance',
#								'XXL')


if __name__ == '__main__':
	main()

