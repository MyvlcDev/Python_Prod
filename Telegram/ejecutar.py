import subprocess

def run_script():
    result = subprocess.run(["py.exe", "ipPublica.py"], capture_output=True, text=True)
    print("Output of script.py:")
    print(result.stdout)

if __name__ == "__main__":
    run_script()