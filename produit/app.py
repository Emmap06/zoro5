from flask import Flask, render_template,request, url_for, redirect,flash
from flask_mysql_connector import MySQL
import MySQLdb.cursors
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)

app.secret_key = 'message'  # Remplacez par une clé secrète sécurisée


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DATABASE'] = "gestion_magasin"

mysql = MySQL(app)

@app.route('/', methods=['POST','GET'])
def first():
    if request.method == 'POST':
        username = request.form['identifiant']
        password = request.form['password']
        print("BIENVENU", username)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT mot_pass FROM utlisateur WHERE identifiant = %s', (username,))
        user = cursor.fetchone()
        cursor.close()
        if user and check_password_hash(user[0], password):
            flash('Connexion réussie', 'success')
            return redirect(url_for('sixth'))
        else:
            flash('Identifiant ou mot de passe incorrect', 'danger')
        return redirect(url_for('first'))
    return(render_template('page_connexion.html'))

@app.route('/page_connexion', methods=['POST','GET'])
def first1():

    return(render_template('page_connexion.html'))

@app.route('/nouveau_compte', methods=['POST','GET'])
def nouveau_compte():
    if request.method=='POST':
        identifiant = request.form['nouvel_identifiant']
        mot_de_passe = request.form['nouveau_mot_de_passe']
        hashed_password = generate_password_hash(mot_de_passe, method='sha256')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('INSERT INTO utlisateur (identifiant, mot_pass) VALUES (%s, %s)', (identifiant, hashed_password))
            mysql.connection.commit()
            flash('Compte créé avec succès. Vous pouvez maintenant vous connecter.', 'success')
            return redirect(url_for('first1'))
        except:
            mysql.connection.rollback()
            flash('Cet identifiant existe déjà. Choisissez un autre.', 'danger')
        finally:
            cursor.close()
        return redirect(url_for('nouveau_compte'))
    return(render_template('nouveau_compte.html'))

@app.route('/accueil/')
def sixth():
    return(render_template('accueil.html'))

@app.route('/list_magasin/', methods=['POST','GET'])
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
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM produit")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('list_produit.html', listes=listes)


@app.route('/ajout_produit', methods=['POST', 'GET'])
def seventh():
    if request.method == 'POST':

        nom = request.form['nom']
        categorie = request.form['categorie']
        description= request.form['description']
        prix = request.form['prix']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor )
        cursor.execute("INSERT INTO produit (NomProduit,Categorie,Description,prixUnitaire) VALUES (%s, %s,%s, %s)", (nom,categorie,description,prix))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for("eight"))
    return render_template("ajout_produit.html")


@app.route('/enregistrer_prod/')
def eight():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM produit")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('enregistrer_prod.html', listes=listes)

@app.route('/modif_produit/<int:id>', methods=['GET', 'POST'])
def nineth(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    requete = "SELECT * FROM produit WHERE produitid = %s"
    cursor.execute(requete, (id,))
    elements = cursor.fetchone()
    cursor.close()

    if request.method == 'POST':
        id = request.form['id']
        nouveau_nom = request.form['nom']
        nouvel_categorie = request.form['categorie']
        nouveau_description = request.form['description']
        nouvel_prix = request.form['prix']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "UPDATE produit SET ProduitID=%s,  nomproduit = %s, categorie = %s, description = %s, prixunitaire = %s WHERE produitID = %s",
            (id, nouveau_nom, nouvel_categorie, nouveau_description, nouvel_prix, id))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('tenth'))
    return (render_template("modif_produit.html", elements=elements))

@app.route('/produit_modifie/')
def tenth():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM produit")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('produit_modifie.html', listes=listes)

@app.route('/valid_sup/<int:id>', methods=['GET', 'POST'])
def eleventh(id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM magasin WHERE magasinID = %s", (id,))
    elements = cursor.fetchone()
    cursor.close()
    if request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("DELETE FROM magasin WHERE magasinid = %s", (id,))
        mysql.connection.commit(  )
        cursor.close()
        return redirect(url_for('fifth4'))

    return render_template("valid_sup.html", elements=elements)


@app.route('/effectue/')
def twelveth():
    return(render_template("effectue.html"))


@app.route('/liste_vente/')
def vente():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM vente")
    listes = cursor.fetchall()
    cursor.close()
    return render_template('liste_vente.html', listes=listes)

@app.route('/ajout_vente', methods=['POST', 'GET'])
def ajout_vente():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT ProduitID, NomProduit FROM Produit')
    produits = cursor.fetchall()
    print(produits)
    cursor.execute('SELECT MagasinID, NomMagasin FROM Magasin')
    magasins = cursor.fetchall()
    print(magasins)
    cursor.close()

    if request.method == 'POST':
        mag = request.form["magasin"]
        pro = request.form["produit"]
        quantite = request.form["quantite"]
        date = request.form["date"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT PrixUnitaire FROM Produit WHERE ProduitID = %s', (pro,))
        produit = cursor.fetchone()

        if produit:
            prix_unitaire = produit[0]
            montant_total = float(prix_unitaire) * int(quantite)

            # Enregistrement de la vente dans la base de données
            cursor.execute(
                'INSERT INTO Vente (DateVente, MagasinID, ProduitID, QuantiteVendue, MontantTotal) VALUES (%s, %s, %s, %s, %s)',
                (date, mag, pro, quantite, montant_total))
            mysql.connection.commit()
            flash('Vente ajoutée avec succès', 'success')
            cursor.close()
            return redirect(url_for('vente'))
        else:
            flash('Produit non trouvé', 'danger')
            cursor.close()
            return redirect(url_for('ajout_vente'))
    return render_template('ajout_vente.html', produits=produits, magasins=magasins)

if __name__ == '__main__':
    app.secret_key = 'message'
    app.run(debug=True)