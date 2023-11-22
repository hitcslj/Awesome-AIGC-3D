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



<details open>
<summary>Object</summary>

<details open>
<summary>high quality</summary>

- [DreamFields: Zero-Shot Text-Guided Object Generation with Dream Fields](https://arxiv.org/abs/2112.01455), Jain et al., CVPR 2022 | [github](https://github.com/google-research/google-research/tree/master/dreamfields) | [bibtex](./citations/dreamfields.txt)
- [DreamFusion: Text-to-3D using 2D Diffusion](https://dreamfusion3d.github.io/), Poole et al., ICLR 2023 | [github](https://github.com/ashawkey/stable-dreamfusion) | [bibtex](./citations/dreamfusion.txt)
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
<summary>Procedural 3D Modeling</summary>

- [3D-GPT: Procedural 3D Modeling with Large Language Models](https://arxiv.org/abs/2310.12945), Sun et al., arxiv 2023 |  [github](https://github.com/Chuny1/3DGPT) | [bibtex](./citations/3dgpt.txt)
</details>

<details open>
<summary>3D Native Generative Models</summary>

- [GET3D: A Generative Model of High Quality 3D Textured Shapes Learned from Images](https://research.nvidia.com/labs/toronto-ai/GET3D/), Gao et al., NeurIPS  2022 |  [github](https://github.com/nv-tlabs/GET3D) | [bibtex](./citations/get3d.txt)
- [LION: Latent Point Diffusion Models for 3D Shape Generation](https://research.nvidia.com/labs/toronto-ai/LION/), Zeng et al., NeurIPS  2022 |  [github](https://github.com/nv-tlabs/LION) | [bibtex](./citations/lion.txt)
- [Diffusion-SDF: Conditional Generative Modeling of Signed Distance Functions](https://light.princeton.edu/publication/diffusion-sdf/), Chou et al., ICCV  2023 |  [github](https://github.com/princeton-computational-imaging/Diffusion-SDF) | [bibtex](./citations/diffusionsdf.txt)
- [SDFusion: Multimodal 3D Shape Completion, Reconstruction, and Generation](https://yccyenchicheng.github.io/SDFusion/), Cheng et al., CVPR  2023 |  [github](https://github.com/yccyenchicheng/SDFusion) | [bibtex](./citations/sdfusion.txt)
- [DiffRF: Rendering-guided 3D Radiance Field Diffusion](https://sirwyver.github.io/DiffRF/), Müller et al., CVPR 2023 | [bibtex](./citations/diffRF.txt)
- [Point-E: A System for Generating 3D Point Clouds from Complex Prompts](https://arxiv.org/abs/2212.08751), Nichol et al., arxiv  2022 |  [github](https://github.com/openai/point-e) | [bibtex](./citations/pointe.txt)
- [3DShape2VecSet: A 3D Shape Representation for Neural Fields and Generative Diffusion Models](https://1zb.github.io/3DShape2VecSet/), Zhang et al., TOG 2023 |  [github](https://github.com/1zb/3DShape2VecSet) | [bibtex](./citations/3dShape2VecSet.txt)
- [MeshDiffusion: Score-based Generative 3D Mesh Modeling](https://meshdiffusion.github.io/), Liu et al., ICLR 2023 |  [github](https://meshdiffusion.github.io/) | [bibtex](./citations/meshdiffusion.txt)
- [3DGen: Triplane Latent Diffusion for Textured Mesh Generation](https://arxiv.org/abs/2303.05371), Gupta et al., arxiv 2023  | [bibtex](./citations/3dgen.txt)
- [3D VADER - AutoDecoding Latent 3D Diffusion Models](https://snap-research.github.io/3DVADER/), Ntavelis et al., arxiv 2023 | [github](https://github.com/snap-research/3DVADER) | [bibtex](./citations/3dvader.txt)
- [HoloDiffusion: Training a 3D Diffusion Model using 2D Images](https://holodiffusion.github.io/), Karnewar et al., CVPR 2023 | [github](https://github.com/facebookresearch/holo_diffusion) | [bibtex](./citations/holodiffusion.txt)
- [HyperDiffusion: Generating Implicit Neural Fields with Weight-Space Diffusion](https://ziyaerkoc.com/hyperdiffusion/), Erkoç et al., ICCV 2023 | [github](https://github.com/Rgtemze/HyperDiffusion) | [bibtex](./citations/hyperdiffusion.txt)
- [Shap-E: Generating Conditional 3D Implicit Functions](https://arxiv.org/abs/2305.02463), Jun et al., arxiv 2023 | [github](https://github.com/openai/shap-e) | [bibtex](./citations/shape.txt)
- [LAS-Diffusion: Locally Attentional SDF Diffusion for Controllable 3D Shape Generation](https://zhengxinyang.github.io/projects/LAS-Diffusion.html), Zheng et al., TOG 2023 | [github](https://github.com/Zhengxinyang/LAS-Diffusion) | [bibtex](./citations/lasdiffusion.txt)
- [Michelangelo: Conditional 3D Shape Generation based on Shape-Image-Text Aligned Latent Representation](https://neuralcarver.github.io/michelangelo/), Zhao et al., arxiv 2023 | [github](https://github.com/NeuralCarver/Michelangelo) | [bibtex](./citations/michelangelo.txt)
- [ARGUS: Visualization of AI-Assisted Task Guidance in AR](https://arxiv.org/abs/2308.06246), Castelo et al., arxiv 2023 | [bibtex](./citations/argus.txt)



</details>



<details open>
<summary>Scene</summary>

- [Text2Light: Zero-Shot Text-Driven HDR Panorama Generation](https://frozenburning.github.io/projects/text2light/), Chen et al., TOG 2022 | [github](https://github.com/FrozenBurning/Text2Light) | [bibtext](./citations/text2light.txt) 
- [SceneScape: Text-Driven Consistent Scene Generation](https://scenescape.github.io/), Fridman et al., arxiv 2023 | [github](https://github.com/RafailFridman/SceneScape) | [bibtext](./citations/scenescape.txt) 
- [Text2Room: Extracting Textured 3D Meshes from 2D Text-to-Image Models](https://lukashoel.github.io/text-to-room/), Höllein et al., ICCV 2023 | [github](https://github.com/lukasHoel/text2room) | [bibtext](./citations/text2room.txt) 
- [Text2NeRF: Text-Driven 3D Scene Generation with Neural Radiance Fields](https://eckertzhang.github.io/Text2NeRF.github.io/), Zhang et al., arxiv 2023 | [github](https://github.com/eckertzhang/Text2NeRF) | [bibtext](./citations/text2nerf.txt) 
- [MVDiffusion: Enabling Holistic Multi-view Image Generation with Correspondence-Aware Diffusion](https://mvdiffusion.github.io/), Tang et al., NeurIPS 2023 | [github](https://github.com/Tangshitao/MVDiffusion) | [bibtext](./citations/mvdiffusion.txt) 
- [Ctrl-Room: Controllable Text-to-3D Room Meshes Generation with Layout Constraints](https://fangchuan.github.io/ctrl-room.github.io/), Fang et al., arxiv 2023 | [github](https://github.com/fangchuan/Ctrl-Room) | [bibtext](./citations/ctrlroom.txt) 
- [ZeroNVS: Zero-Shot 360-Degree View Synthesis from a Single Real Image](https://kylesargent.github.io/zeronvs/), Sargent et al., Arxiv 2023 | [github](https://github.com/kylesargent/zeronvs) | [bibtext](./citations/zeroNVS.txt) 



</details>
 

<details open>
<summary>Dynamic</summary>

- [TADA! Text to Animatable Digital Avatars](https://tada.is.tue.mpg.de/), Liao et al., 3DV 2024 | [github](https://github.com/TingtingLiao/TADA) | [bibtext](./citations/tada.txt) 
- [Consistent4D: Consistent 360° Dynamic Object Generation from Monocular Video](https://consistent4d.github.io/), Jiang et al., arxiv 2023 | [github](https://github.com/yanqinJiang/Consistent4D) | [bibtext](./citations/consistent4d.txt) 
- [Text-To-4D Dynamic Scene Generation](https://make-a-video3d.github.io/), Singer et al., arxiv 2023 | [bibtext](./citations/mav3d.txt) 
- [MAS: Multi-view Ancestral Sampling for 3D motion generation using 2D diffusion](https://guytevet.github.io/mas-page/), Kapon et al., arxiv 2023 | [github](https://github.com/roykapon/MAS) | [bibtext](./citations/mas.txt) 


</details>


<details open>
<summary>Texture</summary>

- [StyleMesh: Style Transfer for Indoor 3D Scene Reconstructions](https://lukashoel.github.io/stylemesh/), Höllein et al., CVPR 2022 | [github](https://github.com/lukasHoel/stylemesh) | [bibtex](./citations/stylemesh.txt)
- [Latent-NeRF for Shape-Guided Generation of 3D Shapes and Textures](https://arxiv.org/abs/2211.07600), Metzer et al., CVPR 2023 | [github](https://github.com/eladrich/latent-nerf) | [bibtex](./citations/latentNerf.txt)
- [TEXTure: Text-Guided Texturing of 3D Shapes](https://texturepaper.github.io/TEXTurePaper/), Richardson et al., SIGGRAPH 2023 | [github](https://github.com/TEXTurePaper/TEXTurePaper) | [bibtex](./citations/texture.txt)
- [Text2Tex: Text-driven Texture Synthesis via Diffusion Models](https://daveredrum.github.io/Text2Tex/), Chen et al., ICCV 2023 | [github](https://github.com/daveredrum/Text2Tex) | [bibtex](./citations/text2tex.txt)
- [TexFusion: Synthesizing 3D Textures with Text-Guided Image Diffusion Models](https://research.nvidia.com/labs/toronto-ai/texfusion/), Cao et al., ICCV 2023 | [bibtex](./citations/texfusion.txt)
- [RoomDreamer: Text-Driven 3D Indoor Scene Synthesis with Coherent Geometry and Texture](https://arxiv.org/abs/2305.11337), Song et al., arxiv 2023 | [bibtex](./citations/roomdreamer.txt)
- [3DStyle-Diffusion: Pursuing Fine-grained Text-driven 3D Stylization with 2D Diffusion Models](https://arxiv.org/abs/2311.05464), Yang et al., ACM Multimedia 2023 | [github](https://github.com/yanghb22-fdu/3DStyle-Diffusion-Official) | [bibtex](./citations/3dstylediffusion.txt)
- [DreamSpace: Dreaming Your Room Space with Text-Driven Panoramic Texture Propagation](https://ybbbbt.com/publication/dreamspace/), Yang et al., arxiv 2023 | [github](https://github.com/ybbbbt/dreamspace) | [bibtext](./citations/dreamspace.txt) 


</details>

## Benchmarks and Datasets

- [Objaverse-XL](https://objaverse.allenai.org/), Deitke et al., arxiv 2023 | [github](https://github.com/allenai/objaverse-xl) | [bibtext](./citations/objaverse-xl.txt) 


## Talks
- [AI 3D Generation, explained](https://www.youtube.com/watch?v=EoAm1yZR-ao), Jia-Bin Huang
- [3D Generation, bilibili](https://space.bilibili.com/23460054/channel/collectiondetail?sid=1860808&ctype=0), Leo

 

## Implementations

- [Threestudio](https://github.com/threestudio-project/threestudio), Yuan-Chen Guo, 2023 | [bibtex](./citations/threestudio.txt)
- [stable-dreamfusion](https://github.com/ashawkey/stable-dreamfusion), Jiaxiang Tang, 2023 | [bibtex](./citations/stable-dreamfusion.txt)
- [Dream Textures](https://github.com/carson-katri/dream-textures), Carson Katri, 2023 

## License 
Awesome AIGC 3D is released under the [MIT license](./LICENSE).

## Contact
contact: `hitcslj@stu.hit.edu.cn`.  
