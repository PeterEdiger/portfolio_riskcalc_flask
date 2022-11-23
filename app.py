from risk_calculations import loss_dollar_calc
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("home.html")


@app.route('/banking')
def banking():
    return render_template("banking.html")


@app.route('/calc_risk')
def risk_calc():
    return render_template("calc_risk.html")


@app.route('/calc_result', methods=["POST", "GET"])
def calc_result():
    selling_threshold_win_dollar_str = request.args.get("selling_threshold_win_dollar")
    win_prct_str = request.args.get("win_prct")

    # --------------------------------------------------------------------------------#
    # Stückzahl einlesen default Wert = 1
    quantity = request.args.get("quantity")
    if quantity:
        quantity = int(quantity)
    else:
        quantity = 1
    # --------------------------------------------------------------------------------#
    # Kurs einlesen, wenn nicht vorhanden --> user_message
    kurs_str = request.args.get("kurs")
    if kurs_str == "":
        # No price input case
        return render_template("calc_result.html", user_warning="Bitte Kurs eingeben")
    else:
        kurs_int = int(kurs_str)

    # --------------------------------------------------------------------------------#
    total_invest = kurs_int * quantity

    # --------------------------------------------------------------------------------#
    # Stop-Loss %, Stop-Loss $ einlesen / Wenn beide vorhanden -> user_message
    # Stop-Loss $ berechnen.

    selling_threshold_loss_dollar_str = request.args.get("selling_threshold_loss_dollar")
    loss_prct_str = request.args.get("loss_prct")
    # Abkürzungen
    s_t_l_d_s = selling_threshold_loss_dollar_str
    rt = render_template
    # Fall beide vorhanden
    if s_t_l_d_s and loss_prct_str:
        return rt("calc_result.html", user_message="Bitte eine Größe eingeben.")
    # nur Stop-Loss $
    if s_t_l_d_s and not loss_prct_str:
        s_t_l_d_i = int(s_t_l_d_s)
        loss_prct_int = round((kurs_int - s_t_l_d_i) / kurs_int * 100)

    # nur Stop-Loss %
    if not s_t_l_d_s and loss_prct_str:
        loss_prct_int = int(loss_prct_str)
        s_t_l_d_i = kurs_int * ((100 - loss_prct_int) / 100)

    if not s_t_l_d_s and not loss_prct_str:
        s_t_l_d_i = None
        loss_dollar = None
        total_loss = None
        loss_prct_int = None
    # Weil einer der oberen Fälle = True
    else:
        total_loss = quantity * (kurs_int - s_t_l_d_i)
        loss_dollar = kurs_int -s_t_l_d_i
    return rt("calc_result.html", kurs=kurs_int, selling_threshold_loss_dollar=s_t_l_d_i, total_invest=total_invest,
              loss_dollar=loss_dollar, total_loss=total_loss, loss_prct=loss_prct_int)

    return render_template("calc_result.html", user_warning="Abverkaufskurs oder Verlust in Prozent eintragen bitte.")


if __name__ == '__main__':
    app.run(debug=True)

# Todos

# Ideen
"""
Zur Übersicht Funktion bauen: 
1. Berechnet alle gültigen Fälle
2. Kümmert sich um die ungültigen Fälle

Optische Aufteilung der Suchfenster Gewinn rechts neben Verlust 
Abkürzungen benutzen für die Übersicht?
"""
# todo Logik auf Gewinn Möglichkeiten ausweiten. Planung aller Möglichkeiten
# todo Die Html forms sollen ausgefüllt bleiben, (vertagt)
#  Html forms sollen wenn es Sinn macht automatisch ausgefüllt werden (vertagt)
# todo Ausgabe: Verlust in $ und %, Gewinn in $ und %


