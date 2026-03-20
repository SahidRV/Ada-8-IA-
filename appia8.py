import streamlit as st

st.set_page_config(page_title="¿Doctor Algoritmo?", layout="wide")

# ---------------------------
# CSS MINIMALISTA + MODO OSCURO
# ---------------------------
st.markdown("""
<style>

/* CONTENEDOR PRINCIPAL */
.article-box{
    padding:35px;
    border-radius:18px;
    border:1px solid #e6e6e6;
    line-height:1.9;
    font-size:19px;
    max-width:900px;
    margin:auto;
    text-align:justify;
}

/* MODO CLARO */
@media (prefers-color-scheme: light) {
    .article-box{
        background-color:#ffffff;
        color:#222222;
    }
}

/* MODO OSCURO */
@media (prefers-color-scheme: dark) {
    .article-box{
        background-color:#1e1e1e;
        color:#f5f5f5;
        border:1px solid #333;
    }
}

/* TÍTULO PRINCIPAL */
.main-title{
    font-size:42px;
    font-weight:700;
    text-align:center;
    margin-bottom:10px;
}

/* FRASE */
.motivational{
    text-align:right;
    font-style:italic;
    margin-bottom:30px;
}

/* SUBTÍTULOS */
.section-title{
    font-size:22px;
    font-weight:600;
    margin-top:25px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------
# TÍTULO Y FRASE
# ---------------------------
st.markdown('<div class="main-title">¿Doctor Algoritmo? Los desafíos reales de la Inteligencia Artificial en nuestra salud</div>', unsafe_allow_html=True)

st.markdown(
'<div class="motivational">La tecnología puede ampliar nuestras capacidades, pero la responsabilidad de cuidar la vida siempre seguirá siendo humana.</div>',
unsafe_allow_html=True
)


# ---------------------------
# ARTÍCULO COMPLETO
# ---------------------------
st.markdown("""
<div class="article-box">

La promesa de una medicina de precisión, donde las máquinas nos ayuden a vivir más y mejor, parece estar a la vuelta de la esquina. Sin embargo, el paso del laboratorio al consultorio es más complejo de lo que sugieren los titulares.

<div class="section-title">1. Más que simples computadoras: La infraestructura invisible</div>

Cuando hablamos de Inteligencia Artificial (IA) en el ámbito sanitario, no nos referimos a robots humanoides, sino a algoritmos complejos capaces de procesar volúmenes de datos que el cerebro humano no podría abarcar en una vida entera. El objetivo principal es claro: facilitar diagnósticos tempranos, reducir la carga de tareas administrativas que agotan a los médicos y personalizar los tratamientos (Ahmed et al., 2023).

Sin embargo, para que un algoritmo sea inteligente, primero debe ser "entrenado". Aquí es donde aparece el primer gran límite: la calidad de los datos. Muchos hospitales aún carecen de sistemas estandarizados para almacenar información.

Imagine que la IA es un motor de última generación, pero el combustible que recibe (los datos de los pacientes) está contaminado o es insuficiente. La falta de interoperabilidad —la capacidad de que diferentes sistemas informáticos se entiendan entre sí— es una de las barreras más críticas identificadas por los líderes del sector (He et al., 2019). Si los datos de una clínica no pueden leerse en otra, la IA pierde su capacidad de ofrecer una visión global de la salud del paciente.

Además, la implementación requiere una infraestructura costosa y una ciberseguridad robusta para evitar filtraciones de datos sensibles, algo que no todos los sistemas de salud están preparados para costear. La adopción no es solo una cuestión de software, sino de una transformación profunda de la arquitectura digital de nuestras instituciones médicas (Petersson et al., 2022).

<div class="section-title">2. El factor humano: ¿Se puede programar la empatía?</div>

Uno de los debates más profundos ocurre en el campo de la salud mental. La IA ha demostrado ser sorprendentemente hábil para predecir patrones de conducta, identificar riesgos de depresión o incluso anticipar crisis suicidas mediante el análisis de la actividad digital de una persona (Biscaia Fernández et al., 2023; Rojas Chacón, 2025).

No obstante, la psicología clínica nos recuerda que el tratamiento de un ser humano no es una ecuación matemática. El límite fundamental de la IA en este terreno es su incapacidad para alcanzar la empatía verdadera. En una terapia, un psicólogo no solo escucha palabras; interpreta silencios, detecta el sarcasmo, la ironía y capta matices emocionales sutiles que un algoritmo, por avanzado que sea, tiende a ignorar (Quirós Valverde et al., 2024).

Existe un riesgo tangible de deshumanización si permitimos que las máquinas tomen el control total de la interacción clínica. La relación médico-paciente es un proceso terapéutico en sí mismo, y la sustitución de este vínculo por interfaces digitales podría erosionar la confianza y la calidez necesarias para la recuperación.

Los expertos advierten que una dependencia excesiva de estas herramientas podría atrofiar el juicio clínico de los nuevos profesionales, quienes podrían dejar de confiar en su intuición y experiencia para ceder ante la "decisión" de una pantalla (Salazar-Garcés & Velastegui-Hernandez, 2024; López Zúñiga & Rodríguez Zúñiga, 2024).

<div class="section-title">3. Ética y responsabilidad: El laberinto de los algoritmos</div>

Finalmente, entramos en el terreno de la ética y la legalidad. Los algoritmos no son entes objetivos; son creados por humanos y aprenden de datos históricos que ya pueden contener prejuicios. Esto se conoce como sesgo algorítmico. Si una IA se entrena con datos mayoritariamente de un grupo étnico o social específico, sus diagnósticos podrían ser menos precisos para otros grupos, perpetuando injusticias en el acceso a la salud (Mennella et al., 2024).

La justicia y la equidad son límites éticos que requieren una vigilancia constante y una regulación estricta que aún está en desarrollo. A esto se suma la "caja negra": a veces, ni siquiera los programadores saben exactamente por qué una IA llegó a una conclusión determinada. En medicina, donde un error puede costar una vida, esta falta de transparencia es inaceptable.

Surge entonces el dilema de la responsabilidad: si un sistema automatizado recomienda un tratamiento erróneo, ¿de quién es la culpa? (Li et al., 2024). El marco legal actual todavía lucha por definir si la responsabilidad recae en el médico que validó la sugerencia, en la empresa que desarrolló el software o en el hospital que lo implementó.

Por ello, la IA debe verse como una herramienta de apoyo, no como un sustituto del juicio humano. El desafío futuro no es tecnológico, sino humano: establecer reglas claras que aseguren que la tecnología siempre actúe en beneficio del paciente, respetando su autonomía y privacidad en todo momento.

</div>
""", unsafe_allow_html=True)


# ---------------------------
# REFERENCIAS
# ---------------------------
st.markdown("---")
st.header("Referencias")

referencias = {
    "Ahmed, M. I., et al. (2023)...": "Revisa los principales obstáculos para implementar IA en salud...",
    "Biscaia Fernández, J. M., et al. (2023)...": "Analiza el uso de IA para detectar riesgos suicidas...",
    "He, J., et al. (2019)...": "Describe cómo implementar IA en medicina...",
    "Li, Y. H., et al. (2024)...": "Examina la medicina personalizada con IA...",
    "Mennella, C., et al. (2024)...": "Analiza retos éticos y regulatorios...",
}

for titulo, resumen in referencias.items():
    with st.expander(titulo):
        st.write(resumen)
