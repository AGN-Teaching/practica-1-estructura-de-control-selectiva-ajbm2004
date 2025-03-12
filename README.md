# Práctica 1. Estructura de control selectiva
Introducción

Este proyecto consiste en desarrollar un programa en Python para determinar el sueldo neto de un empleado en una empresa. El cálculo se basa en el salario por hora y las horas trabajadas durante el mes. Se consideran las reglas de pago de horas normales y extras, además de aplicar deducciones como ISR, seguridad social, caja de ahorros (si corresponde) y ahorro solidario (si aplica). El resultado final es el monto que efectivamente recibe el trabajador.

Algoritmo de cálculo

El proceso sigue los siguientes pasos:

Ingreso de datos: Se solicita al usuario que ingrese su salario por hora, la cantidad de horas trabajadas en el mes y su participación en la caja de ahorros y el ahorro solidario.

Determinación del sueldo bruto:

Si las horas trabajadas no superan 160, el sueldo se calcula multiplicando las horas por el salario.

Si las horas están en el rango de 161 a 200, las primeras 160 se pagan a tarifa normal y las horas extras al 150% del valor estándar.

Si las horas exceden 200, se aplica la regla anterior y las horas adicionales a 200 se pagan al doble de la tarifa normal.

Cálculo del ISR: Se determina el rango correspondiente en la tabla del SAT y se calcula el impuesto aplicando la cuota fija y el porcentaje que corresponde.

Cálculo de deducciones:

Seguridad social: Se descuenta el 2.5% del sueldo bruto.

Caja de ahorros: Dependiendo de la elección del usuario, se aplica un descuento fijo o un porcentaje del 3% o 5%.

Ahorro solidario: Se descuenta el 1% o 2%, según la opción seleccionada.
comentarios
Este programa ofrece un cálculo preciso del sueldo neto considerando distintos factores, como la participación en la caja de ahorros y el ahorro solidario. Gracias a su diseño modular basado en funciones, el código es claro y fácil de modificar. Se recomienda probar diferentes valores de entrada para verificar su correcto desempeño en distintas situaciones.


Cálculo del sueldo neto: Se obtiene restando todas las deducciones al sueldo bruto.

Presentación de resultados: Se muestra un desglose detallado con todas las percepciones y descuentos aplicados.
