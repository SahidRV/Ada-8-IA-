import streamlit as st

st.set_page_config(page_title="¿Doctor Algoritmo?", layout="wide")

# ---------------------------
# CSS minimalista
# ---------------------------
st.markdown("""
<style>

.main-title{
    font-size:42px;
    font-weight:700;
    margin-bottom:0px;
}

.motivational{
    text-align:right;
    font-style:italic;
    color:#555;
    margin-bottom:30px;
}

.article-box{
    background-color:#fafafa;
    padding:35px;
    border-radius:18px;
    border:1px solid #e6e6e6;
    line-height:1.7;
    font-size:17px;
}

.section-title{
    font-size:22px;
    font-weight:600;
    margin-top:25px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------
# Título
# ---------------------------

st.markdown('<div class="main-title">¿Doctor Algoritmo? Los desafíos reales de la Inteligencia Artificial en nuestra salud</div>', unsafe_allow_html=True)

st.markdown(
'<div class="motivational">La tecnología puede ampliar nuestras capacidades, pero la responsabilidad de cuidar la vida siempre seguirá siendo humana.</div>',
unsafe_allow_html=True
)

# ---------------------------
# Artículo
# ---------------------------

st.markdown("""
<div class="article-box">

La promesa de una medicina de precisión, donde las máquinas nos ayuden a vivir más y mejor, parece estar a la vuelta de la esquina. 
Sin embargo, el paso del laboratorio al consultorio es más complejo de lo que sugieren los titulares.

<div class="section-title">1. Más que simples computadoras: La infraestructura invisible</div>

Cuando hablamos de Inteligencia Artificial (IA) en el ámbito sanitario, no nos referimos a robots humanoides, sino a algoritmos capaces de procesar enormes volúmenes de datos. 
El objetivo es facilitar diagnósticos tempranos, reducir tareas administrativas y personalizar tratamientos.

Sin embargo, para que un algoritmo funcione correctamente primero debe ser entrenado con datos de calidad. 
Aquí aparece uno de los mayores límites: muchos hospitales aún no cuentan con sistemas estandarizados de almacenamiento de información.

Imagine que la IA es un motor de última generación, pero el combustible que recibe —los datos médicos— está contaminado o es insuficiente. 
La falta de interoperabilidad entre sistemas hospitalarios impide que la información clínica pueda compartirse de forma eficiente.

Además, implementar estas tecnologías requiere una infraestructura costosa y medidas sólidas de ciberseguridad para proteger datos sensibles. 
Por ello, adoptar IA no es solo instalar software, sino transformar profundamente la arquitectura digital de los sistemas de salud.

<div class="section-title">2. El factor humano: ¿Se puede programar la empatía?</div>

Uno de los debates más intensos surge en el campo de la salud mental. 
La IA ha demostrado capacidad para identificar patrones de comportamiento y detectar señales tempranas de depresión o riesgo suicida mediante el análisis de datos digitales.

Sin embargo, la psicología clínica recuerda que el tratamiento humano no es una ecuación matemática. 
Un terapeuta interpreta silencios, percibe matices emocionales y comprende contextos personales que los algoritmos aún no logran captar completamente.

Existe el riesgo de que una dependencia excesiva de la tecnología conduzca a la deshumanización de la atención. 
La relación médico-paciente es en sí misma parte del proceso terapéutico.

<div class="section-title">3. Ética y responsabilidad: El laberinto de los algoritmos</div>

Los algoritmos tampoco son completamente objetivos. 
Aprenden de datos históricos que pueden contener sesgos sociales o culturales.

Si una IA se entrena con información de un grupo poblacional específico, sus diagnósticos podrían ser menos precisos para otros grupos. 
Esto podría perpetuar desigualdades en el acceso a la salud.

Además, muchos sistemas funcionan como una "caja negra": incluso los desarrolladores pueden tener dificultades para explicar exactamente cómo el algoritmo llegó a una conclusión.

En medicina, donde un error puede costar una vida, esta falta de transparencia plantea dilemas importantes. 
Si un sistema automatizado recomienda un tratamiento incorrecto, surge la pregunta inevitable: ¿quién es responsable?

Por ello, la Inteligencia Artificial debe entenderse como una herramienta de apoyo para los profesionales de la salud, 
no como un sustituto del juicio humano.

</div>
""", unsafe_allow_html=True)


# ---------------------------
# Referencias desplegables
# ---------------------------

st.header("Referencias")

referencias = {
    "Ahmed, M. I., et al. (2023). A Systematic Review of the Barriers to the Implementation of AI in Healthcare. Cureus.":

    "Revisa de forma sistemática los obstáculos para implementar IA en entornos sanitarios y su potencial para mejorar diagnósticos y reducir cargas administrativas.",

    "Biscaia Fernández, J. M., et al. (2023). La inteligencia artificial en la prevención de conductas suicidas. Revista de Bioética y Derecho":

    "Analiza los aspectos técnicos y éticos del uso de IA para detectar riesgos de suicidio mediante datos masivos y redes sociales.",

    "He, J., et al. (2019). The practical implementation of artificial intelligence technologies in medicine. Nature Medicine.":

    "Describe los pasos necesarios para implementar IA en medicina, destacando la importancia de la estandarización de datos y la regulación.",

    "Li, Y. H., et al. (2024). Innovation and challenges of AI technology in personalized healthcare. Scientific Reports.":

    "Examina el uso de chatbots y dispositivos vestibles en medicina personalizada, así como los retos de privacidad y sesgo algorítmico.",

    "Mennella, C., et al. (2024). Ethical and regulatory challenges of AI technologies in healthcare. Heliyon.":

    "Explora las implicaciones éticas y regulatorias del uso de IA en sistemas de apoyo a decisiones clínicas.",

    "Rojas Chacón, L. (2025). Inteligencia artificial: ¿futuro en la psicología?":

    "Analiza el potencial de la IA para detectar trastornos mediante patrones digitales y sus limitaciones en empatía clínica.",

    "Salazar-Garcés, L. F., & Velastegui-Hernandez, D. C. (2024). Inteligencia Artificial y su Impacto en la Psicología Humana.":

    "Estudia cómo la IA puede influir en la práctica psicológica y advierte sobre la posible deshumanización en la atención clínica."
}

for titulo, resumen in referencias.items():
    with st.expander(titulo):
        st.write(resumen)
