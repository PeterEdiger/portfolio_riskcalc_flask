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
    kurs_str = request.args.get("kurs")
    stop_dollar_str = request.args.get("stop_loss_dollar")
    stop_prozent_str = request.args.get("stop_loss_prozent")

    if kurs_str == "":
        # Fall 1
        return render_template("calc_result.html", user_warning="Bitte Kurs eingeben")

        # Fall 2 bis 5
    kurs_int = int(kurs_str)
    if stop_dollar_str == "" and stop_prozent_str == "":
        # Fall 2
        return render_template("calc_result.html", user_warning="Bitte Stop-Loss $"
                                                                "oder Stop-Loss % angeben")
    if stop_dollar_str == "" and stop_prozent_str:
        # Fall 3
        dollar_int = kurs_int * (100 - int(stop_prozent_str)) / 100
        return render_template("calc_result.html", kurs=kurs_int, stop_dollar=dollar_int,
                               verlust_dollar=kurs_int - dollar_int)

    return render_template("calc_result.html", user_warning = "Fall 4, 5")

    # stop_prozent_int = 100 * stop_dollar_int // kurs_int

    # profit_dollar = int(request.args.get("take_profit_dollar"))
    # profit_prozent = int(request.args.get("take_profit_prozent"))
    # verlust_dollar, verlust_prozent = loss_dollar_calc(kurs_int, stop_dollar_int)
    # stop_prozent_int = float(int(stop_loss_prozent))
    # verlust_in_prozent = 100 * (kurs_int - stop_dollar_flt) / kurs_int


if __name__ == '__main__':
    app.run(debug=True)

# Todos

# todo Die Html forms sollen ausgefüllt bleiben, (vertagt)
#  Html forms sollen wenn es Sinn macht automatisch ausgefüllt werden (vertagt)
# todo Zuendeführen der Stop-Loss Fälle / Variablen bennenen nach threshold und difference
# todo requirements für Papa und Einladung
# todo leere Felder der HTML-Form zulassen (Für Losses erledigt)
#  Was soll bei Den Möglichen Fällen für Stop-Loss passieren z.B Stop-Dollar gefüllt, Stop-Prozent leer.
# todo Ausgabe: Verlust in $ und %, Gewinn in $ und %
# todo Was sind decorators in Python https://www.programiz.com/python-programming/decorator
