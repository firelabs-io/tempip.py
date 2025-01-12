## generates basic template ##
import sys
import os

def setupy(project):
    if os.getenv("CI") == "true":
        version = "1.0.0" 
        require = "numpy" 
    else:
        version = input("Version> ")
        require = input("Requires (e.g numpy, separate by ',')> ")
    dependencies = [dep.strip() for dep in require.split(',')]
    setup_content = f"""
from setuptools import setup, find_packages

setup(
    name='{project}',        
    version='{version}',     
    packages=find_packages(),
    install_requires={dependencies},
    entry_points={{
        'console_scripts': [
            '{project}-cli={project}.cli:main', 
        ],
    }},
)
"""
    with open(f"{project}/setup.py", 'w') as file:
        file.write(setup_content)
if __name__ == '__main__':
    if os.getenv("CI") == "true":
        project = "default_project_name" 
    else:
        project = sys.argv[1] if len(sys.argv) > 1 else input("Enter project name> ")
    os.makedirs(project, exist_ok=True)
    os.makedirs(f"{project}/{project}", exist_ok=True)
    os.makedirs(f"{project}/test", exist_ok=True)
    setupy(project)
    with open(f"{project}/{project}/__init__.py", 'w') as f: f.write("import pytest\n")
    with open(f"{project}/test/test.py", 'w') as f: f.write("import pytest\n")
    with open(f'{project}/README.md', 'w') as file: pass
    with open(f"{project}/LICENSE", 'w') as f: pass
    print(f"GENERATED TEMPLATE AT '{project}/'")
    print("Edit README.md and LICENSE as you please.")
