# 🤖 Sistema Multi-Agente de Investigación Colaborativa

## 📋 Descripción

Sistema de agentes de IA colaborativos desarrollado con **CrewAI** que automatiza el proceso de investigación, escritura y revisión de contenido técnico sobre sesgos en Modelos de Lenguaje Grandes (LLMs).

## 🏗️ Arquitectura

### Agentes

| Agente | Rol | Responsabilidad |
|--------|-----|-----------------|
| **Researcher** | Investigador Senior de IA | Busca información en la web con DuckDuckGo |
| **Writer** | Escritor Técnico de IA | Genera borrador estructurado en Markdown (500 palabras) |
| **Reviewer** | Editor Crítico de IA | Revisa y proporciona feedback constructivo |

### Flujo de Trabajo
```
Researcher → Writer (borrador) → Reviewer → Writer (versión final)
```

## 🛠️ Tecnologías

- **CrewAI** (v0.35.0+): Orquestación de agentes
- **LangChain**: Integración con LLMs y herramientas
- **Meta-Llama-3-8B-Instruct**: Modelo de lenguaje vía HuggingFace
- **DuckDuckGo Search**: Búsqueda web

## 📁 Estructura del Proyecto
```
multiagent_project/
├── src/
│   └── agents.py              # Definición de agentes
├── notebooks/
│   └── workflow_demo.ipynb    # Ejecución del workflow
├── data/
│   └── research_summary.md    # Resumen final generado
├── .env                       # API keys
└── requirements.txt           # Dependencias
```

## 🚀 Instalación
```bash
# Crear entorno e instalar dependencias
conda create -n multiagent_2 python=3.11
conda activate multiagent_2
pip install -r requirements.txt

# Configurar .env
echo "HUGGING_FACE_HUB_TOKEN=tu_token_aqui" > .env

# Ejecutar notebook
jupyter notebook
```

## 🔧 Configuración del LLM
```python
from crewai import LLM

llm = LLM(
    model="huggingface/meta-llama/Meta-Llama-3-8B-Instruct",
    api_key=hf_token,
    temperature=0.7,
    max_tokens=1024
)
```

## 📊 Resultado

El workflow genera `data/research_summary.md` con un resumen de 500 palabras sobre sesgos en LLMs.

**Tiempo de ejecución**: 8-15 minutos

## 📚 Referencias

- [CrewAI Docs](https://docs.crewai.com/)
- [HuggingFace Models](https://huggingface.co/models)

---

**Versión**: 1.0 | **Fecha**: Noviembre 2025
