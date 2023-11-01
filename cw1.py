import numpy as np

#Example done in class using Rule of Mixture and HT Method
#Data given:
S3 = 0.2
S12 = 1
WFibre = 0.6 #Fibre weight Fraction
thickness = 0.001 #mm For each layer

# Laminate Configuration for Question 1
laminate_config_q1 = [0, 90, 90, 0]
nLayers = len(laminate_config_q1)
# Calculating the bottom and top thickness
position = [-nLayers * thickness / 2 + i * thickness for i in range(nLayers + 1)]

# Created an empty list to store Qbar matrices for each angle
Qbar_list = []
A1_list = []
B1_list = []
D1_list = []

for i in range(nLayers):  # Use a loop to keep track of the current layer
    angle = laminate_config_q1[i]
    theta = angle * (np.pi / 180)  # Calculate theta based on the angle
    
    #Carbon
    pFibre = 1870 #km/m^3
    EFibre = 310 #GN/m^2
    vFibre = 0.23
    #Epoxy
    pMatrix = 1200 #km/m^3
    EMatrix = 2.4 #GN/m^2
    vMatrix = 0.33

    WMatrix = 1 - WFibre
    VFibre = (WFibre/pFibre)/((WFibre/pFibre)+(WMatrix/pMatrix))
    VMatrix = 1 - VFibre

    #Rule of mixture
    #Young Modulus
    E1 = EMatrix*VMatrix + EFibre*VFibre
    # E2 = (EFibre*EMatrix)/((VFibre*EMatrix)+(VMatrix*EFibre))

    #Shear Modulus
    GFibre = EFibre/(2*(1+vFibre))
    GMatrix = EMatrix/(2*(1+vMatrix))
    # print(EMatrix, vMatrix)
    # G12 = (GFibre*GMatrix)/((GFibre*VMatrix) + (GMatrix*VFibre))
    # print(GMatrix, GFibre, VMatrix, VFibre)

    #Major Poisson Ratio
    v12 = vFibre*VFibre + vMatrix*VMatrix

    #HT Method
    nE = ((EFibre/EMatrix)-1)/((EFibre/EMatrix) + S3)
    E2 = EMatrix * ((1+(S3*nE*VFibre))/(1-(nE*VFibre)))

    nG = ((GFibre/GMatrix) - 1)/((GFibre/GMatrix) + 1)
    G12 = GMatrix * ((1 + S12*nG*VFibre)/(1 - nG*VFibre))

    #Minor Poisson Ration
    v21 = v12 *(E2/E1)
    # print(E1, E2, v12, v21, G12)

    # Checking values with example done in L10
    # E1 = 39
    # E2 = 8.6
    # v12 = 0.28
    # v21 = 0.06
    # G12 = 3.8
    
    #Calculating SMatrix
    # S11 = 1/E1
    # S12 = v12/E1
    # S22 = 1/E2
    # S66 = 1/G12
    # S = np.array([[S11, S12, 0],
    #             [S12, S22, 0],
    #             [0, 0, S66]])
    # print(S)

    #Calculating Qmatrix
    Q11 = E1 / (1 - v12 * v21)
    Q22 = E2 / (1 - v12 * v21)
    Q12 = v12 * E2 / (1 - v12 * v21)
    Q66 = G12
    Q = np.array([[Q11, Q12, 0],
                [Q12, Q22, 0],
                [0, 0, Q66]])

    # Calculating Tmatrix
    T11 = np.cos(theta) ** 2
    T12 = np.sin(theta) ** 2
    T13 = 2 * np.sin(theta) * np.cos(theta)
    T21 = np.sin(theta) ** 2
    T22 = np.cos(theta) ** 2
    T23 = -2 * np.sin(theta) * np.cos(theta)
    T31 = -np.sin(theta) * np.cos(theta)
    T32 = np.sin(theta) * np.cos(theta)
    T33 = np.cos(theta) ** 2 - np.sin(theta) ** 2

    T = np.array([[T11, T12, T13],
                [T21, T22, T23],
                [T31, T32, T33]])

    #Calculate the inverse of T matrix
    T_inv = np.linalg.inv(T)

    #Calculate the transpose of the inverse matrix
    T_inv_transpose = np.transpose(T_inv)

    #Calculating Qbar Matrix
    Qbar = T_inv @ Q @ T_inv_transpose
    # Qbar = np.round(Qbar, 4)

    # Converting the NumPy array to a regular Python list
    Qbar_list.append(Qbar.tolist())

    # A Matrix
    A1 = Qbar * (position[i + 1] - position[i])
    A1_list.append(A1)

    # B Matrix    
    B1 = (1/2)*Qbar * ((position[i + 1]**2) - (position[i]**2))
    B1_list.append(B1)
    
    # D Matrix    
    D1 = (1/3)*Qbar * ((position[i + 1]**3) - (position[i]**3))
    D1_list.append(D1)

    
# Print the Qbar matrices in a human-readable format
# for i, Qbar_matrix in enumerate(Qbar_list):
#     print(f"Qbar for angle {laminate_config_q1[i]} degrees:")
#     for row in Qbar_matrix:
#         print(row)
#     print()
    
# # Print the A1 matrices in a human-readable format
# for i, A1_matrix in enumerate(A1_list):
#     print(f"A1 for angle {laminate_config_q1[i]} degrees:")
#     print(A1_matrix)
#     print()

A = np.sum(A1_list, axis=0)* 1e9
B = np.sum(B1_list, axis=0)* 1e9
D = np.sum(D1_list, axis=0)* 1e9

# print("A:")
# print(A)
# print("B:")
# print(B)
# print("D:")
# print(D)

# Concatenate the A, B, and D matrices in the specified order
ABBD = np.block([[A, B], [B, D]])

# Set numpy print options to display numbers without scientific notation
np.set_printoptions(suppress=True, formatter={'float': lambda x: '0' if x == 0.0 else '{:0.3f}'.format(x)})

# # Print the ABBD matrix
# print("ABBD Matrix:")
# print(ABBD)

# Inverse ABBD Matrix
ABBD_inv = np.linalg.inv(ABBD)

# # Print the ABBD_inv matrix
# print("ABBD_inv Matrix:")
# print(ABBD_inv)

Nx = 1
Ny = 1
Nxy = 1
Mx = 1
My = 1
Mxy = 1

NM = ([[Nx],[Ny],[Nxy],[Mx],[My],[Mxy]])
# print(NM)

# Calculate the [ϵx, ϵy, γxy, κx, κy, κxy] vector
result = np.dot(ABBD_inv, NM)

# Print the result
# print("Resulting [ex, ey, yxy, kx, ky, kxy] vector:")
# print(result)

ex = result[0]
ey = result[1]
yxy = result[2]
kx = result[3]
ky = result[4]
kxy = result[5]

# print(ex)
# print(ey)
# print(yxy)
# print(kx)
# print(ky)
# print(kxy)

Sx = ((A[0,0]*ex + A[0,1]*ey + A[0,2]*yxy + B[0,0]*kx + B[0,1]*ky + B[0,2]*kxy))/(nLayers*thickness)
Sy = ((A[1,0]*ex + A[1,1]*ey + A[1,2]*yxy + B[1,0]*kx + B[1,1]*ky + B[1,2]*kxy))/(nLayers*thickness)
Sxy = ((A[2,0]*ex + A[2,1]*ey + A[2,2]*yxy + B[2,0]*kx + B[2,1]*ky + B[2,2]*kxy))/(nLayers*thickness)
Ex = Sx/ex
Ey = Sy/ey
Ge = Sxy/yxy
print(Ex)
print(Ey)
print(Ge)