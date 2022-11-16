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
    kurs = request.args.get("kurs")
    stop_loss_dollar = request.args.get("stop_loss_dollar")
    stop_loss_prozent = request.args.get("stop_loss_prozent")
    kurs_int = int(float(kurs))
    stop_dollar_flt = int(float(stop_loss_dollar))
    stop_prozent_flt = int(float(stop_loss_prozent))
    verlust_in_prozent = 100 * (kurs_int - stop_dollar_flt) / kurs_int
    return render_template("calc_result.html", kurs=kurs_int,
                           stop_prozent=stop_prozent_flt, stop_dollar=stop_dollar_flt)


if __name__ == '__main__':
    app.run(debug=True)
