# ==============================================================================
# AGNOSTIC LIGHTRAG INTEGRATION: SYSTEMS THINKING & CPS MENTAL GYM
# ==============================================================================
import os
import requests

def init_lightrag_agnostic(working_dir="./agnostic_cps_store"):
    """
    Inicializa el motor LightRAG agnóstico para el Gimnasio de Pensamiento Sistémico
    Soporta GraphRAG de doble nivel sobre Untools.co, Cynefin, y Modelos Mentales
    """
    try:
        from lightrag import LightRAG, QueryParam
        from lightrag.llm import ollama_model_complete, ollama_embedding
        
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)

        rag = LightRAG(
            working_dir=working_dir,
            llm_model_func=ollama_model_complete,
            llm_model_name="llama3.1",
            embedding_func=ollama_embedding,
            embedding_model_name="nomic-embed-text",
        )
        return rag
    except ImportError:
        print("[Warning]: lightrag-hku no está instalado. Ejecuta: pip install lightrag-hku")
        return None

def ingest_mental_models(rag_instance):
    """Indexa marcos agnósticos: Untools.co, Cynefin, Donella Meadows y Recuenco"""
    if rag_instance is None:
        return
    
    concepts = """
    # MARCOS MENTALES DE PENSAMIENTO SISTÉMICO (UNTOOLS & CPS)

    ## 1. El Modelo del Iceberg (Systems Thinking)
    - Eventos (Superficie): Lo que sucede en el momento.
    - Patrones (Debajo): Tendencias recurrentes a lo largo del tiempo.
    - Estructuras Sistémicas: Cómo las partes están interconectadas y los bucles de retroalimentación.
    - Modelos Mentales (Raíz): Creencias, valores y supuestos que sostienen el sistema.

    ## 2. Framework Cynefin (Dave Snowden)
    - Claro/Simple: Causa-Efecto obvia. Regla: Sentir -> Clasificar -> Responder (Mejores Prácticas).
    - Complicado: Causa-Efecto requiere análisis experto. Regla: Sentir -> Analizar -> Responder (Buenas Prácticas).
    - Complejo: Causa-Efecto solo comprensible en retrospectiva. Regla: Experimentar (Probe) -> Sentir -> Responder (Prácticas Emergentes).
    - Caótico: Causa-Efecto no existe. Regla: Actuar -> Sentir -> Responder (Prácticas Novel).

    ## 3. Inversion Thinking (Inversión)
    - En lugar de pensar cómo lograr el éxito, piensa cómo garantizar el fracaso y evita esas acciones.

    ## 4. Factor X & Psicología del Comportamiento (Recuenco / Kahneman)
    - Sistema 1 (Rápido, Emocional, Automático) vs Sistema 2 (Lento, Analítico, Esforzado).
    - Atractores Cognitivos: Miedo a la obsolescencia, evitación de compromiso, sesgo de coste hundido.
    """
    rag_instance.insert(concepts)
    print("✔ Marcos mentales agnósticos indexados correctamente en el Grafo de Conocimiento.")

if __name__ == "__main__":
    print("=== LIGHTRAG AGNÓSTICO: CPS MENTAL GYM ===")
    rag = init_lightrag_agnostic()
    if rag:
        ingest_mental_models(rag)
