import numpy as np

def kernelxx(x,y,z,xs,ys,zs):
    '''
    Calculate the second derivative in relation x of a function 1/r.

    input
    x,y,z : float - Cartesian coordinates (in m) of the i-th observation point
    xs,ys,zs : numpy arrays - Cartesian coordinates of equivalent sources

    output
    phi_xx : numpy array - Values with the second derivatives at one point.
    '''
    assert xs.size == ys.size and ys.size == zs.size and xs.size == zs.size, \
    'All arrays must have the same size'
    r = np.sqrt((x - xs)**2 + (y - ys)**2 + (z - zs)**2)
    r2 = r*r
    phi_xx = (((3.*(x - xs)**2)/(r2*r2*r))-(1./(r2*r)))

    return phi_xx

def kernelxy(x,y,z,xs,ys,zs):
    '''
    Calculate the second derivative in relation x and y of a function 1/r.

    input
    x,y,z : float - Cartesian coordinates (in m) of the i-th observation point
    xs,ys,zs : numpy arrays - Cartesian coordinates of equivalent sources

    output
    phi_xy : numpy array - Values with the second derivatives.
    '''
    assert x.size == y.size and y.size == z.size, \
    'All arrays must have the same size'
    r = np.sqrt((x - xs)**2 + (y - ys)**2 + (z - zs)**2)
    r2 = r*r
    phi_xy = 3.*(((x - xs)*(y - ys))/(r2*r2*r))

    return phi_xy

def kernelxz(x,y,z,xs,ys,zs):
    '''
    Calculate the second derivative in relation x and z of a function 1/r.

    input
    x,y,z : float - Cartesian coordinates (in m) of the i-th observation point
    xs,ys,zs : numpy arrays - Cartesian coordinates of equivalent sources

    output
    phi_xz : numpy array - Values with the second derivatives.
    '''
    assert x.size == y.size and y.size == z.size, \
    'All arrays must have the same size'
    r = np.sqrt((x - xs)**2 + (y - ys)**2 + (z - zs)**2)
    r2 = r*r
    phi_xz = 3.*(((x - xs)*(z - zs))/(r2*r2*r))

    return phi_xz

def kernelyy(x,y,z,xs,ys,zs):
    '''
    Calculate the second derivative in relation y of a function 1/r.

    input
    x,y,z : float - Cartesian coordinates (in m) of the i-th observation point
    xs,ys,zs : numpy arrays - Cartesian coordinates of equivalent sources

    output
    phi_yy : numpy array - Values with the second derivatives.
    '''
    assert x.size == y.size and y.size == z.size and x.size == z.size, \
    'All arrays must have the same size'
    r = np.sqrt((x - xs)**2 + (y - ys)**2 + (z - zs)**2)
    r2 = r*r
    phi_yy = ((3.*(y - ys)**2)/(r2*r2*r))-(1./(r2*r))

    return phi_yy

def kernelyz(x,y,z,xs,ys,zs):
    '''
    Calculate the second derivative in relation y and z of a function 1/r.

    input
    x,y,z : float - Cartesian coordinates (in m) of the i-th observation point
    xs,ys,zs : numpy arrays - Cartesian coordinates of equivalent sources

    output
    phi_yz : numpy array - Values with the second derivatives.
    '''
    assert x.size == y.size and y.size == z.size, \
    'All arrays must have the same size'
    r = np.sqrt((x - xs)**2 + (y - ys)**2 + (z - zs)**2)
    r2 = r*r
    phi_yz = 3.*((y - ys)*(z - zs))/(r2*r2*r)

    return phi_yz

def kernelzz(x,y,z,xs,ys,zs):
    '''
    Calculate the second derivative in relation z of a function 1/r.

    input
    x,y,z : float - Cartesian coordinates (in m) of the i-th observation point
    xs,ys,zs : numpy arrays - Cartesian coordinates of equivalent sources

    output
    phi_zz : numpy array - Values with the second derivatives at one point.
    '''
    assert xs.size == ys.size and ys.size == zs.size and xs.size == zs.size, \
    'All arrays must have the same size'
    r = np.sqrt((x - xs)**2 + (y - ys)**2 + (z - zs)**2)
    r2 = r*r
    phi_zz = (((3.*(z - zs)**2)/(r2*r2*r))-(1./(r2*r)))

    return phi_zz

def tfa(coordinates,sources,main_field,intensities,magnetization):
    '''
    Calculate the Total Field Anomaly produced by a layer

    input

    x,y,z : float - Cartesian coordinates (in m) of the i-th observation point
    xs,ys,zs : numpy arrays - Cartesian coordinates of equivalent sources
    sinc,sdec: float - Main field direction
    p: numpy array - Vector composed by magnetic moment and magnetization direction of the
                     equivalent sources

    return
    tfa : numpy array - total field anomaly of the equivalent layer
    '''
    MAGNETIC_PERM = 0.000001256

    y = coordinates[0]
    x = coordinates[1]
    z = coordinates[2]

    ys = sources[0]
    xs = sources[1]
    zs = sources[2]

    N = x.size
    M = xs.size
    sinc, sdec = main_field
    inc,dec = magnetization
    p = intensities
    
    j0x = np.cos(np.deg2rad(sinc))*np.cos(np.deg2rad(sdec))
    j0y = np.cos(np.deg2rad(sinc))*np.sin(np.deg2rad(sdec))
    j0z = np.sin(np.deg2rad(sinc))
    
    mx = np.cos(np.deg2rad(inc))*np.cos(np.deg2rad(dec))
    my = np.cos(np.deg2rad(inc))*np.sin(np.deg2rad(dec))
    mz = np.sin(np.deg2rad(inc))
    
    
    tfa = np.empty(N,dtype=float)
    for i in range(N):
        phi_xx = kernelxx(x[i],y[i],z[i],xs,ys,zs)
        phi_yy = kernelyy(x[i],y[i],z[i],xs,ys,zs)
        phi_xy = kernelxy(x[i],y[i],z[i],xs,ys,zs)
        phi_xz = kernelxz(x[i],y[i],z[i],xs,ys,zs)
        phi_yz = kernelyz(x[i],y[i],z[i],xs,ys,zs)
        phi_zz = -phi_xx - phi_yy

        gi = (j0x*mx - j0z*mz)*phi_xx + (j0y*my - j0z*mz)*phi_yy + (j0x*my + j0y*mx)*phi_xy +\
             (j0x*mz + j0z*mx)*phi_xz + (j0y*mz + j0z*my)*phi_yz

        tfa[i] = np.dot(p.T,gi)

    tfa *= MAGNETIC_PERM*1e9
    return tfa

def sensitivity(coordinates,sources,main_field,magnetization):
    '''
    Calculate the sensitivity matrix

    input

    return
    '''
    MAGNETIC_PERM = 0.000001256

    y = coordinates[0]
    x = coordinates[1]
    z = coordinates[2]

    ys = sources[0]
    xs = sources[1]
    zs = sources[2]

    N = x.size
    M = xs.size
    sinc, sdec = main_field
    inc,dec = magnetization
    
    j0x = np.cos(np.deg2rad(sinc))*np.cos(np.deg2rad(sdec))
    j0y = np.cos(np.deg2rad(sinc))*np.sin(np.deg2rad(sdec))
    j0z = np.sin(np.deg2rad(sinc))
    
    mx = np.cos(np.deg2rad(inc))*np.cos(np.deg2rad(dec))
    my = np.cos(np.deg2rad(inc))*np.sin(np.deg2rad(dec))
    mz = np.sin(np.deg2rad(inc))
    
    A = np.empty((N,M),dtype=float)
    for i in range(N):
        phi_xx = kernelxx(x[i],y[i],z[i],xs,ys,zs)
        phi_yy = kernelyy(x[i],y[i],z[i],xs,ys,zs)
        phi_xy = kernelxy(x[i],y[i],z[i],xs,ys,zs)
        phi_xz = kernelxz(x[i],y[i],z[i],xs,ys,zs)
        phi_yz = kernelyz(x[i],y[i],z[i],xs,ys,zs)
        phi_zz = - phi_xx - phi_yy
        gi = (j0x*mx - j0z*mz)*phi_xx + (j0y*my - j0z*mz)*phi_yy + (j0x*my + j0y*mx)*phi_xy +\
             (j0x*mz + j0z*mx)*phi_xz + (j0y*mz + j0z*my)*phi_yz
        A[i,:] = gi

    A *= MAGNETIC_PERM*1e9
    return A
