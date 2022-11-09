
import numpy as np

def calculate(vol1, vol2, res1, res2, res3):

        R1 = res1
        R2 = res2
        R3 = res3
        E1 = vol1
        E2 = vol2

        R = np.array([[R1+R3, -R3], [-R3, R2+R3]])
        E = np.array([E1, -E2])
        I = np.round((np.linalg.solve(R, E)), 6)
        I1, I2, I3= I[0], I[1], round(I[0] - I[1], 6)
        V1, V2, V3= round(R1*I[0], 6), round(R2*I[1], 6), round(R3*I3, 6)

        return R1, R2, R3, I1, I2, I3, V1, V2, V3


def calculate_Experiment_2(vol1, res1, res2, res3, res4, res5, res6):

        R1 = res1
        R2 = res2
        R3 = res3
        R4 = res4
        R5 = res5
        R6 = res6
        E1 = vol1


        R = np.array([[R1+R2, -R2, 0], [-R2, R3+R4+R6, -R5], [R1, R3+R4, R6]])
        E = np.array([E1, 0, E1])
        I = np.round((np.linalg.solve(R, E)), 6)
        I1, I2, I3 = I[0], I[1], I[2]
        V1, V2, V3, V4, V5, V6 = round(R1*I[0], 6), round(R2*(I1-I2), 6), round(R3*I[1], 6), round(R4*I[1], 6), round(R5*(I2-I3), 6), round(R6*I3, 6)

        return R1, R2, R3,R4, R5, R6, I1, I2, I3, V1, V2, V3, V4, V5, V6



def calculate_exeprient_3(vol1, res1, res2, res3, res4):

        R1 = res1
        R2 = res2
        R3 = res3
        R4 = res4
        E1 = vol1

        R = np.array([[R1+R3, -R3], [-R3, R2+R3+R4]])
        E = np.array([E1, 0])
        I = np.round((np.linalg.solve(R, E)), 6)
        I1, I2, I3= I[0], I[1], round(I[0] - I[1], 6)
        V1, V2, V3, V4= round(R1*I[0], 6), round(R2*I[1], 6), round(R3*I3, 6), round(R4*I[1], 6)

        return R1, R2, R3, R4, I1, I2, I3, V1, V2, V3, V4






def calculate_exeprient_3B(vol1, res1, res2, res3):

        R1 = res1
        R2 = res2
        R3 = res3
        E1 = vol1

        R = np.array([[R1+R3, -R3], [-R3, R2+R3]])
        E = np.array([E1, 0])
        I = np.round((np.linalg.solve(R, E)), 6)
        I1, I2, I3= I[0], I[1], round(I[0] - I[1], 6)
        V1, V2, V3= round(R1*I[0], 6), round(R2*I[1], 6), round(R3*I3, 6),

        return R1, R2, R3, I1, I2, I3, V1, V2, V3









