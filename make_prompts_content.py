#!/usr/bin/env python3
"""
Generates the HTML content for the 'Prompts Clave de IA' deliverable.
Compliant with Vauxoo Academy brand guidelines.
"""

def get_prompts_html():
    return '''
    <div class="prompts-wrapper" style="max-width: 1040px; margin: 0 auto; padding: 32px 20px;">
      
      <!-- Header Banner -->
      <div style="background: linear-gradient(90deg, #345D90 0%, #172A45 100%); color: #FFFFFF; border-radius: 12px; padding: 36px 32px; position: relative; overflow: hidden; margin-bottom: 32px;">
        <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px;">
          <span class="pill-badge">INGENIERÍA DE PROMPTS</span>
          <span class="pill-badge-outline">METODOLOGÍA DE REPLICACIÓN</span>
          <span class="pill-badge-outline">VAUXOO ACADEMY</span>
        </div>
        <h1 style="font-size: 2rem; font-weight: 700; color: #FFFFFF; margin-bottom: 10px; line-height: 1.25;">
          Prompts Clave de Inteligencia Artificial
        </h1>
        <p style="font-size: 1.05rem; color: #E2E8F0; max-width: 780px; margin-bottom: 0;">
          Documento técnico con los prompts exactos, contexto y decisiones de diseño utilizados para construir el <strong>Plan de 90 min</strong>, el <strong>Script técnico / Guion teleprompter</strong> y la <strong>Suite interactiva de Slides</strong> para la Masterclass de Odoo 19.0.
        </p>
      </div>

      <!-- Quick Index Cards -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 36px;">
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-top: 4px solid #AC0340; border-radius: 8px; padding: 20px;">
          <span style="font-size: 0.8rem; font-weight: 700; color: #AC0340; text-transform: uppercase;">FASE 1</span>
          <h3 style="font-size: 1.15rem; margin: 6px 0 8px 0; color: #27282F;">1. El Plan Estratégico</h3>
          <p style="font-size: 0.88rem; color: #5A6578; margin-bottom: 12px;">Debate dialéctico entre agentes de IA, acotación a México/USD y eliminación de distracciones teóricas.</p>
          <a href="#fase-plan" class="btn btn-sm" style="font-size: 0.8rem; padding: 5px 12px;">Ver Prompts del Plan ↓</a>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-top: 4px solid #345D90; border-radius: 8px; padding: 20px;">
          <span style="font-size: 0.8rem; font-weight: 700; color: #345D90; text-transform: uppercase;">FASE 2</span>
          <h3 style="font-size: 1.15rem; margin: 6px 0 8px 0; color: #27282F;">2. El Script y Teleprompter</h3>
          <p style="font-size: 0.88rem; color: #5A6578; margin-bottom: 12px;">Script ejecutable Python para la base de datos y guion cronológico paso a paso para la transmisión.</p>
          <a href="#fase-script" class="btn btn-sm btn-secondary" style="font-size: 0.8rem; padding: 5px 12px; color: #27282F; border-color: #CBD5E1;">Ver Prompts del Script ↓</a>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-top: 4px solid #172A45; border-radius: 8px; padding: 20px;">
          <span style="font-size: 0.8rem; font-weight: 700; color: #172A45; text-transform: uppercase;">FASE 3</span>
          <h3 style="font-size: 1.15rem; margin: 6px 0 8px 0; color: #27282F;">3. Las Slides y Portal Web</h3>
          <p style="font-size: 0.88rem; color: #5A6578; margin-bottom: 12px;">Estructura del hook visual, presentación interactiva proyectable y compilación a GitHub Pages.</p>
          <a href="#fase-slides" class="btn btn-sm btn-secondary" style="font-size: 0.8rem; padding: 5px 12px; color: #27282F; border-color: #CBD5E1;">Ver Prompts de Slides ↓</a>
        </div>
      </div>

      <!-- FASE 1: PLAN -->
      <section id="fase-plan" style="margin-bottom: 48px;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px; border-bottom: 2px solid #E2E8F0; padding-bottom: 12px;">
          <span class="pill-badge" style="font-size: 0.85rem;">FASE 1</span>
          <h2 style="font-size: 1.5rem; color: #27282F; margin: 0;">Prompts Clave para Generar el PLAN</h2>
        </div>

        <!-- Prompt 1.1 -->
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px; margin-bottom: 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <strong style="color: #AC0340; font-size: 1.05rem;">1.1. Génesis: Debate Dialéctico entre Agentes y Estándar de $100 USD</strong>
            <span class="pill-badge-outline" style="color: #5A6578; border-color: #CBD5E1; font-size: 0.7rem;">Sesión 1 · Paso 0</span>
          </div>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 12px;">
            <strong>Propósito:</strong> Evitar la trampa común de respuestas genéricas de IA basadas en documentación superficial. Se exigió debate cruzado con el skill <code>superpowers</code> y foco en el valor comercial.
          </p>
          <div style="background: #1E293B; color: #F8FAFC; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 0.86rem; line-height: 1.5; white-space: pre-wrap; margin-bottom: 14px;">Necestio que me puedas apoyar para hacer un super y bueno y de calidad y profesional yn plan para dar esta clase en odoo versión 19.0

Necesito que debatas con otro agente gemini el que consideres mejor y usando el skill de superpowers, para que me hagan un plan de como debería abordar esta masterclass, recuerda que es versión 19.0 y en odoo cambio la forma de valoración de inventario, estas es un masterclass de 1:30 es virtual y en directo, los clientes pagan por estar en esa sesión, por lo cual necesito que sea algo de calidad, que no se encuentre en cualquier video o documento que agregue valor y que represente un caso real para los clientes</div>
          <div style="background: #F1F5F9; border-left: 4px solid #345D90; padding: 10px 14px; font-size: 0.86rem; color: #334155;">
            <strong>Resultado:</strong> Dos agentes produjeron el esqueleto en 6 bloques cronológicos, identificando que el núcleo de Odoo 19 no es la teoría sino la eliminación de cuentas en categorías y la nueva valoración automática.
          </div>
        </div>

        <!-- Prompt 1.2 -->
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px; margin-bottom: 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <strong style="color: #AC0340; font-size: 1.05rem;">1.2. Refinamiento: Localización México, AVCO y Multimoneda USD</strong>
            <span class="pill-badge-outline" style="color: #5A6578; border-color: #CBD5E1; font-size: 0.7rem;">Sesión 1 · Paso 71</span>
          </div>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 12px;">
            <strong>Propósito:</strong> Adaptar el caso al contexto de las empresas latinoamericanas (moneda base MXN con compras en USD) y eliminar complejidades que consumirían demasiado tiempo como multicompañía.
          </p>
          <div style="background: #1E293B; color: #F8FAFC; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 0.86rem; line-height: 1.5; white-space: pre-wrap; margin-bottom: 14px;">Ahora necesito unas correciones al plan presentado, sigue usando superpowers y sigue discutiendo un otro agente de gemini
1. Vamos enfocar la masterclass con ejemplo de metodo de costo average
2. Con una configuración para mexico, plan contable y localización
3. por ahora vamos evitar el caso de uso de multicompañía
4. pero si vamos agregar el caso de uso de compras en usd, que aqui veo que pasa que usan tipos de cambio que no son, que confirman la compra pensando que es en usd, etc
5. Compañía en mxn
6. casos de compra en usd
Seguir manteniendo todo con estos cambios en la 1:30 de la mesterclass y lo que ya propusiste solo considera estos comentarios que te deje</div>
          <div style="background: #F1F5F9; border-left: 4px solid #345D90; padding: 10px 14px; font-size: 0.86rem; color: #334155;">
            <strong>Resultado:</strong> El temario se centró en costeo promedio (AVCO) y el impacto del tipo de cambio al recibir mercancía vs facturar al proveedor extranjero.
          </div>
        </div>

        <!-- Prompt 1.3 -->
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px; margin-bottom: 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <strong style="color: #AC0340; font-size: 1.05rem;">1.3. Poda de Ruido: Proteger el Tiempo de Inventarios (Cero Pedimentos / Cero CFDI)</strong>
            <span class="pill-badge-outline" style="color: #5A6578; border-color: #CBD5E1; font-size: 0.7rem;">Sesión 1 · Paso 73</span>
          </div>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 12px;">
            <strong>Propósito:</strong> Evitar la tendencia de la IA a meter temas fiscales o aduanales anexos que se comen el tiempo de la clase.
          </p>
          <div style="background: #1E293B; color: #F8FAFC; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 0.86rem; line-height: 1.5; white-space: pre-wrap; margin-bottom: 14px;">tengo duda aun con los puntos CFDI de Pago, Anticipo en USD como afecta o favore para la masterclass que es de valuación de inventario, sobre todo el punto que comentas de 'Crítico para IVA acreditable', solo quiero validar si es justificable ó no es necesario, recuerda que es una masterclass de valución de inventario y meter un caso o como se va mostrar o mostaría el tema de pedimeitno ya que ahi nos podemos llevar toda la sesion</div>
          <div style="background: #F1F5F9; border-left: 4px solid #345D90; padding: 10px 14px; font-size: 0.86rem; color: #334155;">
            <strong>Resultado:</strong> Eliminación absoluta de anticipos e importaciones complejas, salvando 35 minutos de explicación innecesaria.
          </div>
        </div>

        <!-- Prompt 1.4 -->
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px; margin-bottom: 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <strong style="color: #AC0340; font-size: 1.05rem;">1.4. Inyección de la Voz de Experiencia: Las 3 Causas Raíz Reales</strong>
            <span class="pill-badge-outline" style="color: #5A6578; border-color: #CBD5E1; font-size: 0.7rem;">Sesión 2 · Paso 577</span>
          </div>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 12px;">
            <strong>Propósito:</strong> Pasar de la teoría técnica a los vicios humanos y organizacionales que provocan los descuadres.
          </p>
          <div style="background: #1E293B; color: #F8FAFC; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 0.86rem; line-height: 1.5; white-space: pre-wrap; margin-bottom: 14px;">Lanza un agente que consideres mas intelegie de gemini par que discultan y me den conclusiones

/brainstorming como puedo agregar a la masterclass estas ideas que tengo, que en mi experiencia pasan. muchos, que son algunas de las principales casusas por las sque no se llega a tener un buen control de contabilidad vs logistica, neesito que me digas en donde agrega mas valor meterlo, si agrega valor comentarlo y en que momento de la masterclass
1. Pólizas manuales, el contador en ese momento con poco claridad o sin saber como pero el llega a un numero y decide hacer una póliza manual para cuadrar el inventario
2. El usuario, contadore, nunca audita un reporte...
3. Malas configuraciones, dos configuraciones malas no hacen una buena...</div>
          <div style="background: #F1F5F9; border-left: 4px solid #345D90; padding: 10px 14px; font-size: 0.86rem; color: #334155;">
            <strong>Resultado:</strong> Nació el marco conceptual: <em>"Las 3 Causas Raíz del Divorcio entre Logística y Contabilidad"</em>, pieza pedagógica insignia del Bloque 4.
          </div>
        </div>

        <!-- Prompt 1.5 -->
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <strong style="color: #AC0340; font-size: 1.05rem;">1.5. Delimitación de Casos y Prohibición de Jerga Innecesaria</strong>
            <span class="pill-badge-outline" style="color: #5A6578; border-color: #CBD5E1; font-size: 0.7rem;">Sesión 2 · Paso 1110</span>
          </div>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 12px;">
            <strong>Propósito:</strong> Regla de oro para evitar discusiones bizantinas y asegurar que los 4 desastres a demostrar sean 100% reproducibles en vivo.
          </p>
          <div style="background: #1E293B; color: #F8FAFC; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 0.86rem; line-height: 1.5; white-space: pre-wrap; margin-bottom: 14px;">usando /brainstorming entonces para el bloque 4, solo quiero estos casos:
1. Un ajuste de inventario sin una cuenta de inventario configurada
2. Un recepción de compra con tipo de cambio errroneo
3. Mercancia que se entrega al cliente, sin antes recibir compra ó facturar compra ó ambas
4. Las polizas manuales de ajuste
Bloque 3, por si hay clientes que no usan importación vamos a quitar el caso de importación / aduanal, mejor agregamos el caso de venta entrega de mercancia...
General: Por favor no comentar nada de reglas NIF ya que pudeira ser que yo mismo no las conosco. No comentar que el 'kardex' por que odoo no hay un kardex. No comentar o hacer relación a cosas fiscales por que no es una masterclass de fiscal</div>
          <div style="background: #F1F5F9; border-left: 4px solid #345D90; padding: 10px 14px; font-size: 0.86rem; color: #334155;">
            <strong>Resultado:</strong> Consagró el <strong>Plan Definitivo v4</strong> y la política de lenguaje limpio: cero NIFs, cero mención de "kardex", cero SAT.
          </div>
        </div>
      </section>

      <!-- FASE 2: SCRIPT -->
      <section id="fase-script" style="margin-bottom: 48px;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px; border-bottom: 2px solid #E2E8F0; padding-bottom: 12px;">
          <span class="pill-badge" style="font-size: 0.85rem; background: #345D90;">FASE 2</span>
          <h2 style="font-size: 1.5rem; color: #27282F; margin: 0;">Prompts Clave para Generar el SCRIPT</h2>
        </div>

        <!-- Prompt 2.1 -->
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px; margin-bottom: 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <strong style="color: #345D90; font-size: 1.05rem;">2.1. Automatización Idempotente de Base de Datos (`setup_masterclass.py`)</strong>
            <span class="pill-badge-outline" style="color: #5A6578; border-color: #CBD5E1; font-size: 0.7rem;">Sesión 2 · Paso 16</span>
          </div>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 12px;">
            <strong>Propósito:</strong> Exigir que la base de datos de demostración sea completamente desechable y restaurable en segundos ante fallas en vivo.
          </p>
          <div style="background: #1E293B; color: #F8FAFC; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 0.86rem; line-height: 1.5; white-space: pre-wrap; margin-bottom: 14px;">Ahora con relación al plan que ya esta definido, necesito que en la instancia de masterclass
1. Instales todo lo necesario
2. Hagas las configuraciones necesarias
3. Instales la data necesaria para hacer toda la masterclass
Todo lo que hagas, scripts, etc, tienen que quedar documentados por si necesito volver a crear una nueva base de datos sepas rapido como generar una nueva con todo lo necesario para la masterclass, ó que si te digo vamos de nuevo con la data de inicio pongas esa data, en caso de que haya hecho incorrecto algun ajuste o dato y las pruebas que voy a realizar</div>
          <div style="background: #F1F5F9; border-left: 4px solid #AC0340; padding: 10px 14px; font-size: 0.86rem; color: #334155;">
            <strong>Resultado:</strong> El script Python <code>setup_masterclass.py</code> que configura cuentas 115.01, productos, compras USD, ventas y el descuadre del Hook ($411,275 MXN) desactivando el cron de cierre.
          </div>
        </div>

        <!-- Prompt 2.2 -->
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px; margin-bottom: 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <strong style="color: #345D90; font-size: 1.05rem;">2.2. Supresión de Asientos No Deseados en el Script</strong>
            <span class="pill-badge-outline" style="color: #5A6578; border-color: #CBD5E1; font-size: 0.7rem;">Sesión 2 · Paso 910</span>
          </div>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 12px;">
            <strong>Propósito:</strong> Mantener la pureza de la demostración eliminando pólizas de NIF teóricas generadas previamente.
          </p>
          <div style="background: #1E293B; color: #F8FAFC; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 0.86rem; line-height: 1.5; white-space: pre-wrap; margin-bottom: 14px;">Por favor omite esta póliza manual MISC/2026/09/0002 en el script que tenemos de generar la instancia por favor no agreagr este paso y no considerar almenos esta póliza de nif, solo dejemos el caso de la póliza manual MISC/2026/09/0001</div>
          <div style="background: #F1F5F9; border-left: 4px solid #AC0340; padding: 10px 14px; font-size: 0.86rem; color: #334155;">
            <strong>Resultado:</strong> La BD quedó limpia con únicamente el asiento manual típico del contador que ajusta a ciegas.
          </div>
        </div>

        <!-- Prompt 2.3 -->
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <strong style="color: #345D90; font-size: 1.05rem;">2.3. Guion Teleprompter Minuto a Minuto ("Qué decir y qué hacer")</strong>
            <span class="pill-badge-outline" style="color: #5A6578; border-color: #CBD5E1; font-size: 0.7rem;">Sesión 2 · Paso 569</span>
          </div>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 12px;">
            <strong>Propósito:</strong> Transformar el temario abstracto en un manual operativo de cabina de transmisión con sincronización de pantalla y voz.
          </p>
          <div style="background: #1E293B; color: #F8FAFC; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 0.86rem; line-height: 1.5; white-space: pre-wrap; margin-bottom: 14px;">habias preparado un script de que decir y hacer no lo veo donde esta o por que ya no lo muestras?

Estructura el guion segundo a segundo para la transmisión en directo con dos columnas claras:
- Minuto y Qué proyectar en pantalla en Odoo (pestañas, clics, filtros exactos)
- Speech textual de lo que debo decir frente al micrófono (anécdotas, preguntas al chat y alertas)</div>
          <div style="background: #F1F5F9; border-left: 4px solid #AC0340; padding: 10px 14px; font-size: 0.86rem; color: #334155;">
            <strong>Resultado:</strong> El archivo <code>GUION_DE_TRANSMISION_QUE_DECIR_Y_QUE_HACER.md</code>, con timing rebalanceado para 23 minutos de preguntas y respuestas en vivo.
          </div>
        </div>
      </section>

      <!-- FASE 3: SLIDES -->
      <section id="fase-slides" style="margin-bottom: 32px;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px; border-bottom: 2px solid #E2E8F0; padding-bottom: 12px;">
          <span class="pill-badge" style="font-size: 0.85rem; background: #172A45;">FASE 3</span>
          <h2 style="font-size: 1.5rem; color: #27282F; margin: 0;">Prompts Clave para Generar las SLIDES y Portal Web</h2>
        </div>

        <!-- Prompt 3.1 -->
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px; margin-bottom: 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <strong style="color: #172A45; font-size: 1.05rem;">3.1. Hook Inmediato en Slide 2 y Metodología en 4 Pasos</strong>
            <span class="pill-badge-outline" style="color: #5A6578; border-color: #CBD5E1; font-size: 0.7rem;">Sesión 2 · Diseño Web</span>
          </div>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 12px;">
            <strong>Propósito:</strong> Diseñar la presentación no como diapositivas pasivas, sino como un generador de intriga y una guía metodológica estructurada.
          </p>
          <div style="background: #1E293B; color: #F8FAFC; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 0.86rem; line-height: 1.5; white-space: pre-wrap; margin-bottom: 14px;">Ahora necesitamos las diapositivas de la masterclass. Debe ser una presentación interactiva web en HTML/JS lista para proyectar en pantalla completa, aplicando la marca y colores oficiales de Vauxoo.
Quiero que la Slide 2 sea inmediatamente el HOOK: poner la captura del balance con el descuadre de -$17,760 MXN para captar la atención de inmediato antes de entrar en la teoría de Odoo 19.
En la Slide del Bloque 5, no resuelvas la auditoría diciendo 'haz clic aquí'; explica la metodología paso a paso de los 4 pasos para conciliar contabilidad vs inventario valorado.</div>
          <div style="background: #F1F5F9; border-left: 4px solid #172A45; padding: 10px 14px; font-size: 0.86rem; color: #334155;">
            <strong>Resultado:</strong> Diapositivas interactivas con navegación fluida, cronómetro integrado, visor de notas de orador y la Slide 14 detallando los 4 pasos forenses.
          </div>
        </div>

        <!-- Prompt 3.2 -->
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <strong style="color: #172A45; font-size: 1.05rem;">3.2. Congelación y Publicación en GitHub Pages (Baseline v5.0)</strong>
            <span class="pill-badge-outline" style="color: #5A6578; border-color: #CBD5E1; font-size: 0.7rem;">Sesión 2 · Paso 1339</span>
          </div>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 12px;">
            <strong>Propósito:</strong> Cerrar la fase de desarrollo y publicar una URL pública lista para compartir con alumnos y colegas.
          </p>
          <div style="background: #1E293B; color: #F8FAFC; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 0.86rem; line-height: 1.5; white-space: pre-wrap; margin-bottom: 14px;">por ahora guarda esto como la ultima versión, para cuando te pida cambios no tengas que hacer de nuevo todo y solo se actualice sobre la ultima version</div>
          <div style="background: #F1F5F9; border-left: 4px solid #172A45; padding: 10px 14px; font-size: 0.86rem; color: #334155;">
            <strong>Resultado:</strong> Publicación del tag Git <code>v5.0-baseline</code> en GitHub y despliegue del portal activo en GitHub Pages.
          </div>
        </div>
      </section>

      <!-- Summary Box -->
      <div style="background: #F8FAFC; border: 2px dashed #CBD5E1; border-radius: 8px; padding: 24px; text-align: center;">
        <h4 style="font-size: 1.1rem; color: #27282F; margin-bottom: 8px;">Enlaces de Acceso Directo y Recursos</h4>
        <div style="display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; margin-top: 14px;">
          <a href="index.html" class="btn btn-sm">🖥️ Portal Maestro</a>
          <a href="slides.html" target="_blank" class="btn btn-sm btn-secondary" style="color:#27282F; border-color:#CBD5E1;">↗️ Slides a Pantalla Completa</a>
          <a href="checklist.html" target="_blank" class="btn btn-sm btn-secondary" style="color:#27282F; border-color:#CBD5E1;">📋 Checklist de Auditoría</a>
          <a href="guia-mapeo.html" target="_blank" class="btn btn-sm btn-secondary" style="color:#27282F; border-color:#CBD5E1;">📊 Guía de Mapeo v18→v19</a>
        </div>
      </div>

    </div>
    '''

if __name__ == "__main__":
    print("make_prompts_content.py ready.")
