import configparser

filename = "file.ini"

# Writing Data
config = configparser.ConfigParser()
config.read(filename)

try:
    config.add_section("SETTINGS")
except configparser.DuplicateSectionError:
    pass

username = ""
password = ""
email = ""

try:
    username = config.get("SETTINGS", "username")
except Exception as e:
    if not username:
        config.set("SETTINGS", "username", input("Enter a Username : "))

try:
    password = config.get("SETTINGS", "password")
except Exception as e:
    if not password:
        config.set("SETTINGS", "password", input("Enter a Password : "))

try:
    email = config.get("SETTINGS", "email")
except Exception as e:
    if not email:
        config.set("SETTINGS", "email", input("Enter a Email Address : "))

with open(filename, "w") as config_file:
    config.write(config_file)
