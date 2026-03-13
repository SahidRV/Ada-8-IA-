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
# Referencias desplegables
# ---------------------------

st.header("Referencias")

referencias = {

"Ahmed, M. I., et al. (2023). A Systematic Review of the Barriers to the Implementation of AI in Healthcare. Cureus.":

"Revisa de forma sistemática los principales obstáculos para implementar Inteligencia Artificial en entornos sanitarios. El estudio destaca problemas como la falta de infraestructura tecnológica, la baja calidad o disponibilidad de datos clínicos y la resistencia organizacional al cambio. También subraya el potencial de la IA para mejorar diagnósticos médicos, optimizar procesos hospitalarios y reducir la carga administrativa del personal sanitario, especialmente tras la aceleración digital provocada por la pandemia.",


"Biscaia Fernández, J. M., et al. (2023). La inteligencia artificial en la prevención de conductas suicidas. Revista de Bioética y Derecho.":

"Analiza el uso de algoritmos de Inteligencia Artificial para detectar patrones asociados al riesgo suicida mediante el análisis de grandes volúmenes de datos provenientes de redes sociales, historiales clínicos y comportamiento digital. El artículo discute tanto el potencial preventivo de estas tecnologías como los dilemas éticos relacionados con la privacidad, el consentimiento y el uso de datos sensibles en contextos de salud mental.",


"He, J., et al. (2019). The practical implementation of artificial intelligence technologies in medicine. Nature Medicine.":

"Explica los pasos necesarios para llevar la Inteligencia Artificial desde la investigación académica hasta su implementación práctica en hospitales y clínicas. Los autores enfatizan la importancia de contar con datos médicos estandarizados, marcos regulatorios claros y evaluaciones clínicas rigurosas antes de adoptar estas tecnologías. También analiza el papel de organismos reguladores como la FDA en la validación de sistemas basados en IA.",


"Li, Y. H., et al. (2024). Innovation and challenges of AI technology in personalized healthcare. Scientific Reports.":

"Examina cómo diversas aplicaciones de Inteligencia Artificial, como chatbots médicos, dispositivos vestibles y sistemas de monitoreo remoto, están transformando la medicina personalizada. El estudio analiza los beneficios del análisis masivo de datos para adaptar tratamientos a cada paciente, pero también advierte sobre desafíos relacionados con la privacidad de la información, la seguridad de los datos y la presencia de sesgos algorítmicos.",


"López Zúñiga, L. A., & Rodríguez Zúñiga, M. A. (2024). La Ética de Usar IA en la Evaluación Psicológica en Durango, México. Ciencia Latina.":

"Explora las implicaciones éticas del uso de Inteligencia Artificial en procesos de evaluación psicológica. El estudio analiza cómo estas herramientas pueden mejorar la precisión diagnóstica y ampliar el acceso a servicios psicológicos en regiones con pocos especialistas, especialmente en zonas rurales. Sin embargo, también advierte sobre riesgos de deshumanización, dependencia tecnológica y posibles sesgos culturales en los algoritmos utilizados.",


"Mennella, C., et al. (2024). Ethical and regulatory challenges of AI technologies in healthcare. Heliyon.":

"Analiza las implicaciones éticas, legales y regulatorias del uso de sistemas de Inteligencia Artificial en la atención médica. El artículo examina temas como la transparencia de los algoritmos, la protección de datos de los pacientes, la responsabilidad en caso de errores clínicos y la necesidad de establecer marcos regulatorios sólidos que garanticen un uso seguro y equitativo de estas tecnologías.",


"Petersson, L., et al. (2022). Challenges to implementing AI in healthcare: a qualitative study. BMC Health Services Research.":

"Presenta un estudio cualitativo basado en entrevistas con profesionales del sector salud para identificar los principales desafíos en la implementación de la Inteligencia Artificial en hospitales. Entre los obstáculos identificados destacan la falta de infraestructura tecnológica, la escasa capacitación del personal médico, la resistencia organizacional al cambio y las preocupaciones sobre la seguridad de los datos clínicos.",


"Quirós Valverde, K., et al. (2024). Análisis de los principales aportes y riesgos de la IA en la psicología clínica. LATAM Revista.":

"Analiza tanto los beneficios como los riesgos del uso de Inteligencia Artificial en la práctica clínica psicológica. El estudio examina cómo estas herramientas pueden apoyar el diagnóstico, el análisis de datos clínicos y el seguimiento de pacientes, pero también advierte sobre limitaciones importantes como la incapacidad de las máquinas para comprender plenamente la subjetividad humana, las emociones complejas y los matices del lenguaje interpersonal.",


"Rojas Chacón, L. (2025). Inteligencia artificial: ¿futuro en la psicología? Revisión Bibliográfica.":

"Revisión bibliográfica que analiza el papel emergente de la Inteligencia Artificial en el campo de la psicología. El artículo examina la capacidad de los algoritmos para detectar patrones conductuales, anticipar trastornos psicológicos mediante el análisis de datos digitales y ofrecer intervenciones personalizadas. No obstante, también señala limitaciones importantes relacionadas con la falta de empatía auténtica y la dificultad de las máquinas para comprender el contexto emocional humano.",


"Salazar-Garcés, L. F., & Velastegui-Hernandez, D. C. (2024). Inteligencia Artificial y su Impacto en la Psicología Humana. MEDICIENCIAS UTA.":

"Estudia cómo el desarrollo de tecnologías basadas en Inteligencia Artificial puede influir en la práctica psicológica y en la comprensión del comportamiento humano. Los autores analizan aplicaciones potenciales como el análisis automatizado de datos psicológicos y la asistencia digital en terapia, pero advierten sobre los riesgos de una dependencia excesiva de estas herramientas y sobre la posible pérdida del componente humano en la relación terapéutica.",


"Alowais, S. A., et al. (2023). Revolutionizing healthcare: the role of artificial intelligence in clinical practice. BMC Medical Education.":

"Ofrece una visión integral de cómo la Inteligencia Artificial está transformando la práctica clínica. El artículo describe aplicaciones como el diagnóstico asistido por algoritmos, la predicción de enfermedades y el diseño de tratamientos personalizados mediante el análisis masivo de datos médicos. También examina cómo estas tecnologías pueden mejorar la eficiencia hospitalaria y apoyar la toma de decisiones clínicas.",


"Nunes, H. C., Guimarães, R. M. C., & Dadalto, L. (2022). Desafíos bioéticos del uso de la inteligencia artificial en los hospitales. Revista Bioética.":

"Examina los dilemas bioéticos asociados al uso de Inteligencia Artificial en entornos hospitalarios. El estudio distingue entre la fase de desarrollo tecnológico y la fase de implementación clínica, analizando cuestiones como la responsabilidad profesional, la autonomía del paciente y el papel de los comités de ética en la supervisión del uso de estas tecnologías.",


"Kelly, C., Karthikesalingam, A., Suleyman, M., Corrado, G., & King, D. (2019). Key challenges for delivering clinical impact with artificial intelligence.":

"Analiza por qué, a pesar del crecimiento exponencial de investigaciones sobre Inteligencia Artificial en medicina, su impacto clínico real sigue siendo limitado. Los autores identifican barreras como problemas logísticos, falta de integración con sistemas hospitalarios existentes y dificultades socioculturales relacionadas con la aceptación de estas tecnologías por parte del personal sanitario.",


"Saw, S., & Ng, K. (2022). Current challenges of implementing artificial intelligence in medical imaging.":

"Se centra en los desafíos específicos del uso de Inteligencia Artificial en radiología y diagnóstico por imagen. El artículo examina problemas técnicos relacionados con la robustez de los algoritmos, la calidad de los datos utilizados para entrenarlos y las dificultades para integrar estos sistemas en los flujos de trabajo clínicos.",


"Calligaro, C., & Rodríguez Ceberio, M. (2025). Terapia sistémica e inteligencia artificial: Desafíos y perspectivas futuras.":

"Explora las posibles aplicaciones de la Inteligencia Artificial dentro de la terapia sistémica, particularmente en el análisis de patrones de comunicación familiar y dinámicas relacionales. Los autores plantean que estas tecnologías pueden apoyar el trabajo terapéutico, pero subrayan que no pueden sustituir la comprensión contextual ni el vínculo humano entre terapeuta y paciente.",


"Lambert, S. I., et al. (2023). An integrative review on the acceptance of artificial intelligence among healthcare professionals in hospitals. npj Digital Medicine.":

"Revisión integradora que analiza los factores que influyen en la aceptación o rechazo de la Inteligencia Artificial por parte de médicos y enfermeros en hospitales. El estudio utiliza el modelo UTAUT para explicar cómo variables como la utilidad percibida, la facilidad de uso y el contexto organizacional influyen en la adopción de estas tecnologías.",


"Nair, M., Svedberg, P., Larsson, I., & Nygren, J. M. (2024). A comprehensive overview of barriers and strategies for AI implementation in healthcare. PLoS ONE.":

"Identifica y clasifica de manera exhaustiva las barreras para la implementación de sistemas de Inteligencia Artificial en salud, incluyendo obstáculos técnicos, organizacionales, regulatorios y culturales. Además, propone un marco estructurado de estrategias para facilitar su adopción en los sistemas de salud.",


"Poon, E. G., et al. (2025). Adoption of artificial intelligence in healthcare: Survey of health system priorities, successes, and challenges. Journal of the American Medical Informatics Association.":

"Presenta los resultados de una encuesta aplicada a diversos sistemas de salud para identificar sus prioridades al adoptar tecnologías de Inteligencia Artificial. El estudio describe experiencias exitosas de implementación, pero también señala desafíos persistentes relacionados con costos, capacitación del personal y gobernanza de datos.",


"Rego-Rodríguez, F. A., Germán-Flores, L., & Vitón-Castillo, A. A. (2022). Artificial intelligence and machine learning: present and future applications in health sciences.":

"Ofrece un panorama general de cómo el aprendizaje automático y otras tecnologías de Inteligencia Artificial están transformando las ciencias de la salud. El artículo revisa aplicaciones que van desde el descubrimiento de nuevos fármacos hasta la gestión administrativa de hospitales y el apoyo al diagnóstico clínico.",


"Rivera Estrada, J. E., & Sánchez Salazar, D. V. (2016). Inteligencia artificial ¿reemplazando al humano en la psicoterapia?":

"Cuestiona la posibilidad de que las máquinas puedan sustituir completamente a los terapeutas humanos. El artículo analiza los límites de la Inteligencia Artificial frente a la subjetividad humana, la experiencia emocional y la dimensión filosófica del cuidado psicológico."
}

for titulo, resumen in referencias.items():
    with st.expander(titulo):
        st.write(resumen)
