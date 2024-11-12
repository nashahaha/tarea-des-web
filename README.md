# Tarea 3

## Gráfico número de dispositivos registrados por comuna

Este gráfico tarda un par de segundos en mostrarse, esto es porque las constultas en Mysql no son eficientes por la manera en que están indexadas las tablas. Una forma de solucionar este problema sería agregando una columna `número de dispositivos` a la tabla `comuna` que se actualice cada vez que se registra un dispositivo, de esta manera no sería necesario contar dispositivos por cada comuna por lo que se ahorraría tiempo. Por temas de tiempo no se implementó esta mejora.
