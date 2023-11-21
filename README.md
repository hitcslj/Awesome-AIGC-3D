# Awesome-AIGC-3D [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
A curated list of awesome AIGC 3D papers, inspired by [awesome-NeRF](https://github.com/awesome-NeRF/awesome-NeRF).


<img src="./asset/mvdream.gif" width="696px">
 


#### [How to submit a pull request?](https://github.com/hitcslj/Awesome-AIGC-3D/blob/main/how-to-PR.md)



## Table of Contents

- [Survey](#survey) 
- [Papers](#papers)
- [Benchmarks and Datasets](#Benchmarks-and-Datasets)
- [Talks](#talks)
- [Implementations](#implementations)

## Survey

**TODO**

## Papers
- DreamFusion: Text-to-3D using 2D Diffusion
, Poole et al., ICLR 2023 | [github](https://dreamfusion3d.github.io/) | [bibtex](./citations/dreamfusion.txt)


<details open>
<summary>Object</summary>

<details open>
<summary>high quality</summary>

- [Score Jacobian Chaining: Lifting Pretrained 2D Diffusion Models for 3D Generation](https://pals.ttic.edu/p/score-jacobian-chaining), Wang et al., CVPR 2023 |[github](https://github.com/lukemelas/realfusion)| [bibtex](./citations/sjc.txt)
- [RealFusion: 360° Reconstruction of Any Object from a Single Image](https://lukemelas.github.io/realfusion/), Melas-Kyriazi et al., CVPR 2023 | [github](https://github.com/lukemelas/realfusion) | [bibtex](./citations/realfusion.txt)
- [3DFuse: Let 2D Diffusion Model Know 3D-Consistency
for Robust Text-to-3D Generation](https://ku-cvlab.github.io/3DFuse/), Seo et al., arxiv 2023 | [github](https://github.com/KU-CVLAB/3DFuse) | [bibtex](./citations/3dfuse.txt)
- [Dream3D: Zero-Shot Text-to-3D Synthesis Using 3D Shape Prior and Text-to-Image Diffusion Models](https://bluestyle97.github.io/dream3d/), Xu et al., CVPR 2023 | [bibtex](./citations/dream3d.txt)
- [Magic3D: High-Resolution Text-to-3D Content Creation](https://research.nvidia.com/labs/dir/magic3d/), Lin et al., CVPR 2023 | [bibtex](./citations/magic3d.txt)
- [Fantasia3D: Disentangling Geometry and Appearance for High-quality Text-to-3D Content Creation](https://fantasia3d.github.io/), Chen et al., ICCV 2023 | [github](https://github.com/Gorilla-Lab-SCUT/Fantasia3D) | [bibtex](./citations/fantasia3d.txt)
- [Make-It-3D: High-Fidelity 3D Creation from A Single Image with Diffusion Prior](https://make-it-3d.github.io/), Tang et al., ICCV 2023 | [github](https://github.com/junshutang/Make-It-3D) | [bibtex](./citations/makeit3d.txt)
- [HiFA: High-fidelity Text-to-3D with Advanced Diffusion Guidance](https://hifa-team.github.io/HiFA-site/), Zhu et al., arxiv 2023 | [github](https://github.com/HiFA-team/HiFA) | [bibtex](./citations/hifa.txt)
- [MATLABER: Material-Aware Text-to-3D via LAtent BRDF auto-EncodeR](https://sheldontsui.github.io/projects/Matlaber), Xu et al., arxiv 2023 | [github](https://github.com/SheldonTsui/Matlaber) | [bibtex](./citations/matlaber.txt)
- [ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation with Variational Score Distillation](https://ml.cs.tsinghua.edu.cn/prolificdreamer/), Wang et al., NeurIPS 2023 | [github](https://github.com/thu-ml/prolificdreamer) | [bibtex](./citations/prolificdreamer.txt)
- [DreamCraft3D: Hierarchical 3D Generation with Bootstrapped Diffusion Prior](https://mrtornado24.github.io/DreamCraft3D/), Sun et al., arxiv 2023 | [github](https://github.com/deepseek-ai/DreamCraft3D) | [bibtex](./citations/dreamcraft3d.txt)


</details>

<details open>
<summary>3D diffusion</summary>

- [DiffRF: Rendering-guided 3D Radiance Field Diffusion](https://sirwyver.github.io/DiffRF/), Müller et al., CVPR 2023 | [bibtex](./citations/diffRF.txt)
- [3D VADER - AutoDecoding Latent 3D Diffusion Models](https://snap-research.github.io/3DVADER/), Ntavelis et al., arxiv 2023 | [github](https://github.com/snap-research/3DVADER) | [bibtex](./citations/3dvader.txt)

</details>

<details open>
<summary>multi-view consistent</summary>

- [Zero-1-to-3: Zero-shot One Image to 3D Object](https://zero123.cs.columbia.edu/), Liu et al., ICCV 2023 | [github](https://github.com/cvlab-columbia/zero123) | [bibtex](./citations/zero123.txt)
- [ConRad: Image Constrained Radiance Fields for 3D Generation from a Single Image](https://arxiv.org/abs/2311.05230), Purushwalkam et al., NeurIPS 2023 | [bibtex](./citations/conrad.txt)
- [One-2-3-45: Any Single Image to 3D Mesh in 45 Seconds without Per-Shape Optimization](https://one-2-3-45.github.io/), Liu et al., NeurIPS 2023 | [github](https://github.com/One-2-3-45/One-2-3-45) | [bibtex](./citations/one2345.txt)
- [Magic123: One Image to High-Quality 3D Object Generation Using Both 2D and 3D Diffusion Priors](https://guochengqian.github.io/project/magic123/), Qian et al., arxiv 2023 | [github](https://github.com/guochengqian/Magic123) | [bibtex](./citations/magic123.txt)
- [SyncDreamer: Generating Multiview-consistent Images from a Single-view Image](https://liuyuan-pal.github.io/SyncDreamer/), Liu et al., arxiv 2023 | [github](https://liuyuan-pal.github.io/SyncDreamer/) | [bibtex](./citations/syncdreamer.txt)
- [MVDream: Multi-view Diffusion for 3D Generation](https://mv-dream.github.io/), Shi et al., arxiv 2023 | [github](https://github.com/bytedance/MVDream) | [bibtex](./citations/mvdream.txt)
- [Consistent-1-to-3: Consistent Image to 3D View Synthesis via Geometry-aware Diffusion Models](https://jianglongye.com/consistent123/), Ye et al., 3DV 2024  | [bibtex](./citations/consistent123.txt)
- [Zero123++: a Single Image to Consistent Multi-view Diffusion Base Model](https://arxiv.org/abs/2310.15110), Shi et al., arxiv 2023 | [github](https://github.com/SUDO-AI-3D/zero123plus) | [bibtex](./citations/zero123++.txt)
- [HumanNorm: Learning Normal Diffusion Model for High-quality and Realistic 3D Human Generation](https://humannorm.github.io/), Huang et al., arxiv 2023 | [bibtex](./citations/humannorm.txt)
- [Wonder3D: Single Image to 3D using Cross-Domain Diffusion](https://www.xxlong.site/Wonder3D/), Long et al., arxiv 2023 | [github](https://github.com/xxlong0/Wonder3D) | [bibtex](./citations/wonder3d.txt)
- [SweetDreamer: Aligning Geometric Priors in 2D Diffusion for Consistent Text-to-3D](https://sweetdreamer3d.github.io/), Li et al., arxiv 2023 | [github](https://sweetdreamer3d.github.io/) | [bibtex](./citations/sweetdreamer.txt)
- [One-2-3-45++: Fast Single Image to 3D Objects with Consistent Multi-View Generation and 3D Diffusion](https://sudo-ai-3d.github.io/One2345plus_page/), Liu et al., arxiv 2023 | [github](https://github.com/SUDO-AI-3D/One2345plus) | [bibtex](./citations/one2345++.txt)


</details>

<details open>
<summary>faster</summary>

- [DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation](https://dreamgaussian.github.io/), Tang et al., arxiv 2023 | [github](https://github.com/dreamgaussian/dreamgaussian) | [bibtex](./citations/dreamguassian.txt)
- [Gsgen: Text-to-3D using Gaussian Splatting](https://gsgen3d.github.io/), Chen et al., arxiv 2023 | [github](https://github.com/gsgen3d/gsgen) | [bibtex](./citations/gsgen.txt)
- [LRM: Large Reconstruction Model for Single Image to 3D](https://yiconghong.me/LRM/), Hong et al., arxiv 2023 | [bibtex](./citations/lrm.txt)
- [Instant3D: Fast Text-to-3D with Sparse-View Generation and Large Reconstruction Model](https://jiahao.ai/instant3d/), Li et al., arxiv 2023 | [bibtex](./citations/instant3d.txt) 
- [DMV3D:Denoising Multi-View Diffusion using 3D Large Reconstruction Model](https://dmv3d.github.io/)
- [Instant3D : Instant Text-to-3D Generation](https://ming1993li.github.io/Instant3DProj/), Li et al., arxiv 2023 | [bibtex](./citations/instant3d_.txt) 
- [HyperFields:Towards Zero-Shot Generation of NeRFs from Text](https://threedle.github.io/hyperfields/), Babu et al., arxiv 2023 | [github](https://github.com/threedle/hyperfields) | [bibtex](./citations/hyperfields.txt)

</details>


<details open>
<summary>texture</summary>

- [TEXTure: Text-Guided Texturing of 3D Shapes](https://texturepaper.github.io/TEXTurePaper/), Richardson et al., SIGGRAPH 2023 | [github](https://github.com/TEXTurePaper/TEXTurePaper) | [bibtex](./citations/texture.txt)
- [Text2Tex: Text-driven Texture Synthesis via Diffusion Models](https://daveredrum.github.io/Text2Tex/), Chen et al., ICCV 2023 | [github](https://github.com/daveredrum/Text2Tex) | [bibtex](./citations/text2tex.txt)
- [TexFusion: Synthesizing 3D Textures with Text-Guided Image Diffusion Models](https://research.nvidia.com/labs/toronto-ai/texfusion/), Cao et al., ICCV 2023 | [bibtex](./citations/texfusion.txt)



</details>


<details open>
<summary>editing</summary>

- [DreamBooth3D: Subject-Driven Text-to-3D Generation](https://dreambooth3d.github.io/), Raj et al., ICCV 2023 | [bibtex](./citations/dreambooth3d.txt)
- [TECA: Text-Guided Generation and Editing of Compositional 3D Avatars](https://yfeng95.github.io/teca/), Zhang et al., arxiv 2023 |  [github](https://github.com/HaoZhang990127/TECA) | [bibtex](./citations/teca.txt)
- [Control4D: Dynamic Portrait Editing by Learning 4D GAN from 2D Diffusion-based Editor](https://control4darxiv.github.io/), Shao et al., arxiv 2023 | [bibtex](./citations/control4d.txt)

</details>

<details open>
<summary>conditional control</summary>

- [Control3D: Towards Controllable Text-to-3D Generation](https://arxiv.org/abs/2311.05461), Chen et al., ACM Multimedia 2023 | [bibtex](./citations/control3d.txt)
- [IPDreamer: Appearance-Controllable 3D Object Generation with Image Prompts](https://arxiv.org/abs/2310.05375), Zeng et al., arxiv 2023 | [bibtex](./citations/ipdreamer.txt)

</details>

</details>



<details open>
<summary>Scene</summary>

- [Text2Light: Zero-Shot Text-Driven HDR Panorama Generation](https://frozenburning.github.io/projects/text2light/), Chen et al., TOG 2022 | [github](https://github.com/FrozenBurning/Text2Light) | [bibtext](./citations/text2light.txt) 
- [SceneScape: Text-Driven Consistent Scene Generation](https://scenescape.github.io/), Fridman et al., arxiv 2023 | [github](https://github.com/RafailFridman/SceneScape) | [bibtext](./citations/scenescape.txt) 
- [Text2Room: Extracting Textured 3D Meshes from 2D Text-to-Image Models](https://lukashoel.github.io/text-to-room/), Höllein et al., ICCV 2023 | [github](https://github.com/lukasHoel/text2room) | [bibtext](./citations/text2room.txt) 
- [Text2NeRF: Text-Driven 3D Scene Generation with Neural Radiance Fields](https://eckertzhang.github.io/Text2NeRF.github.io/), Zhang et al., arxiv 2023 | [github](https://github.com/eckertzhang/Text2NeRF) | [bibtext](./citations/text2nerf.txt) 
- [MVDiffusion: Enabling Holistic Multi-view Image Generation with Correspondence-Aware Diffusion](https://mvdiffusion.github.io/), Tang et al., NeurIPS 2023 | [github](https://github.com/Tangshitao/MVDiffusion) | [bibtext](./citations/mvdiffusion.txt) 
- [Ctrl-Room: Controllable Text-to-3D Room Meshes Generation with Layout Constraints](https://fangchuan.github.io/ctrl-room.github.io/), Fang et al., arxiv 2023 | [github](https://github.com/fangchuan/Ctrl-Room) | [bibtext](./citations/ctrlroom.txt) 
- [DreamSpace: Dreaming Your Room Space with Text-Driven Panoramic Texture Propagation](https://ybbbbt.com/publication/dreamspace/), Yang et al., arxiv 2023 | [github](https://github.com/ybbbbt/dreamspace) | [bibtext](./citations/dreamspace.txt) 
- [ZeroNVS: Zero-Shot 360-Degree View Synthesis from a Single Real Image](https://kylesargent.github.io/zeronvs/), Sargent et al., Arxiv 2023 | [github](https://github.com/kylesargent/zeronvs) | [bibtext](./citations/zeroNVS.txt) 



</details>
 

<details open>
<summary>Dynamic</summary>

- [TADA! Text to Animatable Digital Avatars](https://tada.is.tue.mpg.de/), Liao et al., 3DV 2024 | [github](https://github.com/TingtingLiao/TADA) | [bibtext](./citations/tada.txt) 
- [Consistent4D: Consistent 360° Dynamic Object Generation from Monocular Video](https://consistent4d.github.io/), Jiang et al., arxiv 2023 | [github](https://github.com/yanqinJiang/Consistent4D) | [bibtext](./citations/consistent4d.txt) 
- [Text-To-4D Dynamic Scene Generation](https://make-a-video3d.github.io/), Singer et al., arxiv 2023 | [bibtext](./citations/mav3d.txt) 
- [MAS: Multi-view Ancestral Sampling for 3D motion generation using 2D diffusion](https://guytevet.github.io/mas-page/), Kapon et al., arxiv 2023 | [github](https://github.com/roykapon/MAS) | [bibtext](./citations/mas.txt) 


</details>

## Benchmarks and Datasets

- [Objaverse-XL](https://objaverse.allenai.org/), Deitke et al., arxiv 2023 | [github](https://github.com/allenai/objaverse-xl) | [bibtext](./citations/objaverse-xl.txt) 


## Talks
- [AI 3D Generation, explained](https://www.youtube.com/watch?v=EoAm1yZR-ao), Jia-Bin Huang
- [3D Generation, bilibili](https://space.bilibili.com/23460054/channel/collectiondetail?sid=1860808&ctype=0), Leo

 

## Implementations

- [Threestudio](https://github.com/threestudio-project/threestudio), Yuan-Chen Guo, 2023 | [bibtex](./citations/threestudio.txt)
- [stable-dreamfusion](https://github.com/ashawkey/stable-dreamfusion), Jiaxiang Tang, 2023 | [bibtex](./citations/stable-dreamfusion.txt)

## License 
Awesome AIGC 3D is released under the [MIT license](./LICENSE).

## Contact
contact: `hitcslj@stu.hit.edu.cn`.  
