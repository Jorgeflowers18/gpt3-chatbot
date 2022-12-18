import json

data = {}
data['Carreras'] = []

data['Carreras'].append({
    'Nombre': 'Administración de Empresas',
    'Modalidad': ['Abierta y a Distancia',' Presencial'],
    'Descripcion': ['Formamos profesionales competentes, líderes humanistas y emprendedores en el área de las ciencias administrativas y empresariales.',
    'Contamos con excelencia académica que permite identificar, comprender y solventar la problemática que surge dentro de las organizaciones y su entorno.',
    'Trabajamos bajo una filosofía institucional que potencia la innovación y el emprendimiento desde la academia con iniciativas transformadoras.'],
    'Titulo': 'Licenciado/a en Administración de Empresas',
    'Duracion':'4 Años',
    'Director de la Carrera':'Julio Alberto Ríos Zaruma'})


data['Carreras'].append({
    'Nombre': 'Arquitectura',
    'Modalidad': 'Presencial',
    'Descripcion': ['Formamos profesionales competentes, líderes humanistas y emprendedores en el área de las ciencias administrativas y empresariales.',
    'Contamos con excelencia académica que permite identificar, comprender y solventar la problemática que surge dentro de las organizaciones y su entorno.',
    'Trabajos a través de escenarios de aprendizaje con metodologías de enseñanza dinámicas e innovadoras y una infraestructura de vanguardia que te permite la experimentación práctica.',
    'Nuestra carrera contribuye al desarrollo de una postura crítica en los profesionales, capaces de solucionar problemas espaciales; fomentar una arquitectura con identidad propia, considerando la riqueza histórica-cultural de América Latina; e investigar sobre materiales de construcción idóneos para manejarlos con criterios de racionalidad social, económica y sustentable.'],
    'Titulo': 'Arquitecto',
    'Duracion':'4 años y medio', 
    'Director de la Carrera':'Xavier Eduardo Burneo Valdivieso'})

data['Carreras'].append({
    'Nombre': 'Medicina',
    'Modalidad': 'Presencial',
    'Descripcion': ['Formamos médicos generales con sólidas competencias académicas, con una visión integral del proceso salud-enfermedad desde la perspectiva de la Atención Primaria de Salud y basados en los principios éticos de la profesión médica para que sean capaces de contribuir al bienestar integral de la persona, la familia y la comunidad.',
    'La Medicina es el área encargada de identificar y resolver los problemas de salud más frecuentes de la persona y el entorno.',
    'Capacitamos a los futuros profesionales para que, basados en la investigación y el análisis de la realidad epidemiológica, se constituyan en gestores activos de la transformación de la realidad de la salud a nivel internacional, respondiendo a las necesidades del Sistema Nacional de Salud en Ecuador.'],
    'Titulo': 'Médico',
    'Duracion':'6 años',
    'Directora de la Carrera':'Dra. María Irene Carrillo Mayanquer'})

data['Carreras'].append({
    'Nombre': 'Enfermería',
    'Modalidad': 'Presencial',
    'Descripcion': ['Formamos profesionales de enfermería proactivas, innovadoras, con autonomía, con valores éticos y morales y responsabilidad social; capaces de ejercer la profesión con las competencias necesarias para brindar cuidados integrales de enfermería a la persona, familia y comunidad y en los diferentes ciclos de vida.',
    'Utilizamos la investigación, la comunicación y las relaciones humanas, como aporte a la solución de la problemática actual de salud, además capaces de administrar y gestionar los servicios de salud.',
    'Trabajamos en concordancia con los objetivos del desarrollo sustentable y el PNBV, promoviendo así el mejoramiento de la calidad de vida de la población al considerar la humanización del cuidado como eje transversal en su accionar.'],
    'Titulo': 'Licenciado/a en Enfermería',
    'Duracion':'4 años y medio',
    'Directora de la Carrera':'Dra. María Irene Carrillo Mayanquer'})

data['Carreras'].append({
    'Nombre': 'Turismo',
    'Modalidad':  'Abierta y a Distancia',
    'Descripcion': ['Formamos profesionales capaces de analizar los problemas, tensiones y tendencias de los actores involucrados en el quehacer turístico.',
    'Aplicamos modelos estratégicos de planificación, gestión e innovación turística que permiten promover el desarrollo sostenible.',
    'Trabajamos en la preservación del patrimonio natural y cultural, la participación activa de la población, la generación de emprendimientos, la equidad y la eficiencia económica del territorio. '],
    'Titulo': 'Licenciado/a en Turismo',
    'Duracion':'4 Años',
    'Director de la Carrera':'Christian Stalin Viñán Merecí'})

data['Carreras'].append({
    'Nombre': 'Derecho',
    'Modalidad': ['Abierta y a Distancia',' Presencial'],
    'Descripcion': ['Formamos profesionales capaces de diseñar, planificar y generar procesos de intervención e innovación social en el campo jurídico.',
    'Preparamos para que incorporen en el ejercicio profesional los aportes disciplinarios e interdisciplinarios sobre el derecho, los saberes jurídicos globales y locales, las tradiciones dogmáticas y jurisprudenciales sobre el sistema jurídico ecuatoriano, y los valores propios del Estado constitucional de derechos y justicia.',
    'Las capacidades teóricas y técnicas que se potencian en nuestra carrera, logran que nuestros profesionales apliquen, con justicia y equidad, los principios generales del derecho y del ordenamiento jurídico; al tiempo que relacionen los fenómenos políticos, económicos y sociales con la aplicación del derecho.'],
    'Titulo': 'Abogado/a',
    'Duracion':'4 Años',
    'Director de la Carrera':'Jorge Alberto Maldonado Ordóñez'})

data['Carreras'].append({
    'Nombre': 'Ingeniería Civil',
    'Modalidad': 'Presencial',
    'Descripcion': ['Formamos profesionales que brinden soluciones mediante el análisis, diseño, implementación, evaluación y control de proyectos de infraestructura civil.',
    'Formamos profesionales que brinden soluciones mediante el análisis, diseño, implementación, evaluación y control de proyectos de infraestructura civil.'],
    'Titulo': 'Ingeniero/a Civil',
    'Duracion':'4 años y medio',
    'Director de la Carrera':'Belizario Amador Zárate Torres'})

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
