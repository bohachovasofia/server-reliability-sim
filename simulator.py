import numpy as np

from constants import LAMBDA1, LAMBDA2, N

def run_simulation():
    rng = np.random.default_rng(seed = 42)

    server1_lifetimes = rng.exponential(1/LAMBDA1, N)
    server2_lifetimes = rng.exponential(1/LAMBDA2, N)

    system_min = np.minimum(server1_lifetimes, server2_lifetimes)
    system_max = np.maximum(server1_lifetimes, server2_lifetimes)

    lambda_theory_min = LAMBDA1 + LAMBDA2
    mttf_theory_min = 1 / lambda_theory_min
    mttf_exp_min = np.mean(system_min)

    mttf_theory_max = 1/LAMBDA1 + 1/LAMBDA2 - 1/lambda_theory_min
    mttf_exp_max = np.mean(system_max)

    print("=== SERVER SIMULATION RESULTS (N = 1000) ===\n")

    print("1. Sequential System (first failure breaks all -> min(X, Y)):")
    print(f"   - Theoretical Mean Time To Failure (MTTF):    {mttf_theory_min:.2f} h")
    print(f"   - Simulated Mean Time To Failure (Monte Carlo): {mttf_exp_min:.2f} h\n")

    print("2. Redundant System (system lives until the last -> max(X, Y)):")
    print(f"   - Theoretical Mean Time To Failure (MTTF):    {mttf_theory_max:.2f} h")
    print(f"   - Simulated Mean Time To Failure (Monte Carlo): {mttf_exp_max:.2f} h\n")

    print("--- First 5 Sessions Example (in hours) ---")
    for i in range(5):
        s1 = server1_lifetimes[i]
        s2 = server2_lifetimes[i]
        print(f"Session {i+1}: Server1 = {s1:.1f}h | Server2 = {s2:.1f}h | Min = {min(s1, s2):.1f}h | Max = {max(s1, s2):.1f}h")



