# median-cut.py

Implementaion of the Median Cut Algorithm using Python

## Motivation

Since I do a lot of hobby projects on the web domain, this time thought of doing a weekend project without web.
I was looking for a challenge, and chose to read and collect some foundational information about the topic of color quantization. Though I am not a math-head, I started learning about color quantization and how various algorithms acheive the process. Stumbled upon the **Median Cut Algorithm** in the [color quantization](https://en.wikipedia.org/wiki/Color_quantization) wiki.

## Inspiration

As I am very new to the field of Computer Graphics, I really looked up to many existing implementaions and blogs discussing about the topic of color quantization with median cut. The below pieces, inspired me and gave me a lot of hints in writing my implementaion.

1. [Median cut](https://en.wikipedia.org/wiki/Median_cut)
2. [color palette extraction](https://github.com/zygisS22/color-palette-extraction)
3. [Lai Wei's paper on Finding Theme Color Palettes](https://macsphere.mcmaster.ca/bitstream/11375/27665/1/Wei_Lai_2019January_MEng.pdf)

## Usage

### Installation

`pip install -r requirements.txt`

The program takes the image path as arg and generates a palette of 16 colours

### Example usage

`python median.py.py ./images/sample.jpg`

## Bugs/Refactor

There's plenty of room to fix and refactor, file the bugs/refactor suggestions in the issues, will look into it when I find time. You are also free to contribute to the repo on any basis. Thanks in advance for that.

## License

```
MIT License

Copyright (c) 2022 Vishwa.R

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
