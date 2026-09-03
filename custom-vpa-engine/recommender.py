# recommender.py
import time

def run_recommender():
    print("[Recommender] Starting VPA Recommender loop...")
    # Simulating historical usage metrics polled from metrics-server
    historical_cpu_samples = [30, 45, 120, 250, 40, 35]
    
    for i, usage in enumerate(historical_cpu_samples, 1):
        print(f"\n[Recommender] Cycle {i}: Fetched current pod CPU usage -> {usage}m")
        
        # Calculate target (e.g., 85th percentile / safety buffer logic)
        target_cpu = int(usage * 1.25)
        lower_bound = int(target_cpu * 0.7)
        upper_bound = int(target_cpu * 2.0)
        
        print(f"  -> Calculated Recommendation:")
        print(f"     Target CPU : {target_cpu}m")
        print(f"     Lower Bound: {lower_bound}m")
        print(f"     Upper Bound: {upper_bound}m")
        
        time.sleep(1.5)

if __name__ == "__main__":
    run_recommender()
