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
- [Advances in 3D Generation: A Survey](https://export.arxiv.org/abs/2401.17807), Li et al., arxiv 2024 | [bibtex](./citations/advance-3dgeneration.txt)

## Papers




<details close>
<summary>Object</summary>

<details open>
<summary>high quality</summary>

- [DreamFields: Zero-Shot Text-Guided Object Generation with Dream Fields](https://ajayj.com/dreamfields), Jain et al., CVPR 2022 | [github](https://github.com/google-research/google-research/tree/master/dreamfields) | [bibtex](./citations/dreamfields.txt)
- [DreamFusion: Text-to-3D using 2D Diffusion](https://dreamfusion3d.github.io/), Poole et al., ICLR 2023 | [github](https://github.com/ashawkey/stable-dreamfusion) | [bibtex](./citations/dreamfusion.txt)
- [Score Jacobian Chaining: Lifting Pretrained 2D Diffusion Models for 3D Generation](https://pals.ttic.edu/p/score-jacobian-chaining), Wang et al., CVPR 2023 |[github](https://github.com/lukemelas/realfusion)| [bibtex](./citations/sjc.txt)
- [RealFusion: 360° Reconstruction of Any Object from a Single Image](https://lukemelas.github.io/realfusion/), Melas-Kyriazi et al., CVPR 2023 | [github](https://github.com/lukemelas/realfusion) | [bibtex](./citations/realfusion.txt)
- [3DFuse: Let 2D Diffusion Model Know 3D-Consistency for Robust Text-to-3D Generation](https://ku-cvlab.github.io/3DFuse/), Seo et al., arxiv 2023 | [github](https://github.com/KU-CVLAB/3DFuse) | [bibtex](./citations/3dfuse.txt)
- [Dream3D: Zero-Shot Text-to-3D Synthesis Using 3D Shape Prior and Text-to-Image Diffusion Models](https://bluestyle97.github.io/dream3d/), Xu et al., CVPR 2023 | [bibtex](./citations/dream3d.txt)
- [Magic3D: High-Resolution Text-to-3D Content Creation](https://research.nvidia.com/labs/dir/magic3d/), Lin et al., CVPR 2023 | [bibtex](./citations/magic3d.txt)
- [Fantasia3D: Disentangling Geometry and Appearance for High-quality Text-to-3D Content Creation](https://fantasia3d.github.io/), Chen et al., ICCV 2023 | [github](https://github.com/Gorilla-Lab-SCUT/Fantasia3D) | [bibtex](./citations/fantasia3d.txt)
- [Make-It-3D: High-Fidelity 3D Creation from A Single Image with Diffusion Prior](https://make-it-3d.github.io/), Tang et al., ICCV 2023 | [github](https://github.com/junshutang/Make-It-3D) | [bibtex](./citations/makeit3d.txt)
- [HiFA: High-fidelity Text-to-3D with Advanced Diffusion Guidance](https://hifa-team.github.io/HiFA-site/), Zhu et al., arxiv 2023 | [github](https://github.com/HiFA-team/HiFA) | [bibtex](./citations/hifa.txt)
- [DreamCraft3D: Hierarchical 3D Generation with Bootstrapped Diffusion Prior](https://mrtornado24.github.io/DreamCraft3D/), Sun et al., arxiv 2023 | [github](https://github.com/deepseek-ai/DreamCraft3D) | [bibtex](./citations/dreamcraft3d.txt)
- [RichDreamer: A Generalizable Normal-Depth Diffusion Model for Detail Richness in Text-to-3D](https://lingtengqiu.github.io/RichDreamer/), Qiu et al., arxiv 2023 | [github](https://github.com/alibaba/RichDreamer) | [bibtex](./citations/richdreamer.txt)
- [X-Dreamer: Creating High-quality 3D Content by Bridging the Domain Gap Between Text-to-2D and Text-to-3D Generation](https://xmu-xiaoma666.github.io/Projects/X-Dreamer/), Ma et al., arxiv 2023 | [github](https://github.com/xmu-xiaoma666/X-Dreamer) | [bibtex](./citations/xdreamer.txt)
- [BiDiff: Text-to-3D Generation with Bidirectional Diffusion using both 2D and 3D priors](https://bidiff.github.io/), Ding et al., arxiv 2023 | [github](https://github.com/BiDiff/bidiff) | [bibtex](./citations/bidiff.txt)
- [UniDream: Unifying Diffusion Priors for Relightable Text-to-3D Generation](https://yg256li.github.io/UniDream/), Liu et al., arxiv 2023 | [github](https://yg256li.github.io/UniDream/) | [bibtex](./citations/unidream.txt)
- [Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior](https://arxiv.org/abs/2312.06655), Liu et al., arxiv 2023 | [github](https://github.com/liuff19/Sherpa3D) | [bibtex](./citations/sherpa3d.txt)
- [HexaGen3D: StableDiffusion is just one step away from
Fast and Diverse Text-to-3D Generation](https://arxiv.org/abs/2401.07727), Mercier et al., arxiv 2024 | [bibtex](./citations/HexaGen3D.txt)



</details>

<details open>
<summary>SDS understanding and improve</summary>


- [ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation with Variational Score Distillation](https://ml.cs.tsinghua.edu.cn/prolificdreamer/), Wang et al., NeurIPS 2023 | [github](https://github.com/thu-ml/prolificdreamer) | [bibtex](./citations/prolificdreamer.txt)
- [NFSD: Noise Free Score Distillation](https://orenkatzir.github.io/nfsd/), Katzir et al., arxiv 2023 | [github](https://github.com/orenkatzir/nfsd) | [bibtex](./citations/nfsd.txt)
- [LucidDreamer: Towards High-Fidelity Text-to-3D Generation via Interval Score Matching](https://arxiv.org/abs/2311.11284), Liang et al., arxiv 2023 | [github](https://github.com/EnVision-Research/LucidDreamer) | [bibtex](./citations/luciddreamer-object.txt)
- [Text-to-3D with Classifier Score Distillation](https://xinyu-andy.github.io/Classifier-Score-Distillation/), Yu et al., arxiv 2023 | [github](https://github.com/CVMI-Lab/Classifier-Score-Distillation) | [bibtex](./citations/csd.txt)
- [StableDreamer: Taming Noisy Score Distillation Sampling for Text-to-3D](https://arxiv.org/abs/2312.02189), Guo et al., arxiv 2023 | [bibtex](./citations/stabledreamer.txt)
- [CAD: Photorealistic 3D Generation via Adversarial Distillation](http://raywzy.com/CAD/), Wan et al., arxiv 2023 | [github](https://github.com/raywzy/CAD) | [bibtex](./citations/CAD.txt)
- [SSD: Stable Score Distillation for High-Quality 3D Generation](https://arxiv.org/abs/2312.09305), Tang et al., arxiv 2023 | [bibtex](./citations/ssd.txt)
- [SteinDreamer: Variance Reduction for Text-to-3D Score Distillation via Stein Identity](https://vita-group.github.io/SteinDreamer/), Wang et al., arxiv 2023 | [github](https://github.com/VITA-Group/SteinDreamer) | [bibtex](./citations/steindreamer.txt)
- [Taming Mode Collapse in Score Distillation for Text-to-3D Generation](https://vita-group.github.io/3D-Mode-Collapse/), Wang et al., arxiv 2024 | [github](https://github.com/VITA-Group/3D-Mode-Collapse) | [bibtex](./citations/3d-mode-collapse.txt)
- [Score Distillation Sampling with Learned Manifold Corrective](https://arxiv.org/abs/2401.05293), Alldieck et al., arxiv 2024 | [bibtex](./citations/sdslmc.txt)
- [Consistent3D: Towards Consistent High-Fidelity Text-to-3D Generation with Deterministic Sampling Prior](https://arxiv.org/abs/2401.09050), Wu et al., arxiv 2024 | [bibtex](./citations/consistent3d.txt)


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
- [Consistent123: One Image to Highly Consistent 3D Asset Using Case-Aware Diffusion Priors](https://arxiv.org/abs/2309.17261), Lin et al., arxiv 2024  | [bibtex](./citations/consistent123c.txt)
- [Zero123++: a Single Image to Consistent Multi-view Diffusion Base Model](https://arxiv.org/abs/2310.15110), Shi et al., arxiv 2023 | [github](https://github.com/SUDO-AI-3D/zero123plus) | [bibtex](./citations/zero123++.txt)
- [Wonder3D: Single Image to 3D using Cross-Domain Diffusion](https://www.xxlong.site/Wonder3D/), Long et al., arxiv 2023 | [github](https://github.com/xxlong0/Wonder3D) | [bibtex](./citations/wonder3d.txt)
- [SweetDreamer: Aligning Geometric Priors in 2D Diffusion for Consistent Text-to-3D](https://sweetdreamer3d.github.io/), Li et al., arxiv 2023 | [github](https://github.com/wyysf-98/SweetDreamer) | [bibtex](./citations/sweetdreamer.txt)
- [One-2-3-45++: Fast Single Image to 3D Objects with Consistent Multi-View Generation and 3D Diffusion](https://sudo-ai-3d.github.io/One2345plus_page/), Liu et al., arxiv 2023 | [github](https://github.com/SUDO-AI-3D/One2345plus) | [bibtex](./citations/one2345++.txt)
- [TOSS: High-quality Text-guided Novel View Synthesis from a Single Image](https://toss3d.github.io/), Shi et al., arxiv 2023 | [bibtex](./citations/toss.txt)
- [Direct2.5: Diverse Text-to-3D Generation via Multi-view 2.5D Diffusion](https://nju-3dv.github.io/projects/direct25/), Lu et al., arxiv 2023 | [bibtex](./citations/direct25.txt)
- [GeoDream:Disentangling 2D and Geometric Priors for High-Fidelity and Consistent 3D Generation](https://mabaorui.github.io/GeoDream_page/), Ma et al., arxiv 2023 | [github](https://github.com/baaivision/GeoDream/) | [bibtex](./citations/geodream.txt)
- [DreamComposer: Controllable 3D Object Generation via Multi-View Conditions](https://yhyang-myron.github.io/DreamComposer/), Yang et al., arxiv 2023 | [github](https://github.com/yhyang-myron/DreamComposer) | [bibtex](./citations/dreamcomposer.txt)
- [Cascade-Zero123: One Image to Highly Consistent 3D with Self-Prompted Nearby Views](https://cascadezero123.github.io/), Chen et al., arxiv 2023 | [github](https://github.com/AbrahamYabo/Cascade-Zero123) | [bibtex](./citations/cascadeZero123.txt)
- [Free3D: Consistent Novel View Synthesis without 3D Representation](https://chuanxiaz.com/free3d/), Zheng et al., arxiv 2023 | [github](https://github.com/lyndonzheng/Free3D) | [bibtex](./citations/free3d.txt)
- [Repaint123: Fast and High-quality One Image to 3D Generation with Progressive Controllable 2D Repainting](https://junwuzhang19.github.io/repaint123/), Zhang et al., arxiv 2023 | [github](https://github.com/junwuzhang19/repaint123) | [bibtex](./citations/repaint123.txt)
- [Splatter Image: Ultra-Fast Single-View 3D Reconstruction](https://szymanowiczs.github.io/splatter-image), Szymanowicz et al., arxiv 2023 | [github](https://github.com/szymanowiczs/splatter-image) | [bibtex](./citations/splatter-image.txt)
- [Carve3D: Improving Multi-view Reconstruction Consistency for Diffusion Models with RL Finetuning](https://desaixie.github.io/carve-3d/), Xie et al., arxiv 2023 | [bibtex](./citations/carve3d.txt)
- [HarmonyView: Harmonizing Consistency and Diversity in One-Image-to-3D](https://byeongjun-park.github.io/HarmonyView/), Woo et al., arxiv 2023 | [github](https://github.com/byeongjun-park/HarmonyView) | [bibtex](./citations/harmonyView.txt)
- [ImageDream: Image-Prompt Multi-view Diffusion for 3D Generation](https://image-dream.github.io/), Wang et al., arxiv 2023 | [github](https://github.com/bytedance/ImageDream) | [bibtex](./citations/imageDream.txt)
- [iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views](https://chinhsuanwu.github.io/ifusion/), Wu et al., arxiv 2023 | [github](https://github.com/chinhsuanwu/ifusion) | [bibtex](./citations/ifusion.txt)
- [AGG: Amortized Generative 3D Gaussians for Single Image to 3D](https://arxiv.org/abs/2401.04099), Xu et al., arxiv 2024 | [bibtex](./citations/agg.txt)

</details>

<details open>
<summary>faster</summary>

- [DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation](https://dreamgaussian.github.io/), Tang et al., arxiv 2023 | [github](https://github.com/dreamgaussian/dreamgaussian) | [bibtex](./citations/dreamguassian.txt)
- [Gsgen: Text-to-3D using Gaussian Splatting](https://gsgen3d.github.io/), Chen et al., arxiv 2023 | [github](https://github.com/gsgen3d/gsgen) | [bibtex](./citations/gsgen.txt)
- [LRM: Large Reconstruction Model for Single Image to 3D](https://yiconghong.me/LRM/), Hong et al., arxiv 2023 | [bibtex](./citations/lrm.txt)
- [Instant3D: Fast Text-to-3D with Sparse-View Generation and Large Reconstruction Model](https://jiahao.ai/instant3d/), Li et al., arxiv 2023 | [bibtex](./citations/instant3d.txt) 
- [DMV3D:Denoising Multi-View Diffusion using 3D Large Reconstruction Model](https://justimyhxu.github.io/projects/dmv3d/), Xu et al., arxiv 2023 | [bibtex](./citations/dmv3d.txt) 
- [Instant3D : Instant Text-to-3D Generation](https://ming1993li.github.io/Instant3DProj/), Li et al., arxiv 2023 | [bibtex](./citations/instant3d_.txt) 
- [HyperFields:Towards Zero-Shot Generation of NeRFs from Text](https://threedle.github.io/hyperfields/), Babu et al., arxiv 2023 | [github](https://github.com/threedle/hyperfields) | [bibtex](./citations/hyperfields.txt)
- [GaussianDreamer: Fast Generation from Text to 3D Gaussians by Bridging 2D and 3D Diffusion Models](https://taoranyi.com/gaussiandreamer/), Yi et al., arxiv 2023 | [github](https://github.com/hustvl/GaussianDreamer) | [bibtex](./citations/gaussianDreamer.txt)
- [CG3D: Compositional Generation for Text-to-3D via Gaussian Splatting](https://asvilesov.github.io/CG3D/), Vilesov et al., arxiv 2023 | [bibtex](./citations/gc3d.txt)
- [ZeroRF: Fast Sparse View 360° Reconstruction with Zero Pretraining](https://sarahweiii.github.io/zerorf/), Shi et al., arxiv 2023 | [github](https://github.com/eliphatfs/zerorf)  | [bibtex](./citations/zeroRF.txt) 

</details>



<details open>
<summary>editing</summary>

- [DreamBooth3D: Subject-Driven Text-to-3D Generation](https://dreambooth3d.github.io/), Raj et al., ICCV 2023 | [bibtex](./citations/dreambooth3d.txt)
- [TECA: Text-Guided Generation and Editing of Compositional 3D Avatars](https://yfeng95.github.io/teca/), Zhang et al., arxiv 2023 |  [github](https://github.com/HaoZhang990127/TECA) | [bibtex](./citations/teca.txt)
- [Control4D: Dynamic Portrait Editing by Learning 4D GAN from 2D Diffusion-based Editor](https://control4darxiv.github.io/), Shao et al., arxiv 2023 | [bibtex](./citations/control4d.txt)
- [Progressive3D: Progressively Local Editing for Text-to-3D Content Creation with Complex Semantic Prompts](https://cxh0519.github.io/projects/Progressive3D/), Cheng et al., arxiv 2023 |  [github](https://github.com/cxh0519/Progressive3D) | [bibtex](./citations/progressive3d.txt)
- [GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting](https://buaacyw.github.io/gaussian-editor/), Chen et al., arxiv 2023 |  [github](https://github.com/buaacyw/GaussianEditor) | [bibtex](./citations/gaussianeditor.txt)
- [GaussianEditor: Editing 3D Gaussians Delicately with Text Instructions](https://gaussianeditor.github.io/), Fang et al., arxiv 2023 | [bibtex](./citations/gaussianEditor2.txt)
- [Gaussian Grouping: Segment and Edit Anything in 3D Scenes](https://arxiv.org/abs/2312.00732), Ye et al., arxiv 2023 |  [github](https://github.com/lkeab/gaussian-grouping) | [bibtex](./citations/gaussian-group.txt)
- [AGAP:Learning Naturally Aggregated Appearance for Efficient 3D Editing](https://felixcheng97.github.io/AGAP/), Cheng et al., arxiv 2023 |  [github](https://github.com/WU-CVGL/MVControl) | [bibtex](./citations/mvcontrol.txt)
- [SIGNeRF: Scene Integrated Generation for Neural Radiance Fields](https://signerf.jdihlmann.com/), Dihlmann et al., arxiv 2023 |  [github](https://github.com/cgtuebingen/SIGNeRF) | [bibtex](./citations/sigNerf.txt)
- [TIP-Editor: An Accurate 3D Editor Following Both Text-Prompts And Image-Prompts](https://arxiv.org/abs/2401.14828), Zhuang et al., arxiv 2024 | [bibtex](./citations/tipEditor.txt)

</details>

<details open>
<summary>conditional control</summary>

- [Control3D: Towards Controllable Text-to-3D Generation](https://arxiv.org/abs/2311.05461), Chen et al., ACM Multimedia 2023 | [bibtex](./citations/control3d.txt)
- [IPDreamer: Appearance-Controllable 3D Object Generation with Image Prompts](https://arxiv.org/abs/2310.05375), Zeng et al., arxiv 2023 | [bibtex](./citations/ipdreamer.txt)
- [ControlDreamer: Stylized 3D Generation with Multi-View ControlNet](https://controldreamer.github.io/), Oh et al., arxiv 2023 |  [github](https://github.com/oyt9306/ControlDreamer) | [bibtex](./citations/controldreamer.txt)
- [DreamControl: Control-Based Text-to-3D Generation with 3D Self-Prior](https://arxiv.org/abs/2312.06439), Huang et al., arxiv 2023 |  [github](https://github.com/tyhuang0428/DreamControl) | [bibtex](./citations/dreamcontrol.txt)
- [MVControl: Adding Conditional Control to Multi-view Diffusion for Controllable Text-to-3D Generation](https://lizhiqi49.github.io/MVControl/), Li et al., arxiv 2023 |  [github](https://github.com/tyhuang0428/DreamControl) | [bibtex](./citations/dreamcontrol.txt)
- [Sketch2NeRF: Multi-view Sketch-guided Text-to-3D Generation](https://arxiv.org/abs/2401.14257), Chen et al., arxiv 2024 | [bibtex](./citations/Sketch2NeRF.txt)

</details>

</details>





<details close>
<summary>Scene</summary>

- [ATISS: Autoregressive Transformers for Indoor Scene Synthesis](https://arxiv.org/abs/2110.03675), Paschalidou et al., NeurIPS 2021 | [github](https://github.com/nv-tlabs/atiss) | [bibtext](./citations/atiss.txt) 
- [DiffuScene: Scene Graph Denoising Diffusion Probabilistic Model for Generative Indoor Scene Synthesis](https://arxiv.org/abs/2303.14207), Tang et al., arxiv 2023 | [github](https://github.com/tangjiapeng/DiffuScene) | [bibtext](./citations/diffuscene.txt) 
- [Text2Light: Zero-Shot Text-Driven HDR Panorama Generation](https://frozenburning.github.io/projects/text2light/), Chen et al., TOG 2022 | [github](https://github.com/FrozenBurning/Text2Light) | [bibtext](./citations/text2light.txt) 
- [SceneScape: Text-Driven Consistent Scene Generation](https://scenescape.github.io/), Fridman et al., arxiv 2023 | [github](https://github.com/RafailFridman/SceneScape) | [bibtext](./citations/scenescape.txt) 
- [Text2Room: Extracting Textured 3D Meshes from 2D Text-to-Image Models](https://lukashoel.github.io/text-to-room/), Höllein et al., ICCV 2023 | [github](https://github.com/lukasHoel/text2room) | [bibtext](./citations/text2room.txt) 
- [Text2NeRF: Text-Driven 3D Scene Generation with Neural Radiance Fields](https://eckertzhang.github.io/Text2NeRF.github.io/), Zhang et al., arxiv 2023 | [github](https://github.com/eckertzhang/Text2NeRF) | [bibtext](./citations/text2nerf.txt) 
- [Ctrl-Room: Controllable Text-to-3D Room Meshes Generation with Layout Constraints](https://fangchuan.github.io/ctrl-room.github.io/), Fang et al., arxiv 2023 | [github](https://github.com/fangchuan/Ctrl-Room) | [bibtext](./citations/ctrlroom.txt) 
- [ZeroNVS: Zero-Shot 360-Degree View Synthesis from a Single Real Image](https://kylesargent.github.io/zeronvs/), Sargent et al., arxiv 2023 | [github](https://github.com/kylesargent/zeronvs) | [bibtext](./citations/zeroNVS.txt) 
- [LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes](https://luciddreamer-cvlab.github.io/), Chuang et al., arxiv 2023 | [github](https://github.com/luciddreamer-cvlab/LucidDreamer)  | [bibtext](./citations/luciddreamer-scene.txt)
- [Pyramid Diffusion for Fine 3D Large Scene Generation](https://yuheng.ink/project-page/pyramid-discrete-diffusion/), Liu et al., arxiv 2023 | [github](https://yuheng.ink/project-page/pyramid-discrete-diffusion/) | [bibtext](./citations/pyramid.txt) 
- [GraphDreamer: Compositional 3D Scene Synthesis from Scene Graphs](https://graphdreamer.github.io/), Gao et al., arxiv 2023 | [github](https://github.com/GGGHSL/GraphDreamer) | [bibtext](./citations/graphdreamer.txt)
- [RoomDesigner: Encoding Anchor-latents for Style-consistent and Shape-compatible Indoor Scene Generation](https://arxiv.org/abs/2310.10027), Zhao et al., 3DV 2024 | [github](https://github.com/zhao-yiqun/RoomDesigner) | [bibtext](./citations/roomdesigner.txt)
- [ControlRoom3D:Room Generation using Semantic Proxy Rooms](https://jonasschult.github.io/ControlRoom3D/), Schult et al., arxiv 2023 | [bibtext](./citations/controlroom3d.txt)
- [AnyHome: Open-Vocabulary Generation of Structured and Textured 3D Homes](https://arxiv.org/abs/2312.06644), Wen et al., arxiv 2023 | [bibtext](./citations/anyhome.txt)
- [Inpaint3D: 3D Scene Content Generation using 2D Inpainting Diffusion](https://inpaint3d.github.io/), Prabhu et al., arxiv 2023 | [bibtext](./citations/inpaint3d.txt)
- [SceneWiz3D: Towards Text-guided 3D Scene Composition](https://zqh0253.github.io/SceneWiz3D/), Zhang et al., arxiv 2023 | [github](https://github.com/zqh0253/SceneWiz3D) | [bibtext](./citations/scenewiz3d.txt)
- [Text2Immersion: Generative Immersive Scene with 3D Gaussians](https://arxiv.org/abs/2312.09242), Ouyang et al., arxiv 2023 | [bibtext](./citations/text2immersion.txt)
- [ShowRoom3D: Text to High-Quality 3D Room Generation Using 3D Priors](https://showroom3d.github.io/), Mao et al., arxiv 2023 | [github](https://github.com/showlab/ShowRoom3D) | [bibtext](./citations/showRoom3d.txt)
<!-- - [FMGS: Foundation Model Embedded 3D Gaussian Splatting for Holistic 3D Scene Understanding](https://arxiv.org/abs/2401.01970), Zuo et al., arxiv 2024 | [bibtext](./citations/fmgs.txt) -->


<details close>
<summary>Procedural 3D Modeling</summary>

- [ProcTHOR: Large-Scale Embodied AI Using Procedural Generation](https://procthor.allenai.org/), Deitke et al., NeurIPS 2022 |  [github](https://github.com/allenai/procthor) | [bibtex](./citations/procthor.txt)
- [3D-GPT: Procedural 3D Modeling with Large Language Models](https://arxiv.org/abs/2310.12945), Sun et al., arxiv 2023 |  [github](https://github.com/Chuny1/3DGPT) | [bibtex](./citations/3dgpt.txt)

</details>

</details>

<details close>
<summary>Human</summary>

- [Rodin: A Generative Model for Sculpting 3D Digital Avatars Using Diffusion](https://arxiv.org/abs/2212.06135), Wang et al., CVPR 2023 | [bibtex](./citations/rodin.txt)
- [HumanNorm: Learning Normal Diffusion Model for High-quality and Realistic 3D Human Generation](https://humannorm.github.io/), Huang et al., arxiv 2023 |  [github](https://github.com/xhuangcv/humannorm) | [bibtex](./citations/humannorm.txt)
- [HeadArtist: Text-conditioned 3D Head Generation with Self Score Distillation](https://kumapowerliu.github.io/HeadArtist/), Liu et al., arxiv 2023 | [bibtex](./citations/headArtist.txt)
- [3DGS-Avatar: Animatable Avatars via Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2312.09228), Qian et al., arxiv 2023 |  [github](https://github.com/mikeqzy/3dgs-avatar-release) | [bibtex](./citations/3dgsAvatar.txt)

</details>


<details close>
<summary>Dynamic</summary>

- [TADA! Text to Animatable Digital Avatars](https://tada.is.tue.mpg.de/), Liao et al., 3DV 2024 | [github](https://github.com/TingtingLiao/TADA) | [bibtext](./citations/tada.txt) 
- [MAV3d: Text-To-4D Dynamic Scene Generation](https://make-a-video3d.github.io/), Singer et al., arxiv 2023 | [bibtext](./citations/mav3d.txt) 
- [Animate124: Animating One Image to 4D Dynamic Scene](https://animate124.github.io/), Zhao et al., arxiv 2023 | [github](https://github.com/HeliosZhao/Animate124) | [bibtext](./citations/animate124.txt) 
- [Consistent4D: Consistent 360° Dynamic Object Generation from Monocular Video](https://consistent4d.github.io/), Jiang et al., arxiv 2023 | [github](https://github.com/yanqinJiang/Consistent4D) | [bibtext](./citations/consistent4d.txt) 
- [4D-fy: Text-to-4D Generation Using Hybrid Score Distillation Sampling](https://sherwinbahmani.github.io/4dfy/), Bahmani et al., arxiv 2023 | [github](https://github.com/sherwinbahmani/4dfy) | [bibtext](./citations/4dfy.txt) 
- [MAS: Multi-view Ancestral Sampling for 3D motion generation using 2D diffusion](https://guytevet.github.io/mas-page/), Kapon et al., arxiv 2023 | [github](https://github.com/roykapon/MAS) | [bibtext](./citations/mas.txt) 
- [AnimatableDreamer: Text-Guided Non-rigid 3D Model Generation and Reconstruction with Canonical Score Distillation](https://web1.arxiv.org/abs/2312.03795), Wang et al., arxiv 2023 | [bibtext](./citations/animatable-dreamer.txt) 
- [Virtual Pets: Animatable Animal Generation in 3D Scenes](https://yccyenchicheng.github.io/VirtualPets/), Cheng et al., arxiv 2023 | [github](https://github.com/yccyenchicheng/VirtualPets) | [bibtext](./citations/virtual-pets.txt) 
- [Dream-in-4D: A Unified Approach for Text- and Image-guided 4D Scene Generation](https://research.nvidia.com/labs/nxp/dream-in-4d/), Zheng et al., arxiv 2023 | [bibtext](./citations/dream-in-4d.txt) 
- [Align Your Gaussians:Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models](https://research.nvidia.com/labs/toronto-ai/AlignYourGaussians/), Ling et al., arxiv 2023 [bibtext](./citations/aligngaussian.txt) 
- [Ponymation: Learning 3D Animal Motions from Unlabeled Online Videos](https://keqiangsun.github.io/projects/ponymation/), Sun et al., arxiv 2023 | [bibtext](./citations/ponyMation.txt) 
- [4DGen: Grounded 4D Content Generation with Spatial-temporal Consistency](https://vita-group.github.io/4DGen/), Yin et al., arxiv 2023 | [github](https://github.com/VITA-Group/4DGen) | [bibtext](./citations/4dgen.txt) 
- [DreamGaussian4D: Generative 4D Gaussian Splatting](https://jiawei-ren.github.io/projects/dreamgaussian4d/), Ren et al., arxiv 2023 | [github](https://github.com/jiawei-ren/dreamgaussian4d) | [bibtext](./citations/dreamgaussian4d.txt) 
- [Fast Dynamic 3D Object Generation from a Single-view Video](https://arxiv.org/abs/2401.08742), Pan et al., arxiv 2024 | [github](https://github.com/fudan-zvg/Efficient4D) | [bibtext](./citations/efficient4d.txt)


</details>



<details close>
<summary>3D Representation</summary>

- [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://www.matthewtancik.com/nerf), Mildenhall et al., ECCV 2020 | [github](https://github.com/bmild/nerf) | [bibtex](./citations/nerf.txt)
- [Deep Marching Tetrahedra: a Hybrid Representation for High-Resolution 3D Shape Synthesis](https://arxiv.org/abs/2111.04276), Shen et al., arxiv 2021 | [bibtex](./citations/dmtet.txt)
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/), Kerbl et al., TOG 2023 | [github](https://github.com/graphdeco-inria/gaussian-splatting) | [bibtex](./citations/3dgaussian.txt)
- [Uni3D: Exploring Unified 3D Representation at Scale](https://arxiv.org/abs/2310.06773), Zhou et al., arxiv 2023 | [github](https://github.com/baaivision/Uni3D) | [bibtex](./citations/uni3d.txt)
- [SMERF: Streamable Memory Efficient Radiance Fields for Real-Time Large-Scene](https://smerf-3d.github.io/), Duckworth et al., arxiv 2023 | [bibtex](./citations/smerf.txt)
- [Triplane Meets Gaussian Splatting:Fast and Generalizable Single-View 3D Reconstruction with Transformers](https://zouzx.github.io/TriplaneGaussian/), Zou et al., arxiv 2023 | [bibtex](./citations/tmgs.txt)
- [SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes](https://yihua7.github.io/SC-GS-web/), Huang et al., arxiv 2023 | [github](https://github.com/yihua7/SC-GS) | [bibtex](./citations/scgs.txt)
</details>

<details close>
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
- [WildFusion:Learning 3D-Aware Latent Diffusion Models in View Space](https://katjaschwarz.github.io/wildfusion/), Schwarz et al., arxiv 2023 | [bibtex](./citations/wildfusion.txt)
- [MeshGPT: Generating Triangle Meshes with Decoder-Only Transformers](https://nihalsid.github.io/mesh-gpt/), Siddiqui et al., arxiv 2023 | [github](https://github.com/nihalsid/mesh-gpt) | [bibtex](./citations/meshgpt.txt)
- [SPiC·E: Structural Priors in 3D Diffusion Models using Cross-Entity Attention](https://tau-vailab.github.io/spic-e/), Sella et al., arxiv 2023 | [github](https://github.com/TAU-VAILab/spic-e) | [bibtex](./citations/spice.txt)
- [X3: Large-Scale 3D Generative Modeling using Sparse Voxel Hierarchies](https://research.nvidia.com/labs/toronto-ai/xcube/), Ren et al., arxiv 2023 | [bibtex](./citations/xcube.txt)
- [MagicPony: Learning Articulated 3D Animals in the Wild](https://3dmagicpony.github.io/), Wu et al., CVPR 2023 | [github](https://github.com/elliottwu/MagicPony) | [bibtex](./citations/magicpony.txt)
- [Learning the 3D Fauna of the Web](https://kyleleey.github.io/3DFauna/), Li et al., arxiv 2024 | [bibtex](./citations/3dfauna.txt)
- [CityDreamer: Compositional Generative Model of Unbounded 3D Cities](https://arxiv.org/abs/2309.00610), Xie et al., arxiv 2023 | [github](https://github.com/hzxie/city-dreamer) | [bibtext](./citations/cityDreamer.txt)

</details>

<details close>
<summary>Material</summary>

- [Generating Parametric BRDFs from Natural Language Descriptions](https://arxiv.org/abs/2306.15679), Memery et al., arxiv 2023  [bibtex](./citations/BRDF.txt)
- [MATLABER: Material-Aware Text-to-3D via LAtent BRDF auto-EncodeR](https://sheldontsui.github.io/projects/Matlaber), Xu et al., arxiv 2023 | [github](https://github.com/SheldonTsui/Matlaber) | [bibtex](./citations/matlaber.txt)

</details>



<details close>
<summary>Texture</summary>

- [StyleMesh: Style Transfer for Indoor 3D Scene Reconstructions](https://lukashoel.github.io/stylemesh/), Höllein et al., CVPR 2022 | [github](https://github.com/lukasHoel/stylemesh) | [bibtex](./citations/stylemesh.txt)
- [TANGO: Text-driven PhotoreAlistic aNd Robust 3D Stylization via LiGhting DecompOsition](https://cyw-3d.github.io/tango/), Chen et al., NeurIPS 2022 | [github](https://github.com/Gorilla-Lab-SCUT/tango) | [bibtex](./citations/tango.txt)
- [CLIP-Mesh: Generating textured meshes from text using pretrained image-text models](https://www.nasir.lol/clipmesh), Khalid et al., SIGGRAPH Asia 2022 | [github](https://github.com/NasirKhalid24/CLIP-Mesh) | [bibtex](./citations/clipmesh.txt)
- [Latent-NeRF for Shape-Guided Generation of 3D Shapes and Textures](https://arxiv.org/abs/2211.07600), Metzer et al., CVPR 2023 | [github](https://github.com/eladrich/latent-nerf) | [bibtex](./citations/latentNerf.txt)
- [TEXTure: Text-Guided Texturing of 3D Shapes](https://texturepaper.github.io/TEXTurePaper/), Richardson et al., SIGGRAPH 2023 | [github](https://github.com/TEXTurePaper/TEXTurePaper) | [bibtex](./citations/texture.txt)
- [Text2Tex: Text-driven Texture Synthesis via Diffusion Models](https://daveredrum.github.io/Text2Tex/), Chen et al., ICCV 2023 | [github](https://github.com/daveredrum/Text2Tex) | [bibtex](./citations/text2tex.txt)
- [TexFusion: Synthesizing 3D Textures with Text-Guided Image Diffusion Models](https://research.nvidia.com/labs/toronto-ai/texfusion/), Cao et al., ICCV 2023 | [bibtex](./citations/texfusion.txt)
- [MVDiffusion: Enabling Holistic Multi-view Image Generation with Correspondence-Aware Diffusion](https://mvdiffusion.github.io/), Tang et al., NeurIPS 2023 | [github](https://github.com/Tangshitao/MVDiffusion) | [bibtext](./citations/mvdiffusion.txt) 
- [RoomDreamer: Text-Driven 3D Indoor Scene Synthesis with Coherent Geometry and Texture](https://arxiv.org/abs/2305.11337), Song et al., ACM Multimedia 2023 | [bibtex](./citations/roomdreamer.txt)
- [3DStyle-Diffusion: Pursuing Fine-grained Text-driven 3D Stylization with 2D Diffusion Models](https://arxiv.org/abs/2311.05464), Yang et al., ACM Multimedia 2023 | [github](https://github.com/yanghb22-fdu/3DStyle-Diffusion-Official) | [bibtex](./citations/3dstylediffusion.txt)
- [ITEM3D: Illumination-Aware Directional Texture Editing for 3D Models](https://shengqiliu1.github.io/ITEM3D/), Liu et al., arxiv 2023 | [github](https://github.com/shengqiliu1/ITEM3D) | [bibtex](./citations/item3d.txt)
- [DreamSpace: Dreaming Your Room Space with Text-Driven Panoramic Texture Propagation](https://ybbbbt.com/publication/dreamspace/), Yang et al., arxiv 2023 | [github](https://github.com/ybbbbt/dreamspace) | [bibtext](./citations/dreamspace.txt) 
- [Text-Guided Texturing by Synchronized Multi-View Diffusion](https://arxiv.org/abs/2311.12891), Liu et al., arxiv 2023 | [bibtex](./citations/textsync.txt)
- [SceneTex: High-Quality Texture Synthesis for Indoor Scenes via Diffusion Priors](https://daveredrum.github.io/SceneTex/), Chen et al., arxiv 2023 | [github](https://github.com/daveredrum/SceneTex) | [bibtext](./citations/scenetex.txt) 
- [TeMO: Towards Text-Driven 3D Stylization for Multi-Object Meshes](https://arxiv.org/abs/2312.04248), Zhang et al., arxiv 2023 | [bibtex](./citations/temo.txt)
- [Single Mesh Diffusion Models with Field Latents for Texture Generation](https://arxiv.org/abs/2312.09250), Mitchel et al., arxiv 2023 | [bibtex](./citations/smd.txt)
- [Paint-it: Text-to-Texture Synthesis via Deep Convolutional Texture Map Optimization and Physically-Based Rendering](https://kim-youwang.github.io/paint-it), Youwang et al., arxiv 2023 | [github](https://github.com/postech-ami/paint-it) | [bibtext](./citations/paint-it.txt) 
- [Paint3D: Paint Anything 3D with Lighting-Less Texture Diffusion Models](https://arxiv.org/abs/2312.13913), Zeng et al., arxiv 2023 | [github](https://github.com/OpenTexture/Paint3D) | [bibtext](./citations/paint3d.txt) 

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




## Implementations

- [Threestudio](https://github.com/threestudio-project/threestudio), Yuan-Chen Guo, 2023 | [bibtex](./citations/threestudio.txt)
- [stable-dreamfusion](https://github.com/ashawkey/stable-dreamfusion), Jiaxiang Tang, 2023 | [bibtex](./citations/stable-dreamfusion.txt)
- [Dream Textures](https://github.com/carson-katri/dream-textures), Carson Katri, 2023 

## License 
Awesome AIGC 3D is released under the [MIT license](./LICENSE).

## Contact
contact: `hitcslj@stu.hit.edu.cn`.  
