import subprocess

NUM_THREADS = 12
NUM_MAX = 100000

def run_simulation(num_threads, num_max):
    
    command = [
        "java", "-cp", "bin:lib/*", "BenchmarkNumerosPrimos",
        str(num_threads), str(num_max)
    ]

    subprocess.run(command)
    
run_simulation(NUM_THREADS, NUM_MAX)

