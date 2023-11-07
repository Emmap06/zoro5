from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysql_connector import MySQL
import pymysql.cursors


app = Flask(__name__)

app.secret_key = 'message'  # Remplacez par une clé secrète sécurisée


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DATABASE'] = "gestion_magasin"

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def first():
    return(render_template('page_connexion.html'))

@app.route('/page_connexion', methods=['GET', 'POST'])
def first1():
    return(render_template('page_connexion.html'))

@app.route('/accueil', methods=['GET', 'POST'])
def sixth():
    return(render_template('accueil.html'))

@app.route('/list_magasin/')
def second():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM magasin")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('list_magasin.html', listes=listes)

@app.route('/ajout_mag', methods=['POST', 'GET'])
def third():

    if request.method == 'POST':

        nom = request.form['nom']
        adresse = request.form['adresse']
        telephone = request.form['telephone']
        email = request.form['email']

        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor )
        cursor.execute("INSERT INTO magasin (nomMagasin,adresse,telephone,email) VALUES (%s, %s,%s, %s)", (nom,adresse,telephone,email))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for("fourth"))
    flash('Modification réussie !', 'success')
    return render_template("ajout_mag.html")

@app.route('/enregistrement_mag/')
def fourth():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM magasin")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('enregistrement_mag.html', listes=listes)

@app.route('/modif_magasin/<int:id>', methods=['GET', 'POST'])
def fifth1(id):
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    requete = "SELECT * FROM magasin WHERE magasinid = %s"
    cursor.execute(requete, (id,))
    elements = cursor.fetchone()
    cursor.close()

    if request.method == 'POST':
        id = request.form['id']
        nouveau_nom = request.form['nom']
        nouvel_adresse = request.form['adresse']
        nouveau_telephone = request.form['telephone']
        nouvel_email = request.form['email']
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("UPDATE magasin SET MagasinID=%s,  nomMagasin = %s, adresse = %s, telephone = %s, email = %s WHERE magasinID = %s", (id,nouveau_nom, nouvel_adresse,nouveau_telephone,nouvel_email, id))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('fifth2'))

    return(render_template("modif_magasin.html", elements=elements))

@app.route('/mag_modifie/')
def fifth2():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM magasin")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('mag_modifie.html', listes=listes)

@app.route('/sup_magasin/<int:id>', methods=['GET', 'POST'])
def fifth3(id):
    cursor = mysql.connection.cursor(pymysql)
    cursor.execute("SELECT * FROM magasin WHERE magasinID = %s", (id,))
    elements = cursor.fetchone()
    cursor.close()
    if request.method == 'POST':
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("DELETE FROM magasin WHERE magasinid = %s", (id,))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('fifth4'))

    return render_template("sup_magasin.html", elements=elements)

@app.route('/effec_magasin/')
def fifth4():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM magasin")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('effec_magasin.html', listes=listes)

@app.route('/list_produit/')
def sixth2():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM produit")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('list_produit.html', listes=listes)

@app.route('/ajout_produit/', methods=['GET', 'POST'])
def seventh():
    if request.method == 'POST':

        nomProduit = request.form['nomProduit']
        categorie = request.form['categorie']
        prix = request.form['prix']
        quantite = request.form['quantite']

        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO produit (nomProduit,categorie,prix,quantite) VALUES (%s, %s,%s, %s)", (nomProduit,categorie,prix,quantite))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for("eigth"))
    flash('Modification réussie !', 'success')
    return render_template("ajout_produit.html")

@app.route('/enregistrer_prod/')
def eight():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM produit")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('enregistrer_prod.html', listes=listes)

@app.route('/modif_produit/<int:id>', methods=['GET', 'POST'])
def nineth(id):
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    requete = "SELECT * FROM produit WHERE produitid = %s"
    cursor.execute(requete, (id,))
    elements = cursor.fetchone()
    cursor.close()

    if request.method == 'POST':
        id = request.form['id']
        nouveau_nom = request.form['nom']
        nouvelle_categorie = request.form['categorie']
        nouveau_prix = request.form['prix']
        nouvelle_quantite = request.form['quantite']
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "UPDATE produit SET ProduitID=%s,  nomProduit = %s, categorie = %s, prix = %s, quantite = %s WHERE ProduitID = %s",
            (id, nouveau_nom, nouvelle_categorie, nouveau_prix, nouvelle_quantite, id))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('tenth'))

    return (render_template("modif_produit.html", elements=elements))

@app.route('/produit_modifie/')
def tenth():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM produit")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('produit_modifie.html', listes=listes)

@app.route('/valid_sup/<int:id>', methods=['GET', 'POST'])
def eleventh(id):
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM produit WHERE produitID = %s", (id,))
    elements = cursor.fetchone()
    cursor.close()
    if request.method == 'POST':
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("DELETE FROM produit WHERE produitid = %s", (id,))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('twelveth'))

    return render_template("valid_sup.html", elements=elements)


@app.route('/effectue/')
def twelveth():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM produit")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('effectue.html', listes=listes)

if __name__ == '__main__':
    app.run(debug=True)