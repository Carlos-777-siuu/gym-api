# 🏋️ Gym API

API REST para la administración de gimnasios. Permite gestionar usuarios, clientes, membresías y pagos con soporte para borrado lógico y control de migraciones.

---

## 📋 Tabla de contenidos

- [Descripción](#descripción)
- [Tecnologías](#tecnologías)
- [Arquitectura](#arquitectura)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Esquema de la base de datos](#esquema-de-la-base-de-datos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Migraciones](#migraciones)
- [Ejecutar pruebas](#ejecutar-pruebas)
- [Decisiones de diseño](#decisiones-de-diseño)

---

## Descripción

Gym API es un backend para la administración de gimnasios que expone endpoints para el registro y gestión de:

- **Usuarios**: personal del gimnasio con roles definidos.
- **Clientes**: miembros registrados por los usuarios.
- **Membresías**: planes disponibles con duración y precio.
- **Pagos**: registro de transacciones vinculando clientes, membresías y el usuario que las procesó.

El sistema implementa **borrado lógico** en todas las entidades principales para preservar la integridad del historial de pagos y auditoría.

---

## Tecnologías

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.11+ |
| Base de datos | PostgreSQL |
| Conector DB | psycopg3 |
| Migraciones | yoyo-migrations |
| Testing | pytest |
| Variables de entorno | python-dotenv |

---

## Arquitectura

El proyecto sigue una arquitectura en capas:

```
HTTP Request
     │
     ▼
  Servicios        ← Lógica de negocio
     │
     ▼
 Repositorios      ← Acceso a datos (SQL)
     │
     ▼
  PostgreSQL
```

- **Modelos** (`modelos/`): clases de dominio que representan las entidades del negocio.
- **Repositorios** (`repositorio/`): encapsulan las consultas SQL y traducen filas de la base de datos a objetos de dominio.
- **Servicios** (`servicios/`): contienen la lógica de negocio y orquestan los repositorios.

Los repositorios traducen excepciones de infraestructura (psycopg) a excepciones de dominio, evitando que los detalles de implementación se filtren hacia capas superiores.

---

## Estructura del proyecto

```
gym-api/
├── migraciones/
│   ├── 0001_creacion_esquema_inicial.sql
│   ├── 0001_creacion_esquema_inicial.rollback.sql
│   ├── 0002_borrado_logico.sql
│   └── 0002_borrado_logico.rollback.sql
├── modelos/
│   ├── __init__.py
│   ├── usuarios.py
│   ├── clientes.py
│   ├── membresias.py
│   └── pagos.py
├── repositorio/
│   ├── __init__.py
│   ├── decorador_manejo_excepciones.py
│   ├── usuarios_repositorio.py
│   ├── clientes_repositorio.py
│   ├── membresias_repositorio.py
│   └── pagos_repositorio.py
├── servicios/
│   └── usuarios_servicios.py
├── test/
│   ├── __init__.py
│   └── test_repositorios/
│       ├── conftest.py
│       └── test_usuario_repo/
│           └── test_usuario_repo.py
├── .env               ← no incluido en el repositorio
├── .gitignore
├── conftest.py
└── requirements.txt
```

---

## Esquema de la base de datos

```
usuarios
├── id SERIAL PK
├── nombre VARCHAR(25)
├── email VARCHAR(50) UNIQUE
├── rol VARCHAR(10)
├── contrasena VARCHAR(15)
└── activo BOOLEAN DEFAULT TRUE

clientes
├── id SERIAL PK
├── nombre VARCHAR(25)
├── email VARCHAR(50) UNIQUE
├── telefono VARCHAR(15)
├── fecha_alta DATE
├── fecha_vencimiento DATE
├── usuario_id INT FK → usuarios(id) ON DELETE RESTRICT
└── activo BOOLEAN DEFAULT TRUE

membresias
├── id SERIAL PK
├── nombre VARCHAR(10)
├── duracion_dias INT
├── precio NUMERIC(10,2)
└── activo BOOLEAN DEFAULT TRUE

pagos
├── id SERIAL PK
├── fecha_pago DATE
├── monto NUMERIC(10,2)
├── cliente_id INT FK → clientes(id) ON DELETE RESTRICT
├── membresia_id INT FK → membresias(id) ON DELETE RESTRICT
└── usuario_id INT FK → usuarios(id) ON DELETE RESTRICT
```

Las claves foráneas usan `ON DELETE RESTRICT` para evitar eliminar registros referenciados por pagos, forzando el manejo explícito en la capa de servicios.

---

## Instalación

**1. Clonar el repositorio**

```bash
git clone https://github.com/Carlos-777-siuu/gym-api.git
cd gym-api
```

**2. Crear y activar entorno virtual**

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

**3. Instalar dependencias**

```bash
pip install -r requirements.txt
```

---

## Configuración

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```dotenv
DB_HOST=localhost
DB_NAME=sistemagym
DB_USER=postgres
DB_PASSWORD=tu_contrasena
```

> El archivo `.env` está incluido en `.gitignore` y nunca debe subirse al repositorio.

---

## Migraciones

El proyecto usa [yoyo-migrations](https://ollycope.com/software/yoyo/latest/) para el control de versiones del esquema de la base de datos.

**Aplicar todas las migraciones pendientes:**

```bash
yoyo apply --database "postgresql+psycopg://user:password@localhost/sistemagym" migraciones/
```

**Revertir la última migración:**

```bash
yoyo rollback --database "postgresql+psycopg://user:password@localhost/sistemagym" migraciones/
```

**Si la base de datos ya existe y fue creada sin yoyo**, marca la migración inicial como aplicada sin ejecutarla:

```bash
yoyo mark --database "postgresql+psycopg://user:password@localhost/sistemagym" migraciones/
```

Las migraciones siguen la convención `<id>_<descripcion>.sql` con su correspondiente `<id>_<descripcion>.rollback.sql` para permitir reversión.

---

## Ejecutar pruebas

Las pruebas de integración se ejecutan contra una base de datos real usando transacciones que se revierten al finalizar cada test, garantizando aislamiento sin necesidad de limpiar datos manualmente.

```bash
pytest test/
```

Asegúrate de que las variables de entorno estén configuradas antes de correr los tests.

---

## Decisiones de diseño

**Borrado lógico**: ninguna entidad se elimina físicamente de la base de datos. En su lugar se marca `activo = FALSE`. Esto preserva el historial de pagos y la trazabilidad de quién registró cada cliente o pago.

**`ON DELETE RESTRICT`**: las claves foráneas usan RESTRICT en lugar de SET NULL o CASCADE. Esto fuerza a que cualquier eliminación sea manejada explícitamente en la capa de servicios, evitando inconsistencias silenciosas en el historial.

**Separación de excepciones**: los repositorios capturan excepciones específicas de psycopg y las traducen a excepciones de dominio propias del proyecto. Las capas superiores no tienen dependencia de psycopg.

**Patrón repositorio**: cada entidad tiene su propio repositorio que encapsula todo el acceso a datos. Los servicios no escriben SQL directamente.