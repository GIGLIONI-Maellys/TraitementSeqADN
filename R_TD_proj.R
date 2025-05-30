# pour le chromosome du poulet

# on cr�er ici un fichier_sortie dans lequel on met les r�sultats du % de GC de chaque chromosome pour pouvoir ensuite faire
# un graphique en fonction de la taillle de chaque chr
setwd("H:/Demarche_scientifique")
data = read.table("seqtdproj.txt", sep="\t",header=TRUE)
getwd()
dev.new(width = 1000, height = 1000) # taille de la fen�tre
plot(data[,3] ~ data[,1], type = "l", xlab ="Position (Centre de la fen�tre)" , ylab = "Taux de GC en %",main ="Graphique repr�sentant le taux de GC en fonction de la taille du chromosome")
summary(data)
