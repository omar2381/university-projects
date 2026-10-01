# Image Filters from Scratch

A menu-driven program that applies four photo effects to a portrait. The effects are implemented mostly pixel by pixel with NumPy rather than relying on library filters.

University coursework on image processing.

## Filters

| Filter | How it works |
|---|---|
| Light leak (simple or rainbow) | Blends the photo with a light-ray or rainbow mask, then darkens it. The blending and darkening strengths are adjustable |
| Pencil sketch (monochrome or coloured) | Builds a greyscale image, adds random noise, applies a motion blur to create pencil strokes, and blends the result back in. The coloured version uses separate stroke textures per colour channel |
| Smoothing ("beautify") | Normalises the image and applies an adjustable blur |
| Swirl | Rotates each pixel around the image centre by an angle that decreases with distance from the centre. Strength and radius are adjustable |

Every parameter has a default and a valid range. Out-of-range or invalid input falls back to the default instead of crashing.

## Running it

```bash
pip install opencv-python numpy
python image_filters.py
```

The sample portraits are `face1.jpg` and `face2.jpg`. The light-leak filter also expects `mask.jpg` and `rainbowmask.jpg` in the same folder, and these are not included in the repository.

## Tech

Python, NumPy, OpenCV (for image input and output)
