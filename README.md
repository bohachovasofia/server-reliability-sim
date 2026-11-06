# Monte Carlo System Reliability Simulator 📊

A modular Python simulation project that models and compares the reliability of **sequential** and **redundant** server architectures using the Monte Carlo method and Exponential distribution ($\text{Exp}(\lambda)$).

## 🚀 Features
- **Modular Architecture:** Clean separation of concerns (`constants.py`, `simulator.py`, `main.py`).
- **Statistical Modeling:** Generates synthetic server lifetimes based on failure rates ($\lambda$).
- **System Analysis:** Computes and compares theoretical MTTF (Mean Time To Failure) formulas against empirical Monte Carlo simulation results ($N = 1000$).
- **Interactive CLI:** A user-friendly command-line menu to run specific simulations.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Library:** NumPy (vectorized operations for performance)
- **Version Control:** Git & GitHub

## ⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
2. pip install -r requirements.txt
3. python main.py

