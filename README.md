# simparser.py

This script takes two directories that contain your output simulation folders, finds the "console1" files, extracts the overall, y, u, v, and bit values. Then finds the average of all of them. It then exports a CSV file that displays the first overall, Y, U, V, and bit results and the average of all of them for each QP tested.

## To run the parser:
- Type: `python [path/to/simparser.py] [path/to/AV1/directory] [path/to/HEVC/directory]`
- The directories should hold all of your output simulation folders from AV1 and HEVC (e.g. `MarketPlace_1920x1080_60fps_10bit_420_0/`, `MarketPlace_1920x1080_60fps_10bit_420_1/`, etc.)
  - Those folders should contain three files each: `console0`, `console1`, `console2`, and a `.ivf` file.
