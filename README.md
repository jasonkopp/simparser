# simparser.py
Created by Jason Kopp for Alexis Tourapis and Krishna Rapaka of Apple Inc.  
Last updated: 7/11/2019

This script takes two directories that contain your output simulation folders, finds the "console1" files, extracts the overall, y, u, v, and bit values. Then finds the average of all of them. It then exports a CSV file that displays the first overall, Y, U, V, and bit results and the average of all of them for each QP tested.

## To run the script:
- Type: `python [path/to/simparser.py] [path/to/AV1/directory] [path/to/HEVC/directory]`
- The directories should hold all of your output simulation folders from AV1 and HEVC (e.g. `MarketPlace_1920x1080_60fps_10bit_420_0/`, `MarketPlace_1920x1080_60fps_10bit_420_1/`, etc.)
  - Those folders should contain four files each: `console0`, `console1`, `console2`, and a `.ivf` file.

## Output:
The script will output three files. One CSV file for the AV1 data, one CSV file for the HEVC data, and one PNG graph of the comparison.

The CSV files list the QP Value, the first frame's overall, y, u, v, and bit values and then the average of all ten frame's overall, y, u, v, and bit values, as shown below:

|QP Value|Overall1| Y1 | U1 | V1 |Bits|Avg Overall|Avg Y|Avg U|Avg V|Avg Bits|
|--------|--------|----|----|----|----|-----------|-----|-----|-----|--------|
|0|100.0|100.0|100.0|100.0|16332624.0|100.0|100.0|100.0|100.0|16322724.0|
|1|64.65|64.645|64.688|64.631|12584608.0|82.326|82.324|82.344|82.318|14450066.8|
|...|

The PNG file is a graph comparing the Avg Y and Avg Bits values for each QP for both AV1 and HEVC.
