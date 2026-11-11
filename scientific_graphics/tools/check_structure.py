#!/usr/bin/env python3
"""Lekki sprawdzacz obecności plików w forku; nie ocenia ich jakości."""
from pathlib import Path

BASE=Path(__file__).resolve().parent.parent
CHECKS={
 'IrfanView 1':('pages/solutions/01_sol_irfanview/01_batch',['batch_settings.png']),
 'IrfanView 2':('pages/solutions/01_sol_irfanview/02_panorama',['left.png','right.png','panorama.png']),
 'Inkscape 1':('pages/solutions/02_sol_inkscape/01_objects',['objects.svg','objects.png']),
 'Inkscape 2':('pages/solutions/02_sol_inkscape/02_arrange',['arranged.svg','arranged.png']),
 'Inkscape 3':('pages/solutions/02_sol_inkscape/03_bezier_01',['bezier_01.svg','bezier_01.png']),
 'Inkscape 4':('pages/solutions/02_sol_inkscape/04_bezier_02',['bezier_02.svg','bezier_02.png']),
 'Inkscape 5':('pages/solutions/02_sol_inkscape/05_trace_bitmap',['traced.svg','traced.png']),
 'TikZiT':('pages/solutions/03_sol_tikzit',['main.tex','main.pdf','styles.tikzstyles','figures/01_energy_flow.tikz','figures/02_stable_equilibrium.tikz','figures/03_measurement_chain.tikz']),
 'AI 1':('pages/solutions/04_sol_ai/01_style_transfer',['drawing.png','prompts.md']),
 'AI 2':('pages/solutions/04_sol_ai/02_room',['room_before.png','room_after.png','prompts.md']),
 'AI 3':('pages/solutions/04_sol_ai/03_historical_backpack',['backpack.png','description.md','prompts.md']),
 'AI 4':('pages/solutions/04_sol_ai/04_building',['new_faculty.png','prompts.md']),
 'AI 5':('pages/solutions/04_sol_ai/05_lecture_infographics',['reference_pl.png','lecture_plan.md','01.png','02.png','03.png','04.png','05.png','lecture.pdf','prompts.md']),
 'AI 6':('pages/solutions/04_sol_ai/06_red_corrections',['checked.png','mistakes.md','prompts.md']),
 'AI 7':('pages/solutions/04_sol_ai/07_handwritten_notes',['notes_01.png','verification.md','prompts.md']),
}

for name,(folder,paths) in CHECKS.items():
    missing=[p for p in paths if not (BASE/folder/p).is_file()]
    status='OK' if not missing else 'BRAKUJE'
    print(f'{status:7} | {name}: '+(', '.join(missing) if missing else 'wszystkie podstawowe pliki obecne'))
print('\nWeryfikacja wyłącznie techniczna. Sprawdź merytorycznie zawartość, SVG i obrazy.')
