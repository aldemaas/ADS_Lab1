
import subprocess

ARRAY_KB = 1024
NUM_REPETITIONS = 110000000

def run_simulation(array_kb, num_repetitions):
    
    command = [
        "java", "-cp", "bin:lib/*", "BenchmarkAcessoMemoria",
        str(array_kb), str(num_repetitions)
    ]

    subprocess.run(command)

run_simulation(ARRAY_KB, NUM_REPETITIONS)