from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def calculate_sfd_bmd(P, L, a):
    R1 = P * (L - a) / L
    R2 = P - R1

    l = np.linspace(0, L, 1000)
    X = []
    SF = []
    M = []

    for x in l:
        if x <= a:
            m = R1 * x
            sf = R1
        elif x > a:
            m = R1 * x - P * (x - a)
            sf = -R2
        M.append(m)
        X.append(x)
        SF.append(sf)

    max_SF = max(SF)
    maxBM = max(M)

    maxBM_index = M.index(maxBM)
    maxBM_position = round(l[maxBM_index], 3)

    return R1, R2, X, SF, M, max_SF, maxBM, maxBM_position

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def result():
    P = float(request.form['load'])
    L = float(request.form['length'])
    a = float(request.form['distance'])

    R1, R2, X, SF, M, max_SF, maxBM, maxBM_position = calculate_sfd_bmd(P, L, a)

    # Plotting
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(X, SF)
    plt.plot([0, L], [0, 0])
    plt.plot([0, 0], [0, R1], [L, L], [0, -R2])
    plt.title("SFD")
    plt.xlabel("Length in m")
    plt.ylabel("Shear Force")

    plt.subplot(1, 2, 2)
    plt.plot(X, M)
    plt.plot([0, L], [0, 0])
    plt.title("BMD")
    plt.xlabel("Length in m")
    plt.ylabel("Bending Moment")

    # Save plot to a bytes object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('result.html', R1=R1, R2=R2, max_SF=max_SF, maxBM=maxBM,
                        maxBM_position=maxBM_position, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
