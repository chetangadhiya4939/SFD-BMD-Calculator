````markdown
# 🧮 SFD & BMD Calculator (Shear Force & Bending Moment Diagram)

[![Stars](https://img.shields.io/github/stars/chetangadhiya4939/SFD-BMD-Calculator?style=social)](https://github.com/chetangadhiya4939/SFD-BMD-Calculator/stargazers)
[![Forks](https://img.shields.io/github/forks/chetangadhiya4939/SFD-BMD-Calculator?style=social)](https://github.com/chetangadhiya4939/SFD-BMD-Calculator/network/members)
[![License](https://img.shields.io/github/license/chetangadhiya4939/SFD-BMD-Calculator)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/chetangadhiya4939/SFD-BMD-Calculator)](https://github.com/chetangadhiya4939/SFD-BMD-Calculator/commits/main)

This Python tool calculates and visualizes **Shear Force Diagrams (SFD)** and **Bending Moment Diagrams (BMD)** for beams under various types of loading conditions. It's ideal for engineering students and professionals working with structural mechanics.

---

## 📌 Features

- 🧱 Supports **Point Load**, **Uniformly Distributed Load (UDL)**, and **Moment Load**
- 📈 Plots clear and scalable **SFD** and **BMD** diagrams using Matplotlib
- 🧮 Computes key values: reactions, shear forces, and bending moments
- ✅ Simple CLI-based user interaction
- 📂 Extensible structure for future GUI integration

---

## 🛠️ Tech Stack

| Technology | Description |
|------------|-------------|
| `Python`   | Core programming language |
| `Matplotlib` | Diagram plotting |
| `NumPy`    | Numerical calculations |

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/chetangadhiya4939/SFD-BMD-Calculator.git
cd SFD-BMD-Calculator
````

### 2. Install Dependencies

```bash
pip install matplotlib numpy
```

### 3. Run the Calculator

```bash
python main.py
```

---

## 📸 Screenshots

> *(Add actual screenshots and update image paths accordingly)*

### 📋 Input Section

![Input](https://via.placeholder.com/600x300?text=Input+CLI)

### 📉 Shear Force Diagram (SFD)

![SFD](https://via.placeholder.com/600x300?text=SFD+Diagram)

### 📊 Bending Moment Diagram (BMD)

![BMD](https://via.placeholder.com/600x300?text=BMD+Diagram)

---

## 🧠 Example Input

```text
Enter beam length: 10
Number of point loads: 1
Load 1 position and magnitude: 5 20

Number of UDLs: 1
UDL 1 start, end, and intensity: 2 8 5

Number of moments: 0
```

> The system calculates reactions, SFD values, and BMD values and plots them using Matplotlib.

---

## 📁 Folder Structure

```
SFD-BMD-Calculator/
├── main.py              # Main script
├── beam.py              # Core classes and methods
├── load.py              # Load modeling
├── sfd_bmd.py           # SFD & BMD logic and plotting
├── utils.py             # Helper functions (if any)
└── README.md
```

---

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=chetangadhiya4939&show_icons=true&theme=merko" width="48%" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=chetangadhiya4939&theme=merko" width="48%" />
</p>

---

## 🧩 Future Improvements

* [ ] GUI interface using Tkinter or PyQt
* [ ] Add support for cantilever and fixed beams
* [ ] Save/load beam configurations
* [ ] Interactive plot zooming and annotations

---

## 🤝 Contributors

* [Chetan Gadhiya](https://github.com/chetangadhiya4939)

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 🌟 Show Your Support

If you found this project helpful or interesting, **please give it a ⭐️** and share it with your peers!

```
