# app.py
import numpy as np
import matplotlib.pyplot as plt
import os
import base64
from io import BytesIO

from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate reactions for multiple point loads
def calculate_reactions_point_loads(point_loads, L):
    total_load = 0
    total_moment = 0
    for load in point_loads:
        total_load += load['magnitude']
        total_moment += load['magnitude'] * load['position']
    R1 = total_load * (L - total_moment) / L
    R2 = total_load - R1
    return R1, R2

# Function to calculate reactions for distributed loads
def calculate_reactions_distributed_loads(distributed_loads, L):
    total_load = 0
    total_moment = 0
    for load in distributed_loads:
        total_load += load['magnitude'] * load['length']
        total_moment += load['magnitude'] * load['length'] * load['position'] + 0.5 * load['magnitude'] * load['length'] ** 2
    R1 = total_load * (L - total_moment) / L
    R2 = total_load - R1
    return R1, R2

# Function to create plots
def create_plots(R1, R2, max_SF, maxBM, u1, u2, L, point_loads, distributed_loads):
    l = np.linspace(0, L, 1000)
    X = []
    SF = []
    M = []

    for x in l:
        # Calculate shear force
        sf = 0
        for load in point_loads:
            sf -= load['magnitude'] * (x >= load['position'])
        for load in distributed_loads:
            sf -= load['magnitude'] * (x >= load['position']) * (x <= load['position'] + load['length'])
        SF.append(sf)

        # Calculate bending moment
        m = 0
        for load in point_loads:
            m -= load['magnitude'] * (x - load['position']) * (x >= load['position'])
        for load in distributed_loads:
            m -= load['magnitude'] * (x - load['position']) * (x >= load['position']) * (x <= load['position'] + load['length'])
        M.append(m)

        X.append(x)

    max_SF = min(SF)
    maxBM = max(M)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

    ax1.plot(X, SF)
    ax1.plot([0, L], [0, 0])
    ax1.set_title("Shear Force Diagram")
    ax1.set_xlabel("Length in {}".format(u2))
    ax1.set_ylabel("Shear Force ({})".format(u1))
    ax1.grid(True)

    ax2.plot(X, M)
    ax2.plot([0, L], [0, 0])
    ax2.set_title("Bending Moment Diagram")
    ax2.set_xlabel("Length in {}".format(u2))
    ax2.set_ylabel("Bending Moment ({})".format(u1))
    ax2.grid(True)

    plt.tight_layout()

    # Convert plot to base64-encoded string
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

    plt.close()

    return plot_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    point_loads = []
    distributed_loads = []
    for key, value in request.form.items():
        if key.startswith('point_load_magnitude'):
            index = key.split('_')[-1]
            point_loads.append({
                'magnitude': float(value),
                'position': float(request.form[f'point_load_position_{index}'])
            })
        elif key.startswith('distributed_load_magnitude'):
            index = key.split('_')[-1]
            distributed_loads.append({
                'magnitude': float(value),
                'length': float(request.form[f'distributed_load_length_{index}']),
                'position': float(request.form[f'distributed_load_position_{index}'])
            })

    L = float(request.form['length'])

    R1_point, R2_point = calculate_reactions_point_loads(point_loads, L)
    R1_distributed, R2_distributed = calculate_reactions_distributed_loads(distributed_loads, L)

    R1 = R1_point + R1_distributed
    R2 = R2_point + R2_distributed

    plot_data = create_plots(R1, R2, None, None, None, None, L, point_loads, distributed_loads)

    return render_template('result.html', R1=R1, R2=R2, plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)
