#!/usr/bin/env python3
import base64
import os
import json

from make_slides_content import get_slides
from make_checklist_content import get_checklist_html
from make_mapeo_content import get_mapeo_html
from make_cronograma_content import get_cronograma_html

def b64_font(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Load font base64
sora_bold = b64_font("assets/fonts/sora-bold.woff2")
sora_semibold = b64_font("assets/fonts/sora-semibold.woff2")
sora_regular = b64_font("assets/fonts/sora-regular.woff2")
manrope_regular = b64_font("assets/fonts/manrope-regular.woff2")
manrope_semibold = b64_font("assets/fonts/manrope-semibold.woff2")

logo_white_svg = read_text("assets/logos/vauxoo-academy-logo-white.svg")
logo_light_svg = read_text("assets/logos/vauxoo-academy-logo-light.svg")
texture_svg = read_text("assets/backgrounds/vauxoo-academy-gradient-bg.svg")
texture_b64 = base64.b64encode(texture_svg.encode("utf-8")).decode("utf-8")

DOODLE_OVAL = '''<svg class="doodle-oval" viewBox="0 0 260 70" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14 36 C8 15, 75 7, 150 7 C225 7, 252 20, 248 38 C242 56, 168 62, 96 60 C46 58, 6 48, 15 30" stroke="#AC0340" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

DOODLE_ARROW = '''<svg class="doodle-arrow" viewBox="0 0 70 45" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 38 C26 12, 50 10, 64 16 M46 9 L64 16 L56 32" stroke="#AC0340" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

DOODLE_UNDERLINE = '''<svg class="doodle-underline" viewBox="0 0 220 18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 12 C60 4, 140 16, 216 8" stroke="#AC0340" stroke-width="3" stroke-linecap="round"/></svg>'''

slides = get_slides(DOODLE_OVAL, DOODLE_ARROW, DOODLE_UNDERLINE, logo_white_svg, logo_light_svg)
checklist_html = get_checklist_html(logo_light_svg, DOODLE_UNDERLINE)
mapeo_html = get_mapeo_html(logo_light_svg, DOODLE_UNDERLINE, DOODLE_ARROW)
cronograma_html = get_cronograma_html(logo_light_svg)

CSS_STYLES = f"""
@font-face {{
  font-family: 'Sora';
  src: url('data:font/woff2;base64,{sora_bold}') format('woff2');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}}
@font-face {{
  font-family: 'Sora';
  src: url('data:font/woff2;base64,{sora_semibold}') format('woff2');
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}}
@font-face {{
  font-family: 'Sora';
  src: url('data:font/woff2;base64,{sora_regular}') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}}
@font-face {{
  font-family: 'Manrope';
  src: url('data:font/woff2;base64,{manrope_regular}') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}}
@font-face {{
  font-family: 'Manrope';
  src: url('data:font/woff2;base64,{manrope_semibold}') format('woff2');
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}}

:root {{
  --bg-gradient: linear-gradient(90deg, #345D90 0%, #172A45 100%);
  --rojo-vauxoo: #AC0340;
  --rojo-brillante: #E11E4D;
  --negro-suave: #27282F;
  --blanco: #FFFFFF;
  --borde-suave: #E2E8F0;
  --borde-card: #CBD5E1;
  --gris-fondo: #F1F5F9;
  --gris-surface: #F8FAFC;
  --gris-muted: #64748B;
}}

* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

body {{
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
  color: var(--negro-suave);
  background-color: var(--gris-fondo);
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}}

h1, h2, h3, h4, h5, h6 {{
  font-family: 'Sora', sans-serif;
  font-weight: 700;
  line-height: 1.25;
}}

/* Academy Tokens */
.pill-badge {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background-color: var(--rojo-vauxoo);
  color: var(--blanco);
  font-family: 'Sora', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 4px 12px;
  border-radius: 9999px;
  border: none;
}}

.pill-badge-outline {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background-color: transparent;
  color: var(--blanco);
  font-family: 'Sora', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 3px 11px;
  border-radius: 9999px;
  border: 1px solid rgba(255, 255, 255, 0.45);
}}

.btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background-color: var(--rojo-vauxoo);
  color: var(--blanco);
  font-family: 'Sora', sans-serif;
  font-size: 0.88rem;
  font-weight: 600;
  padding: 8px 18px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.15s ease;
}}
.btn:hover {{
  background-color: var(--rojo-brillante);
}}
.btn-secondary {{
  background-color: transparent;
  color: var(--blanco);
  border: 1px solid rgba(255, 255, 255, 0.45);
}}
.btn-secondary:hover {{
  background-color: rgba(255, 255, 255, 0.15);
}}
.btn-light {{
  background-color: var(--blanco);
  color: var(--negro-suave);
  border: 1px solid var(--borde-card);
}}
.btn-light:hover {{
  background-color: #E2E8F0;
}}
.btn-sm {{
  font-size: 0.78rem;
  padding: 6px 14px;
}}

/* Doodles */
.doodle-wrap {{
  position: relative;
  display: inline-block;
}}
.doodle-oval {{
  position: absolute;
  top: -8px;
  left: -10px;
  width: calc(100% + 20px);
  height: calc(100% + 16px);
  pointer-events: none;
}}
.doodle-underline {{
  position: absolute;
  bottom: -6px;
  left: 0;
  width: 100%;
  height: 12px;
  pointer-events: none;
}}

/* Navbar */
.academy-navbar {{
  background: var(--bg-gradient);
  color: var(--blanco);
  border-bottom: 3px solid var(--rojo-vauxoo);
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 10px rgba(0,0,0,0.15);
}}
.nav-container {{
  max-width: 1440px;
  margin: 0 auto;
  padding: 10px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}}
.nav-brand {{
  display: flex;
  align-items: center;
  gap: 16px;
}}
.nav-logo-svg {{
  height: 38px;
  width: auto;
  display: block;
}}
.nav-logo-svg svg {{
  height: 38px;
  width: auto;
  display: block;
}}
.nav-badge-box {{
  display: flex;
  flex-direction: column;
  gap: 2px;
}}
.nav-main-title {{
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--blanco);
  display: flex;
  align-items: center;
  gap: 8px;
}}
.nav-sub-title {{
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.75);
}}

.nav-tabs-wrapper {{
  display: flex;
  align-items: center;
  gap: 4px;
  background: rgba(0, 0, 0, 0.3);
  padding: 4px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.15);
}}
.tab-btn {{
  background: transparent;
  color: rgba(255, 255, 255, 0.85);
  border: none;
  font-family: 'Sora', sans-serif;
  font-size: 0.82rem;
  font-weight: 600;
  padding: 8px 14px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 6px;
}}
.tab-btn:hover {{
  color: var(--blanco);
  background: rgba(255, 255, 255, 0.12);
}}
.tab-btn.active {{
  background: var(--rojo-vauxoo);
  color: var(--blanco);
}}

.nav-actions {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

/* Main App Wrapper */
.app-wrapper {{
  max-width: 1440px;
  margin: 20px auto 40px;
  padding: 0 20px;
}}

.tab-pane {{
  display: none;
}}
.tab-pane.active {{
  display: block;
}}

/* Deck Presenter Styles */
.deck-container {{
  background: var(--blanco);
  border: 1px solid var(--borde-card);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
}}
.deck-top-bar {{
  background: #1E293B;
  color: var(--blanco);
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}}
.deck-info {{
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 0.85rem;
}}
.deck-controls {{
  display: flex;
  align-items: center;
  gap: 8px;
}}
.deck-timer {{
  background: rgba(255, 255, 255, 0.1);
  padding: 4px 12px;
  border-radius: 6px;
  font-family: monospace;
  font-size: 0.95rem;
  font-weight: 700;
}}

/* Slide Stage */
.slide-stage {{
  position: relative;
  min-height: 640px;
  background: var(--blanco);
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
}}
.slide-box {{
  display: none;
  height: 100%;
  width: 100%;
  padding: 48px 56px;
}}
.slide-box.active {{
  display: block;
}}

.slide-box.bg-gradient {{
  background: var(--bg-gradient);
  color: var(--blanco);
  position: relative;
}}
.slide-box.bg-gradient .texture-overlay {{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('data:image/svg+xml;base64,{texture_b64}');
  background-size: cover;
  background-position: center;
  opacity: 0.18;
  pointer-events: none;
}}
.slide-box.bg-white {{
  background: var(--blanco);
  color: var(--negro-suave);
}}

/* Cover Slide Specifics */
.cover-slide {{
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: relative;
  z-index: 2;
  height: 100%;
}}
.cover-logo-wrap {{
  margin-bottom: 24px;
}}
.cover-logo-wrap svg {{
  height: 52px;
  width: auto;
  display: block;
}}
.cover-badge-row {{
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}}
.cover-title {{
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--blanco);
  line-height: 1.2;
  margin-bottom: 20px;
  max-width: 950px;
}}
.cover-subtitle {{
  font-size: 1.15rem;
  color: rgba(255, 255, 255, 0.88);
  max-width: 800px;
  line-height: 1.6;
  margin-bottom: 40px;
}}
.cover-footer {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  padding-top: 24px;
  max-width: 950px;
}}
.speaker-card {{
  display: flex;
  align-items: center;
  gap: 14px;
}}
.speaker-avatar {{
  width: 48px;
  height: 48px;
  background: var(--rojo-vauxoo);
  color: var(--blanco);
  font-family: 'Sora', sans-serif;
  font-size: 1.1rem;
  font-weight: 700;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255, 255, 255, 0.4);
}}
.speaker-info {{
  display: flex;
  flex-direction: column;
}}
.speaker-name {{
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--blanco);
}}
.speaker-role {{
  font-size: 0.82rem;
  color: rgba(255, 255, 255, 0.75);
}}
.cover-price-tag {{
  text-align: right;
}}
.price-val {{
  display: block;
  font-family: 'Sora', sans-serif;
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--blanco);
}}
.price-label {{
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.75);
}}

/* Slide Components */
.slide-header {{
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 24px;
  position: relative;
  z-index: 2;
}}
.slide-title {{
  font-size: 1.85rem;
  font-weight: 700;
  color: var(--negro-suave);
  margin-top: 6px;
}}
.slide-header-logo svg {{
  height: 34px;
  width: auto;
}}
.slide-lead {{
  font-size: 1.05rem;
  color: #475569;
  margin-bottom: 24px;
  max-width: 900px;
  position: relative;
  z-index: 2;
}}

/* Agenda Grid */
.agenda-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}}
.agenda-card {{
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 18px;
  position: relative;
}}
.agenda-time {{
  font-family: monospace;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--rojo-vauxoo);
  margin-bottom: 6px;
}}
.agenda-num {{
  position: absolute;
  top: 14px;
  right: 16px;
  font-family: 'Sora', sans-serif;
  font-size: 1.3rem;
  font-weight: 700;
  color: #CBD5E1;
}}
.agenda-title {{
  font-family: 'Sora', sans-serif;
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--negro-suave);
  margin-bottom: 6px;
}}
.agenda-desc {{
  font-size: 0.8rem;
  color: var(--gris-muted);
  line-height: 1.4;
}}

/* Split Audit Hook (Slide 3) */
.split-audit-container {{
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 20px;
  align-items: center;
  margin-bottom: 24px;
}}
.audit-col {{
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 24px;
}}
.audit-col-badge {{
  font-family: 'Sora', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--gris-muted);
  text-transform: uppercase;
  margin-bottom: 8px;
}}
.audit-col-title {{
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--negro-suave);
  margin-bottom: 6px;
}}
.audit-code {{
  font-family: monospace;
  font-size: 0.85rem;
  color: #475569;
  background: #E2E8F0;
  padding: 3px 8px;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 12px;
}}
.audit-amount {{
  font-family: 'Sora', sans-serif;
  font-size: 1.9rem;
  font-weight: 700;
  color: var(--negro-suave);
  margin-bottom: 6px;
}}
.audit-detail {{
  font-size: 0.82rem;
  color: var(--gris-muted);
  margin-bottom: 12px;
}}
.audit-status {{
  font-size: 0.82rem;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 6px;
}}
.audit-err {{
  background: #FEE2E2;
  color: #991B1B;
}}
.audit-ok {{
  background: #DCFCE7;
  color: #166534;
}}
.audit-diff-card {{
  background: #FFF1F2;
  border: 2px dashed var(--rojo-vauxoo);
  border-radius: 10px;
  padding: 20px;
  text-align: center;
  min-width: 220px;
}}
.diff-label {{
  font-family: 'Sora', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--rojo-vauxoo);
  text-transform: uppercase;
  display: block;
  margin-bottom: 6px;
}}
.diff-amount {{
  font-family: 'Sora', sans-serif;
  font-size: 1.7rem;
  font-weight: 800;
  color: var(--rojo-vauxoo);
  display: inline-block;
  margin-bottom: 8px;
}}
.diff-warn {{
  font-size: 0.78rem;
  color: #881337;
  font-weight: 600;
  display: block;
}}

.interactive-chat-prompt {{
  background: #EFF6FF;
  border-left: 4px solid #3B82F6;
  padding: 14px 18px;
  border-radius: 0 8px 8px 0;
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 0.95rem;
}}
.prompt-icon {{
  font-size: 1.4rem;
}}

/* Value Grid (Slide 4) */
.value-cards-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  position: relative;
  z-index: 2;
}}
.value-card {{
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 8px;
  padding: 20px;
}}
.value-icon {{
  font-size: 1.6rem;
  margin-bottom: 8px;
}}
.value-card h4 {{
  font-size: 1.05rem;
  color: #FFFFFF;
  margin-bottom: 8px;
}}
.value-card p {{
  font-size: 0.84rem;
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.45;
}}

/* Paradigm Table (Slide 5) */
.paradigm-table-container {{
  overflow-x: auto;
}}
.paradigm-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
}}
.paradigm-table th {{
  background: #1E293B;
  color: #FFFFFF;
  font-family: 'Sora', sans-serif;
  font-size: 0.82rem;
  text-transform: uppercase;
  padding: 12px 16px;
  text-align: left;
}}
.paradigm-table td {{
  padding: 14px 16px;
  border-bottom: 1px solid var(--borde-suave);
  vertical-align: top;
}}
.tag-old {{
  display: inline-block;
  background: #F1F5F9;
  color: #64748B;
  padding: 2px 8px;
  border-radius: 4px;
  font-family: monospace;
  font-size: 0.8rem;
  margin-bottom: 4px;
}}
.tag-new {{
  display: inline-block;
  background: #DCFCE7;
  color: #166534;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  font-family: monospace;
  font-size: 0.8rem;
  margin-bottom: 4px;
}}

/* AVCO Comparison (Slide 6) */
.avco-comparison-grid {{
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 20px;
}}
.avco-card {{
  border-radius: 8px;
  padding: 24px;
}}
.avco-winner {{
  background: var(--gris-surface);
  border: 2px solid var(--rojo-vauxoo);
}}
.avco-discarded {{
  background: #F8FAFC;
  border: 1px solid var(--borde-card);
}}
.avco-card-badge {{
  font-family: 'Sora', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--rojo-vauxoo);
  margin-bottom: 8px;
}}
.avco-legal {{
  font-family: monospace;
  font-size: 0.8rem;
  color: #475569;
  background: #E2E8F0;
  display: inline-block;
  padding: 2px 8px;
  border-radius: 4px;
  margin: 6px 0 12px;
}}
.avco-formula-box {{
  background: #FFFFFF;
  border: 1px solid var(--borde-card);
  border-radius: 6px;
  padding: 14px;
  margin-top: 16px;
}}
.formula-label {{
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--gris-muted);
  display: block;
  margin-bottom: 6px;
}}
.formula-math {{
  font-family: monospace;
  font-size: 0.95rem;
  color: var(--negro-suave);
}}

/* Flow Steps (Slide 7) */
.flow-steps-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}}
.flow-step-card {{
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 20px;
}}
.step-badge {{
  font-family: 'Sora', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--rojo-vauxoo);
  margin-bottom: 8px;
}}
.asiento-box {{
  background: #FFFFFF;
  border: 1px solid var(--borde-card);
  border-radius: 6px;
  padding: 10px;
  margin: 12px 0;
  font-family: monospace;
  font-size: 0.78rem;
}}
.asiento-row {{
  margin-bottom: 4px;
}}
.cargo {{
  color: #166534;
  font-weight: 700;
}}
.abono {{
  color: #991B1B;
  font-weight: 700;
}}
.step-avco {{
  font-size: 0.82rem;
  color: #475569;
  border-top: 1px solid #E2E8F0;
  padding-top: 8px;
}}

/* MRP Split (Slide 8) */
.mrp-split {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  align-items: center;
}}
.mrp-diagram {{
  display: flex;
  flex-direction: column;
  gap: 10px;
}}
.mrp-box {{
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 6px;
  padding: 14px;
}}
.mrp-arrow {{
  text-align: center;
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--gris-muted);
}}
.mrp-tag {{
  font-family: 'Sora', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  color: #475569;
  display: block;
  margin-bottom: 4px;
}}
.alert-box {{
  background: #FEF2F2;
  border-left: 4px solid var(--rojo-vauxoo);
  padding: 20px;
  border-radius: 0 8px 8px 0;
}}
.alert-box h4 {{
  color: #991B1B;
  margin-bottom: 10px;
}}
.styled-list {{
  margin-left: 18px;
  font-size: 0.88rem;
  line-height: 1.6;
}}

/* USD Timeline (Slide 9) */
.usd-timeline {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 24px;
  position: relative;
  z-index: 2;
}}
.timeline-step {{
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 8px;
  padding: 18px;
}}
.timeline-dot {{
  width: 28px;
  height: 28px;
  background: var(--rojo-vauxoo);
  color: #FFFFFF;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Sora', sans-serif;
  font-size: 0.82rem;
  font-weight: 700;
  margin-bottom: 10px;
}}
.timeline-header {{
  font-family: 'Sora', sans-serif;
  font-size: 0.95rem;
  font-weight: 700;
  color: #FFFFFF;
  margin-bottom: 8px;
}}
.tc-badge {{
  display: inline-block;
  background: rgba(255, 255, 255, 0.2);
  color: #FFFFFF;
  font-family: monospace;
  font-size: 0.8rem;
  padding: 3px 8px;
  border-radius: 4px;
  margin: 6px 0;
}}
.timeline-val {{
  font-size: 0.9rem;
  font-weight: 700;
  color: #FFFFFF;
  margin-bottom: 4px;
}}
.timeline-body small {{
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.7);
}}
.usd-verdict-box {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  background: rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 8px;
  padding: 20px;
  position: relative;
  z-index: 2;
}}
.verdict-col h4 {{
  color: #FFFFFF;
  margin-bottom: 6px;
}}
.verdict-col p {{
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.85);
}}

/* Disaster Grid (Slide 10) */
.disaster-grid {{
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 20px;
}}
.disaster-sequence {{
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 14px;
}}
.seq-step {{
  display: flex;
  align-items: center;
  gap: 12px;
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 6px;
  padding: 12px;
  font-size: 0.88rem;
}}
.seq-num {{
  width: 24px;
  height: 24px;
  background: #334155;
  color: #FFFFFF;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 700;
  flex-shrink: 0;
}}
.sat-warn-card {{
  background: #FFF1F2;
  border: 1px solid #FECDD3;
  border-radius: 8px;
  padding: 20px;
}}
.sat-warn-card h4 {{
  color: #9F1239;
  margin-bottom: 12px;
}}
.sat-rule-badge {{
  margin-top: 16px;
  background: var(--rojo-vauxoo);
  color: #FFFFFF;
  padding: 8px 12px;
  border-radius: 6px;
  font-family: 'Sora', sans-serif;
  font-size: 0.78rem;
  font-weight: 700;
  text-align: center;
}}

/* Two Col Grid (Slide 11) */
.two-col-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}}
.disaster-col-card {{
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 22px;
}}
.card-pill {{
  font-family: 'Sora', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  color: #B91C1C;
  margin-bottom: 6px;
}}
.card-lead {{
  font-size: 0.95rem;
  color: #475569;
  margin-bottom: 12px;
}}
.detail-box {{
  background: #FFFFFF;
  border: 1px solid var(--borde-card);
  border-radius: 6px;
  padding: 14px;
  font-size: 0.85rem;
  line-height: 1.5;
}}

/* SAT Fiscal Table (Slide 12) */
.sat-fiscal-table-container {{
  overflow-x: auto;
}}
.sat-fiscal-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
}}
.sat-fiscal-table th {{
  background: #1E293B;
  color: #FFFFFF;
  font-family: 'Sora', sans-serif;
  font-size: 0.8rem;
  padding: 12px 16px;
  text-align: left;
}}
.sat-fiscal-table td {{
  padding: 14px 16px;
  border-bottom: 1px solid var(--borde-suave);
  vertical-align: top;
}}

/* Audit Steps Grid (Slide 13) */
.audit-steps-grid {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  position: relative;
  z-index: 2;
}}
.audit-step-card {{
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 8px;
  padding: 20px;
}}
.audit-step-num {{
  font-family: 'Sora', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--rojo-brillante);
  margin-bottom: 8px;
}}
.audit-step-card h4 {{
  font-size: 1.05rem;
  color: #FFFFFF;
  margin-bottom: 8px;
}}
.audit-step-card p {{
  font-size: 0.82rem;
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.45;
}}
.audit-step-card code {{
  background: rgba(0, 0, 0, 0.3);
  padding: 2px 6px;
  border-radius: 4px;
  color: #FFFFFF;
}}

/* Resolution Container (Slide 14) */
.resolution-container {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}}
.culprit-box {{
  background: #FEF2F2;
  border: 1px solid #FCA5A5;
  border-radius: 8px;
  padding: 22px;
}}
.culprit-badge {{
  font-family: 'Sora', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  color: #B91C1C;
  margin-bottom: 8px;
}}
.culprit-desc {{
  font-size: 0.9rem;
  color: #7F1D1D;
  margin: 10px 0;
}}
.culprit-flaw {{
  background: #FFFFFF;
  border: 1px solid #FECDD3;
  padding: 10px;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 600;
  color: #991B1B;
}}
.action-result-box {{
  background: #F0FDF4;
  border: 1px solid #86EFAC;
  border-radius: 8px;
  padding: 22px;
}}
.result-step {{
  font-size: 0.9rem;
  color: #14532D;
  margin-bottom: 16px;
}}
.balanced-state {{
  background: #FFFFFF;
  border: 1px solid #BBF7D0;
  border-radius: 6px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}}
.bal-item {{
  display: flex;
  justify-content: space-between;
  font-size: 0.9rem;
}}
.bal-equal {{
  text-align: center;
  font-size: 1.2rem;
  font-weight: 700;
  color: #16A34A;
}}
.bal-status {{
  background: #DCFCE7;
  color: #15803D;
  font-family: 'Sora', sans-serif;
  font-size: 0.85rem;
  font-weight: 700;
  text-align: center;
  padding: 8px;
  border-radius: 6px;
  margin-top: 6px;
}}

/* Golden Rules (Slide 15) */
.golden-rules-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}}
.golden-rule-card {{
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 24px;
}}
.rule-medal {{
  font-size: 2rem;
  margin-bottom: 8px;
}}
.rule-num {{
  font-family: 'Sora', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--rojo-vauxoo);
  margin-bottom: 6px;
}}
.golden-rule-card h3 {{
  font-size: 1.1rem;
  color: var(--negro-suave);
  margin-bottom: 10px;
}}
.golden-rule-card p {{
  font-size: 0.85rem;
  color: #475569;
  line-height: 1.5;
}}

/* Hotseat (Slide 16) */
.hotseat-container {{
  display: grid;
  grid-template-columns: 1fr 1.5fr;
  gap: 24px;
  background: rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 8px;
  padding: 30px;
  position: relative;
  z-index: 2;
}}
.hotseat-badge-col {{
  text-align: center;
  border-right: 1px solid rgba(255, 255, 255, 0.15);
  padding-right: 24px;
}}
.hotseat-icon {{
  font-size: 3rem;
  margin-bottom: 10px;
}}
.hotseat-badge-col h3 {{
  font-size: 1.3rem;
  color: #FFFFFF;
  margin-bottom: 8px;
}}
.hotseat-badge-col p {{
  font-size: 0.88rem;
  color: rgba(255, 255, 255, 0.8);
}}
.hotseat-topics h4 {{
  color: #FFFFFF;
  margin-bottom: 12px;
}}

/* Deliverables Grid (Slide 17) */
.deliverables-grid {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}}
.deliv-card {{
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 20px;
  display: flex;
  flex-direction: column;
}}
.deliv-icon {{
  font-size: 2rem;
  margin-bottom: 10px;
}}
.deliv-card h4 {{
  font-size: 1rem;
  color: var(--negro-suave);
  margin-bottom: 8px;
}}
.deliv-card p {{
  font-size: 0.82rem;
  color: var(--gris-muted);
  line-height: 1.45;
  margin-bottom: 16px;
  flex-grow: 1;
}}

/* Closing Card (Slide 18) */
.closing-contact-card {{
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  padding: 24px;
  max-width: 500px;
  margin: 0 auto;
}}

/* Speaker Notes Panel */
.speaker-notes-panel {{
  background: #0F172A;
  color: #E2E8F0;
  padding: 16px 24px;
  border-top: 1px solid #334155;
  font-size: 0.88rem;
  line-height: 1.6;
  display: none;
}}
.speaker-notes-panel.active {{
  display: block;
}}
.notes-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
  font-family: 'Sora', sans-serif;
  font-size: 0.78rem;
  font-weight: 700;
  color: #94A3B8;
  text-transform: uppercase;
}}

/* Thumbnails Strip */
.deck-thumbnails-strip {{
  background: #0F172A;
  padding: 12px 20px;
  display: flex;
  gap: 10px;
  overflow-x: auto;
  border-top: 1px solid #334155;
}}
.thumb-btn {{
  background: #1E293B;
  color: #94A3B8;
  border: 1px solid #334155;
  padding: 6px 12px;
  border-radius: 6px;
  font-family: 'Sora', sans-serif;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.15s ease;
}}
.thumb-btn:hover {{
  background: #334155;
  color: #FFFFFF;
}}
.thumb-btn.active {{
  background: var(--rojo-vauxoo);
  color: #FFFFFF;
  border-color: var(--rojo-vauxoo);
}}

/* DELIVERABLE DOCS (Checklist, Mapeo, Cronograma) */
.deliverable-doc {{
  background: var(--blanco);
  border: 1px solid var(--borde-card);
  border-radius: 12px;
  padding: 40px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
  margin-bottom: 30px;
}}
.doc-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 2px solid var(--rojo-vauxoo);
  padding-bottom: 24px;
  margin-bottom: 24px;
}}
.doc-header-brand svg {{
  height: 42px;
  width: auto;
  display: block;
}}
.doc-header-title {{
  text-align: right;
}}
.doc-header-title h2 {{
  font-size: 1.6rem;
  color: var(--negro-suave);
  margin: 6px 0 4px;
}}
.doc-subtitle {{
  font-size: 0.88rem;
  color: var(--gris-muted);
}}

.doc-toolbar {{
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 14px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}}
.progress-bar-wrap {{
  width: 240px;
  height: 8px;
  background: #E2E8F0;
  border-radius: 9999px;
  overflow: hidden;
  margin-bottom: 4px;
}}
.progress-bar-fill {{
  height: 100%;
  background: var(--rojo-vauxoo);
  transition: width 0.3s ease;
}}
.stats-text {{
  font-size: 0.82rem;
  font-weight: 600;
  color: #475569;
}}
.toolbar-actions {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

/* Meta Grid */
.doc-meta-grid {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 30px;
}}
.meta-field label {{
  font-family: 'Sora', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  color: #475569;
  display: block;
  margin-bottom: 6px;
}}
.meta-input {{
  width: 100%;
  border: 1px solid var(--borde-card);
  border-radius: 4px;
  padding: 6px 10px;
  font-family: 'Manrope', sans-serif;
  font-size: 0.85rem;
  color: var(--negro-suave);
}}

/* Checklist Sections */
.checklist-sections {{
  display: flex;
  flex-direction: column;
  gap: 28px;
}}
.chk-section {{
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  overflow: hidden;
}}
.chk-section-header {{
  background: #F8FAFC;
  border-bottom: 1px solid var(--borde-suave);
  padding: 12px 18px;
  display: flex;
  align-items: center;
  gap: 12px;
}}
.section-badge {{
  background: #334155;
  color: #FFFFFF;
  font-family: 'Sora', sans-serif;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
}}
.chk-section-header h3 {{
  font-size: 1.05rem;
  color: var(--negro-suave);
}}
.chk-list {{
  display: flex;
  flex-direction: column;
}}
.chk-item {{
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 16px;
  align-items: flex-start;
  padding: 14px 18px;
  border-bottom: 1px solid #F1F5F9;
  cursor: pointer;
  transition: background 0.1s ease;
}}
.chk-item:hover {{
  background: #F8FAFC;
}}
.chk-item:last-child {{
  border-bottom: none;
}}
.chk-item input[type="checkbox"] {{
  width: 18px;
  height: 18px;
  accent-color: var(--rojo-vauxoo);
  margin-top: 3px;
}}
.chk-title {{
  font-family: 'Sora', sans-serif;
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--negro-suave);
  margin-bottom: 4px;
}}
.chk-desc {{
  font-size: 0.82rem;
  color: #64748B;
  line-height: 1.45;
}}
.chk-tag {{
  font-family: 'Sora', sans-serif;
  font-size: 0.68rem;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
  white-space: nowrap;
}}
.tag-critico {{
  background: #FEE2E2;
  color: #991B1B;
}}
.tag-alto {{
  background: #FEF3C7;
  color: #92400E;
}}
.tag-normativo {{
  background: #E0E7FF;
  color: #3730A3;
}}
.tag-control {{
  background: #F1F5F9;
  color: #475569;
}}

/* Signoff */
.doc-signoff {{
  margin-top: 36px;
  border-top: 2px solid var(--borde-suave);
  padding-top: 24px;
}}
.signoff-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  margin-top: 16px;
}}
.signoff-box {{
  border: 1px solid var(--borde-card);
  border-radius: 8px;
  padding: 20px;
}}
.signoff-role {{
  font-family: 'Sora', sans-serif;
  font-size: 0.78rem;
  font-weight: 700;
  color: #475569;
  text-transform: uppercase;
  margin-bottom: 40px;
}}
.signoff-line {{
  border-bottom: 1px solid #94A3B8;
  margin-bottom: 8px;
}}
.signoff-name {{
  font-size: 0.82rem;
  color: #64748B;
  margin-bottom: 10px;
}}
.signoff-clause {{
  font-size: 0.75rem;
  color: #94A3B8;
  line-height: 1.4;
}}
.doc-footer {{
  margin-top: 30px;
  border-top: 1px solid var(--borde-suave);
  padding-top: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.78rem;
  color: var(--gris-muted);
}}

/* MAPEO STYLES */
.doc-section {{
  margin-bottom: 36px;
}}
.section-title-wrap {{
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}}
.section-title-wrap h3 {{
  font-size: 1.3rem;
  color: var(--negro-suave);
}}
.section-intro {{
  font-size: 0.95rem;
  color: #475569;
  margin-bottom: 18px;
}}
.table-responsive {{
  overflow-x: auto;
}}
.comparison-table, .sat-matrix-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
}}
.comparison-table th, .sat-matrix-table th {{
  background: #1E293B;
  color: #FFFFFF;
  font-family: 'Sora', sans-serif;
  font-size: 0.8rem;
  padding: 12px 14px;
  text-align: left;
}}
.comparison-table td, .sat-matrix-table td {{
  padding: 14px;
  border-bottom: 1px solid var(--borde-suave);
  vertical-align: top;
}}
.badge-old {{
  display: inline-block;
  background: #F1F5F9;
  color: #475569;
  font-family: monospace;
  font-size: 0.8rem;
  padding: 2px 6px;
  border-radius: 4px;
  margin-bottom: 4px;
}}
.badge-new {{
  display: inline-block;
  background: #DCFCE7;
  color: #166534;
  font-family: monospace;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
  margin-bottom: 4px;
}}

.import-lifecycle-box {{
  display: flex;
  flex-direction: column;
  gap: 16px;
}}
.lifecycle-stage {{
  display: flex;
  gap: 18px;
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 18px;
}}
.stage-num {{
  width: 36px;
  height: 36px;
  background: var(--rojo-vauxoo);
  color: #FFFFFF;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Sora', sans-serif;
  font-weight: 700;
  font-size: 1rem;
  flex-shrink: 0;
}}
.stage-info h4 {{
  font-size: 1.05rem;
  color: var(--negro-suave);
  margin-bottom: 6px;
}}
.asiento-mini {{
  background: #FFFFFF;
  border: 1px solid var(--borde-card);
  border-radius: 6px;
  padding: 10px 14px;
  font-family: monospace;
  font-size: 0.82rem;
  margin: 10px 0;
}}
.stage-memo {{
  font-size: 0.82rem;
  color: #475569;
}}

.math-card {{
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 20px;
}}
.math-formula {{
  background: #FFFFFF;
  border: 1px solid var(--borde-card);
  border-radius: 6px;
  padding: 16px;
  font-family: monospace;
  font-size: 1rem;
  margin-top: 10px;
  color: var(--negro-suave);
}}

/* CRONOGRAMA STYLES */
.cron-summary-grid {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 28px;
}}
.cron-summary-card {{
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 18px;
}}
.cron-summary-label {{
  font-family: 'Sora', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--gris-muted);
  margin-bottom: 4px;
}}
.cron-summary-val {{
  font-family: 'Sora', sans-serif;
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--negro-suave);
}}
.cron-blocks-container {{
  display: flex;
  flex-direction: column;
  gap: 18px;
}}
.cron-block-card {{
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  overflow: hidden;
}}
.cron-block-header {{
  background: #F8FAFC;
  border-bottom: 1px solid var(--borde-suave);
  padding: 14px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}
.cron-time-pill {{
  background: #1E293B;
  color: #FFFFFF;
  font-family: monospace;
  font-size: 0.78rem;
  padding: 4px 10px;
  border-radius: 9999px;
}}
.cron-block-header h3 {{
  font-size: 1.05rem;
  color: var(--negro-suave);
  flex-grow: 1;
  margin: 0 16px;
}}
.cron-block-body {{
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 0.88rem;
}}
.cron-element {{
  line-height: 1.5;
}}
.cron-prep-section {{
  margin-top: 36px;
  background: var(--gris-surface);
  border: 1px solid var(--borde-suave);
  border-radius: 8px;
  padding: 24px;
}}
.prep-grid {{
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 0.9rem;
}}

/* PRINT STYLES */
@media print {{
  .academy-navbar, .doc-toolbar, .deck-top-bar, .deck-thumbnails-strip, .speaker-notes-panel, .no-print {{
    display: none !important;
  }}
  body {{
    background: #FFFFFF !important;
    color: #000000 !important;
  }}
  .app-wrapper {{
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
  }}
  .tab-pane {{
    display: none !important;
  }}
  .tab-pane.active {{
    display: block !important;
  }}
  .deliverable-doc {{
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
  }}
  .doc-meta-grid, .chk-section, .signoff-box, .comparison-table, .sat-matrix-table {{
    border-color: #94A3B8 !important;
  }}
  .page-break {{
    page-break-before: always;
  }}
}}
"""

print("Styles and assets loaded.")
