# Awesome-AIGC-3D [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
A curated list of awesome AIGC 3D papers, inspired by [awesome-NeRF](https://github.com/awesome-NeRF/awesome-NeRF).


<img src="./asset/mvdream.gif" width="696px">
 


#### [How to submit a pull request?](https://github.com/hitcslj/Awesome-AIGC-3D/blob/main/how-to-PR.md)



## Table of Contents

- [Survey](#survey) 
- [Papers](#papers)
- [Benchmarks and Datasets](#Benchmarks-and-Datasets)
- [Talks](#talks)
- [Company](#company)
- [Implementations](#implementations)

## Survey

- [3D Generative Models: A Survey](https://arxiv.org/abs/2210.15663), Shi et al., arxiv 2022 | [bibtex](./citations/3d-generative-survey.txt)
- [Generative AI meets 3D: A Survey on Text-to-3D in AIGC Era](https://arxiv.org/abs/2305.06131), Li et al., arxiv 2023 | [bibtex](./citations/aigc3d.txt)
- [AI-Generated Content (AIGC) for Various Data Modalities: A Survey](https://arxiv.org/abs/2308.14177), Foo et al., arxiv 2023 | [bibtex](./citations/aigcvdm.txt)
- [Advances in 3D Generation: A Survey](https://arxiv.org/abs/2401.17807), Li et al., arxiv 2024 | [bibtex](./citations/advance-3dgeneration.txt)
- [A Comprehensive Survey on 3D Content Generation](https://arxiv.org/abs/2402.01166), Liu et al., arxiv 2024 | [bibtex](./citations/3dcg.txt)

## Papers

<details close>
<summary>3D Native Generative Methods</summary>

<details open>
<summary>Object</summary>

- [Text2Shape: Generating Shapes from Natural Language by Learning Joint Embeddings](https://arxiv.org/abs/1803.08495), Chen et al., ACCV  2018 |  [github](https://github.com/kchen92/text2shape) | [bibtex](./citations/text2shape.txt)
- [ShapeCrafter: A Recursive Text-Conditioned 3D Shape Generation Model](https://arxiv.org/abs/2207.09446), Fu et al., NeurIPS  2022 |  [github](https://github.com/FreddieRao/ShapeCrafter) | [bibtex](./citations/shapecrafter.txt)
- [GET3D: A Generative Model of High Quality 3D Textured Shapes Learned from Images](https://arxiv.org/abs/2209.11163), Gao et al., NeurIPS  2022 |  [github](https://github.com/nv-tlabs/GET3D) | [bibtex](./citations/get3d.txt)
- [LION: Latent Point Diffusion Models for 3D Shape Generation](https://arxiv.org/abs/2210.06978), Zeng et al., NeurIPS  2022 |  [github](https://github.com/nv-tlabs/LION) | [bibtex](./citations/lion.txt)
- [Diffusion-SDF: Conditional Generative Modeling of Signed Distance Functions](https://arxiv.org/abs/2211.13757), Chou et al., ICCV  2023 |  [github](https://github.com/princeton-computational-imaging/Diffusion-SDF) | [bibtex](./citations/diffusionsdf.txt)
- [MagicPony: Learning Articulated 3D Animals in the Wild](https://arxiv.org/abs/2211.12497), Wu et al., CVPR 2023 | [github](https://github.com/elliottwu/MagicPony) | [bibtex](./citations/magicpony.txt)
- [DiffRF: Rendering-guided 3D Radiance Field Diffusion](https://arxiv.org/abs/2212.01206), Müller et al., CVPR 2023 | [bibtex](./citations/diffRF.txt)
- [SDFusion: Multimodal 3D Shape Completion, Reconstruction, and Generation](https://arxiv.org/abs/2212.04493), Cheng et al., CVPR  2023 |  [github](https://github.com/yccyenchicheng/SDFusion) | [bibtex](./citations/sdfusion.txt)
- [Point-E: A System for Generating 3D Point Clouds from Complex Prompts](https://arxiv.org/abs/2212.08751), Nichol et al., arxiv  2022 |  [github](https://github.com/openai/point-e) | [bibtex](./citations/pointe.txt)
- [3DShape2VecSet: A 3D Shape Representation for Neural Fields and Generative Diffusion Models](https://arxiv.org/abs/2301.11445), Zhang et al., TOG 2023 |  [github](https://github.com/1zb/3DShape2VecSet) | [bibtex](./citations/3dShape2VecSet.txt)
- [3DGen: Triplane Latent Diffusion for Textured Mesh Generation](https://arxiv.org/abs/2303.05371), Gupta et al., arxiv 2023  | [bibtex](./citations/3dgen.txt)
- [MeshDiffusion: Score-based Generative 3D Mesh Modeling](https://arxiv.org/abs/2303.08133), Liu et al., ICLR 2023 |  [github](https://github.com/lzzcd001/MeshDiffusion/) | [bibtex](./citations/meshdiffusion.txt)
- [HoloDiffusion: Training a 3D Diffusion Model using 2D Images](https://arxiv.org/abs/2303.16509), Karnewar et al., CVPR 2023 | [github](https://github.com/facebookresearch/holo_diffusion) | [bibtex](./citations/holodiffusion.txt)
- [HyperDiffusion: Generating Implicit Neural Fields with Weight-Space Diffusion](https://arxiv.org/abs/2303.17015), Erkoç et al., ICCV 2023 | [github](https://github.com/Rgtemze/HyperDiffusion) | [bibtex](./citations/hyperdiffusion.txt)
- [Shap-E: Generating Conditional 3D Implicit Functions](https://arxiv.org/abs/2305.02463), Jun et al., arxiv 2023 | [github](https://github.com/openai/shap-e) | [bibtex](./citations/shape.txt)
- [LAS-Diffusion: Locally Attentional SDF Diffusion for Controllable 3D Shape Generation](https://arxiv.org/abs/2305.04461), Zheng et al., TOG 2023 | [github](https://github.com/Zhengxinyang/LAS-Diffusion) | [bibtex](./citations/lasdiffusion.txt)
- [Michelangelo: Conditional 3D Shape Generation based on Shape-Image-Text Aligned Latent Representation](https://arxiv.org/abs/2306.17115), Zhao et al., NeurIPS 2023 | [github](https://github.com/NeuralCarver/Michelangelo) | [bibtex](./citations/michelangelo.txt)
- [DiffComplete: Diffusion-based Generative 3D Shape Completion](https://arxiv.org/abs/2306.16329), Chu et al., NeurIPS 2023 | [bibtex](./citations/diffcomplete.txt)
- [DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation](https://arxiv.org/abs/2307.01831), Mo et al., arxiv 2023 | [github](https://github.com/DiT-3D/DiT-3D) | [bibtext](./citations/dit3d.txt)
- [3D VADER - AutoDecoding Latent 3D Diffusion Models](https://arxiv.org/abs/2307.05445), Ntavelis et al., arxiv 2023 | [github](https://github.com/snap-research/3DVADER) | [bibtex](./citations/3dvader.txt)
- [ARGUS: Visualization of AI-Assisted Task Guidance in AR](https://arxiv.org/abs/2308.06246), Castelo et al., TVCG 2023 | [bibtex](./citations/argus.txt)
- [Large-Vocabulary 3D Diffusion Model with Transformer](https://arxiv.org/abs/2309.07920), Cao et al., ICLR 2024 | [github](https://github.com/ziangcao0312/DiffTF) | [bibtext](./citations/largevoc.txt)
- [TextField3D: Towards Enhancing Open-Vocabulary 3D Generation with Noisy Text Fields](https://arxiv.org/abs/2309.17175), Huang et al., ICLR 2024 | [bibtex](./citations/textfield3d.txt) 
- [HyperFields:Towards Zero-Shot Generation of NeRFs from Text](https://arxiv.org/abs/2310.17075), Babu et al., arxiv 2023 | [github](https://github.com/threedle/hyperfields) | [bibtex](./citations/hyperfields.txt)
- [LRM: Large Reconstruction Model for Single Image to 3D](https://arxiv.org/abs/2311.04400), Hong et al., ICLR 2024 | [bibtex](./citations/lrm.txt)
- [DMV3D:Denoising Multi-View Diffusion using 3D Large Reconstruction Model](https://arxiv.org/abs/2311.09217), Xu et al., ICLR 2024 | [bibtex](./citations/dmv3d.txt) 
- [WildFusion:Learning 3D-Aware Latent Diffusion Models in View Space](https://arxiv.org/abs/2311.13570), Schwarz et al., ICLR 2024 | [bibtex](./citations/wildfusion.txt)
- [Functional Diffusion](https://arxiv.org/abs/2311.15435), Zhang et al., CVPR 2024 | [github](https://github.com/1zb/functional-diffusion) | [bibtex](./citations/fd.txt)
- [MeshGPT: Generating Triangle Meshes with Decoder-Only Transformers](https://arxiv.org/abs/2311.15475), Siddiqui et al., arxiv 2023 | [github](https://github.com/nihalsid/mesh-gpt) | [bibtex](./citations/meshgpt.txt)
- [SPiC·E: Structural Priors in 3D Diffusion Models using Cross-Entity Attention](https://arxiv.org/abs/2311.17834), Sella et al., arxiv 2023 | [github](https://github.com/TAU-VAILab/spic-e) | [bibtex](./citations/spice.txt)
- [ZeroRF: Fast Sparse View 360° Reconstruction with Zero Pretraining](https://arxiv.org/abs/2312.09249), Shi et al., arxiv 2023 | [github](https://github.com/eliphatfs/zerorf)  | [bibtex](./citations/zeroRF.txt) 
- [Learning the 3D Fauna of the Web](https://arxiv.org/abs/2401.02400), Li et al., arxiv 2024 | [bibtex](./citations/3dfauna.txt)
- [Pushing Auto-regressive Models for 3D Shape Generation at Capacity and Scalability](https://arxiv.org/abs/2402.12225), Qian et al., arxiv 2024 | [github](https://github.com/FVPLab/Argus-3D) | [bibtext](./citations/argus3d.txt)
- [LN3Diff: Scalable Latent Neural Fields Diffusion for Speedy 3D Generation](https://arxiv.org/abs/2403.12019), Lan et al., arxiv 2024 | [github](https://github.com/NIRVANALAN/LN3Diff) | [bibtext](./citations/LN3Diff.txt)
- [GRM: Large Gaussian Reconstruction Model for Efficient 3D Reconstruction and Generation](https://arxiv.org/abs/2403.14621), Xu et al., arxiv 2024 | [github](https://github.com/justimyhxu/grm) | [bibtext](./citations/grm.txt)
- [Lift3D: Zero-Shot Lifting of Any 2D Vision Model to 3D](https://arxiv.org/abs/2403.18922), Varma T et al., CVPR 2024 | [github](https://github.com/MukundVarmaT/Lift3D) | [bibtext](./citations/lift3d.txt)
- [MeshLRM: Large Reconstruction Model for High-Quality Meshes](https://arxiv.org/abs/2404.12385), Wei et al., arxiv 2024 | [bibtext](./citations/meshlrm.txt)
- [Interactive3D🪄: Create What You Want by Interactive 3D Generation](https://arxiv.org/abs/2404.16510), Dong et al., CVPR 2024 | [github](https://github.com/interactive-3d/interactive3d) | [bibtex](./citations/interactive3D.txt)


</details>


<details open>
<summary>Scene</summary>


- [GRAF: Generative Radiance Fields for 3D-Aware Image Synthesis](https://arxiv.org/abs/2007.02442), Schwarz et al., NeurIPS 2020 | [github](https://github.com/autonomousvision/graf) | [bibtext](./citations/graf.txt)
- [ATISS: Autoregressive Transformers for Indoor Scene Synthesis](https://arxiv.org/abs/2110.03675), Paschalidou et al., NeurIPS 2021 | [github](https://github.com/nv-tlabs/atiss) | [bibtext](./citations/atiss.txt) 
- [GAUDI: A Neural Architect for Immersive 3D Scene Generation](https://arxiv.org/abs/2207.13751), Bautista et al., NeurIPS 2022 | [github](https://github.com/apple/ml-gaudi) | [bibtext](./citations/gaudi.txt)
- [NeuralField-LDM: Scene Generation with Hierarchical Latent Diffusion Models](https://arxiv.org/abs/2304.09787), Kim et al., CVPR 2023 | [bibtext](./citations/nerfldm.txt)
- [Pyramid Diffusion for Fine 3D Large Scene Generation](https://arxiv.org/abs/2311.12085), Liu et al., arxiv 2023 | [github](https://yuheng.ink/project-page/pyramid-discrete-diffusion/) | [bibtext](./citations/pyramid.txt) 
- [XCube: Large-Scale 3D Generative Modeling using Sparse Voxel Hierarchies](https://arxiv.org/abs/2312.03806), Ren et al., arxiv 2023 | [bibtex](./citations/xcube.txt)
- [DUSt3R: Geometric 3D Vision Made Easy](https://arxiv.org/abs/2312.14132), Wang et al., arxiv 2023 | [github](https://github.com/naver/dust3r) | [bibtext](./citations/dust3r.txt)


</details>

<details open>
<summary>Human Avatar</summary>

- [SMPL: A skinned multi-person linear model](https://dl.acm.org/doi/10.1145/2816795.2818013), Loper et al., TOG 2015 | [bibtex](./citations/smpl.txt)
- [SMPLicit: Topology-aware Generative Model for Clothed People](https://arxiv.org/abs/2103.06871), Corona et al., CVPR 2021 | [github](https://github.com/enriccorona/SMPLicit) | [bibtext](./citations/smplicit.txt)
- [HeadNeRF: A Real-time NeRF-based Parametric Head Model](https://arxiv.org/abs/2112.05637), Hong et al., CVPR 2022 | [github](https://github.com/CrisHY1995/headnerf) | [bibtext](./citations/headnerf.txt)
- [gDNA: Towards Generative Detailed Neural Avatars](https://arxiv.org/abs/2201.04123), Chen et al., CVPR 2022 | [github](https://github.com/xuchen-ethz/gdna) | [bibtext](./citations/gdna.txt)
- [Rodin: A Generative Model for Sculpting 3D Digital Avatars Using Diffusion](https://arxiv.org/abs/2212.06135), Wang et al., CVPR 2023 | [bibtex](./citations/rodin.txt)
- [Single-View 3D Human Digitalization with Large Reconstruction Models](https://arxiv.org/abs/2401.12175), Weng et al., CVPR 2023 | [bibtex](./citations/singlehuman.txt)


</details>

</details>

<details close>
<summary>2D Prior-based 3D Generative Methods</summary>

<details open>
<summary>Object</summary>

- [DreamFields: Zero-Shot Text-Guided Object Generation with Dream Fields](https://arxiv.org/abs/2112.01455), Jain et al., CVPR 2022 | [github](https://github.com/google-research/google-research/tree/master/dreamfields) | [bibtex](./citations/dreamfields.txt)
- [DreamFusion: Text-to-3D using 2D Diffusion](https://arxiv.org/abs/2209.14988), Poole et al., ICLR 2023 | [github](https://github.com/ashawkey/stable-dreamfusion) | [bibtex](./citations/dreamfusion.txt)
- [Dream3D: Zero-Shot Text-to-3D Synthesis Using 3D Shape Prior and Text-to-Image Diffusion Models](https://arxiv.org/abs/2212.14704), Xu et al., CVPR 2023 | [bibtex](./citations/dream3d.txt)
- [Magic3D: High-Resolution Text-to-3D Content Creation](https://arxiv.org/abs/2211.10440), Lin et al., CVPR 2023 | [bibtex](./citations/magic3d.txt)
- [Score Jacobian Chaining: Lifting Pretrained 2D Diffusion Models for 3D Generation](https://arxiv.org/abs/2212.00774), Wang et al., CVPR 2023 |[github](https://github.com/pals-ttic/sjc/)| [bibtex](./citations/sjc.txt)
- [RealFusion: 360° Reconstruction of Any Object from a Single Image](https://arxiv.org/abs/2302.10663), Melas-Kyriazi et al., CVPR 2023 | [github](https://github.com/lukemelas/realfusion) | [bibtex](./citations/realfusion.txt)
- [3DFuse: Let 2D Diffusion Model Know 3D-Consistency for Robust Text-to-3D Generation](https://arxiv.org/abs/2303.07937), Seo et al., ICLR 2024 | [github](https://github.com/KU-CVLAB/3DFuse) | [bibtex](./citations/3dfuse.txt)
- [DreamBooth3D: Subject-Driven Text-to-3D Generation](https://arxiv.org/abs/2303.13508), Raj et al., ICCV 2023 | [bibtex](./citations/dreambooth3d.txt)
- [Fantasia3D: Disentangling Geometry and Appearance for High-quality Text-to-3D Content Creation](https://arxiv.org/abs/2303.13873/), Chen et al., ICCV 2023 | [github](https://github.com/Gorilla-Lab-SCUT/Fantasia3D) | [bibtex](./citations/fantasia3d.txt)
- [Make-It-3D: High-Fidelity 3D Creation from A Single Image with Diffusion Prior](https://arxiv.org/abs/2303.14184), Tang et al., ICCV 2023 | [github](https://github.com/junshutang/Make-It-3D) | [bibtex](./citations/makeit3d.txt)
- [HiFA: High-fidelity Text-to-3D with Advanced Diffusion Guidance](https://arxiv.org/abs/2305.18766), Zhu et al., ICLR 2024 | [github](https://github.com/HiFA-team/HiFA) | [bibtex](./citations/hifa.txt)
- [ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation with Variational Score Distillation](https://arxiv.org/abs/2305.16213), Wang et al., NeurIPS 2023 | [github](https://github.com/thu-ml/prolificdreamer) | [bibtex](./citations/prolificdreamer.txt)
- [ATT3D: Amortized Text-to-3D Object Synthesis](https://arxiv.org/abs/2306.07349), Lorraine et al., ICCV 2023 | [bibtex](./citations/att3d.txt)
- [DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation](https://arxiv.org/abs/2309.16653), Tang et al., ICLR 2024 | [github](https://github.com/dreamgaussian/dreamgaussian) | [bibtex](./citations/dreamguassian.txt)
- [NFSD: Noise Free Score Distillation](https://arxiv.org/abs/2310.17590), Katzir et al., arxiv 2023 | [github](https://github.com/orenkatzir/nfsd) | [bibtex](./citations/nfsd.txt)
- [Text-to-3D with Classifier Score Distillation](https://arxiv.org/abs/2310.19415), Yu et al., arxiv 2023 | [github](https://github.com/CVMI-Lab/Classifier-Score-Distillation) | [bibtex](./citations/csd.txt)
- [IPDreamer: Appearance-Controllable 3D Object Generation with Image Prompts](https://arxiv.org/abs/2310.05375), Zeng et al., arxiv 2023 | [bibtex](./citations/ipdreamer.txt)
- [Progressive3D: Progressively Local Editing for Text-to-3D Content Creation with Complex Semantic Prompts](https://arxiv.org/abs/2310.11784), Cheng et al., arxiv 2023 |  [github](https://github.com/cxh0519/Progressive3D) | [bibtex](./citations/progressive3d.txt)
- [Instant3D : Instant Text-to-3D Generation](https://arxiv.org/abs/2311.08403), Li et al., ICLR 2024 | [bibtex](./citations/instant3d_.txt) 
- [LucidDreamer: Towards High-Fidelity Text-to-3D Generation via Interval Score Matching](https://arxiv.org/abs/2311.11284), Liang et al., arxiv 2023 | [github](https://github.com/EnVision-Research/LucidDreamer) | [bibtex](./citations/luciddreamer-object.txt)
- [Control3D: Towards Controllable Text-to-3D Generation](https://arxiv.org/abs/2311.05461), Chen et al., ACM Multimedia 2023 | [bibtex](./citations/control3d.txt)
- [CG3D: Compositional Generation for Text-to-3D via Gaussian Splatting](https://arxiv.org/abs/2311.17907), Vilesov et al., arxiv 2023 | [bibtex](./citations/gc3d.txt)
- [StableDreamer: Taming Noisy Score Distillation Sampling for Text-to-3D](https://arxiv.org/abs/2312.02189), Guo et al., arxiv 2023 | [bibtex](./citations/stabledreamer.txt)
- [CAD: Photorealistic 3D Generation via Adversarial Distillation](https://arxiv.org/abs/2312.06663), Wan et al., arxiv 2023 | [github](https://github.com/raywzy/CAD) | [bibtex](./citations/CAD.txt)
- [DreamControl: Control-Based Text-to-3D Generation with 3D Self-Prior](https://arxiv.org/abs/2312.06439), Huang et al., arxiv 2023 |  [github](https://github.com/tyhuang0428/DreamControl) | [bibtex](./citations/dreamcontrol.txt)
- [AGAP:Learning Naturally Aggregated Appearance for Efficient 3D Editing](https://arxiv.org/abs/2312.06657), Cheng et al., arxiv 2023 |  [github](https://github.com/felixcheng97/AGAP) | [bibtex](./citations/agap.txt)
- [SSD: Stable Score Distillation for High-Quality 3D Generation](https://arxiv.org/abs/2312.09305), Tang et al., arxiv 2023 | [bibtex](./citations/ssd.txt)
- [SteinDreamer: Variance Reduction for Text-to-3D Score Distillation via Stein Identity](https://arxiv.org/abs/2401.00604), Wang et al., arxiv 2023 | [github](https://github.com/VITA-Group/SteinDreamer) | [bibtex](./citations/steindreamer.txt)
- [Taming Mode Collapse in Score Distillation for Text-to-3D Generation](https://arxiv.org/abs/2401.00909), Wang et al., arxiv 2024 | [github](https://github.com/VITA-Group/3D-Mode-Collapse) | [bibtex](./citations/3d-mode-collapse.txt)
- [Score Distillation Sampling with Learned Manifold Corrective](https://arxiv.org/abs/2401.05293), Alldieck et al., arxiv 2024 | [bibtex](./citations/sdslmc.txt)
- [Consistent3D: Towards Consistent High-Fidelity Text-to-3D Generation with Deterministic Sampling Prior](https://arxiv.org/abs/2401.09050), Wu et al., arxiv 2024 | [bibtex](./citations/consistent3d.txt)
- [TIP-Editor: An Accurate 3D Editor Following Both Text-Prompts And Image-Prompts](https://arxiv.org/abs/2401.14828), Zhuang et al., arxiv 2024 | [bibtex](./citations/tipEditor.txt)


</details>


<details open>
<summary>Scene</summary>

- [Text2Light: Zero-Shot Text-Driven HDR Panorama Generation](https://arxiv.org/abs/2209.09898), Chen et al., TOG 2022 | [github](https://github.com/FrozenBurning/Text2Light) | [bibtext](./citations/text2light.txt) 
- [SceneScape: Text-Driven Consistent Scene Generation](https://arxiv.org/abs/2302.01133), Fridman et al., NeurIPS 2023 | [github](https://github.com/RafailFridman/SceneScape) | [bibtext](./citations/scenescape.txt) 
- [DiffuScene: Scene Graph Denoising Diffusion Probabilistic Model for Generative Indoor Scene Synthesis](https://arxiv.org/abs/2303.14207), Tang et al., arxiv 2023 | [github](https://github.com/tangjiapeng/DiffuScene) | [bibtext](./citations/diffuscene.txt) 
- [Text2Room: Extracting Textured 3D Meshes from 2D Text-to-Image Models](https://arxiv.org/abs/2303.11989), Höllein et al., ICCV 2023 | [github](https://github.com/lukasHoel/text2room) | [bibtext](./citations/text2room.txt) 
- [Text2NeRF: Text-Driven 3D Scene Generation with Neural Radiance Fields](https://arxiv.org/abs/2305.11588), Zhang et al., TVCG 2024 | [github](https://github.com/eckertzhang/Text2NeRF) | [bibtext](./citations/text2nerf.txt) 
- [CityDreamer: Compositional Generative Model of Unbounded 3D Cities](https://arxiv.org/abs/2309.00610), Xie et al., arxiv 2023 | [github](https://github.com/hzxie/city-dreamer) | [bibtext](./citations/cityDreamer.txt)
- [GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting](https://arxiv.org/abs/2311.14521), Chen et al., arxiv 2023 |  [github](https://github.com/buaacyw/GaussianEditor) | [bibtex](./citations/gaussianeditor.txt)
- [LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2311.13384), Chuang et al., arxiv 2023 | [github](https://github.com/luciddreamer-cvlab/LucidDreamer)  | [bibtext](./citations/luciddreamer-scene.txt)
- [GaussianEditor: Editing 3D Gaussians Delicately with Text Instructions](https://arxiv.org/abs/2311.16037), Fang et al., arxiv 2023 | [bibtex](./citations/gaussianEditor2.txt)
- [Gaussian Grouping: Segment and Edit Anything in 3D Scenes](https://arxiv.org/abs/2312.00732), Ye et al., arxiv 2023 |  [github](https://github.com/lkeab/gaussian-grouping) | [bibtex](./citations/gaussian-group.txt)
- [Inpaint3D: 3D Scene Content Generation using 2D Inpainting Diffusion](https://arxiv.org/abs/2312.03869), Prabhu et al., arxiv 2023 | [bibtext](./citations/inpaint3d.txt)
- [SIGNeRF: Scene Integrated Generation for Neural Radiance Fields](https://arxiv.org/abs/2401.01647), Dihlmann et al., arxiv 2024 |  [github](https://github.com/cgtuebingen/SIGNeRF) | [bibtex](./citations/sigNerf.txt)
- [Disentangled 3D Scene Generation with Layout Learning](https://arxiv.org/abs/2402.16936), Epstein, et al., arxiv 2024 | [bibtex](./citations/disentangled.txt)


</details>

<details open>
<summary>Human Avatar</summary>

- [AvatarCLIP: Zero-Shot Text-Driven Generation and Animation of 3D Avatars](https://arxiv.org/abs/2205.08535), Hong et al., SIGGRAPH 2022 |  [github](https://github.com/hongfz16/AvatarCLIP) | [bibtex](./citations/teca.txt)
- [DreamWaltz: Make a Scene with Complex 3D Animatable Avatars](https://arxiv.org/abs/2305.12529), Huang et al., NeurIPS 2023 |  [github](https://github.com/IDEA-Research/DreamWaltz) | [bibtex](./citations/dreamwaltz.txt)
- [DreamHuman: Animatable 3D Avatars from Text](https://arxiv.org/abs/2306.09329), Wang et al., arxiv 2023 | [bibtex](./citations/dreamhuman.txt)
- [TECA: Text-Guided Generation and Editing of Compositional 3D Avatars](https://arxiv.org/abs/2309.07125), Zhang et al., arxiv 2023 |  [github](https://github.com/HaoZhang990127/TECA) | [bibtex](./citations/teca.txt)
- [HumanGaussian: Text-Driven 3D Human Generation with Gaussian Splatting](https://arxiv.org/abs/2311.17061), Liu et al., arxiv 2023 |  [github](https://github.com/alvinliu0/HumanGaussian) | [bibtex](./citations/humangaussian.txt)
- [HeadArtist: Text-conditioned 3D Head Generation with Self Score Distillation](https://arxiv.org/abs/2312.07539), Liu et al., arxiv 2023 | [bibtex](./citations/headArtist.txt)
- [3DGS-Avatar: Animatable Avatars via Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2312.09228), Qian et al., arxiv 2023 |  [github](https://github.com/mikeqzy/3dgs-avatar-release) | [bibtex](./citations/3dgsAvatar.txt)


</details>


</details>


<details close>
<summary>Hybrid 3D Generative Methods</summary>

<details open>
<summary>Object</summary>

- [Zero-1-to-3: Zero-shot One Image to 3D Object](https://arxiv.org/abs/2303.11328), Liu et al., ICCV 2023 | [github](https://github.com/cvlab-columbia/zero123) | [bibtex](./citations/zero123.txt)
- [One-2-3-45: Any Single Image to 3D Mesh in 45 Seconds without Per-Shape Optimization](https://arxiv.org/abs/2306.16928), Liu et al., NeurIPS 2023 | [github](https://github.com/One-2-3-45/One-2-3-45) | [bibtex](./citations/one2345.txt)
- [Magic123: One Image to High-Quality 3D Object Generation Using Both 2D and 3D Diffusion Priors](https://arxiv.org/abs/2306.17843), Qian et al., arxiv 2023 | [github](https://github.com/guochengqian/Magic123) | [bibtex](./citations/magic123.txt)
- [MVDream: Multi-view Diffusion for 3D Generation](https://arxiv.org/abs/2308.16512), Shi et al., arxiv 2023 | [github](https://github.com/bytedance/MVDream) | [bibtex](./citations/mvdream.txt)
- [SyncDreamer: Generating Multiview-consistent Images from a Single-view Image](https://arxiv.org/abs/2309.03453), Liu et al., arxiv 2023 | [github](https://liuyuan-pal.github.io/SyncDreamer/) | [bibtex](./citations/syncdreamer.txt)
- [Gsgen: Text-to-3D using Gaussian Splatting](https://arxiv.org/abs/2309.16585), Chen et al., arxiv 2023 | [github](https://github.com/gsgen3d/gsgen) | [bibtex](./citations/gsgen.txt)
- [Consistent123: One Image to Highly Consistent 3D Asset Using Case-Aware Diffusion Priors](https://arxiv.org/abs/2309.17261), Lin et al., arxiv 2024  | [bibtex](./citations/consistent123c.txt)
- [GaussianDreamer: Fast Generation from Text to 3D Gaussians by Bridging 2D and 3D Diffusion Models](https://arxiv.org/abs/2310.08529), Yi et al., arxiv 2023 | [github](https://github.com/hustvl/GaussianDreamer) | [bibtex](./citations/gaussianDreamer.txt)
- [Consistent-1-to-3: Consistent Image to 3D View Synthesis via Geometry-aware Diffusion Models](https://arxiv.org/abs/2310.03020), Ye et al., 3DV 2024  | [bibtex](./citations/consistent123.txt)
- [Zero123++: a Single Image to Consistent Multi-view Diffusion Base Model](https://arxiv.org/abs/2310.15110), Shi et al., arxiv 2023 | [github](https://github.com/SUDO-AI-3D/zero123plus) | [bibtex](./citations/zero123++.txt)
- [TOSS: High-quality Text-guided Novel View Synthesis from a Single Image](https://arxiv.org/abs/2310.10644), Shi et al., arxiv 2023 | [bibtex](./citations/toss.txt)
- [Wonder3D: Single Image to 3D using Cross-Domain Diffusion](https://arxiv.org/abs/2310.15008), Long et al., arxiv 2023 | [github](https://github.com/xxlong0/Wonder3D) | [bibtex](./citations/wonder3d.txt)
- [DreamCraft3D: Hierarchical 3D Generation with Bootstrapped Diffusion Prior](https://arxiv.org/abs/2310.16818), Sun et al., ICLR 2024 | [github](https://github.com/deepseek-ai/DreamCraft3D) | [bibtex](./citations/dreamcraft3d.txt)
- [SweetDreamer: Aligning Geometric Priors in 2D Diffusion for Consistent Text-to-3D](https://arxiv.org/abs/2310.02596), Li et al., arxiv 2023 | [github](https://github.com/wyysf-98/SweetDreamer) | [bibtex](./citations/sweetdreamer.txt)
- [One-2-3-45++: Fast Single Image to 3D Objects with Consistent Multi-View Generation and 3D Diffusion](https://arxiv.org/abs/2311.07885), Liu et al., arxiv 2023 | [github](https://github.com/SUDO-AI-3D/One2345plus) | [bibtex](./citations/one2345++.txt)
- [Direct2.5: Diverse Text-to-3D Generation via Multi-view 2.5D Diffusion](https://arxiv.org/abs/2311.15980), Lu et al., arxiv 2023 | [bibtex](./citations/direct25.txt)
- [ConRad: Image Constrained Radiance Fields for 3D Generation from a Single Image](https://arxiv.org/abs/2311.05230), Purushwalkam et al., NeurIPS 2023 | [bibtex](./citations/conrad.txt)
- [Instant3D: Fast Text-to-3D with Sparse-View Generation and Large Reconstruction Model](https://arxiv.org/abs/2311.06214), Li et al., arxiv 2023 | [bibtex](./citations/instant3d.txt) 
- [MVControl: Adding Conditional Control to Multi-view Diffusion for Controllable Text-to-3D Generation](https://arxiv.org/abs/2311.14494), Li et al., arxiv 2023 |  [github](https://github.com/WU-CVGL/MVControl/) | [bibtex](./citations/mvcontorl.txt)
- [GeoDream:Disentangling 2D and Geometric Priors for High-Fidelity and Consistent 3D Generation](https://arxiv.org/abs/2311.17971), Ma et al., arxiv 2023 | [github](https://github.com/baaivision/GeoDream/) | [bibtex](./citations/geodream.txt)
- [RichDreamer: A Generalizable Normal-Depth Diffusion Model for Detail Richness in Text-to-3D](https://arxiv.org/abs/2311.16918), Qiu et al., arxiv 2023 | [github](https://github.com/alibaba/RichDreamer) | [bibtex](./citations/richdreamer.txt)
- [Slice3D: Multi-Slice, Occlusion-Revealing, Single View 3D Reconstruction](https://arxiv.org/abs/2312.02221), Wang et al., CVPR 2024 | [github](https://github.com/yizhiwang96/Slice3D) | [bibtex](./citations/slice3d.txt)
- [DreamComposer: Controllable 3D Object Generation via Multi-View Conditions](https://arxiv.org/abs/2312.03611), Yang et al., arxiv 2023 | [github](https://github.com/yhyang-myron/DreamComposer) | [bibtex](./citations/dreamcomposer.txt)
- [Cascade-Zero123: One Image to Highly Consistent 3D with Self-Prompted Nearby Views](https://arxiv.org/abs/2312.04424), Chen et al., arxiv 2023 | [github](https://github.com/AbrahamYabo/Cascade-Zero123) | [bibtex](./citations/cascadeZero123.txt)
- [Free3D: Consistent Novel View Synthesis without 3D Representation](https://arxiv.org/abs/2312.04551), Zheng et al., arxiv 2023 | [github](https://github.com/lyndonzheng/Free3D) | [bibtex](./citations/free3d.txt)
- [Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior](https://arxiv.org/abs/2312.06655), Liu et al., arxiv 2023 | [github](https://github.com/liuff19/Sherpa3D) | [bibtex](./citations/sherpa3d.txt)
- [UniDream: Unifying Diffusion Priors for Relightable Text-to-3D Generation](https://arxiv.org/abs/2312.08754), Liu et al., arxiv 2023 | [github](https://yg256li.github.io/UniDream/) | [bibtex](./citations/unidream.txt)
- [Repaint123: Fast and High-quality One Image to 3D Generation with Progressive Controllable 2D Repainting](https://arxiv.org/abs/2312.13271), Zhang et al., arxiv 2023 | [github](https://github.com/junwuzhang19/repaint123) | [bibtex](./citations/repaint123.txt)
- [BiDiff: Text-to-3D Generation with Bidirectional Diffusion using both 2D and 3D priors](https://arxiv.org/abs/2312.04963), Ding et al., arxiv 2023 | [github](https://github.com/BiDiff/bidiff) | [bibtex](./citations/bidiff.txt)
- [ControlDreamer: Stylized 3D Generation with Multi-View ControlNet](https://arxiv.org/abs/2312.01129), Oh et al., arxiv 2023 |  [github](https://github.com/oyt9306/ControlDreamer) | [bibtex](./citations/controldreamer.txt)
- [X-Dreamer: Creating High-quality 3D Content by Bridging the Domain Gap Between Text-to-2D and Text-to-3D Generation](https://arxiv.org/abs/2312.00085), Ma et al., arxiv 2023 | [github](https://github.com/xmu-xiaoma666/X-Dreamer) | [bibtex](./citations/xdreamer.txt)
- [Splatter Image: Ultra-Fast Single-View 3D Reconstruction](https://arxiv.org/abs/2312.13150), Szymanowicz et al., arxiv 2023 | [github](https://github.com/szymanowiczs/splatter-image) | [bibtex](./citations/splatter-image.txt)
- [Carve3D: Improving Multi-view Reconstruction Consistency for Diffusion Models with RL Finetuning](https://arxiv.org/abs/2312.13980), Xie et al., arxiv 2023 | [bibtex](./citations/carve3d.txt)
- [HarmonyView: Harmonizing Consistency and Diversity in One-Image-to-3D](https://arxiv.org/abs/2312.15980), Woo et al., arxiv 2023 | [github](https://github.com/byeongjun-park/HarmonyView) | [bibtex](./citations/harmonyView.txt)
- [ImageDream: Image-Prompt Multi-view Diffusion for 3D Generation](https://arxiv.org/abs/2312.02201), Wang et al., arxiv 2023 | [github](https://github.com/bytedance/ImageDream) | [bibtex](./citations/imageDream.txt)
- [iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views](https://arxiv.org/abs/2312.17250), Wu et al., arxiv 2023 | [github](https://github.com/chinhsuanwu/ifusion) | [bibtex](./citations/ifusion.txt)
- [AGG: Amortized Generative 3D Gaussians for Single Image to 3D](https://arxiv.org/abs/2401.04099), Xu et al., arxiv 2024 | [bibtex](./citations/agg.txt)
- [HexaGen3D: StableDiffusion is just one step away from Fast and Diverse Text-to-3D Generation](https://arxiv.org/abs/2401.07727), Mercier et al., arxiv 2024 | [bibtex](./citations/HexaGen3D.txt)
- [HexaGen3D: StableDiffusion is just one step away from Fast and Diverse Text-to-3D Generation](https://arxiv.org/abs/2401.07727), Mercier et al., arxiv 2024 | [bibtex](./citations/HexaGen3D.txt)
- [Sketch2NeRF: Multi-view Sketch-guided Text-to-3D Generation](https://arxiv.org/abs/2401.14257), Chen et al., arxiv 2024 | [bibtex](./citations/Sketch2NeRF.txt)
- [IM-3D: Iterative Multiview Diffusion and Reconstruction for High-Quality 3D Generation](https://arxiv.org/abs/2402.08682), Melas-Kyriazi et al., arxiv 2024 | [bibtex](./citations/im3d.txt)
- [LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation](https://arxiv.org/abs/2402.05054), Tang et al., arxiv 2024 | [github](https://github.com/3DTopia/LGM)  | [bibtex](./citations/lgm.txt) 
- [Retrieval-Augmented Score Distillation for Text-to-3D Generation](https://arxiv.org/abs/2402.02972), Seo et al., arxiv 2024 | [github](https://github.com/KU-CVLAB/RetDream) | [bibtex](./citations/retdream.txt) 
- [EscherNet: A Generative Model for Scalable View Synthesis](https://arxiv.org/abs/2402.03908), Kong et al., arxiv 2024 | [github](https://github.com/kxhit/EscherNet)  | [bibtex](./citations/eschernet.txt) 
- [MVDiffusion++: A Dense High-resolution Multi-view Diffusion Model for Single or Sparse-view 3D Object Reconstruction](https://arxiv.org/abs/2402.12712), Tang et al., arxiv 2024  | [bibtex](./citations/mvdiffusionplus.txt) 
- [MVD2: Efficient Multiview 3D Reconstruction for Multiview Diffusion](https://arxiv.org/abs/2402.14253), Zheng et al., arxiv 2024  | [bibtex](./citations/mvd2.txt) 
- [Consolidating Attention Features for Multi-view Image Editing](https://arxiv.org/abs/2402.14792), Patashnik et al., arxiv 2024  | [bibtex](./citations/mvie.txt) 
- [ViewFusion: Towards Multi-View Consistency via Interpolated Denoising](https://arxiv.org/abs/2402.18842), Yang et al., CVPR 2024 | [github](https://github.com/Wi-sc/ViewFusion)  | [bibtex](./citations/viewfusion.txt) 
- [CRM: Single Image to 3D Textured Mesh with Convolutional Reconstruction Model](https://arxiv.org/abs/2403.05034), Wang et al., arxiv 2024 | [github](https://github.com/thu-ml/CRM) | [bibtext](./citations/crm.txt)
- [Sculpt3D: Multi-View Consistent Text-to-3D Generation with Sparse 3D Prior](https://arxiv.org/abs/2403.09140), Chen et al., CVPR 2024 | [github](https://github.com/StellarCheng/Scuplt_3d) | [bibtext](./citations/Scuplt_3d.txt)
- [Make-Your-3D: Fast and Consistent Subject-Driven 3D Content Generation](https://arxiv.org/abs/2403.09625), Liu et al., arxiv 2024 | [github](https://github.com/liuff19/Make-Your-3D) | [bibtext](./citations/make_your_3d.txt)
- [Controllable Text-to-3D Generation via Surface-Aligned Gaussian Splatting](https://arxiv.org/abs/2403.09981), Li et al., arxiv 2024 |  [github](https://github.com/WU-CVGL/MVControl/) | [bibtex](./citations/controllable.txt)
- [VideoMV: Consistent Multi-View Generation Based on Large Video Generative Model](https://arxiv.org/abs/2403.12010), Zuo et al., arxiv 2024 |  [github](https://github.com/alibaba/VideoMV) | [bibtex](./citations/videomv.txt)
- [SV3D: Novel Multi-view Synthesis and 3D Generation from a Single Image using Latent Video Diffusion](https://arxiv.org/abs/2403.12008), Voleti et al., arxiv 2024 | [bibtex](./citations/sv3d.txt)
- [DreamReward: Text-to-3D Generation with Human Preference](https://arxiv.org/abs/2403.14613), Ye et al., arxiv 2024 | [bibtex](./citations/dreamreward.txt)
- [LATTE3D: Large-scale Amortized Text-To-Enhanced3D Synthesis](https://arxiv.org/abs/2403.15385), Xie et al., arxiv 2024 | [bibtex](./citations/latte3d.txt)
- [DreamPolisher: Towards High-Quality Text-to-3D Generation via Geometric Diffusion](https://arxiv.org/abs/2403.17237), Lin et al., arxiv 2024 | [github](https://github.com/yuanze-lin/DreamPolisher) | [bibtex](./citations/dreampolisher.txt)
- [GeoWizard: Unleashing the Diffusion Priors for 3D Geometry Estimation from a Single Image](https://arxiv.org/abs/2403.12013), Fu et al., arxiv 2024 | [github](https://github.com/fuxiao0719/GeoWizard) | [bibtex](./citations/geowizard.txt)
- [ThemeStation: Generating Theme-Aware 3D Assets from Few Exemplars](https://arxiv.org/abs/2403.15383), Wang et al., arxiv 2024 | [github](https://github.com/3DThemeStation/ThemeStation) | [bibtex](./citations/ThemeStation.txt)
- [FlexiDreamer: Single Image-to-3D Generation with FlexiCubes](https://arxiv.org/abs/2404.00987), Zhao et al., arxiv 2024 | [github](https://github.com/zhaorw02/FlexiDreamer) | [bibtex](./citations/flexidreamer.txt)
- [Sketch3D: Style-Consistent Guidance for Sketch-to-3D Generation](https://arxiv.org/abs/2404.01843), Zheng et al., arxiv 2024 | [bibtex](./citations/sketch3d.txt)
- [DreamView: Injecting View-specific Text Guidance into Text-to-3D Generation](https://arxiv.org/abs/2404.06119), Yan et al., arxiv 2024 | [github](https://github.com/iSEE-Laboratory/DreamView) | [bibtex](./citations/dreamview.txt)
- [InstantMesh: Efficient 3D Mesh Generation from a Single Image with Sparse-view Large Reconstruction Models](https://arxiv.org/abs/2404.07191), Xu et al., arxiv 2024 | [github](https://github.com/TencentARC/InstantMesh) | [bibtex](./citations/instant_mesh.txt)
- [DGE: Direct Gaussian 3D Editing by Consistent Multi-view Editing](https://arxiv.org/abs/2404.18929), Chen et al., arxiv 2024 | [github](https://github.com/silent-chen/DGE) | [bibtex](./citations/dge.txt)
- [MicroDreamer: Zero-shot 3D Generation in ∼20 Seconds by Score-based Iterative Reconstruction](https://arxiv.org/abs/2404.19525), Chen et al., arxiv 2024 | [github](https://github.com/ML-GSAI/MicroDreamer) | [bibtex](./citations/microdreamer.txt)



</details>


<details open>
<summary>Scene</summary>


- [Ctrl-Room: Controllable Text-to-3D Room Meshes Generation with Layout Constraints](https://arxiv.org/abs/2310.03602), Fang et al., arxiv 2023 | [github](https://github.com/fangchuan/Ctrl-Room) | [bibtext](./citations/ctrlroom.txt) 
- [RoomDesigner: Encoding Anchor-latents for Style-consistent and Shape-compatible Indoor Scene Generation](https://arxiv.org/abs/2310.10027), Zhao et al., 3DV 2024 | [github](https://github.com/zhao-yiqun/RoomDesigner) | [bibtext](./citations/roomdesigner.txt)
- [ZeroNVS: Zero-Shot 360-Degree View Synthesis from a Single Real Image](https://arxiv.org/abs/2310.17994), Sargent et al., arxiv 2023 | [github](https://github.com/kylesargent/zeronvs) | [bibtext](./citations/zeroNVS.txt) 
- [GraphDreamer: Compositional 3D Scene Synthesis from Scene Graphs](https://arxiv.org/abs/2312.00093), Gao et al., arxiv 2023 | [github](https://github.com/GGGHSL/GraphDreamer) | [bibtext](./citations/graphdreamer.txt)
- [ControlRoom3D:Room Generation using Semantic Proxy Rooms](https://arxiv.org/abs/2312.05208), Schult et al., arxiv 2023 | [bibtext](./citations/controlroom3d.txt)
- [AnyHome: Open-Vocabulary Generation of Structured and Textured 3D Homes](https://arxiv.org/abs/2312.06644), Wen et al., arxiv 2023 | [bibtext](./citations/anyhome.txt)
- [SceneWiz3D: Towards Text-guided 3D Scene Composition](https://arxiv.org/abs/2312.08885), Zhang et al., arxiv 2023 | [github](https://github.com/zqh0253/SceneWiz3D) | [bibtext](./citations/scenewiz3d.txt)
- [Text2Immersion: Generative Immersive Scene with 3D Gaussians](https://arxiv.org/abs/2312.09242), Ouyang et al., arxiv 2023 | [bibtext](./citations/text2immersion.txt)
- [ShowRoom3D: Text to High-Quality 3D Room Generation Using 3D Priors](https://arxiv.org/abs/2312.13324), Mao et al., arxiv 2023 | [github](https://github.com/showlab/ShowRoom3D) | [bibtext](./citations/showRoom3d.txt)
- [GALA3D: Towards Text-to-3D Complex Scene Generation via Layout-guided Generative Gaussian Splatting](https://arxiv.org/abs/2402.07207), Zhou et al., arxiv 2024 | [github](https://github.com/VDIGPKU/GALA3D) | [bibtext](./citations/gala3d.txt)
- [3D-SceneDreamer: Text-Driven 3D-Consistent Scene Generation](https://arxiv.org/abs/2403.09439), Zhang et al., arxiv 2024 | [bibtext](./citations/3dscenedreamer.txt)

</details>

<details open>
<summary>Human Avatar</summary>

- [SofGAN: A Portrait Image Generator with Dynamic Styling](https://arxiv.org/abs/2007.03780), Chen et al., TOG 2022 | [github](https://github.com/apchenstu/sofgan) | [bibtext](./citations/sofgan.txt) 
- [Get3DHuman: Lifting StyleGAN-Human into a 3D Generative Model using Pixel-aligned Reconstruction Priors](https://arxiv.org/abs/2302.01162), Xiong et al., ICCV 2023 | [github](https://github.com/X-zhangyang/Get3DHuman) | [bibtext](./citations/get3dhuman.txt) 
- [DreamFace: Progressive Generation of Animatable 3D Faces under Text Guidance](https://arxiv.org/abs/2304.03117), Zhang et al., arxiv 2023 | [bibtext](./citations/dreamface.txt) 
- [TADA! Text to Animatable Digital Avatars](https://arxiv.org/abs/2308.10899), Liao et al., 3DV 2024 | [github](https://github.com/TingtingLiao/TADA) | [bibtext](./citations/tada.txt) 
- [SCULPT: Shape-Conditioned Unpaired Learning of Pose-dependent Clothed and Textured Human Meshes](https://arxiv.org/abs/2308.10638), Sanyal et al., arxiv 2023 | [bibtext](./citations/sculpt.txt) 
- [HumanNorm: Learning Normal Diffusion Model for High-quality and Realistic 3D Human Generation](https://arxiv.org/abs/2310.01406), Huang et al., arxiv 2023 |  [github](https://github.com/xhuangcv/humannorm) | [bibtex](./citations/humannorm.txt)



</details>

<details open>
<summary>Dynamic</summary>

- [MAV3d: Text-To-4D Dynamic Scene Generation](https://arxiv.org/abs/2301.11280), Singer et al., arxiv 2023 | [bibtext](./citations/mav3d.txt) 
- [Control4D: Dynamic Portrait Editing by Learning 4D GAN from 2D Diffusion-based Editor](https://arxiv.org/abs/2305.20082), Shao et al., arxiv 2023 | [bibtex](./citations/control4d.txt)
- [MAS: Multi-view Ancestral Sampling for 3D motion generation using 2D diffusion](https://arxiv.org/abs/2310.14729), Kapon et al., arxiv 2023 | [github](https://github.com/roykapon/MAS) | [bibtext](./citations/mas.txt) 
- [Consistent4D: Consistent 360° Dynamic Object Generation from Monocular Video](https://arxiv.org/abs/2311.02848), Jiang et al., arxiv 2023 | [github](https://github.com/yanqinJiang/Consistent4D) | [bibtext](./citations/consistent4d.txt) 
- [Animate124: Animating One Image to 4D Dynamic Scene](https://arxiv.org/abs/2311.14603), Zhao et al., arxiv 2023 | [github](https://github.com/HeliosZhao/Animate124) | [bibtext](./citations/animate124.txt) 
- [A Unified Approach for Text- and Image-guided 4D Scene Generation](https://arxiv.org/abs/2311.16854), Zheng et al., arxiv 2023 | [bibtext](./citations/dream-in-4d.txt) 
- [4D-fy: Text-to-4D Generation Using Hybrid Score Distillation Sampling](https://arxiv.org/abs/2311.17984), Bahmani et al., arxiv 2023 | [github](https://github.com/sherwinbahmani/4dfy) | [bibtext](./citations/4dfy.txt) 
- [AnimatableDreamer: Text-Guided Non-rigid 3D Model Generation and Reconstruction with Canonical Score Distillation](https://arxiv.org/abs/2312.03795), Wang et al., arxiv 2023 | [bibtext](./citations/animatable-dreamer.txt) 
- [Virtual Pets: Animatable Animal Generation in 3D Scenes](https://arxiv.org/abs/2312.14154), Cheng et al., arxiv 2023 | [github](https://github.com/yccyenchicheng/VirtualPets) | [bibtext](./citations/virtual-pets.txt) 
- [Align Your Gaussians:Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models](https://arxiv.org/abs/2312.13763), Ling et al., arxiv 2023 [bibtext](./citations/aligngaussian.txt) 
- [Ponymation: Learning 3D Animal Motions from Unlabeled Online Videos](https://arxiv.org/abs/2312.13604), Sun et al., arxiv 2023 | [bibtext](./citations/ponyMation.txt) 
- [4DGen: Grounded 4D Content Generation with Spatial-temporal Consistency](https://arxiv.org/abs/2312.17225), Yin et al., arxiv 2023 | [github](https://github.com/VITA-Group/4DGen) | [bibtext](./citations/4dgen.txt) 
- [DreamGaussian4D: Generative 4D Gaussian Splatting](https://arxiv.org/abs/2312.17142), Ren et al., arxiv 2023 | [github](https://github.com/jiawei-ren/dreamgaussian4d) | [bibtext](./citations/dreamgaussian4d.txt) 
- [Fast Dynamic 3D Object Generation from a Single-view Video](https://arxiv.org/abs/2401.08742), Pan et al., arxiv 2024 | [github](https://github.com/fudan-zvg/Efficient4D) | [bibtext](./citations/efficient4d.txt)
- [ComboVerse: Compositional 3D Assets Creation Using Spatially-Aware Diffusion Guidance](https://arxiv.org/abs/2403.12409), Chen et al., arxiv 2024 | [bibtext](./citations/comboVerse.txt)
- [STAG4D: Spatial-Temporal Anchored Generative 4D Gaussians](https://arxiv.org/abs/2403.14939), Zeng et al., arxiv 2024  | [bibtext](./citations/stag4d.txt)
- [TC4D: Trajectory-Conditioned Text-to-4D Generation](https://arxiv.org/abs/2403.17920), Bahmani et al., arxiv 2024  | [bibtext](./citations/tc4d.txt)
- [Diffusion^2: Dynamic 3D Content Generation via Score Composition of Orthogonal Diffusion Models](https://arxiv.org/abs/2404.02148), Yang et al., arxiv 2024  | [bibtext](./citations/diffusion^2.txt)
- [Hash3D: Training-free Acceleration for 3D Generation](https://arxiv.org/abs/2404.06091), Yang et al., arxiv 2024 | [github](https://github.com/Adamdad/hash3D) | [bibtext](./citations/hash3d.txt)
- [Magic-Boost: Boost 3D Generation with Mutli-View Conditioned Diffusion](https://arxiv.org/abs/2404.06429), Yang et al., arxiv 2024 | [github](https://github.com/magic-research/magic-boost) | [bibtext](./citations/magicboost.txt)
- [Enhancing 3D Fidelity of Text-to-3D using Cross-View Correspondences](https://arxiv.org/abs/2404.10603), Kim et al., CVPR 2024 | [bibtext](./citations/cross-view-correspondences.txt)

</details>

</details>

<details close>
<summary>Others</summary>

<details open>
<summary>Physical</summary>

- [Physical Property Understanding from Language-Embedded Feature Fields](https://arxiv.org/abs/2404.04242), Zhai et al., CVPR 2024 | [github](https://github.com/ajzhai/NeRF2Physics) | [bibtext](./citations/nerf2physics.txt) 

</details>



<details open>
<summary>Texture</summary>

- [StyleMesh: Style Transfer for Indoor 3D Scene Reconstructions](https://arxiv.org/abs/2112.01530), Höllein et al., CVPR 2022 | [github](https://github.com/lukasHoel/stylemesh) | [bibtex](./citations/stylemesh.txt)
- [CLIP-Mesh: Generating textured meshes from text using pretrained image-text models](https://arxiv.org/abs/2203.13333), Khalid et al., SIGGRAPH Asia 2022 | [github](https://github.com/NasirKhalid24/CLIP-Mesh) | [bibtex](./citations/clipmesh.txt)
- [TANGO: Text-driven PhotoreAlistic aNd Robust 3D Stylization via LiGhting DecompOsition](https://arxiv.org/abs/2210.11277), Chen et al., NeurIPS 2022 | [github](https://github.com/Gorilla-Lab-SCUT/tango) | [bibtex](./citations/tango.txt)
- [Latent-NeRF for Shape-Guided Generation of 3D Shapes and Textures](https://arxiv.org/abs/2211.07600), Metzer et al., CVPR 2023 | [github](https://github.com/eladrich/latent-nerf) | [bibtex](./citations/latentNerf.txt)
- [TEXTure: Text-Guided Texturing of 3D Shapes](https://arxiv.org/abs/2302.01721), Richardson et al., SIGGRAPH 2023 | [github](https://github.com/TEXTurePaper/TEXTurePaper) | [bibtex](./citations/texture.txt)
- [Text2Tex: Text-driven Texture Synthesis via Diffusion Models](https://arxiv.org/abs/2303.11396), Chen et al., ICCV 2023 | [github](https://github.com/daveredrum/Text2Tex) | [bibtex](./citations/text2tex.txt)
- [RoomDreamer: Text-Driven 3D Indoor Scene Synthesis with Coherent Geometry and Texture](https://arxiv.org/abs/2305.11337), Song et al., ACM Multimedia 2023 | [bibtex](./citations/roomdreamer.txt)
- [Generating Parametric BRDFs from Natural Language Descriptions](https://arxiv.org/abs/2306.15679), Memery et al., arxiv 2023  [bibtex](./citations/BRDF.txt)
- [MVDiffusion: Enabling Holistic Multi-view Image Generation with Correspondence-Aware Diffusion](https://arxiv.org/abs/2307.01097), Tang et al., NeurIPS 2023 | [github](https://github.com/Tangshitao/MVDiffusion) | [bibtext](./citations/mvdiffusion.txt) 
- [MATLABER: Material-Aware Text-to-3D via LAtent BRDF auto-EncodeR](https://arxiv.org/abs/2308.09278), Xu et al., arxiv 2023 | [github](https://github.com/SheldonTsui/Matlaber) | [bibtex](./citations/matlaber.txt)
- [ITEM3D: Illumination-Aware Directional Texture Editing for 3D Models](https://arxiv.org/abs/2309.14872), Liu et al., arxiv 2023 | [github](https://github.com/shengqiliu1/ITEM3D) | [bibtex](./citations/item3d.txt)
- [TexFusion: Synthesizing 3D Textures with Text-Guided Image Diffusion Models](https://arxiv.org/abs/2310.13772), Cao et al., ICCV 2023 | [bibtex](./citations/texfusion.txt)
- [DreamSpace: Dreaming Your Room Space with Text-Driven Panoramic Texture Propagation](https://arxiv.org/abs/2310.13119), Yang et al., arxiv 2023 | [github](https://github.com/ybbbbt/dreamspace) | [bibtext](./citations/dreamspace.txt) 
- [3DStyle-Diffusion: Pursuing Fine-grained Text-driven 3D Stylization with 2D Diffusion Models](https://arxiv.org/abs/2311.05464), Yang et al., ACM Multimedia 2023 | [github](https://github.com/yanghb22-fdu/3DStyle-Diffusion-Official) | [bibtex](./citations/3dstylediffusion.txt)
- [Text-Guided Texturing by Synchronized Multi-View Diffusion](https://arxiv.org/abs/2311.12891), Liu et al., arxiv 2023 | [bibtex](./citations/textsync.txt)
- [SceneTex: High-Quality Texture Synthesis for Indoor Scenes via Diffusion Priors](https://arxiv.org/abs/2311.17261), Chen et al., arxiv 2023 | [github](https://github.com/daveredrum/SceneTex) | [bibtext](./citations/scenetex.txt) 
- [TeMO: Towards Text-Driven 3D Stylization for Multi-Object Meshes](https://arxiv.org/abs/2312.04248), Zhang et al., arxiv 2023 | [bibtex](./citations/temo.txt)
- [Single Mesh Diffusion Models with Field Latents for Texture Generation](https://arxiv.org/abs/2312.09250), Mitchel et al., arxiv 2023 | [bibtex](./citations/smd.txt)
- [Paint-it: Text-to-Texture Synthesis via Deep Convolutional Texture Map Optimization and Physically-Based Rendering](https://arxiv.org/abs/2312.11360), Youwang et al., arxiv 2023 | [github](https://github.com/postech-ami/paint-it) | [bibtext](./citations/paint-it.txt) 
- [Paint3D: Paint Anything 3D with Lighting-Less Texture Diffusion Models](https://arxiv.org/abs/2312.13913), Zeng et al., arxiv 2023 | [github](https://github.com/OpenTexture/Paint3D) | [bibtext](./citations/paint3d.txt) 
- [TextureDreamer: Image-guided Texture Synthesis through Geometry-aware Diffusion](https://arxiv.org/abs/2401.09416), Yeh et al., arxiv 2024 | [bibtext](./citations/texturedreamer.txt) 
- [FlashTex: Fast Relightable Mesh Texturing with LightControlNet](https://arxiv.org/abs/2402.13251), Deng et al., arxiv 2024 | [bibtext](./citations/flashtex.txt) 

</details>

<details open>
<summary>Procedural 3D Modeling</summary>

- [ProcTHOR: Large-Scale Embodied AI Using Procedural Generation](https://procthor.allenai.org/), Deitke et al., NeurIPS 2022 |  [github](https://github.com/allenai/procthor) | [bibtex](./citations/procthor.txt)
- [3D-GPT: Procedural 3D Modeling with Large Language Models](https://arxiv.org/abs/2310.12945), Sun et al., arxiv 2023 |  [github](https://github.com/Chuny1/3DGPT) | [bibtex](./citations/3dgpt.txt)

</details>


<details open>
<summary>3D Representation</summary>

- [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://arxiv.org/abs/2003.08934), Mildenhall et al., ECCV 2020 | [github](https://github.com/bmild/nerf) | [bibtex](./citations/nerf.txt)
- [Deep Marching Tetrahedra: a Hybrid Representation for High-Resolution 3D Shape Synthesis](https://arxiv.org/abs/2111.04276), Shen et al., arxiv 2021 | [bibtex](./citations/dmtet.txt)
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079), Kerbl et al., TOG 2023 | [github](https://github.com/graphdeco-inria/gaussian-splatting) | [bibtex](./citations/3dgaussian.txt)
- [Uni3D: Exploring Unified 3D Representation at Scale](https://arxiv.org/abs/2310.06773), Zhou et al., ICLR 2024 | [github](https://github.com/baaivision/Uni3D) | [bibtex](./citations/uni3d.txt)
- [SMERF: Streamable Memory Efficient Radiance Fields for Real-Time Large-Scene](https://arxiv.org/abs/2312.07541), Duckworth et al., arxiv 2023 | [bibtex](./citations/smerf.txt)
- [Triplane Meets Gaussian Splatting:Fast and Generalizable Single-View 3D Reconstruction with Transformers](https://arxiv.org/abs/2312.09147), Zou et al., arxiv 2023 | [bibtex](./citations/tmgs.txt)
- [SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes](https://arxiv.org/abs/2312.14937), Huang et al., arxiv 2023 | [github](https://github.com/yihua7/SC-GS) | [bibtex](./citations/scgs.txt)
- [DMesh: A Differentiable Representation for General Meshes](https://arxiv.org/abs/2404.13445), Son et al., arxiv 2024 | [github](https://github.com/SonSang/dmesh) | [bibtex](./citations/dmesh.txt)

</details>

</details>


## Benchmarks and Datasets

- [Objaverse-XL](https://objaverse.allenai.org/), Deitke et al., NeurIPS 2023 | [github](https://github.com/allenai/objaverse-xl) | [bibtext](./citations/objaverse-xl.txt) 
- [G-buffer Objaverse: High-Quality Rendering Dataset of Objaverse](https://aigc3d.github.io/gobjaverse/), Xu et al.
- [GPT-4V(ision) is a Human-Aligned Evaluator for Text-to-3D Generation](https://arxiv.org/abs/2401.04092), Wu et al., arXiv 2024 | [github](https://github.com/3DTopia/GPTEval3D) | [bibtext](./citations/gpt4v.txt) 
- [SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding](https://arxiv.org/abs/2401.09340), Jia et al., arXiv 2024 | [bibtext](./citations/sceneverse.txt) 
- [Make-A-Shape: a Ten-Million-scale 3D Shape Model](https://arxiv.org/abs/2401.11067), Wu et al., arXiv 2024 | [bibtext](./citations/make-a-shape.txt) 


## Talks
- [AI 3D Generation, explained](https://www.youtube.com/watch?v=EoAm1yZR-ao), Jia-Bin Huang
- [3D Generation, bilibili](https://space.bilibili.com/23460054/channel/collectiondetail?sid=1860808&ctype=0), Leo
- [3D AIGC Algorithm Trends and Industry Implementation](https://app6ca5octe2206.pc.xiaoe-tech.com/p/t_pc/course_pc_detail/video/v_65810adbe4b04c10093fdacc), Ding Liang
- [3D Generation: Past, Present and Future](https://www.bilibili.com/video/BV1wT4y1879Y/?spm_id_from=333.999.0.0&vd_source=0fb3bb9416e8fa252211d77e6b01b9d0),GAMES Webinar 311


## Company
- [TRIPOAI](https://www.tripo3d.ai/)
- [LumaAI](https://lumalabs.ai/)
- [CSMAI](https://www.csm.ai/)
- [SUDOAI](https://www.sudo.ai/)
- [Meshy](https://www.meshy.ai/)
- [StabilityAI](https://stability.ai/)




## Implementations

- [Threestudio](https://github.com/threestudio-project/threestudio), Yuan-Chen Guo, 2023 | [bibtex](./citations/threestudio.txt)
- [stable-dreamfusion](https://github.com/ashawkey/stable-dreamfusion), Jiaxiang Tang, 2023 | [bibtex](./citations/stable-dreamfusion.txt)
- [Dream Textures](https://github.com/carson-katri/dream-textures), Carson Katri, 2023 
- [ComfyTextures](https://github.com/AlexanderDzhoganov/ComfyTextures), Alexander Dzhoganov, 2023  
- [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack), MrForExample, 2024
- [GauStudio](https://arxiv.org/abs/2403.19632), Ye et al., arxiv 2024 | [github](https://github.com/GAP-LAB-CUHK-SZ/gaustudio) | [bibtex](./citations/gaustudio.txt)


## License 
Awesome AIGC 3D is released under the [MIT license](./LICENSE).

## Citation
If you find this project useful in your research, please consider citing:
```BibTeX
@article{liu2024comprehensive,
  title={A Comprehensive Survey on 3D Content Generation},
  author={Liu, Jian and Huang, Xiaoshui and Huang, Tianyu and Chen, Lu and Hou, Yuenan and Tang, Shixiang and Liu, Ziwei and Ouyang, Wanli and Zuo, Wangmeng and Jiang, Junjun and others},
  journal={arXiv preprint arXiv:2402.01166},
  year={2024}
}
```

## Contact
contact: `hitcslj@stu.hit.edu.cn`.  
