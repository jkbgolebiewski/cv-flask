import os
import yaml
from flask import Flask, render_template

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Jakub Gołębiewski")
environment = "development"

# Load info.yml file
with open('info.yml', encoding='utf-8') as f:
    try:
        info = yaml.load(f, Loader=yaml.FullLoader)
    except yaml.YAMLError as e:
        print(f"Error loading YAML file: {e}")
        info = {}


@app.route("/")
def profile():
    # Validate keys within info for 'profile' and 'other'
    profile_data = info.get("profile", {})
    other_data = profile_data.get("other", {})

    # Ensure 'other' is a dictionary, fallback to an empty dict if not
    if not isinstance(other_data, dict):
        other_data = {}

    # Pass updated info object with validated data
    profile_data['other'] = other_data
    info["profile"] = profile_data

    return render_template("profile.html", info=info)


@app.route("/education")
def education():
    return render_template("education.html", info=info)


@app.route("/experience")
def experience():
    return render_template("experience.html", info=info)

if __name__ == "__main__":
    debug = False
    if environment == "development" or environment == "local":
        debug = True
    print("Local change.")
    app.run(host="0.0.0.0", debug=debug)