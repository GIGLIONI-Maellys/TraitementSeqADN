# pour le chromosome du poulet 
# on créer ici un fichier_sortie dans lequel on met les résultats du % de GC de chaque chromosome pour pouvoir ensuite faire 
# un graphique en fonction de la taillle de chaque chr
setwd("H:/Demarche_scientifique")
data = read.table("seqTDprojbiais.txt", sep="\t",header=TRUE)
getwd()
dev.new(width = 10, height = 10) # taille de la fenêtre 
data[,2]
plot(data[,1],data[,2], xlab ="Taille du chromosome" , ylab = "Biais de GC", main ="Graphique représentant le biais de GC en fonction de la taille du chromosome", type = "o")
summary(data)
