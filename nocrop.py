from pathlib import Path
import sys
from PIL import Image, ImageDraw
import json


def no_crop(img_path: Path, res_path: Path, final_rat: float, bg_color: tuple[int], padx: float = 0, pady: float = 0):

    img = Image.open(str(img_path))
    wx, hx = img.width, img.height
    padx = max(0, min(padx, 1))
    pady = max(0, min(pady, 1))
    innter_rat = final_rat * (1-padx) / (1-pady)

    if innter_rat < wx/hx:
        final_wx = wx * (1 / (1-padx))
        final_hx = final_wx / final_rat
    else:
        final_hx = hx * (1 / (1-pady))
        final_wx = final_hx * final_rat

    final_hx, final_wx = round(final_hx), round(final_wx)
    offxx = round((final_wx - wx)/2)
    offyx = round((final_hx - hx)/2)

    bg = Image.new('RGB', (final_wx, final_hx), bg_color)
    bg.paste(img, (offxx, offyx))

    bg.save(str(res_path))


if __name__ == '__main__':
    try:
        with open(Path(__file__).parents[0]/'config.json', 'r') as jfile:
            config = json.load(jfile)
    except:
        with open(Path(__file__).parents[1]/'config.json', 'r') as jfile:
            config = json.load(jfile)

    for file in sys.stdin.readlines():
        img = Path(file.strip())
        if img.is_file():
            result_dir = img.parents[0] / config['sub-directory']
            result_dir.mkdir(exist_ok = True)
            result_path = result_dir / f'nocrop-{img.name}'
            try:
                no_crop(img,
                        result_path,
                        config['result_width_height_ratio'],
                        tuple(config['bg_color']),
                        config['padding_x'],
                        config['padding_y'])
                print(f'{img.name} is processed.')
            except Image.UnidentifiedImageError:
                print(f'{img.name} is not an image.')
