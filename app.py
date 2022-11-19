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
    selling_threshold_loss_dollar_str = request.args.get("selling_threshold_loss_dollar")
    loss_prct_str = request.args.get("loss_prct")

    if kurs_str == "":
        # Fall 1
        return render_template("calc_result.html", user_warning="Bitte Kurs eingeben")

        # Fall 2 bis 5
    kurs_int = int(kurs_str)
    if selling_threshold_loss_dollar_str == "" and loss_prct_str == "":
        # Fall 2
        return render_template("calc_result.html", user_warning="Bitte Stop-Loss $"
                                                                "oder Stop-Loss % angeben")
    if not selling_threshold_loss_dollar_str and loss_prct_str:
        # Fall 3
        selling_threshold_loss_dollar_int = kurs_int * (100 - int(loss_prct_str)) // 100
        return render_template("calc_result.html", kurs=kurs_int, stop_dollar=selling_threshold_loss_dollar_int,
                               verlust_dollar=kurs_int - selling_threshold_loss_dollar_int)
    if selling_threshold_loss_dollar_str and not loss_prct_str:
        # Fall 4
        selling_threshold_loss_dollar_int = int(selling_threshold_loss_dollar_str)

        return render_template("calc_result.html", kurs=kurs_int, stop_dollar=selling_threshold_loss_dollar_int,
                               verlust_dollar=kurs_int - selling_threshold_loss_dollar_int)

    # Fall 5

    return render_template("calc_result.html", user_warning="Abverkaufskurs oder Verlust in Prozent eintragen bitte.")


if __name__ == '__main__':
    app.run(debug=True)

# Todos

# todo Logik auf Gewinn Möglichkeiten ausweiten. Planung aller Möglichkeiten
# todo Weitere Parameter wie Stückzahl Maximaler Verlust in die Rechnungen einbeziehen.
# todo Die Html forms sollen ausgefüllt bleiben, (vertagt)
#  Html forms sollen wenn es Sinn macht automatisch ausgefüllt werden (vertagt)

# todo Ausgabe: Verlust in $ und %, Gewinn in $ und %
