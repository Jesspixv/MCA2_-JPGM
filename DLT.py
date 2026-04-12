import numpy as np

# Estos son X ,Y , Z en el lado real
puntos_3D = np.array([
    [0, 0, 0],       
    [17, 0, 0],      
    [17, 10, 0],     
    [0, 10, 0],      
    [17, 10, -4.5]  
], dtype=np.float32)

# Esos son u , v dados en el lado 2D
puntos_2D = np.array([
    [318, 1225],
    [951, 1128],
    [891, 701],
    [272, 787],
    [893, 718]    
], dtype=np.float32)

# Resolvemos el DLT 

def resolver_DLT(obj_pts, img_pts):
    A = []
    for i in range(len(obj_pts)):
        X, Y, Z = obj_pts[i]
        u, v = img_pts[i]
        #Ecuaciones que lo resuelven que ya  son las finales
        A.append([X, Y, Z, 1, 0, 0, 0, 0, -u*X, -u*Y, -u*Z, -u])
        A.append([0, 0, 0, 0, X, Y, Z, 1, -v*X, -v*Y, -v*Z, -v])
    
    A = np.array(A)
    # Usar SDV
    _, _, Vh = np.linalg.svd(A)
    L = Vh[-1, :] 
    
    # Normalizar para que el último valor sea 1 
    L = L / L[-1]
    return L.reshape((3, 4))

# Calcula Matriz de Proyección P , es decir ya como es que se ve
P = resolver_DLT(puntos_3D, puntos_2D)

print("--- Proyecion  ---")
print(P)

print("\n--- Estos son los datos que se supone tenemos , si coincide estan bien ---")
for i in range(len(puntos_3D)):
    M = np.append(puntos_3D[i], 1)
    m_calc_homog = P @ M
    u_calc = m_calc_homog[0] / m_calc_homog[2]
    v_calc = m_calc_homog[1] / m_calc_homog[2]
    print(f" Real{puntos_2D[i]} ---> Proyectado [{int(u_calc)}, {int(v_calc)}]")