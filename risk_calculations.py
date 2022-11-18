def loss_dollar_calc(kurs_int, stop_dollar_int):
    verlust_dollar = kurs_int - stop_dollar_int
    verlust_prozent = 100 * verlust_dollar // kurs_int
    return verlust_dollar, verlust_prozent

