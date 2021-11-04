import numpy as np

def gz(xp,zp,x_verts,z_verts,density=None):
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

    if xp.shape != zp.shape:
        raise ValueError("As coordenadas de observacao devem ter o mesmo shape")

    nverts = x_verts.size
    resultado = np.zeros_like(xp)
    nverts = x_verts.size
    for v in range(x_verts.size):
        X0 = x_verts[v] - xp
        Z0 = z_verts[v] - zp
        if v == nverts - 1:
            X1 = x_verts[0] - xp
            Z1 = z_verts[0] - zp
        else:
            X1 = x_verts[v+1] - xp
            Z1 = z_verts[v+1] - zp

        R0 = X0*X0 + Z0*Z0
        R1 = X1*X1 + Z1*Z1
        if (R0.any() == 0) or (R1.any() == 0):
            break
        den = Z1 - Z0
        den[den == 0.] = 0.01
        alpha = (X1 - X0)/den
        beta = (X0 * Z1 - X1 * Z0)/den
        factor = beta / (1. + alpha*alpha)
        term1 = 0.5*(np.log(R1) - np.log(R0))
        term2 = np.arctan2(Z1,X1) - np.arctan2(Z0,X0)
        tmp = factor*(term1 - alpha*term2)
        resultado = resultado + tmp
    gz = 2*resultado*SI2MGAL*gamma*density
    return gz

def prism(xp,zp,xmin,xmax,top,bottom,density):
    """
    Calculo da atracao gravitacional de um prisma bidimensional aproximado por um poligono
    vertical utilizando a formula de Talwani et al. (1959).

    input

    x: numpy array - Coordenadas x de observacao
    z: numpy array - Coordenadas z de observacao
    model: lista - Lista com os vértices do poligono

    return

    gz: numpy array - Atracao gravitacional gerado pelo conjunto de poligonos

    """
    if xp.shape != zp.shape:
        raise ValueError("As coordenadas de observacao devem ter o mesmo shape")


    x_verts = np.array([xmin,xmax,xmax,xmin])
    z_verts = np.array([top,top,bottom,bottom])

    resultado = gz(xp,zp,x_verts,z_verts,density=density)
    return resultado

def basin(xp,zp,ref,depths,density):
    """
    Calculo da atracao gravitacional de um prisma bidimensional aproximado por um poligono
    vertical utilizando a formula de Talwani et al. (1959).

    input

    x: numpy array - Coordenadas x de observacao
    z: numpy array - Coordenadas z de observacao
    model: lista - Lista com os vértices do poligono

    return

    gz: numpy array - Atracao gravitacional gerado pelo conjunto de poligonos

    """
    if xp.shape != zp.shape:
        raise ValueError("As coordenadas de observacao devem ter o mesmo shape")

    dx = xp[1] - xp[0]
    gravitational = np.zeros_like(xp)
    for p,d in zip(xp,depths):
        xmin,xmax = p-0.5*dx,p+0.5*dx
        gz = prism(xp,zp,xmin,xmax,ref,d,density)
        gravitational += gz

    return gravitational

def sensitivity(xp,depths,density):
    '''
    Calculating the sensitivity matrix based on Uieda and Barbosa [2017].
    '''    
    N = xp.size
    M = depths.size
    gamma = 6.670*1e-11
    SI2MGAL = 1.0*1e5
    
    I = np.identity(M)
    A = 2.*np.pi*density*SI2MGAL*gamma*I
    
    return A

def smoothness(xp,depths):
    '''
    Calculating the finite difference matrix for smoothness regularization    
    
    '''
    N = xp.size
    M = depths.size
    
    R = np.zeros(M+1)
    R[0] = 1.
    R[1] = -1.
    
    R = np.resize(R,(N,M))    
    return R

def GN_solver_smoothness(xp,zp,obs,ref,p0,density,itmax,stop,mu):
    """
    Gauss-Newton method solver for estimating the basement of a 2D Basin using smoothness regularization

    input

    xp: numpy array - Coordinates x 
    zp: numpy array - Coordinates z 
    obs: numpy array - Observation vector with gravitational effect of the basin
    ref: float - Reference surface
    p0: numpy array - Initial step for basement depths
    itmax: integer - Maximum iteration
    stop: float - Stop criteria for iteration
    mu: float - Regularization parameter

    return

    gz: numpy array - Predicted data at the final of the iteration process
    p0: numpy array - Estimated depths for the basement

    """
    ## Initial step
    grav0 = basin(xp,zp,ref,p0,density)
    G = sensitivity(xp,p0,density)
    GtG = np.dot(G.T,G)
    R = smoothness(xp,p0)
    RtR = np.dot(R.T,R)
    r0 = obs - grav0
    phi0 = np.linalg.norm(r0) + mu*np.linalg.norm(np.dot(R,p0)) 
     
    ## Iteration process
    for i in range(itmax):
        print (i)
        H = GtG + mu*RtR
        J = -np.dot(G.T,r0) + mu*np.dot(RtR,p0)
    
        dp = np.linalg.solve(H,-J)
        p0 += dp
    
        grav = basin(xp,zp,ref,p0,density)
        r = obs - grav
        phi = np.linalg.norm(r) + mu*np.linalg.norm(np.dot(R,p0))
    
        dphi = phi - phi0
    
        condition = np.abs(dphi)/phi0        
        if (condition <= stop):
            break
    
        r0[:] = r[:]
        phi0 = phi
        grav0[:] = grav[:]
    
    return grav0, p0
