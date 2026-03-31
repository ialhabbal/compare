# Compare
## ComfyUI Custom Node

Simple ComfyUI custom node to compare two images.

![Save_It Node](https://raw.githubusercontent.com/ialhabbal/compare/main/compare.png)

## Installation

Install directly from ComfyUI Manager by searching for Compare.

Alternatively:

1. Go to your ComfyUI `custom_nodes` folder
2. Open a terminal or command prompt there
3. Run: `git clone https://github.com/ialhabbal/compare.git`
4. Restart ComfyUI

Or manually:

1. Go to your ComfyUI `custom_nodes` folder
2. Create a folder named `compare`
3. Copy all files into it
4. Restart ComfyUI

## To Update:

- Update through ComfyUI Manager, or
- Go the node's folder, run a cmd, then: Git Pull

## Node Inputs

**image a:** Connect this to the output of any node that produces the generated image , such as a VAE Decode node. This is the image that will be previewed and saved.

**image b:** Connect this to the output of any node that produces the original image.

## How it works

The image displays the two images side by side. Click on either of the images and they will appear one over the other. switch between them with the "1/2" toggle at the bottom right. Close the comparison by clicking on "x" on the top-right.
