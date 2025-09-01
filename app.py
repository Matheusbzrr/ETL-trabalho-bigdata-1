from flask import Flask, request, jsonify
import sqlite3
import pandas as pd

DB_FILE = "universidades.db"

app = Flask(__name__)

def total_por_pais():
    with sqlite3.connect(DB_FILE) as conn:
        return pd.read_sql_query("""
            SELECT country, COUNT(*) AS total
            FROM universities
            GROUP BY country
            ORDER BY total DESC
        """, conn)

def universidades_do_pais(pais):
    with sqlite3.connect(DB_FILE) as conn:
        return pd.read_sql_query(f"""
            SELECT name
            FROM universities
            WHERE country = '{pais}'
        """, conn)

def universidades_por_termo(termo):
    with sqlite3.connect(DB_FILE) as conn:
        return pd.read_sql_query(f"""
            SELECT name, country
            FROM universities
            WHERE name LIKE '%{termo}%'
        """, conn)
    
def todas_de_pernambuco():
    with sqlite3.connect(DB_FILE) as conn:
        return pd.read_sql_query(f"""
            SELECT name, country
            FROM universities
            WHERE name LIKE '%Pernambuco%'
            """, conn)


@app.route("/total_por_pais") #http://127.0.0.1:5000/total_por_pais
def api_total_por_pais():
    resp =  total_por_pais().to_json(orient="records", force_ascii=False) 
    return jsonify(resp)


@app.route("/universidades_do_pais") #http://127.0.0.1:5000/universidades_do_pais?pais=Brazil
def api_universidades_do_pais():
    pais = request.args.get("pais")
    resp = universidades_do_pais(pais).to_json(orient="records", force_ascii=False)
    return jsonify(resp)

@app.route("/universidades_por_termo") #http://127.0.0.1:5000/universidades_por_termo?termo=Technology
def por_termo():
    termo = request.args.get("termo")
    resp =  universidades_por_termo(termo).to_json(orient="records", force_ascii=False)
    return jsonify(resp)

@app.route("/todas_de_pernambuco") #http://127.0.0.1:5000/todas_de_pernambuco
def api_universidades_de_pernambuco():
    resp = todas_de_pernambuco().to_json(orient="records", force_ascii=False)
    return jsonify(resp)

if __name__ == "__main__":
    app.run(debug=True)
