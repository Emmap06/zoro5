from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def first():
    return(render_template('page_connexion.html'))

@app.route('/page_connexion/')
def first1():
    return(render_template('page_connexion.html'))

@app.route('/accueil/')
def sixth():
    return(render_template('accueil.html'))

@app.route('/list_magasin/')
def second():
    return(render_template("list_magasin.html"))

@app.route('/ajout_mag/')
def third():
    return(render_template("ajout_mag.html"))

@app.route('/enregistrement_mag/')
def fourth():
    return(render_template("enregistrement_mag.html"))

@app.route('/modif_magasin/')
def fifth1():
    return(render_template("modif_magasin.html"))

@app.route('/mag_modifie/')
def fifth2():
    return(render_template("mag_modifie.html"))

@app.route('/sup_magasin/')
def fifth3():
    return(render_template("sup_magasin.html"))

@app.route('/effec_magasin/')
def fifth4():
    return(render_template("effec_magasin.html"))

@app.route('/list_produit/')
def sixth2():
    return(render_template("list_produit.html"))

@app.route('/ajout_produit/')
def seventh():
    return(render_template("ajout_produit.html"))

@app.route('/enregistrer_prod/')
def eight():
    return(render_template("enregistrer_prod.html"))

@app.route('/modif_produit/')
def nineth():
    return(render_template("modif_produit.html"))

@app.route('/produit_modifie/')
def tenth():
    return(render_template("produit_modifie.html"))

@app.route('/valid_sup/')
def eleventh():
    return(render_template("valid_sup.html"))

@app.route('/effectue/')
def twelveth():
    return(render_template("effectue.html"))

if __name__ == '__main__':
    app.run(debug=True)