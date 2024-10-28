
# Gestión de Clientes

Este proyecto es un sistema básico de gestión de clientes (CRM) desarrollado en Python, diseñado para almacenar y administrar información de clientes, registrar sus interacciones y analizar datos relevantes mediante visualizaciones. Su objetivo es proporcionar a pequeñas empresas o autónomos una herramienta de administración de clientes que sea sencilla y efectiva.

## Tabla de Contenidos
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Uso](#uso)
3. [Características](#características)
4. [Tecnologías y Librerías](#tecnologías-y-librerías)
5. [Estructura del Código](#estructura-del-código)

## Descripción del Proyecto

Este sistema de gestión de clientes permite registrar información de clientes, almacenar interacciones detalladas y generar análisis y gráficos sobre preferencias de clientes. Los datos se guardan en una base de datos SQLite local, lo que facilita la gestión y acceso a la información sin necesidad de configuraciones avanzadas. También ofrece consultas avanzadas y exportación de datos en CSV para informes y análisis.

## Uso

Para utilizar el sistema, ejecute `main.py`. Esto mostrará automáticamente una tabla de todos los clientes registrados y una gráfica de sus preferencias. También puede personalizar el código para agregar nuevos clientes o realizar consultas específicas.

Ejemplo de ejecución:
```bash
python main.py
```

### Ejemplos de Comandos

En el archivo `main.py`, puede llamar a funciones específicas para agregar clientes, registrar interacciones o realizar consultas. Ejemplos de uso:

- **Agregar un cliente**:
  ```python
  agregar_cliente("Juan Pérez", "juan.perez@gmail.com", "Calle Falsa 123", "Tecnología")
  ```

- **Registrar una interacción**:
  ```python
  agregar_interaccion(1, "Llamada", "Consultó sobre productos tecnológicos.")
  ```

- **Buscar clientes por nombre**:
  ```python
  buscar_clientes(nombre="Juan")
  ```

## Características

- **Administración de Clientes**: Agregue, edite y elimine registros de clientes con datos básicos y preferencias.
- **Registro de Interacciones**: Guarde interacciones con clientes para crear un historial detallado.
- **Consultas y Exportación**: Filtre clientes por nombre o fecha y exporte los resultados a un archivo CSV.
- **Visualización de Datos**: Genere gráficos de las preferencias de los clientes para análisis rápido.

## Tecnologías y Librerías

El proyecto se basa en varias librerías de Python para su funcionalidad:

- **Python**: Lenguaje base del proyecto.
- **sqlite3**: Proporciona una base de datos local, ideal para gestionar datos de clientes de manera eficiente.
- **pandas**: Permite manipular y analizar los datos de clientes y exportarlos en formato CSV.
- **matplotlib**: Se usa para generar gráficos de barras que muestran las preferencias de los clientes.

## Estructura del Código

Aquí se explica cada parte principal del código y su funcionalidad:

- **Conexión y Creación de Tablas**: `sqlite3` crea dos tablas:
  - `clientes`: Almacena información básica de cada cliente.
  - `interacciones`: Registra las interacciones con los clientes para mantener un historial detallado.

- **Funciones Principales**:
  - **agregar_cliente**: Inserta un cliente nuevo.
  - **editar_cliente**: Permite modificar la información de un cliente.
  - **eliminar_cliente**: Elimina un cliente de la base de datos.
  - **listar_clientes**: Muestra todos los clientes en una tabla.
  - **agregar_interaccion**: Registra una interacción con un cliente específico.
  - **buscar_clientes**: Permite filtrar clientes por nombre o fecha.
  - **graficar_preferencias**: Crea un gráfico de las preferencias de los clientes usando `matplotlib`.

- **Ejemplos de Ejecución**: Se incluyen líneas de ejemplo en el archivo `main.py` para agregar clientes, registrar interacciones, y generar gráficos automáticamente al iniciar el sistema.
