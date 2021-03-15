from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<command>")
def index(command=None):
    # Load current count
    f = open("lic.txt", "r")
    lic = f.read()
    f.close()
    
    allLics = lic.split('\n')
    
    check = False
    for all in allLics:
        if command == all:
            check=True
            break
    var = 'a'
    if check:
        var = ''
    return render_template("index.html", command = var)


if __name__ == "__main__":
    app.run()