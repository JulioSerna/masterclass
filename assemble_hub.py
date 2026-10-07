#!/usr/bin/env python3
import os
from compile_all import CSS_STYLES, slides, checklist_html, mapeo_html, cronograma_html, logo_white_svg
from make_prompts_content import get_prompts_html

prompts_html = get_prompts_html()

# Build slides HTML inside stage
slides_boxes_html = []
thumbnails_html = []

for idx, s in enumerate(slides):
    active_cls = " active" if idx == 0 else ""
    bg_cls = " bg-gradient" if s["bg"] == "gradient" else " bg-white"
    texture_markup = '<div class="texture-overlay"></div>' if s["bg"] == "gradient" else ""
    
    slides_boxes_html.append(f'''
    <div class="slide-box{active_cls}{bg_cls}" id="slide-{s["id"]}" data-id="{s["id"]}" data-title="{s["title"]}" data-notes="{s["notes"]}" data-time="{s["time"]}">
      {texture_markup}
      {s["html"]}
    </div>
    ''')
    
    thumbnails_html.append(f'''
    <button class="thumb-btn{active_cls}" onclick="goToSlide({s["id"]})" id="thumb-{s["id"]}">
      {s["id"]}. {s["title"]}
    </button>
    ''')

ALL_SLIDES_HTML = "\n".join(slides_boxes_html)
ALL_THUMBS_HTML = "\n".join(thumbnails_html)

INDEX_JS = '''
<script>
let currentSlide = 1;
const totalSlides = __TOTAL_SLIDES__;
let timerSeconds = 0;
let timerInterval = null;
let timerRunning = false;

function switchTab(tabId) {
  document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  
  const targetPane = document.getElementById('tab-' + tabId);
  const targetBtn = document.getElementById('btn-tab-' + tabId);
  if (targetPane) targetPane.classList.add('active');
  if (targetBtn) targetBtn.classList.add('active');
  
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function updateSlideDisplay() {
  document.querySelectorAll('.slide-box').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.thumb-btn').forEach(el => el.classList.remove('active'));
  
  const activeSlide = document.getElementById('slide-' + currentSlide);
  const activeThumb = document.getElementById('thumb-' + currentSlide);
  
  if (activeSlide) {
    activeSlide.classList.add('active');
    document.getElementById('currentSlideNum').innerText = currentSlide;
    document.getElementById('currentSlideTitle').innerText = activeSlide.dataset.title;
    document.getElementById('speakerNotesText').innerText = activeSlide.dataset.notes;
    document.getElementById('slideTargetTime').innerText = activeSlide.dataset.time;
  }
  if (activeThumb) {
    activeThumb.classList.add('active');
    activeThumb.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
  }
}

function nextSlide() {
  if (currentSlide < totalSlides) {
    currentSlide++;
    updateSlideDisplay();
  }
}

function prevSlide() {
  if (currentSlide > 1) {
    currentSlide--;
    updateSlideDisplay();
  }
}

function goToSlide(n) {
  if (n >= 1 && n <= totalSlides) {
    currentSlide = n;
    updateSlideDisplay();
  }
}

function toggleFullscreen() {
  const elem = document.getElementById('deckContainer');
  if (!document.fullscreenElement) {
    elem.requestFullscreen().catch(err => {
      alert(`Pantalla completa: ${err.message}`);
    });
  } else {
    document.exitFullscreen();
  }
}

function toggleSpeakerNotes() {
  document.getElementById('speakerNotesPanel').classList.toggle('active');
}

function formatTime(sec) {
  const m = Math.floor(sec / 60).toString().padStart(2, '0');
  const s = (sec % 60).toString().padStart(2, '0');
  return `${m}:${s}`;
}

function toggleTimer() {
  const btn = document.getElementById('timerToggleBtn');
  if (timerRunning) {
    clearInterval(timerInterval);
    timerRunning = false;
    btn.innerText = '▶️ Iniciar';
  } else {
    timerInterval = setInterval(() => {
      timerSeconds++;
      document.getElementById('deckTimerVal').innerText = formatTime(timerSeconds);
    }, 1000);
    timerRunning = true;
    btn.innerText = '⏸️ Pausar';
  }
}

function resetTimer() {
  clearInterval(timerInterval);
  timerRunning = false;
  timerSeconds = 0;
  document.getElementById('deckTimerVal').innerText = '00:00';
  document.getElementById('timerToggleBtn').innerText = '▶️ Iniciar';
}

window.addEventListener('keydown', (e) => {
  const isDeckVisible = document.getElementById('tab-presentacion').classList.contains('active');
  if (!isDeckVisible) return;
  
  if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
    e.preventDefault();
    nextSlide();
  } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
    e.preventDefault();
    prevSlide();
  } else if (e.key === 'Home') {
    e.preventDefault();
    goToSlide(1);
  } else if (e.key === 'End') {
    e.preventDefault();
    goToSlide(totalSlides);
  } else if (e.key.toLowerCase() === 'f') {
    toggleFullscreen();
  } else if (e.key.toLowerCase() === 'n') {
    toggleSpeakerNotes();
  }
});

function updateProgress(changedCheckbox) {
  const checkboxes = document.querySelectorAll('.checklist-sections input[type="checkbox"]');
  let checked = 0;
  const state = {};
  
  checkboxes.forEach((cb, idx) => {
    const parent = cb.closest('.chk-item');
    const id = parent ? parent.dataset.id : 'chk_' + (idx + 1);
    state[id] = cb.checked;
    if (cb.checked) checked++;
  });
  
  const total = checkboxes.length;
  const pct = Math.round((checked / total) * 100);
  
  const pBar = document.getElementById('checklistProgress');
  const pStats = document.getElementById('checklistStats');
  if (pBar) pBar.style.width = pct + '%';
  if (pStats) pStats.innerText = `${checked} de ${total} puntos validados (${pct}%)`;
  
  localStorage.setItem('vauxoo_masterclass_chk_state', JSON.stringify(state));
}

function loadChecklistState() {
  const saved = localStorage.getItem('vauxoo_masterclass_chk_state');
  if (saved) {
    try {
      const state = JSON.parse(saved);
      document.querySelectorAll('.checklist-sections input[type="checkbox"]').forEach((cb) => {
        const parent = cb.closest('.chk-item');
        if (parent && parent.dataset.id in state) {
          cb.checked = state[parent.dataset.id];
        }
      });
      updateProgress();
    } catch(e) {}
  }
  
  const metaSaved = localStorage.getItem('vauxoo_masterclass_meta');
  if (metaSaved) {
    try {
      const m = JSON.parse(metaSaved);
      if (document.getElementById('metaEmpresa')) document.getElementById('metaEmpresa').value = m.empresa || '';
      if (document.getElementById('metaFecha')) document.getElementById('metaFecha').value = m.fecha || '';
      if (document.getElementById('metaLogistica')) document.getElementById('metaLogistica').value = m.logistica || '';
      if (document.getElementById('metaContador')) document.getElementById('metaContador').value = m.contador || '';
    } catch(e) {}
  }
}

function saveMeta() {
  const m = {
    empresa: document.getElementById('metaEmpresa') ? document.getElementById('metaEmpresa').value : '',
    fecha: document.getElementById('metaFecha') ? document.getElementById('metaFecha').value : '',
    logistica: document.getElementById('metaLogistica') ? document.getElementById('metaLogistica').value : '',
    contador: document.getElementById('metaContador') ? document.getElementById('metaContador').value : ''
  };
  localStorage.setItem('vauxoo_masterclass_meta', JSON.stringify(m));
}

function checkAllItems(val) {
  document.querySelectorAll('.checklist-sections input[type="checkbox"]').forEach(cb => cb.checked = val);
  updateProgress();
}

function resetChecklist() {
  if (confirm('¿Deseas reiniciar todas las casillas del checklist?')) {
    checkAllItems(false);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  updateSlideDisplay();
  loadChecklistState();
});
</script>
'''

# 1. INDEX.HTML
INDEX_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vauxoo Academy · Masterclass 2026: De la Logística a la Contabilidad (Odoo 19.0 MX)</title>
  <style>
    {CSS_STYLES}
  </style>
</head>
<body>

  <!-- Top Navbar -->
  <header class="academy-navbar">
    <div class="nav-container">
      <div class="nav-brand">
        <div class="nav-logo-svg">{logo_white_svg}</div>
        <div class="nav-badge-box">
          <div class="nav-main-title">
            <span>MASTERCLASS 2026</span>
            <span class="pill-badge-outline">ODOO 19.0 · MX</span>
          </div>
          <span class="nav-sub-title">Julio Serna · De la Logística a la Contabilidad</span>
        </div>
      </div>

      <!-- Navigation Tabs -->
      <nav class="nav-tabs-wrapper">
        <button class="tab-btn active" id="btn-tab-presentacion" onclick="switchTab('presentacion')">
          🖥️ Presentación en Vivo
        </button>
        <button class="tab-btn" id="btn-tab-checklist" onclick="switchTab('checklist')">
          📋 Entregable #1: Checklist
        </button>
        <button class="tab-btn" id="btn-tab-mapeo" onclick="switchTab('mapeo')">
          📊 Entregable #2: Tabla de Mapeo
        </button>
        <button class="tab-btn" id="btn-tab-cronograma" onclick="switchTab('cronograma')">
          ⏱️ Minuto a Minuto
        </button>
        <button class="tab-btn" id="btn-tab-prompts" onclick="switchTab('prompts')">
          💡 Prompts de IA
        </button>
      </nav>

      <!-- Action buttons -->
      <div class="nav-actions">
        <a href="prompts.html" target="_blank" class="btn btn-sm btn-secondary">
          ↗️ Prompts Standalone
        </a>
        <a href="slides.html" target="_blank" class="btn btn-sm btn-secondary">
          ↗️ Slides Standalone
        </a>
        <button class="btn btn-sm" onclick="window.print()">
          🖨️ Imprimir PDF
        </button>
      </div>
    </div>
  </header>

  <!-- Main Content Wrapper -->
  <main class="app-wrapper">

    <!-- TAB 1: PRESENTACIÓN INTERACTIVA -->
    <div class="tab-pane active" id="tab-presentacion">
      <div class="deck-container" id="deckContainer">
        <!-- Deck Top Toolbar -->
        <div class="deck-top-bar">
          <div class="deck-info">
            <span class="pill-badge" id="currentSlideNumBadge">Slide <span id="currentSlideNum">1</span> / {len(slides)}</span>
            <strong id="currentSlideTitle" style="color:#FFFFFF;">Portada Oficial</strong>
            <span class="pill-badge-outline" style="font-size:0.7rem;">Meta: <span id="slideTargetTime">00:00</span></span>
          </div>
          <div class="deck-controls">
            <div class="deck-timer" id="deckTimerVal">00:00</div>
            <button class="btn btn-sm btn-secondary" id="timerToggleBtn" onclick="toggleTimer()">▶️ Iniciar</button>
            <button class="btn btn-sm btn-secondary" onclick="resetTimer()">🔄</button>
            <button class="btn btn-sm btn-light" onclick="prevSlide()" title="Slide Anterior (Flecha Izq)">◀ Anterior</button>
            <button class="btn btn-sm btn-light" onclick="nextSlide()" title="Siguiente Slide (Flecha Der)">Siguiente ▶</button>
            <button class="btn btn-sm btn-secondary" onclick="toggleSpeakerNotes()" title="Notas del Orador (N)">🎙️ Notas</button>
            <button class="btn btn-sm btn-secondary" onclick="toggleFullscreen()" title="Pantalla Completa (F)">⛶ Fullscreen</button>
          </div>
        </div>

        <!-- Slide Stage -->
        <div class="slide-stage" id="slideStage">
          {ALL_SLIDES_HTML}
        </div>

        <!-- Speaker Notes Panel -->
        <div class="speaker-notes-panel" id="speakerNotesPanel">
          <div class="notes-header">
            <span>🎙️ Notas y Puntos de Control del Ponente (Julio Serna)</span>
            <span>Atajo: Tecla [N] para ocultar/mostrar</span>
          </div>
          <div id="speakerNotesText">
            Bienvenida y contextualización inicial.
          </div>
        </div>

        <!-- Slide Thumbnails Strip -->
        <div class="deck-thumbnails-strip">
          {ALL_THUMBS_HTML}
        </div>
      </div>
    </div>

    <!-- TAB 2: ENTREGABLE #1 CHECKLIST -->
    <div class="tab-pane" id="tab-checklist">
      {checklist_html}
    </div>

    <!-- TAB 3: ENTREGABLE #2 MAPEO & ARQUITECTURA -->
    <div class="tab-pane" id="tab-mapeo">
      {mapeo_html}
    </div>

    <!-- TAB 4: CRONOGRAMA MINUTO A MINUTO -->
    <div class="tab-pane" id="tab-cronograma">
      {cronograma_html}
    </div>

    <!-- TAB 5: PROMPTS CLAVE DE IA -->
    <div class="tab-pane" id="tab-prompts">
      {prompts_html}
    </div>

  </main>

  {INDEX_JS.replace("__TOTAL_SLIDES__", str(len(slides)))}
</body>
</html>
"""

# 2. SLIDES.HTML (Standalone Presentation)
SLIDES_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Slides · Vauxoo Academy Masterclass 2026: Valoración de Inventarios en Odoo 19.0</title>
  <style>
    {CSS_STYLES}
    html, body {{
      height: 100%;
      background: #0F172A;
      overflow: hidden;
    }}
    .slides-app {{
      display: flex;
      flex-direction: column;
      height: 100vh;
      width: 100vw;
    }}
    .slides-stage-fs {{
      flex: 1;
      position: relative;
      background: #FFFFFF;
      overflow-y: auto;
    }}
  </style>
</head>
<body>
  <div class="slides-app">
    <!-- Top Bar -->
    <div class="deck-top-bar" style="border-radius:0;">
      <div class="deck-info">
        <span class="pill-badge">Slide <span id="currentSlideNum">1</span> / {len(slides)}</span>
        <strong id="currentSlideTitle" style="color:#FFFFFF;">Portada Oficial</strong>
        <span class="pill-badge-outline">Tiempo: <span id="slideTargetTime">00:00</span></span>
      </div>
      <div class="deck-controls">
        <div class="deck-timer" id="deckTimerVal">00:00</div>
        <button class="btn btn-sm btn-secondary" id="timerToggleBtn" onclick="toggleTimer()">▶️</button>
        <button class="btn btn-sm btn-secondary" onclick="resetTimer()">🔄</button>
        <button class="btn btn-sm btn-light" onclick="prevSlide()">◀ Anterior</button>
        <button class="btn btn-sm btn-light" onclick="nextSlide()">Siguiente ▶</button>
        <button class="btn btn-sm btn-secondary" onclick="toggleSpeakerNotes()">🎙️ Notas</button>
        <button class="btn btn-sm btn-secondary" onclick="toggleFullscreen()">⛶ Fullscreen</button>
        <a href="index.html" class="btn btn-sm btn-secondary">🏠 Portal Principal</a>
      </div>
    </div>

    <!-- Stage -->
    <div class="slides-stage-fs" id="deckContainer">
      {ALL_SLIDES_HTML}
    </div>

    <!-- Speaker Notes -->
    <div class="speaker-notes-panel" id="speakerNotesPanel">
      <div class="notes-header">
        <span>🎙️ Notas del Orador</span>
        <span onclick="toggleSpeakerNotes()" style="cursor:pointer;">✖ Cerrar</span>
      </div>
      <div id="speakerNotesText">Notas...</div>
    </div>

    <!-- Thumbnails -->
    <div class="deck-thumbnails-strip">
      {ALL_THUMBS_HTML}
    </div>
  </div>

  <script>
  let currentSlide = 1;
  const totalSlides = {len(slides)};
  let timerSeconds = 0;
  let timerInterval = null;
  let timerRunning = false;

  function updateSlideDisplay() {{
    document.querySelectorAll('.slide-box').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.thumb-btn').forEach(el => el.classList.remove('active'));
    
    const activeSlide = document.getElementById('slide-' + currentSlide);
    const activeThumb = document.getElementById('thumb-' + currentSlide);
    
    if (activeSlide) {{
      activeSlide.classList.add('active');
      document.getElementById('currentSlideNum').innerText = currentSlide;
      document.getElementById('currentSlideTitle').innerText = activeSlide.dataset.title;
      document.getElementById('speakerNotesText').innerText = activeSlide.dataset.notes;
      document.getElementById('slideTargetTime').innerText = activeSlide.dataset.time;
    }}
    if (activeThumb) {{
      activeThumb.classList.add('active');
      activeThumb.scrollIntoView({{ behavior: 'smooth', inline: 'center', block: 'nearest' }});
    }}
  }}

  function nextSlide() {{
    if (currentSlide < totalSlides) {{
      currentSlide++;
      updateSlideDisplay();
    }}
  }}
  function prevSlide() {{
    if (currentSlide > 1) {{
      currentSlide--;
      updateSlideDisplay();
    }}
  }}
  function goToSlide(n) {{
    if (n >= 1 && n <= totalSlides) {{
      currentSlide = n;
      updateSlideDisplay();
    }}
  }}
  function toggleFullscreen() {{
    if (!document.fullscreenElement) {{
      document.documentElement.requestFullscreen();
    }} else {{
      document.exitFullscreen();
    }}
  }}
  function toggleSpeakerNotes() {{
    document.getElementById('speakerNotesPanel').classList.toggle('active');
  }}
  function formatTime(sec) {{
    const m = Math.floor(sec / 60).toString().padStart(2, '0');
    const s = (sec % 60).toString().padStart(2, '0');
    return `${{m}}:${{s}}`;
  }}
  function toggleTimer() {{
    const btn = document.getElementById('timerToggleBtn');
    if (timerRunning) {{
      clearInterval(timerInterval);
      timerRunning = false;
      btn.innerText = '▶️';
    }} else {{
      timerInterval = setInterval(() => {{
        timerSeconds++;
        document.getElementById('deckTimerVal').innerText = formatTime(timerSeconds);
      }}, 1000);
      timerRunning = true;
      btn.innerText = '⏸️';
    }}
  }}
  function resetTimer() {{
    clearInterval(timerInterval);
    timerRunning = false;
    timerSeconds = 0;
    document.getElementById('deckTimerVal').innerText = '00:00';
    document.getElementById('timerToggleBtn').innerText = '▶️';
  }}

  window.addEventListener('keydown', (e) => {{
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
      e.preventDefault();
      nextSlide();
    }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
      e.preventDefault();
      prevSlide();
    }} else if (e.key === 'Home') {{
      e.preventDefault();
      goToSlide(1);
    }} else if (e.key === 'End') {{
      e.preventDefault();
      goToSlide(totalSlides);
    }} else if (e.key.toLowerCase() === 'f') {{
      toggleFullscreen();
    }} else if (e.key.toLowerCase() === 'n') {{
      toggleSpeakerNotes();
    }}
  }});

  document.addEventListener('DOMContentLoaded', () => {{
    updateSlideDisplay();
  }});
  </script>
</body>
</html>
"""

# 3. CHECKLIST.HTML
STANDALONE_CHECKLIST_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Entregable #1 · Checklist de Auditoría Logística-Contable (Odoo 19.0 MX)</title>
  <style>
    {CSS_STYLES}
    body {{
      background: #F1F5F9;
      padding: 30px 20px;
    }}
    .container {{
      max-width: 1100px;
      margin: 0 auto;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div style="margin-bottom: 20px; display:flex; justify-content:space-between; align-items:center;" class="no-print">
      <a href="index.html" class="btn btn-sm btn-light">◀ Regresar al Portal Principal</a>
      <span class="pill-badge">VAUXOO ACADEMY · ENTREGABLE OFICIAL</span>
    </div>
    {checklist_html}
  </div>

  <script>
  function updateProgress() {{
    const checkboxes = document.querySelectorAll('.checklist-sections input[type="checkbox"]');
    let checked = 0;
    const state = {{}};
    checkboxes.forEach((cb, idx) => {{
      const parent = cb.closest('.chk-item');
      const id = parent ? parent.dataset.id : 'chk_' + (idx + 1);
      state[id] = cb.checked;
      if (cb.checked) checked++;
    }});
    const total = checkboxes.length;
    const pct = Math.round((checked / total) * 100);
    const pBar = document.getElementById('checklistProgress');
    const pStats = document.getElementById('checklistStats');
    if (pBar) pBar.style.width = pct + '%';
    if (pStats) pStats.innerText = `${{checked}} de ${{total}} puntos validados (${{pct}}%)`;
    localStorage.setItem('vauxoo_masterclass_chk_state', JSON.stringify(state));
  }}

  function loadChecklistState() {{
    const saved = localStorage.getItem('vauxoo_masterclass_chk_state');
    if (saved) {{
      try {{
        const state = JSON.parse(saved);
        document.querySelectorAll('.checklist-sections input[type="checkbox"]').forEach((cb) => {{
          const parent = cb.closest('.chk-item');
          if (parent && parent.dataset.id in state) {{
            cb.checked = state[parent.dataset.id];
          }}
        }});
        updateProgress();
      }} catch(e) {{}}
    }}
    const metaSaved = localStorage.getItem('vauxoo_masterclass_meta');
    if (metaSaved) {{
      try {{
        const m = JSON.parse(metaSaved);
        if (document.getElementById('metaEmpresa')) document.getElementById('metaEmpresa').value = m.empresa || '';
        if (document.getElementById('metaFecha')) document.getElementById('metaFecha').value = m.fecha || '';
        if (document.getElementById('metaLogistica')) document.getElementById('metaLogistica').value = m.logistica || '';
        if (document.getElementById('metaContador')) document.getElementById('metaContador').value = m.contador || '';
      }} catch(e) {{}}
    }}
  }}

  function saveMeta() {{
    const m = {{
      empresa: document.getElementById('metaEmpresa') ? document.getElementById('metaEmpresa').value : '',
      fecha: document.getElementById('metaFecha') ? document.getElementById('metaFecha').value : '',
      logistica: document.getElementById('metaLogistica') ? document.getElementById('metaLogistica').value : '',
      contador: document.getElementById('metaContador') ? document.getElementById('metaContador').value : ''
    }};
    localStorage.setItem('vauxoo_masterclass_meta', JSON.stringify(m));
  }}

  function checkAllItems(val) {{
    document.querySelectorAll('.checklist-sections input[type="checkbox"]').forEach(cb => cb.checked = val);
    updateProgress();
  }}

  function resetChecklist() {{
    if (confirm('¿Deseas reiniciar todas las casillas del checklist?')) {{
      checkAllItems(false);
    }}
  }}

  document.addEventListener('DOMContentLoaded', loadChecklistState);
  </script>
</body>
</html>
"""

# 4. GUIA-MAPEO.HTML
STANDALONE_MAPEO_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Entregable #2 · Tabla de Mapeo v18 → v19 (Vauxoo Academy)</title>
  <style>
    {CSS_STYLES}
    body {{
      background: #F1F5F9;
      padding: 30px 20px;
    }}
    .container {{
      max-width: 1100px;
      margin: 0 auto;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div style="margin-bottom: 20px; display:flex; justify-content:space-between; align-items:center;" class="no-print">
      <a href="index.html" class="btn btn-sm btn-light">◀ Regresar al Portal Principal</a>
      <span class="pill-badge">VAUXOO ACADEMY · ENTREGABLE OFICIAL</span>
    </div>
    {mapeo_html}
  </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(INDEX_HTML)
print("index.html written:", len(INDEX_HTML))

with open("slides.html", "w", encoding="utf-8") as f:
    f.write(SLIDES_HTML)
print("slides.html written:", len(SLIDES_HTML))

with open("checklist.html", "w", encoding="utf-8") as f:
    f.write(STANDALONE_CHECKLIST_HTML)
print("checklist.html written:", len(STANDALONE_CHECKLIST_HTML))

with open("guia-mapeo.html", "w", encoding="utf-8") as f:
    f.write(STANDALONE_MAPEO_HTML)
print("guia-mapeo.html written:", len(STANDALONE_MAPEO_HTML))

print("Build complete!")
