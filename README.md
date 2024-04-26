# ComfyUI-ZeroShot-MTrans: Zero-Shot Material Transfer from a Single Image

An unofficial ComfyUI custom node for ZeST(Zero-Shot Material Transfer from a Single Image)

## install

in `ComfyUI Manager` or git clone to `ComfyUI/custom_nodes`

## dependences

- ControlNet
- IP-Adaptor
- Segment Anything Model

## Input/Outpu

- INPUT: 
  - `target_image` : the original image for inpaint
  - `subject_mask` : the `mask` for inpaint
  - `brighter` : default is 1, means no change
    - value < 1 , means darker the subject, useful when subject in high light
    - value >  1, means brighter the subject, useful when subject in dark light

- OUTPUT:
  - `IMAGE` : image with `subject` in luminosity(grey) mode. used for inpaint

## Workflow 

![ZeST Simple Workflow](ZeSTSimpleWorkflow.png)

# Thanks to

- [ZeST: Zero-Shot Material Transfer from a Single Image Paper](https://arxiv.org/abs/2404.06425)
- [ZeST official DEMO](https://github.com/ttchengab/zest_code/)
- [ZeST site](https://ttchengab.github.io/zest/)
- [ZeST official video](https://www.youtube.com/watch?v=atG1VvgeG_g)

```bibtex
@article{cheng2024zest,
  title={ZeST: Zero-Shot Material Transfer from a Single Image},
  author={Cheng, Ta-Ying and Sharma, Prafull and Markham, Andrew and Trigoni, Niki and Jampani, Varun},
  journal={arXiv preprint arXiv:2404.06425},
  year={2024}
}
``` 