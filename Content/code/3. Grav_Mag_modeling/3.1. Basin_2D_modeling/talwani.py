import numpy as np

def gz(xc,zc,x_verts,z_verts,density=None):
    """
    Calculo da atracao gravitacional de um corpo bidimensional aproximado por um poligono
    vertical utilizando a formula de Talwani et al. (1959).

    input

    x: numpy array - Coordenadas x de observacao
    z: numpy array - Coordenadas z de observacao
    model: lista - Lista com os vértices do poligono

    return

    gz: numpy array - Atracao gravitacional gerado pelo conjunto de poligonos

    """
    gamma = 6.670*1e-11
    SI2MGAL = 1.0*1e5

    if xc.shape != zc.shape:
        raise ValueError("As coordenadas de observacao devem ter o mesmo shape")

    nverts = x_verts.size
    resultado = np.zeros_like(xc)
    for v in range(nverts):
        # Mudanca de coordenadas do vertice
        xv = x_verts[v] - xc
        zv = z_verts[v] - zc
        # O ultimo par de vertices igual ao primeiro
        if v == nverts - 1:
            xv1 = x_verts[0] - xc
            zv1 = z_verts[0] - zc
        else:
            xv1 = x_verts[v + 1] - xc
            zv1 = z_verts[v + 1] - zc
        # Determinando as condicoes onde os limites nao funcionam
        xv[xv == 0.] = xv[xv == 0.] + 0.01
        xv[xv == xv1] = xv[xv == xv1] + 0.01
        zv[zv[xv == zv] == 0.] = zv[zv[xv == zv] == 0.] + 0.01
        zv[zv == zv1] = zv[zv == zv1] + 0.01
        zv1[zv1[xv1 == zv1] == 0.] = zv1[zv1[xv1 == zv1] == 0.] + 0.01
        xv1[xv1 == 0.] = xv1[xv1 == 0.] + 0.01
        # Comecando o calculo do efeito da gravidade
        phi_v = np.arctan2(zv1 - zv, xv1 - xv)
        ai = xv1 + zv1 * (xv1 - xv) / (zv - zv1)
        theta_v = np.arctan2(zv, xv)
        theta_v1 = np.arctan2(zv1, xv1)
        theta_v[theta_v < 0] += np.pi
        theta_v1[theta_v1 < 0] += np.pi
        tmp = ai * np.sin(phi_v) * np.cos(phi_v) * (
        theta_v - theta_v1 + np.tan(phi_v) * np.log(
        (np.cos(theta_v) * (np.tan(theta_v) - np.tan(phi_v))) /
        (np.cos(theta_v1) * (np.tan(theta_v1) - np.tan(phi_v)))))
        tmp[theta_v == theta_v1] = 0.
        resultado = resultado + tmp
    gz = 2*resultado*SI2MGAL*gamma*density
    return gz
