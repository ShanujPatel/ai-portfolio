projects = ["Website refresh", "Fabric migration", "Copilot pilot", "HR portal"]
for project in projects:
    print(project)

for number, project in enumerate(projects, start=1):
    print(f"{number}. {project}")


name = input("Enter your name: ")
print(f"Hello, {name}! Here are your projects:")