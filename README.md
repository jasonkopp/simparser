# simparser.py README

This script takes a directory that contains your output simulation folders, find the "console1" files, extract the overall, y, u, v, and bits values. Then find the average of all of them. It then exports a CSV file that displays the first overall, Y, U, V, and bits results and the average of all of them for each QP tested.


## To run the parser, type:
- "python simparser.py [codec type] [path/to/directory] [*optional* newfilename]"
- [codec type]:
  - AV1 or HEVC, case-insensitive
- [path/to/directory]:
  - Path to the directory that holds all your output simulation folders (e.g. "MarketPlace_1920x1080_60fps_10bit_420_0", "MarketPlace_1920x1080_60fps_10bit_420_1", etc.)
- [*optional* newfilename]:
  - The name of the output CSV file.
  - The default will be your codectype + "-test.csv".
