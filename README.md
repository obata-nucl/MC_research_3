# IBM Hamiltonian Parameter Predictor with NPBOS Emulator

## 概要 (Overview)
本プロジェクトは、原子核物理学における相互作用するボソン模型 (**Interacting boson model : IBM**) のハミルトニアンのパラメータを推定するための研究用コードです。

ここでは、**Hartree-Fock-Bogoliubov (HFB)** 法などで計算された **Potential Energy Surface (PES)** と、各原子核のスペクトルから最適なIBMパラメータを逆推定しています。実験値のスペクトルを学習させる際、**IBM** の通常の数値計算コードである **NPBOS** を、微分可能なニューラルネットワーク (サロゲートモデル) で近似・置換することで、誤差逆伝播法を用いた実験値からの直接的なパラメータ最適化を可能にしています。

## ディレクトリ構成

```
project3/
├─ configs/
│   ├─ common.yaml
│   ├─ emulator.yaml
│   └─ predictor.yaml
├─ data/
│   ├─ emulator/
│   │   ├─ raw/
│   │   │   └ npbos_dataset.csv
│   │   ├─ processed/
│   └─ predictor/
│        ├─ spectra/
│        ├─ pes/
│        └─ processed/
├─ models/
├─ results/
│   ├─ training/
│   └─ inference/
├─ scripts/
│   ├─ train_emulator.py
│   ├─ train_predictor.py
├─ src/
│   ├─ __init__.py
│   ├─ emulator/
│   │   ├─ dataset.py           # ニューラルネットワークで学習させるデータセットを読み込む
│   │   ├─ generate_data.py     # NPBOSデータ生成スクリプト -> npbos_dataset.csv
│   │   ├─ model.py             # NNの定義
│   │   └─ trainer.py           # 学習
│   ├─ predictor/
│   │   ├─ dataset.py
│   │   ├─ model.py
│   │   └─ trainer.py
│   └─ utils.py
├─ NPBOS/
├─ .gitignore
├─ README.md
└─ requirements.txt             # python依存ライブラリ
```