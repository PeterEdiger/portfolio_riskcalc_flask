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
    test_request = request.args.get("kurs")

    kurs_int = int(request.args.get("kurs"))
    stop_dollar_int = int(request.args.get("stop_loss_dollar"))

    stop_loss_prozent_str = request.args.get("stop_loss_prozent")
    if stop_loss_prozent_str == "":
        stop_prozent_int = 100 * stop_dollar_int // kurs_int
    else:
        stop_prozent_int = int(stop_loss_prozent_str)

    profit_dollar = int(request.args.get("take_profit_dollar"))
    profit_prozent = int(request.args.get("take_profit_prozent"))
    verlust_dollar, verlust_prozent = loss_dollar_calc(kurs_int, stop_dollar_int)
    # stop_prozent_int = float(int(stop_loss_prozent))
    # verlust_in_prozent = 100 * (kurs_int - stop_dollar_flt) / kurs_int
    return render_template("calc_result.html", kurs=kurs_int, stop_dollar=stop_dollar_int,
                           verlust_dollar=verlust_dollar, stop_prozent_int=stop_prozent_int
                           )


if __name__ == '__main__':
    app.run(debug=True)

# Todos

# todo Die Html forms sollen ausgefüllt bleiben, (vertagt)
#  Html forms sollen wenn es Sinn macht automatisch ausgefüllt werden (vertagt)

# todo leere Felder der HTML-Form zulassen
#  Was soll bei Den Möglichen Fällen für Stop-Loss passieren z.B Stop-Dollar gefüllt, Stop-Prozent leer.
# todo Ausgabe: Verlust in $ und %, Gewinn in $ und %
# todo Was sind decorators in Python https://www.programiz.com/python-programming/decorator
