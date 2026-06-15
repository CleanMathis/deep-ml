import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places

        1.Listen länge verglecihen, länger = inner Loop
    	2. Liste initialsieren
        3.Loopen und rechen
        4 Ableiten
        5 return

        3.1 Ergebnis Lsite ist die läneg der beiden anderne Listen addiert
        Wert mal wert und dann Index der beiden werte addiern
        dann über den addierten Index zu dem wert in der ErgebnisListe hinzuaddiern

        Ableiten ist Indexposi mal den wert an der stelle der ergebnis Liste
    """
    result = [0] *(len(f_coeffs)+len(g_coeffs)-1)
    list1 = f_coeffs
    list2 = g_coeffs
    if len(list1) <=1 and len(list2) <=1:
        return[0.0]

    for i in range(len(list2)):
        for y in range(len(list1)):
            res = 0
            res_index = i + y
            res = list1[y] * list2[i]
            result[res_index] += res
    
    derivates = [0] * (len(result)-1)
    for x in range(1,len(result)):
        derivates[x-1] = result[x] * x
    
    return derivates
    
    