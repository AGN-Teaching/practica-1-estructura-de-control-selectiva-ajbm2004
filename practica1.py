def calcular_sueldo_neto(salario_por_hora, horas_trabajadas, tipo_caja_ahorro=None, ahorro_solidario=0):
    # Cálculo del sueldo bruto
    if horas_trabajadas <= 160:
        sueldo_bruto = salario_por_hora * horas_trabajadas
    elif horas_trabajadas <= 200:
        sueldo_bruto = (160 * salario_por_hora) + ((horas_trabajadas - 160) * salario_por_hora * 1.5)
    else:
        sueldo_bruto = (160 * salario_por_hora) + (40 * salario_por_hora * 1.5) + (
                    (horas_trabajadas - 200) * salario_por_hora * 2)

    # Tabla de ISR (SAT 2025)
    tabla_isr = [
        (0.01, 746.04, 0.00, 1.92),
        (746.05, 6332.05, 14.32, 6.40),
        (6332.06, 11128.01, 371.83, 10.88),
        (11128.02, 12935.82, 893.63, 16.00),
        (12935.83, 15487.71, 1182.88, 17.92),
        (15487.72, 31236.49, 1640.18, 21.36),
        (31236.50, 49233.00, 5004.12, 23.52),
        (49233.01, 93993.90, 9236.89, 30.00),
        (93993.91, 125325.20, 22665.17, 32.00),
        (125325.21, 375975.61, 32691.18, 34.00),
        (375975.62, float("inf"), 117912.32, 35.00)
    ]

    # Cálculo del ISR
    isr = 0
    for limite_inferior, limite_superior, cuota_fija, porcentaje in tabla_isr:
        if limite_inferior <= sueldo_bruto <= limite_superior:
            isr = cuota_fija + ((sueldo_bruto - limite_inferior) * (porcentaje / 100))
            break

    # Seguridad Social (2.5%)
    seguridad_social = sueldo_bruto * 0.025

    # Descuento por caja de ahorros
    if tipo_caja_ahorro == "cuota_fija":
        descuento_caja = 1000.00
    elif tipo_caja_ahorro == "3%":
        descuento_caja = sueldo_bruto * 0.03
    elif tipo_caja_ahorro == "5%":
        descuento_caja = sueldo_bruto * 0.05
    else:
        descuento_caja = 0.00

    # Ahorro solidario (1% o 2%)
    if ahorro_solidario == 1:
        descuento_solidario = sueldo_bruto * 0.01
    elif ahorro_solidario == 2:
        descuento_solidario = sueldo_bruto * 0.02
    else:
        descuento_solidario = 0.00

    # Cálculo del sueldo neto
    sueldo_neto = sueldo_bruto - (isr + seguridad_social + descuento_caja + descuento_solidario)

    return {
        "Sueldo Bruto": sueldo_bruto,
        "ISR": isr,
        "Seguridad Social": seguridad_social,
        "Descuento Caja de Ahorros": descuento_caja,
        "Ahorro Solidario": descuento_solidario,
        "Sueldo Neto": sueldo_neto
    }


# Ejemplo de uso
datos = calcular_sueldo_neto(salario_por_hora=100, horas_trabajadas=180, tipo_caja_ahorro="5%", ahorro_solidario=2)
for clave, valor in datos.items():
    print(f"{clave}: ${valor:.2f}")

