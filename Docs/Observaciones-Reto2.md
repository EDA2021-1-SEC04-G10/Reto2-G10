# Análisis

## Autores :writing_hand:
* Hernán Buitrago
  * hf.buitrago10@uniandes.edu.co
  * 201512807
* Daniel Aguilera
  * d.aguilera@uniandes.edu.co
  * 202010592

## Máquina

| | Máquina |
| --- | --- |
| Procesador | 2.6 GHz Dual-Core Intel Core i5 |
| Memoria | 8 GB 1600 MHz DDR3 |
| OS | MacOS Big Sur 11.2.3 |

## Tiempo :stopwatch:
Para la recolección de datos se promedió el tiempo de ejecución para cada requerimiento después de ser ejecutados 5 veces. La siguiente tabla muestra los resultados de las pruebas para el reto 1 y el reto 2.

|  | Reto 1 | Reto 2 | Diferencia |
| --- | --- | --- | --- |
| __Carga de datos__ | 32057.725 [ms] | 73076.714 [ms] | 41018.989 [ms] |
| __Requerimiento 1__ | 1174.642 [ms] | 341.054 [ms] | -833.588 [ms] |
| __Requerimiento 2__ | 4747.066 [ms] | 2532.477 [ms] | -2214.589 [ms] |
| __Requerimiento 3__ | 5111.147 [ms] | 2148.295 [ms] | -2962.852 [ms] |
| __Requerimiento 4__ | 1405.217 [ms] | 592.370 [ms] | -812.847 [ms] |

Se observa que los tiempos de ejecución de cada requerimiento son significativamente menores para el reto 2.

## Memoria
Para la recolección de datos se promedió la memoria asignada para cada requerimiento después de ser ejecutado 5 veces. La siguiente tabla muestra los resultados de las pruebas para el reto 1 y el reto 2.

|  | Reto 1 | Reto 2 | Diferencia |
| --- | --- | --- | --- |
| __Carga de datos__ | 1321167.344 [kB] | 1427564.975 [kB] | 106397.631 [kB] |
| __Requerimiento 1__ | 66.027 [kB] | 50.004 [kB] | -16.023 [kB] |
| __Requerimiento 2__ | 351.203 [kB] | 37.083 [kB] | -314.12 [kB] |
| __Requerimiento 3__ | 346.020 [kB] | 25.766 [kB] | -320.254 [kB] |
| __Requerimiento 4__ | 68.561 [kB] | 54.773 [kB] | -13.788 [kB] |

Se observa que la memoria asignada para cada requerimiento es significativamente menor para el reto 2.

## Complejidad :chart_with_upwards_trend:
Se realizó un análisis de complejidad en el peor caso para cada requerimiento. La siguiente tabla muestra la complejidad temporal de cada requerimiento para el reto 1 y el reto 2.

|  | Reto 1 | Reto 2 |
| --- | --- | --- |
| __Requerimiento 1__ | O(n log n) | O(n log n) |
| __Requerimiento 2__ | O(n log n) | O(n) |
| __Requerimiento 3__ | O(n log n) | O(n) |
| __Requerimiento 4__ | O(n log n) | O(n log n) |
