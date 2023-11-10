# Awesome-AIGC-3D [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
A curated list of awesome AIGC 3D papers, inspired by [awesome-NeRF](https://github.com/awesome-NeRF/awesome-NeRF).


#### [How to submit a pull request?](https://github.com/hitcslj/Awesome-AIGC-3D/blob/main/how-to-PR.md)



## Table of Contents

- [Survey](#survey) 
- [Papers](#papers)
- [Benchmarks and Datasets](#Benchmarks-and-Datasets)
- [Talks](#talks)
- [Implementations](#implementations)

## Survey


## Papers
- DreamFusion: DreamFusion: Text-to-3D using 2D Diffusion
, Poole et al., ICLR 2023 | [github](https://dreamfusion3d.github.io/) | [bibtex](./citations/dreamfusion.txt)


<details open>
<summary>Object</summary>

<details open>
<summary>high quality</summary>

- [Magic3D: High-Resolution Text-to-3D Content Creation](https://research.nvidia.com/labs/dir/magic3d/), Lin et al., CVPR 2023 | [bibtex](./citations/magic3d.txt)
- [Fantasia3D: Disentangling Geometry and Appearance for High-quality Text-to-3D Content Creation](https://fantasia3d.github.io/), Chen et al., ICCV 2023 | [github](https://github.com/Gorilla-Lab-SCUT/Fantasia3D) | [bibtex](./citations/fantasia3d.txt)
- [ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation with Variational Score Distillation](https://ml.cs.tsinghua.edu.cn/prolificdreamer/), Wang et al., NeurIPS 2023 | [github](https://github.com/thu-ml/prolificdreamer) | [bibtex](./citations/prolificdreamer.txt)
- [DreamCraft3D: Hierarchical 3D Generation with Bootstrapped Diffusion Prior](https://mrtornado24.github.io/DreamCraft3D/), Sun et al., arxiv 2023 | [github](https://github.com/deepseek-ai/DreamCraft3D) | [bibtex](./citations/dreamcraft3d.txt)


</details>


<details open>
<summary>consistent</summary>

- [Zero-1-to-3: Zero-shot One Image to 3D Object](https://zero123.cs.columbia.edu/), Liu et al., ICCV 2023 | [github](https://github.com/cvlab-columbia/zero123) | [bibtex](./citations/zero123.txt)
- [SyncDreamer: Generating Multiview-consistent Images from a Single-view Image](https://liuyuan-pal.github.io/SyncDreamer/), Liu et al., arxiv 2023 | [github](https://liuyuan-pal.github.io/SyncDreamer/) | [bibtex](./citations/syncdreamer.txt)
- [MVDream: Multi-view Diffusion for 3D Generation](https://mv-dream.github.io/), Shi et al., arxiv 2023 | [github](https://github.com/bytedance/MVDream) | [bibtex](./citations/mvdream.txt)
- [Consistent-1-to-3: Consistent Image to 3D View Synthesis via Geometry-aware Diffusion Models](https://jianglongye.com/consistent123/), Ye et al., 3DV 2024  | [bibtex](./citations/consistent123.txt)
- [Zero123++: a Single Image to Consistent Multi-view Diffusion Base Model](https://arxiv.org/abs/2310.15110), Shi et al., arxiv 2023 | [github](https://github.com/SUDO-AI-3D/zero123plus) | [bibtex](./citations/zero123++.txt)
- [Wonder3D: Single Image to 3D using Cross-Domain Diffusion](https://www.xxlong.site/Wonder3D/), Long et al., arxiv 2023 | [github](https://github.com/xxlong0/Wonder3D) | [bibtex](./citations/wonder3d.txt)
- [SweetDreamer: Aligning Geometric Priors in 2D Diffusion for Consistent Text-to-3D](https://sweetdreamer3d.github.io/), Li et al., arxiv 2023 | [github](https://sweetdreamer3d.github.io/) | [bibtex](./citations/sweetdreamer.txt)


</details>

<details open>
<summary>faster</summary>

- [DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation](https://dreamgaussian.github.io/), Tang et al., arxiv 2023 | [github](https://github.com/dreamgaussian/dreamgaussian) | [bibtex](./citations/dreamguassian.txt)
- [Gsgen: Text-to-3D using Gaussian Splatting](https://gsgen3d.github.io/), Chen et al., arxiv 2023 | [github](https://github.com/gsgen3d/gsgen) | [bibtex](./citations/gsgen.txt)
- [LRM: Large Reconstruction Model for Single Image to 3D](https://yiconghong.me/LRM/), Hong et al., arxiv 2023 | [bibtex](./citations/lrm.txt)
- [Instant3D: Fast Text-to-3D with Sparse-View Generation and Large Reconstruction Model](https://yiconghong.me/LRM/) 
- [DMV3D:Denoising Multi-View Diffusion using 3D Large Reconstruction Model](https://dmv3d.github.io/)
- [Instant3D : Instant Text-to-3D Generation](https://ming1993li.github.io/Instant3DProj/)




</details>



</details>



<details open>
<summary>Scene</summary>

- [ZeroNVS: Zero-Shot 360-Degree View Synthesis from a Single Real Image](https://kylesargent.github.io/zeronvs/), Sargent et al., Arxiv 2023 | [github](https://github.com/kylesargent/zeronvs) | [bibtext](./citations/zeroNVS.txt) 
- [MVDiffusion: Enabling Holistic Multi-view Image Generation with Correspondence-Aware Diffusion](https://mvdiffusion.github.io/), Tang et al., NeurIPS 2023 | [github](https://github.com/Tangshitao/MVDiffusion) | [bibtext](./citations/mvdiffusion.txt) 

</details>
 

<details open>
<summary>Dynamic</summary>

- [TADA! Text to Animatable Digital Avatars](https://tada.is.tue.mpg.de/), Liao et al., 3DV 2024 | [github](https://github.com/TingtingLiao/TADA) | [bibtext](./citations/tada.txt) 



</details>

## Benchmarks and Datasets

- [Objaverse-XL](https://objaverse.allenai.org/), Deitke et al., arxiv 2023 | [github](https://github.com/allenai/objaverse-xl) | [bibtext](./citations/objaverse-xl.txt) 


## Talks
- [AI 3D Generation, explained](https://www.youtube.com/watch?v=EoAm1yZR-ao), Jia-Bin Huang
 

## Implementations

- [Threestudio](https://github.com/threestudio-project/threestudio), Yuan-Chen Guo, 2023 | [bibtex](./citations/threestudio.txt)
- [stable-dreamfusion](https://github.com/ashawkey/stable-dreamfusion), Jiaxiang Tang, 2023 | [bibtex](./citations/stable-dreamfusion.txt)

## License 
Awesome AIGC 3D is released under the [MIT license](./LICENSE).

## Contact
contact: `hitcslj@stu.hit.edu.cn`.  
