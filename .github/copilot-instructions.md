# Copilot Instructions for this Repository

This repo is a small image-processing project written as executable Python scripts. The key behavior is procedural filtering of a single local image (`rosa.png`) using OpenCV and plotting results with Matplotlib.

## Key files
- `filtros.py`: primary script showing mean blur, Sobel edge detection, and median blur on `rosa.png`.
- `filtros_experimentacao.py`: experimental script comparing multiple kernel sizes for mean and median filters.
- `Relatorio.txt`: human-written results summary and expected visual outcomes for the filters.

## What an AI agent should know
- There is no package structure, test suite, or build system. The repo is intended to run as plain Python scripts from the repository root.
- Both scripts rely on `cv2.imread('rosa.png', cv2.IMREAD_GRAYSCALE)` and expect `rosa.png` to be present in the same folder.
- Output is displayed via `matplotlib.pyplot.show()`; this is the visible result of the code rather than saving specific files.
- The scripts are not modular: they execute image processing immediately when imported/run. Avoid introducing complex runtime entrypoints unless refactoring the code into reusable functions.

## Common patterns in this project
- Use OpenCV filters directly: `cv2.blur`, `cv2.medianBlur`, `cv2.Sobel`, `cv2.convertScaleAbs`, `cv2.addWeighted`.
- Use Matplotlib for visualization with `plt.subplot(...); plt.imshow(..., cmap='gray'); plt.axis('off')`.
- Kernel size values are important and should remain odd for median filters and sensible sizes for blur filters.
- The scripts use grayscale images only; do not assume color images without an explicit code change.

## Execution / debugging
- Run scripts from the repository root in a Python environment with `opencv-python`, `numpy`, and `matplotlib` installed.
- Example command: `python filtros.py` or `python filtros_experimentacao.py`.
- If the image does not load, check that `rosa.png` exists and that the current working directory is the repository root.

## When editing
- Keep changes small and consistent with the repository’s exploratory nature.
- If adding new filter variants, preserve the existing `plt.figure` + `plt.subplot` visualization style.
- Document any new experiments or results in `Relatorio.txt` if they are intended as an analysis deliverable.

## No hidden infrastructure
- There are no CI config files, no `.gitignore`, no tests, and no package metadata in this repository.
- Assume the primary goal is clarity of image-filter demonstrations rather than production packaging.
