
# Import necessary libraries
from NetworkModel import NetworkModel
import numpy as np
import tkinter as tk

# Define constants
SPECIFIC_TIME = 1
TIME_STEPS = 10
GRID_SIZE = 10
value_layers = []
inital_collagen = 0.25

# Generate value layers
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        tgf_beta = (0.72 - (i * 0.08))
        il_1_beta = il_6 = tnfa = j * 0.08
        value_layers.append([tgf_beta, il_1_beta, il_6, tnfa, inital_collagen])

# Array for holding values of collagen for each grid cell (assuming there is a fibroblast)
collagen_values = []

# Simulate the collagen production for different input conditions
for x in range(len(value_layers)):

    results_list = [] # Holds the results of the network model
    current_value_layer = value_layers[x] # Different value layer each time

    # Species parameters
    tau = np.array([1, 1.000000e-01, 10, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1, 1.000000e-01, 1, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1, 1.000000e-01, 1.000000e-01, 10, 10, 1.000000e-01, 1, 1.000000e-01, 1, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1, 1.000000e-01, 1.000000e-01, 1, 1.000000e-01, 1, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1.000000e-01, 1, 1, 10, 1.000000e-01, 1.000000e-01, 10, 1.000000e-01, 10, 10, 1.000000e-01, 10, 10, 10, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 1, 1, 10, 10, ])
    ymax = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5.000000e-01, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5.000000e-01, 5.000000e-01, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ])
    y0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

    # Reaction parameters
    w = [2.500000e-01, 2.500000e-01, 2.500000e-01, 2.500000e-01, 2.500000e-01, 2.500000e-01, 2.500000e-01, 2.500000e-01, 2.500000e-01, 2.500000e-01, 2.500000e-01, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
    n = np.array([1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, 1.400000e+00, ])
    EC50 = np.array([6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, 6.000000e-01, ])

    # ALL species involved in the network model
    speciesNames = ['AngII', 'AT1R', 'AGT', 'ACE', 'NOX', 'ROS', 'ET1', 'ETAR', 'DAG', 'PKC', 'TRPC', 'NE', 'BAR',
                    'Forskolin', 'AC', 'cAMP', 'PKA', 'CREB', 'CBP', 'TGFB', 'TGFB1R', 'smad3', 'smad7', 'latentTGFB',
                    'BAMBI', 'PDGF', 'PDGFR', 'NP', 'NPRA', 'cGMP', 'PKG', 'mechanical', 'B1int', 'Rho', 'ROCK', 'Ca',
                    'calcineurin', 'NFAT', 'IL6', 'gp130', 'STAT', 'IL1', 'IL1RI', 'TNFa', 'TNFaR', 'NFKB', 'PI3K',
                    'Akt', 'p38', 'TRAF', 'ASK1', 'MKK3', 'PP1', 'JNK', 'abl', 'Rac1', 'MEKK1', 'MKK4', 'ERK', 'Ras', 'Raf',
                    'MEK1', 'FAK', 'epac', 'Factin', 'FA', 'migration', 'cmyc', 'CTGF', 'proliferation', 'SRF', 'EDAFN',
                    'aSMA', 'AP1', 'TIMP1', 'TIMP2', 'PAI1', 'proMMP14', 'proMMP1', 'proMMP2', 'proMMP9', 'MMP1',
                    'MMP2', 'MMP9', 'MMP14', 'fibronectin', 'periostin', 'CImRNA', 'CIIImRNA', 'CI', 'CIII', 'latentTGFB_ABM',
                    'IL1_ABM', 'IL6_ABM', 'TNFa_ABM', 'Collagen']

    # Placeholders to keep track of weights and collagen for time steps
    w_IL6 = 0
    w_IL1 = 0
    w_TNFa = 0
    w_TGFB = 0
    collagen = 0

    for x in range(TIME_STEPS):

        # Set initial values for first run of simulation
        if x == 0:
            w[1] = current_value_layer[0] # TGFB
            w[3] = current_value_layer[1] # IL6
            w[4] = current_value_layer[1] # IL1
            w[5] = current_value_layer[1] # TNFa
            new_y0 = y0 + current_value_layer

        # Update values each time after the first simulation
        else:
            w[1] = w_TGFB  # TGFB
            w[3] = w_IL6  # IL6
            w[4] = w_IL1  # IL1
            w[5] = w_TNFa  # TNFa

            new_y0 = results_list

        # Simulate the network model
        networkModel = NetworkModel(specific_time=SPECIFIC_TIME, species_names=speciesNames)
        networkModel.set_params(tau_values=tau, y_max_values=ymax, w_values=w, n_values=n, ec50_values=EC50)
        results_list = networkModel.return_numpy_array([0, SPECIFIC_TIME], new_y0)

        # Calculate updated weights
        w_IL6 = results_list[speciesNames.index('IL6_ABM')] / (results_list[speciesNames.index('IL6_ABM')] + 462000)
        w_IL1 = results_list[speciesNames.index('IL1_ABM')] / (results_list[speciesNames.index('IL1_ABM')] + 8750)
        w_TNFa = results_list[speciesNames.index('TNFa_ABM')] / (results_list[speciesNames.index('TNFa_ABM')] + 323)

        TGFB_ABM = 0.045 * results_list[speciesNames.index('latentTGFB_ABM')]
        w_TGFB = TGFB_ABM / (TGFB_ABM + 700)

        # Stores value of collagen
        collagen = results_list[speciesNames.index('Collagen')]

    # Displays collagen for each grid cell to the output
    print(collagen)

    # Appends each grid cell of collagen to a list keeping tracking of all values
    collagen_values.append(collagen)


# Allows for the Color Gradient in each of the cells of the grid showing collagen
def scale_color(value):
    # Convert value from 0 to 1 to a shade of grey (0:black, 0.6:white)
    shade = int(float(value * 152))  # Scale to range from 0 to 153 (0.6 * 255)
    color = "#{:02x}{:02x}{:02x}".format(shade, shade, shade)  # Convert to hexadecimal color code
    return color

# Creates the grid to see values of collagen in each cell
def create_grid(values):
    root = tk.Tk()
    root.title("Grid Display")

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if len(values) > 0:
                value = float(values.pop(0))
                color = scale_color(value)
            else:
                value = 0.0
                color = "white"
            label = tk.Label(root, text=str(value), borderwidth=1, relief="solid", width=10, height=5, bg=color)
            label.grid(row=i, column=j)

    root.mainloop()


# Rounds all the values in the list to 4 decimal places as to not make it too long
rounded_values = [ '%.4f' % elem for elem in collagen_values]
print(rounded_values)

# Displays the Grid
create_grid(rounded_values)
