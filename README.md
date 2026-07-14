# NODO EPIDEMIOLÓGICO DEL HOSPITAL MATERNO INFANTIL "SAN ROQUE"

## Estructura de archivos

```text
epidemiologia_hsr/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── importacion/
│   ├── limpieza/
│   ├── indicadores/
│   └── visualizaciones/
├── app/
├── docs/
├── requirements.txt
└── README.md
```

### Descripción

- **data/raw/**: datos originales exportados desde Epi Info.
- **data/processed/**: datos transformados y listos para análisis.
- **notebooks/**: notebooks de exploración y pruebas.
- **src/importacion/**: scripts para importar y convertir datos.
- **src/limpieza/**: procesos de limpieza y validación.
- **src/indicadores/**: cálculo de indicadores epidemiológicos.
- **src/visualizaciones/**: generación de gráficos y reportes.
- **app/**: aplicación para usuarios finales.
- **docs/**: documentación del proyecto.
- **requirements.txt**: dependencias de Python.

## Evaluación de archivos exportados del EPI INFO

### Características comunes

Los archivos exportados están compuestos por 10 columnas. Las que contienen texto siempre es con MAYÚSCULAS. A continuación hay un breve repaso de las mismas.

* _SEMEPI:_ Acá se indica con un número la semana epidemiológica a la que pertenece el registro.
* _FECHA:_ En formato "Mes/Día" se indica la fecha de la consulta. Le falta indicar el año.
* _MES:_ Está el nombre completo del mes y el dato es redundante con el campo FECHA.
* _EDAD:_ Si es un número solo, el valor indica años. Si es un período indica meses.
* _SEXO:_ No se especifíca nunca, siempre está vacio
* _LOCALIDAD:_ Siempre es "PARANA".
* _CONSULTA:_ Es por donde se atendió el paciente, esta base de datos siempre lo hace por "GUARDIA".
* _MÉDICO:_ Siempre se especifica "RESIDENTE".
* _DIAGNOSTIC:_ Nombre del diagnóstico. 
* _ACCIDENTE:_ Si en el campo anterior se especifica como diagnóstico "ACCIDENTE", este campo tiene un subtipo de este sino se coloca "NINGUNO".

No se indica el año epidemiológico.

### Características de los datos del 2025

* Este archivo solamente tiene datos de las semanas epidemiológicas correspondientes al año 2025.
* La primer semana epidemiológica arranca en el año anterior 2024. Si SEMEPI = 1 y MES = DICIEMBRE, entonces corresponde al año 2024.
* Este año tuvo 53 semanas epidemiológicas
* La última semana epidemiológica termina en enero del 2026. Si SEMEPI = 53 y MES = ENERO, entonces corresponde al año 2026.