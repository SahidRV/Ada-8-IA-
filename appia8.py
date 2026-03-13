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
