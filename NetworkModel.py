import pandas as pd
import numpy as np
from scipy.integrate import ode
import NetfluxODE


class NetworkModel:

    # Specific time and species name to initialize NetworkModel Object
    def __init__(self, specific_time, species_names):
        self.species_names = species_names
        self.specific_time = specific_time
        self.params = None

    # Sets the default parameters needed to calculate y
    def set_params(self, tau_values, y_max_values, w_values, n_values, ec50_values):
        self.params = [tau_values, y_max_values, w_values, n_values, ec50_values]

    # Runs the simulation (came with original ODE Model from Saucerman and I haven't changed it)
    def run_simulation(self, tspan, y0):
        if self.params is None:
            raise ValueError("Parameters are not set. Call set_params method before running the simulation.")

        t = []
        dt = tspan[1] / ((self.specific_time * 150) / 10)
        r = ode(NetfluxODE.ODEfunc).set_integrator('vode', method='adams', order=10, rtol=0, atol=1e-6,
                                                   with_jacobian=False)
        r.set_initial_value(y0, tspan[0]).set_f_params(*self.params)
        results = np.empty([0, len(self.species_names)])
        while r.successful() and r.t <= tspan[1]:
            r.integrate(r.t + dt)
            results = np.append(results, [r.y], axis=0)
            t.append(r.t)
        return t, results

    # Runs the simulation and returns a numpy array with the results of the model
    def return_numpy_array(self, tspan, y0):
        if self.params is None:
            raise ValueError("Parameters are not set. Call set_params method before running the simulation.")
        t, results = self.run_simulation(tspan, y0)
        index = int((self.specific_time - tspan[0]) / (tspan[1] / ((self.specific_time * 150) / 10))) - 1
        results_list = results[index, :]
        return np.array(results_list)
