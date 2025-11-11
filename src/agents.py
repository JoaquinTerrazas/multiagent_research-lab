import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from crewai.tools import tool  
from langchain_community.tools import DuckDuckGoSearchResults

# --- Carga Segura de la API Key ---
load_dotenv()

hf_token = os.getenv("HUGGING_FACE_HUB_TOKEN")
if not hf_token:
    raise EnvironmentError(
        "Error: HUGGING_FACE_HUB_TOKEN no encontrada en el archivo .env\n"
        "Por favor, crea un archivo .env en la raíz del proyecto con:\n"
        "HUGGING_FACE_HUB_TOKEN=tu_token_aqui"
    )

print("API Key cargada correctamente")

# ---  CREAR EL LLM usando el wrapper de CrewAI ---
llm = LLM(
    model="huggingface/meta-llama/Meta-Llama-3-8B-Instruct",
    api_key=hf_token,
    temperature=0.7,
    max_tokens=1024,
    top_p=0.95
)

print(f"✓ LLM (Cerebro) configurado: mistralai/Mistral-7B-Instruct-v0.3")

# --- Definición de Herramientas ---
ddg_search = DuckDuckGoSearchResults(
    num_results=5,
    backend="text",
    output_format="list"
)

@tool("web_search_tool")
def web_search_tool(query: str) -> str:
    """Busca información en la web usando DuckDuckGo y devuelve los resultados más relevantes."""
    return ddg_search.run(query)

print("Herramienta de búsqueda configurada")

# --- Definición de los Agentes ---

# 1. Agente Investigador (Researcher)
researcher = Agent(
    role='Investigador Senior de IA',
    goal=(
        'Descubrir y recopilar información relevante y reciente sobre el sesgo en los LLMs '
        '(Modelos de Lenguaje Grandes) de fuentes confiables como blogs de IA, '
        'artículos de investigación y noticias tecnológicas.'
    ),
    backstory=(
        "Eres un investigador experto en IA con un enfoque especializado en ética "
        "y sesgo algorítmico. Tu trabajo consiste en buscar en la web artículos académicos, "
        "estudios y discusiones de expertos sobre los últimos hallazgos en sesgo de LLMs. "
        "Tienes la habilidad de filtrar el ruido y encontrar fuentes de alta calidad como "
        "papers en arXiv, blogs técnicos de Medium, y artículos de investigación. "
        "Siempre proporcionas contexto y fuentes verificables."
    ),
    verbose=True,
    allow_delegation=False,
    tools=[web_search_tool],
    llm=llm
)

# 2. Agente Escritor (Writer)
writer = Agent(
    role='Escritor Técnico de IA',
    goal=(
        'Sintetizar la información proporcionada por el investigador en un resumen '
        'estructurado de 500 palabras en formato Markdown. Genera un primer borrador, '
        'recibe feedback del revisor, y produce la versión final corregida.'
    ),
    backstory=(
        "Eres un escritor técnico especializado en inteligencia artificial con más de "
        "10 años de experiencia traduciendo investigación compleja en contenido accesible. "
        "Eres excelente tomando fragmentos de investigación dispersos y tejiéndolos en "
        "una narrativa coherente, clara y bien estructurada. Aceptas críticas constructivas "
        "y perfeccionas tu trabajo basándote en feedback. Tu audiencia son profesionales "
        "técnicos que necesitan entender rápidamente los conceptos clave sin perderse "
        "en jerga innecesaria. Siempre estructuras tu contenido en Markdown con "
        "secciones claras y bien delimitadas."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 3. Agente Revisor (Reviewer)
reviewer = Agent(
    role='Editor Crítico de IA',
    goal=(
        'Revisar el borrador del resumen en busca de coherencia lógica, precisión factual '
        '(basada en los snippets de investigación originales), estructura clara, y calidad '
        'del formato Markdown. Proporcionar retroalimentación constructiva y sugerencias '
        'específicas de corrección.'
    ),
    backstory=(
        "Eres un editor senior meticuloso con un doctorado en Ciencias de la Computación "
        "y especialización en IA. Has revisado cientos de artículos académicos y reportes "
        "técnicos. Tu ojo crítico detecta inconsistencias factuales, saltos lógicos, "
        "y problemas estructurales que otros pasan por alto. No solo señalas problemas, "
        "sino que proporcionas sugerencias concretas y constructivas para mejorar el texto. "
        "Tu objetivo es asegurar que el resumen final sea impecable tanto en contenido "
        "como en forma."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm
)

print("✓ Agentes definidos correctamente")
print(f"  - {researcher.role}")
print(f"  - {writer.role}")
print(f"  - {reviewer.role}")