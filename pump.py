import numpy as np
import matplotlib.pyplot as plt
import WaterProperties as wp
import iapws._iapws as iapws


def find_flow_rate(D_H, head):

    rho = WaterProperties.Density(25, 101325)

    #Re = rho*D_H*V_avg/mu
    ## find f
    #f_new = 0.0
    #f_old = 1.0
    #while abs(f_new-f_old)<1.0e-5:
        #f_old = f_new
        #f_new = (1/(np.log10(2.51/(Re*np.sqrt(f_old)))))**2

    pass


if __name__ == "__main__":

    prop = iapws._Liquid(300, 0.1)
    print("WATER DENSITY: ", prop)