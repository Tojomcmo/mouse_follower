import time
from pyautogui import position
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('seaborn-pastel')

def time_step(start_time, print_freq, time_vector):
    elapsed_time = time.time() - start_time
    dt = elapsed_time - time_vector[0]
    t = elapsed_time
    print_time = time_vector[2]
    if t - time_vector[2] >= print_freq:
        print_time = t
        is_print_time = 1
    else:
        is_print_time = 0
    t_vector = [t, dt, print_time, is_print_time]
    return t_vector

def calculate_error (sys_state):
    mouse_pos = position()
    ref_pos = mouse_pos[0]-1250
    error = ref_pos - sys_state[0]
    error_vector = [ref_pos, error]
    return error_vector

def pid_act(k_vec, error, error_past, error_int, time_vector, act_saturate):
    error_slope = (error - error_past) / time_vector[1]
    act = k_vec[0] * error + k_vec[1] * error_int + k_vec[2] * error_slope
    if abs(act) > act_saturate:
        act = np.sign(act) * act_saturate
    return act

def plant_dynamics(force, dist, mass, sys_state, time_vector):
    sys_state[1] = sys_state[1] + ((force + dist) / mass) * time_vector[1]
    sys_state[0] = sys_state[0] + sys_state[1] * time_vector[1]
    return sys_state

def plot(sys_state, error_vector):
    plt.clf()
    plt.cla()
    plt.close()
    x1 = error_vector[0]
    x2 = sys_state[0]
    y1 = 0.5
    y2 = -0.5
    plt.plot(x1, y1, 'bo')
    plt.plot(x2, y2, 'bo')
    plt.pause(0.0001)
    return