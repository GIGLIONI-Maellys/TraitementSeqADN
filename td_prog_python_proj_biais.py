monfichier = input("Veuillez entrer le nom du fichier")

taille = int(input("Quelle est la taille de la fenêtre ?"))
pas = int(input("Entrez le pas de la fenêtre"))


#faire des vérifications

F1 = open(monfichier,"r")# en mode lecture
ma_ligne = F1.readline()
print(ma_ligne[:-1])
seq=""
for ligne in F1:
    if ligne =="\n":
        break;
    else :
        seq = seq + ligne[:-1]  
#print(seq)
     
name2 = "seqTDprojbiais.txt"
fichier2 =open(name2,"a")# en mode ecriture

#utiliser seconde boucle pour mettre dans une seconde variable les 10 nucléotides qui suivent le i
debut = 0 
fin = taille 
for i in range(1, len(seq), pas)  :
    nbC = 0
    nbG = 0
    nbT = 0
    nbA = 0
    nbN = 0
    nb_total = 0
    biais_gc=0

    seq = seq.upper()
    #mettre la séquence en majuscule et on compte pour chaque nucléotide le nombre de C,G,A,T  
    #nbC += seq.count("C")
    #nbG += seq.count("G")
    #nbT += seq.count("T")
    #nbA += seq.count("A")
    #nbN += seq.count("N")# la séquence inconnue

    if (len(seq) >= i+taille) :
        
        for a in range (i, i+taille) :
                if (seq[a]=="C") :
                    nbC = nbC + 1 
                elif (seq[a]=="G") :
                    nbG=nbG+1

                elif (seq[a]=="T") :
                    nbT=nbT+1

                elif (seq[a]=="A") :
                    nbA=nbA+1
            
                elif (seq[a]=="N") :
                    nbN=nbN+1
    else :
        break ;
    nb_total = nbC + nbG + nbT + nbA + nbN
    biais_gc = (nbC - nbG) / (nbC+ nbG)

    fichier2.write(str(i+taille) + "\t" + str(biais_gc) + "\n")
    fichier2.write("\n")
    fin=debut+taille
     

    # on calcule le taux de GC

     



F1.close()
fichier2.close()
