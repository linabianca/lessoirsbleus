from pathlib import Path
import re

path = Path(r'c:\Users\linab\OneDrive\Bureau\Lina - Portfolio\ophelia.html')
content = path.read_text(encoding='utf-8')

replacements = [
    (
        r'(<tr><th>UNIVERS SONORE</th><td>)Musique baroque européenne &amp; opéra cantonais en direct(</td></tr><tr><th>ESPACES CIBLES</th>)',
        r'\1Musique baroque européenne &amp; opéra cantonais en direct, musique originale de <a href="https://www.instagram.com/romainfirroloni/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Romain Firroloni</a>\2',
    ),
    (
        r'(<tr><th>SONIC WORLD</th><td>)European baroque music &amp; live Cantonese opera(</td></tr><tr><th>TARGET SPACES</th>)',
        r'\1European baroque music &amp; live Cantonese opera, original music by <a href="https://www.instagram.com/romainfirroloni/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Romain Firroloni</a>\2',
    ),
    (
        r'(<tr><th>UNIVERSO SONORO</th><td>)Musica barocca europea &amp; opera cantonese dal vivo(</td></tr><tr><th>SPAZI TARGET</th>)',
        r'\1Musica barocca europea &amp; opera cantonese dal vivo, musica originale di <a href="https://www.instagram.com/romainfirroloni/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Romain Firroloni</a>\2',
    ),
    (
        r'(<tr><th>KLANGWELT</th><td>)Europäische Barockmusik &amp; kantonesische Oper live(</td></tr><tr><th>ZIELRÄUME</th>)',
        r'\1Europäische Barockmusik &amp; kantonesische Oper live, Originalmusik von <a href="https://www.instagram.com/romainfirroloni/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Romain Firroloni</a>\2',
    ),
    (
        r'(<tr><th>UNIVERSO SONORO</th><td>)Música barroca europea &amp; ópera cantonesa en directo(</td></tr><tr><th>ESPACIOS OBJETIVO</th>)',
        r'\1Música barroca europea &amp; ópera cantonesa en directo, música original de <a href="https://www.instagram.com/romainfirroloni/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Romain Firroloni</a>\2',
    ),
    (
        r'(<tr><th>العالم الصوتي</th><td>)موسيقى باروكية أوروبية &amp; أوبرا كانتونية حية(</td></tr><tr><th>الأماكن المستهدفة</th>)',
        r'\1موسيقى باروكية أوروبية &amp; أوبرا كانتونية حية، موسيقى أصلية من <a href="https://www.instagram.com/romainfirroloni/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Romain Firroloni</a>\2',
    ),
]

for pattern, replacement in replacements:
    content, count = re.subn(pattern, replacement, content, count=1)
    if count != 1:
        raise SystemExit(f'Pattern not replaced: {pattern}')

# Add the visuals/poster line to each localized table right before the target spaces row.
insertions = [
    (
        r'(</td></tr><tr><th>ESPACES CIBLES</th>)',
        r'</td></tr><tr><th>VISUELS ET AFFICHE</th><td><a href="https://www.instagram.com/mehrasa_tavasolian/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Mehrasa Tavasolian</a></td></tr><tr><th>ESPACES CIBLES</th>',
        1,
    ),
    (
        r'(</td></tr><tr><th>TARGET SPACES</th>)',
        r'</td></tr><tr><th>VISUALS AND POSTER</th><td><a href="https://www.instagram.com/mehrasa_tavasolian/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Mehrasa Tavasolian</a></td></tr><tr><th>TARGET SPACES</th>',
        1,
    ),
    (
        r'(</td></tr><tr><th>SPAZI TARGET</th>)',
        r'</td></tr><tr><th>VISUALI E LOCANDINA</th><td><a href="https://www.instagram.com/mehrasa_tavasolian/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Mehrasa Tavasolian</a></td></tr><tr><th>SPAZI TARGET</th>',
        1,
    ),
    (
        r'(</td></tr><tr><th>ZIELRÄUME</th>)',
        r'</td></tr><tr><th>VISUELLE UND PLAKAT</th><td><a href="https://www.instagram.com/mehrasa_tavasolian/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Mehrasa Tavasolian</a></td></tr><tr><th>ZIELRÄUME</th>',
        1,
    ),
    (
        r'(</td></tr><tr><th>ESPACIOS OBJETIVO</th>)',
        r'</td></tr><tr><th>VISUALES Y CARTEL</th><td><a href="https://www.instagram.com/mehrasa_tavasolian/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Mehrasa Tavasolian</a></td></tr><tr><th>ESPACIOS OBJETIVO</th>',
        1,
    ),
    (
        r'(</td></tr><tr><th>الأماكن المستهدفة</th>)',
        r'</td></tr><tr><th>المرئيات والملصق</th><td><a href="https://www.instagram.com/mehrasa_tavasolian/" target="_blank" rel="noopener noreferrer" style="color: #f4d03f; text-decoration: none; border-bottom: 2px solid #f4d03f;">Mehrasa Tavasolian</a></td></tr><tr><th>الأماكن المستهدفة</th>',
        1,
    ),
]

for pattern, replacement, expected_count in insertions:
    content, count = re.subn(pattern, replacement, content, count=expected_count)
    if count != expected_count:
        raise SystemExit(f'Insertion failed for: {pattern}')

path.write_text(content, encoding='utf-8', newline='\n')
print('updated')
