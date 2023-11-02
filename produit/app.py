from flask import Flask, render_template,request, url_for, redirect,flash
from flask_mysql_connector import MySQL
import MySQLdb.cursors


app = Flask(__name__)

app.secret_key = 'message'  # Remplacez par une clé secrète sécurisée


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DATABASE'] = "gestion_magasin"

mysql = MySQL(app)

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
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
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

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor )
        cursor.execute("INSERT INTO magasin (nomMagasin,adresse,telephone,email) VALUES (%s, %s,%s, %s)", (nom,adresse,telephone,email))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for("fourth"))
    flash('Modification réussie !', 'success')
    return render_template("ajout_mag.html")

@app.route('/enregistrement_mag/')
def fourth():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM magasin")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('enregistrement_mag.html', listes=listes)

@app.route('/modif_magasin/<int:id>', methods=['GET', 'POST'])
def fifth1(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
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
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE magasin SET MagasinID=%s,  nomMagasin = %s, adresse = %s, telephone = %s, email = %s WHERE magasinID = %s", (id,nouveau_nom, nouvel_adresse,nouveau_telephone,nouvel_email, id))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('fifth2'))

    return(render_template("modif_magasin.html", elements=elements))

@app.route('/mag_modifie/')
def fifth2():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM magasin")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('mag_modifie.html', listes=listes)

@app.route('/sup_magasin/')
def fifth3():
    return(render_template("sup_magasin.html"))

@app.route('/effec_magasin/')
def fifth4():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM magasin")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('effec_magasin.html', listes=listes)

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

@app.route('/valid_sup/<int:id>', methods=['GET', 'POST'])
def eleventh(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM magasin WHERE magasinID = %s", (id,))
    elements = cursor.fetchone()
    cursor.close()
    if request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("DELETE FROM magasin WHERE magasinid = %s", (id,))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('fifth4'))

    return render_template("valid_sup.html", elements=elements)


@app.route('/effectue/')
def twelveth():
    return(render_template("effectue.html"))

if __name__ == '__main__':
    app.run(debug=True)