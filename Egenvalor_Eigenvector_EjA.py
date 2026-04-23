from sympy import Matrix , pprint
import numpy as np

print("INICISO A ")

A1_a = np.array([[1, 1/2, 1/3],
                [1/2, 1/3, 1/4],
                [1/3, 1/4, 1/5]])

A2_a = Matrix([[1, 1/2, 1/3],
            [1/2, 1/3, 1/4],
            [1/3, 1/4, 1/5]])


eigenvalores_a, eigenvectores_a = np.linalg.eig(A1_a)
print("\nEigenvalores y Eigenvectores con numpy \n")
print("Eigenvalores:\n", eigenvalores_a)
print("Eigenvectores unitarios:\n", eigenvectores_a)


eigen_data_a = A2_a.eigenvects()
print("\nEigenvalores y Eigenvectores (en formato 'exacto') con sympy ")
for i, (val, mult, vecs) in enumerate(eigen_data_a):
    print(f"\nEl Eigenvalor {i+1} es: {val}")
    for j, vec in enumerate(vecs):
        print(f"  Un eigenvector de {val} es: {vec.tolist()}")


print("\nMatriz P de eigenvectores (A): ")
P_a = A2_a.eigenvects()[0][2][0].row_join(A2_a.eigenvects()[1][2][0]).row_join(A2_a.eigenvects()[2][2][0])
pprint(P_a)


print("INICISO B ")

A1_b = np.array([[1, 1, 1, 1],
                [1.01, 1.02, 1.03, 1.04],
                [1.01**2, 1.02**2, 1.03**2, 1.04**2],
                [1.01**3, 1.02**3, 1.03**3, 1.04**3]])

A2_b = Matrix([[1, 1, 1, 1],
             [1.01, 1.02, 1.03, 1.04],
             [1.01**2, 1.02**2, 1.03**2, 1.04**2],
             [1.01**3, 1.02**3, 1.03**3, 1.04**3]])



eigenvalores_b, eigenvectores_b = np.linalg.eig(A1_b)
print("\nEigenvalores y Eigenvectores con numpy \n")
print("Eigenvalores:\n", eigenvalores_b)
print("Eigenvectores unitarios:\n", eigenvectores_b)


eigen_data_b = A2_b.eigenvects()
print("\nEigenvalores y Eigenvectores (en formato 'exacto') con sympy ")
for i, (val, mult, vecs) in enumerate(eigen_data_b):
    print(f"\nEl Eigenvalor {i+1} es: {val}")
    for j, vec in enumerate(vecs):
        print(f"  Un eigenvector de {val} es: {vec.tolist()}")



print("\nMatriz P de eigenvectores (B): ")
P_b = A2_b.eigenvects()[0][2][0].row_join(A2_b.eigenvects()[1][2][0]).row_join(A2_b.eigenvects()[2][2][0]).row_join(A2_b.eigenvects()[3][2][0])
pprint(P_b)