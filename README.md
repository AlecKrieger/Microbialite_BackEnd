# Microbialite_BackEnd

INFO
This is a backend API to create, read, update, and delete microbialte information from a mySQL database. It uses FastAPI to create the web interface, MySQLdb, and PlanetScale cloud database (free tier)

SETUP INSTRUCTIONS

1. Ensure that you have git installed and have a Github account
2. Clone project using the https link: git clone https://github.com/AlecKrieger/Microbialite_BackEnd.git
3. CD into project directory and use pip to install virtualenv if you don't already have it.
4. Create virtual environment using: python3 -m venv env
5. Activate the virtual environment (actual command varries by system)
   1. On mac: "source env/bin/activate"
   2. on pc in CMD: "env/Scripts/activate.bat"
6. If the virtual environment is working, you'll see (env) on the left side of your terminal
7. Install the project dependencies in the requirements folder: "pip install -r requirements.txt"
8. move the .env folder into the project's root folder. This has the connection information to the cloud database
   1. On windows you should be able to replace the value next to CA with an empty string
9.  In the root folder, run: "pip install -e ." to load the packages and create a .egg-info file
10. Try running the API from the CLI: uvicorn main:app --reload


REFERENCES
How to setup a virtual environment in python: https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
How to install dependencies with from requirements.txt: https://www.freecodecamp.org/news/python-requirementstxt-explained/
Using a .env file to store environment variables: https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
Video with the pip install -e . hack: https://www.youtube.com/watch?v=Mgp6-ZMEcE0
