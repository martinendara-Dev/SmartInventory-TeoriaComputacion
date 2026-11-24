# Subir la entrega conservando los tres commits

El repositorio remoto estaba vacío al preparar la entrega. No se ha subido ni modificado nada en GitHub. El ZIP contiene la carpeta `LOGISTPULSE` para leer los archivos y un archivo `Historial_LOGISTPULSE.bundle` con el repositorio, sus tres commits y la etiqueta `v1.0.0`.

## 1. Extraer el ZIP

Extraer todo en una carpeta. Deben quedar al mismo nivel `LOGISTPULSE/` y `Historial_LOGISTPULSE.bundle`.

## 2. Abrir esa carpeta en una terminal

Usar la terminal de VS Code o Git Bash. Comprobar que Git está instalado:

```bash
git --version
```

## 3. Recuperar el repositorio desde el bundle

Ejecutar desde la carpeta que contiene el bundle:

```bash
git clone Historial_LOGISTPULSE.bundle SmartInventory-TeoriaComputacion
cd SmartInventory-TeoriaComputacion
git log --oneline --decorate
git tag
```

Se crea una carpeta nueva con los archivos y el historial. Deben aparecer los tres bloques de sprint y `v1.0.0`. No hace falta ejecutar `git init`, `git add` ni inventar fechas.

## 4. Confirmar las pruebas

```bash
python -m unittest discover -s tests -v
python -m codigo.demo
```

En Windows puede usarse `py` en lugar de `python`. El resultado de las pruebas debe terminar en `Ran 61 tests` y `OK`.

## 5. Conectar con el repositorio de GitHub

Al clonar un bundle, `origin` apunta al archivo local. Cambiarlo:

```bash
git remote set-url origin https://github.com/martinendara-Dev/SmartInventory-TeoriaComputacion.git
git remote -v
git ls-remote origin
```

Si `git ls-remote origin` no muestra ramas ni etiquetas, el remoto sigue vacío. Continuar:

```bash
git push -u origin main
git push origin v1.0.0
```

Git puede abrir el navegador para iniciar sesión. Usar la cuenta con permiso sobre ese repositorio. No escribir contraseñas ni tokens dentro de los archivos del proyecto. Si el remoto ya contiene commits, detenerse y revisar cómo integrarlos; no usar `--force`.

## 6. Crear la release

1. Abrir el repositorio en GitHub.
2. Entrar a Releases y elegir Draft a new release.
3. Seleccionar la etiqueta existente `v1.0.0`.
4. Usar el título `LOGISTPULSE Deber 2 v1.0.0`.
5. Copiar el texto de `gestion/RELEASE.md` en la descripción.
6. Publicar la release. GitHub añadirá el ZIP del código de esa etiqueta.

## 7. Entregar en el curso

Pegar el enlace del repositorio, adjuntar `documentos/Informe_LOGISTPULSE.pdf` y las fichas. Los JFLAP, diagramas, pruebas, documentos y presentación quedan incluidos en el repositorio y en su ZIP.

La subida por “Add file > Upload files” también copia archivos, pero **no conserva los tres commits del bundle**. Para esta consigna conviene seguir el procedimiento de Git.
