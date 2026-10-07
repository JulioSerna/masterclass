#!/usr/bin/env python3
import os
from compile_all import CSS_STYLES, logo_white_svg
from make_prompts_content import get_prompts_html

prompts_body = get_prompts_html()

PROMPTS_PAGE = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prompts Clave de IA · Masterclass Odoo 19.0 · Vauxoo Academy</title>
  <style>
    {CSS_STYLES}
  </style>
</head>
<body style="background: #F1F5F9;">

  <!-- Header -->
  <header class="academy-navbar">
    <div class="nav-container">
      <div class="nav-brand">
        <div class="nav-logo-svg">{logo_white_svg}</div>
        <div class="nav-badge-box">
          <div class="nav-main-title">
            <span>PROMPTS CLAVE & METODOLOGÍA</span>
            <span class="pill-badge-outline">INGENIERÍA DE IA</span>
          </div>
          <span class="nav-sub-title">Julio Serna · Masterclass Odoo 19.0</span>
        </div>
      </div>
      <div class="nav-actions">
        <a href="index.html" class="btn btn-sm btn-secondary">
          🏠 Portal Principal
        </a>
        <button class="btn btn-sm" onclick="window.print()">
          🖨️ Imprimir / Guardar PDF
        </button>
      </div>
    </div>
  </header>

  <main style="padding: 24px 16px;">
    {prompts_body}
  </main>

  <footer style="text-align: center; padding: 24px; color: #64748B; font-size: 0.85rem;">
    Vauxoo Academy © 2026 · Documentación técnica de prompts para la Masterclass Odoo 19.0
  </footer>

</body>
</html>
"""

with open("prompts.html", "w", encoding="utf-8") as f:
    f.write(PROMPTS_PAGE)

print("prompts.html generated successfully!")
