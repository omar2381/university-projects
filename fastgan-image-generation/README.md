# FastGAN image generation

Deep learning coursework: a lightweight GAN that generates images, trained on
CIFAR-10 and STL-10. Based on FastGAN, which is designed to train on small
datasets and limited compute — the point of the assignment, since everything
ran in a Colab session.

## What is in it

A single notebook holding the whole pipeline, because Colab has no file tree:

- **Generator** built from `InitLayer`, upsampling blocks, `NoiseInjection`,
  `GLU` and squeeze-and-excite blocks (`SEBlock`) — the FastGAN architecture,
  with skip-layer excitation connecting low and high resolution features.
- **Discriminator** with `DownBlock` / `DownBlockComp` and a `SimpleDecoder`
  self-supervision branch, so the discriminator is also trained to reconstruct,
  which is what keeps it from overfitting a small dataset.
- **`DiffAugment`** (colour and translation policies) applied to both real and
  fake images.
- **LPIPS perceptual loss**, vendored into the notebook: `squeezenet`,
  `alexnet` and `vgg16` feature extractors with `PerceptualLoss` and
  `DistModel` on top.

Run at `im_size = 256`, `nz = 256`, `ngf = ndf = 64`, `batch_size = 16`,
Adam at `2e-4` with `beta1 = 0.5`.

## Running it

Colab, with a GPU runtime. The notebook calls `drive.mount` and reads datasets
from `drive/My Drive/training/`, writing checkpoints to
`/content/drive/MyDrive/`. Those paths are mine; point them somewhere real
before running.

LPIPS needs its pretrained weights (`vgg.pth`, `squeezenet.pth`,
`alexnet.pth`, the v0.1 set). They are not in this repository — the notebook's
first cell says they were supplied alongside it as a folder.

## Credit

The architecture is from [odegeasslbc/FastGAN-pytorch](https://github.com/odegeasslbc/FastGAN-pytorch),
with minor parts from [lucidrains/lightweight-gan](https://github.com/lucidrains/lightweight-gan),
both credited in the notebook's first cell. LPIPS is Zhang et al.'s. My work is
the assembly, the training setup and the experiments, not the architecture.

Outputs were stripped before committing, so the generated image grids are not
here.
