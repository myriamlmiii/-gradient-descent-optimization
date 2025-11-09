# 🌄 Gradient Descent Optimization from Scratch

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-gray?logo=numpy)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-darkblue?logo=plotly)](https://matplotlib.org/)
[![Status](https://img.shields.io/badge/Status-Complete-success)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Made with ❤️ by Mimi](https://img.shields.io/badge/Made%20with%20❤️%20by-Mimi-pink)](https://github.com/myriamlmi)

> *A complete, from-scratch implementation of Gradient Descent — exploring how machines “learn” to minimize error through mathematics.*

---

## 🧠 Overview

This project dives deep into **Gradient Descent**, one of the most fundamental optimization algorithms in machine learning.  
All implementations were built **entirely from scratch in Python**, without any machine learning libraries — focusing on pure algorithmic understanding.

> 🎯 **Goal:** Experiment with different types of gradient descent (single variable, multivariable, adaptive) to understand convergence behavior, learning rates, and optimizer performance.

---

## 🧩 Core Experiments

| Experiment | Description | File |
|-------------|-------------|------|
| 🧮 **Q1: Basic Gradient Descent** | Implemented gradient descent on `y = (3x + 5)²` | `question1.py` |
| ⚙️ **Q2: Precision Stop** | Added a precision-based stopping condition to halt convergence automatically | `question2.py` |
| 📈 **Q3: Learning Rate Analysis** | Compared convergence speed and stability across various learning rates | `question3.py` |
| 🧭 **Q4: Multivariable Descent** | Extended the algorithm to optimize a 2-variable function `f(x, y)` | `question4.py` |
| 🤖 **Q5: ADAM Optimizer** | Implemented the adaptive moment estimation (ADAM) optimizer manually | `question5.py` |

---

## 📊 Key Results

| Experiment | Outcome |
|-------------|----------|
| **Basic GD** | Smooth convergence with correct step updates |
| **Precision Stop** | Faster runtime through dynamic termination |
| **Learning Rate Tests** | Optimal range found around 0.01–0.05 |
| **Multivariable GD** | Nonlinear 3D descent accurately visualized |
| **ADAM Optimizer** | Reached minimum faster and more smoothly |

---

## ⚙️ Technologies

| Library | Use |
|----------|------|
| **NumPy** | Numerical computation and gradient calculations |
| **Matplotlib** | 2D/3D plotting for convergence paths and analysis |
| *(Future Work)* | Seaborn · Plotly · Streamlit · Dash |

---


---

## 🪄 Visuals

*(Visuals generated via Matplotlib)*

| Algorithm | Visualization |
|------------|----------------|
| Gradient Descent | ![2D Descent Example](assets/gradient_descent_plot.png) |
| Multivariable GD | ![3D Path Example](assets/multivariable_descent.png) |
| ADAM Optimizer | ![ADAM Trajectory](assets/adam_optimizer.png) |

---

## 💡 Insights & Learnings

- The **learning rate** controls convergence — too high overshoots, too low slows progress.  
- **Precision stopping** makes optimization more efficient.  
- **ADAM** adapts learning rate dynamically, offering smoother convergence.  
- Visualization is key to understanding optimization behavior intuitively.  

> ✨ *Gradient descent may go down, but your understanding goes up.*

---

## 🚀 Future Improvements

- 🎛️ Add interactive dashboards with **Streamlit/Dash**  
- 📊 Implement real-time visualization with **Plotly**  
- 🧩 Integrate **TensorFlow/PyTorch** for neural network optimization demos  
- 🌐 Publish a web-interactive version using **nbconvert + HTML/CSS**

---

## 👩‍💻 Contributors

| Name | Role |
|------|------|
| **Meriem Lmoubariki (Mimi)** | Algorithm Design, Implementation, Analysis |
| **Adam Mohammed Sterhaltou** | Visualization, Experimental Design |
| **Dr. Tajjeeddine Rachidi** | Supervising Professor |

---

## 📚 References

- [Gradient Descent From Scratch – CamNZ (GitHub)](https://github.com/CamNZ/gradient-descent-from-scratch)  
- [Gradient Descent Step-by-Step (YouTube)](https://www.youtube.com/watch?v=sDv4f4s2SB8)  
- [Backpropagation Explained (YouTube)](https://www.youtube.com/watch?v=iyn2zdALii8)

---

## 🏁 Conclusion

This project bridges **theory and practice**, transforming the math behind optimization into visual, interpretable code.  
By implementing everything from scratch, we built a strong foundation for future work in **machine learning, deep learning, and optimization research**.

> 💫 *“The gradient may descend, but our understanding rises.”*

---

### ⭐ If you like this project...
Give it a star on GitHub 🌟 and check out more of my work on [@myriamlmi](https://github.com/myriamlmi)

