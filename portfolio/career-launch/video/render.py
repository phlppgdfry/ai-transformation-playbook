"""Compose authentic browser clips with a caption band outside the application image."""
import argparse
import json
import subprocess
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

CAPTIONS = [
    ('Een bedrijfsprobleem, zes onderdelen', 'Onafhankelijk AI-ondersteund portfolio. Fictieve accountingcase; geen klantresultaten.'),
    ('1 / Businesscase: aannames zichtbaar maken', 'Interactieve browserberekening. Adoptie op nul geeft geen vrijgemaakte capaciteit; geen gerealiseerde besparing.'),
    ('2 / Factuurcontrole: regels boven overtuigende taal', 'Interactieve browsercontroles: een cent verschil wordt afgewezen; een onbekende leverancier vraagt review. Geen API-opslag.'),
    ('3 / Agentworkflow: model stelt voor, mensen beslissen', 'Replay van een eerder vastgelegde echte lokale Qwen-run. Geen nieuwe modelaanroep; de CRM-actie is een lokale mock.'),
    ('4 / Kennis: eerst toegang, daarna zoeken', 'Interactieve browserdemo met synthetische bronnen. Finance krijgt geen HR-bron; HR kan de toegestane bron vinden.'),
    ('5 / Evaluatie: ook onveilige antwoorden testen', 'Vergelijking van twee bestaande evaluatierapporten. De onveilige controle hoort te falen; dit bewijst geen algemene AI-veiligheid.'),
    ('6 / Microsoft: voorstellen is niet goedkeuren', 'Replay van de lokale API-demo: eerst weigeren, dan reviewer, dan executor. Geen live Copilot Studio- of Dataverse-uitvoering.'),
    ('Bekijk het bewijs en oefen zelf', 'Azure OCR/inference en de volledige Copilot-runtime blijven ongeverifieerd. Code, demo en leerplan staan in het portfolio.'),
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('capture', type=Path)
    p.add_argument('output', type=Path)
    p.add_argument('--font', required=True, type=Path)
    a = p.parse_args()
    a.output.mkdir(parents=True, exist_ok=True)
    scenes = json.loads((a.capture / 'capture.json').read_text())['scenes']
    if len(scenes) != len(CAPTIONS):
        raise ValueError('Incomplete capture; do not substitute invented footage')
    title = ImageFont.truetype(str(a.font), 25)
    copy = ImageFont.truetype(str(a.font), 20)
    clips, transcript, manifest = [], [], []
    clock = 0
    for scene, (heading, body) in zip(scenes, CAPTIONS):
        band = Image.new('RGB', (1280, 120), '#101c28')
        d = ImageDraw.Draw(band)
        d.text((28, 12), heading, font=title, fill='#6ce5bd')
        lines = textwrap.wrap(body, width=112)
        for i, line in enumerate(lines):
            if d.textbbox((0, 0), line, font=copy)[2] > 1220:
                raise ValueError('Caption wider than safe area')
            d.text((28, 51 + i * 25), line, font=copy, fill='white')
        caption = a.capture / (scene['id'] + '-caption.png')
        band.save(caption)
        clip = a.capture / (scene['id'] + '-edited.mp4')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(scene['start']), '-i', str(a.capture / (scene['id'] + '.webm')),
                        '-loop', '1', '-i', str(caption), '-filter_complex', '[0:v]pad=1280:720:0:0:color=0x101c28[v];[v][1:v]overlay=0:600',
                        '-t', str(scene['duration']), '-r', '24', '-an', '-c:v', 'libx264', '-preset', 'fast', '-crf', '27',
                        '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(clip)], check=True)
        clips.append(clip)
        transcript.append(f'## {clock // 60:02d}:{clock % 60:02d} — {heading}\n\n{body}\n')
        manifest.append({'id': scene['id'], 'start_seconds': clock, 'duration_seconds': scene['duration'], 'source_url': scene['url'], 'heading': heading, 'caption': body})
        clock += scene['duration']
    listing = a.capture / 'concat.txt'
    listing.write_text(''.join(f"file '{x.as_posix()}'\n" for x in clips))
    video = a.output / 'portfolio-tour-nl.mp4'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(listing), '-c', 'copy', '-movflags', '+faststart', str(video)], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '3', '-i', str(video), '-frames:v', '1', str(a.output / 'poster.jpg')], check=True)
    (a.output / 'TRANSCRIPT-NL.md').write_text('# Nederlandstalige videotekst\n\nStille schermopname met zichtbare captions; geen gesproken auteursgetuigenis.\n\n' + '\n'.join(transcript))
    (a.output / 'provenance.json').write_text(json.dumps({'recorded_at': json.loads((a.capture / 'capture.json').read_text())['recordedAt'], 'duration_seconds': clock, 'audio': 'none', 'editing': 'Real browser recordings, trimmed and concatenated; caption band added below unmodified UI. No generated app screens or synthetic voice.', 'scenes': manifest}, ensure_ascii=False, indent=2) + '\n')
    print(video)


if __name__ == '__main__':
    main()
