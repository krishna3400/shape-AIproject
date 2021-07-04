import bcrypt
from flask import flash

password = b"setpassword55"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# username: = request.form.get("username") #or email
# password = request.form.get("password").encode("utf-8")

if bcrypt.checkpw(password, hashed):
    print("it matches!")
    # return redirect(url_for("user_profile"))
else:
    print("didn't match")
    flash("invalide credentials", "warning")

import time

start = time.time()
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
end = time.time()
f = end - start

# print(f)
