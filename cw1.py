import numpy as np

#Rule of mixture
#Finding E1
strain1 = strainFibre
strain1 = StrainMatrix

stressFibre = EFibre*strain1
stressMatrix = EMatrix*strain1

PFibre = EFibre*strain1*AFibre
PMatrix = EMatrix*strain1*AMatrix

#Total Load
PTotal = EFibre*strain1*AFibre + EMatrix*strain1*AMatrix

#Average Stress
stress1 = (EFibre*strain1*AFibre + EMatrix*strain1*AMatrix)/(AFibre+AMatrix)

#Elastic Module
E1 = (EFibre*AFibre + EMatrix*AMatrix)/(AFibre+AMatrix)

VFibre = AFibre/(AFibre+AMatrix)
VMatrix = AMatrix/(AFibre+AMatrix)

E1 = EFibre*VFibre + EMatrix*VMatrix


