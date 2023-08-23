import subprocess

data = [1,2214,123,"ahoj"]

s=open("data.txt","w")
for r in data:
    s.write(f"{r}\n")
s.close()

# subprocess.run("notepad.exe data.txt")

proces = subprocess.run("ifconfig",capture_output=True,text=True)
print(proces.stdout)

print("jede se dal ....")