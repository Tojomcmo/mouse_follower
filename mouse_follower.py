import mouse_follower_funcs as mff
import time
from matplotlib import pyplot as plt

sys_state = [0, 0]

kp = 10
ki = 1
kd = 1
k_vec = [kp, ki, kd]

mass = 1
act_saturate = 10000000
dist = 2000

error_past = 0
error_int = 0

start_time = time.time()
print_freq = 0.25

plt.style.use('seaborn-pastel')
plt.ion()

fig = plt.figure()
ax = plt.axes(xlim=(-3000, 3000), ylim=(-1, 1))
line, = ax.plot([], [], lw=3)
plt.show()
y = [0.25, -0.25]
t = 0
dt = 0
print_time = 0
is_print_time = 0
time_vector = [t, dt, print_time, is_print_time]
while 1==1:
    time_vector = mff.time_step(start_time, print_freq, time_vector)
    error_vector = mff.calculate_error(sys_state)
    error_int = error_int + error_vector[1] * time_vector[1]
    act = mff.pid_act(k_vec, error_vector[1], error_past, error_int, time_vector, act_saturate)
    sys_state = mff.plant_dynamics(act, dist, mass, sys_state, time_vector)
    error_past = error_vector[1]
    x = [error_vector[0], sys_state[0]]
    points, = plt.plot(x, y, 'bo')
    plt.draw()
    plt.pause(0.0001)
    points.remove()
    # mff.plot(sys_state, error_vector, fig)
    # if time_vector[3] == 1:
    #     print("ref_pos: " + str(int(error_vector[0])) + " error: " + str(int(error_vector[1])) \
    #           + " sys_pos: " + str(int(sys_state[0])) + " Act: " + str(int(act)) + " time: " + str(int(time_vector[0])) \
    #           + " error past: " + str(int(error_past)) + " error int: " + str(int(error_int)))