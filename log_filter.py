logs = [
    "login success from 10.0.0.1",
    "login failed from 10.0.0.5",
    "login failed from 10.0.0.5",
    "login success from 10.0.0.2",
    "login failed from 10.0.0.9",
]

for line in logs:
    if "failed" in line:
        print(line)