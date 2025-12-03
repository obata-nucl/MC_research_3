# IBM Hamiltonian Parameter Predictor with NPBOS Emulator

## 概要 (Overview)
本プロジェクトは、原子核物理学における相互作用するボソン模型 (**Interacting boson model : IBM**) のハミルトニアンのパラメータを推定するための研究用コードです。

ここでは、**Hartree-Fock-Bogoliubov (HFB)** 法などで計算された **Potential Energy Surface (PES)** と、各原子核のスペクトルから最適なIBMパラメータを逆推定しています。実験値のスペクトルを学習させる際、**IBM** の計算コードである **NPBOS** をエミュレートしたニューラルネットワーク(**NN**)を用いることで、学習を可能にしています。

## ディレクトリ構成

```
project3/
├ emulator/             # NPBOS Emulator
│   ├ data/
│   ├ outputs/
│   ├ src/
│   │   ├ dataset.py
│   │   ├ loss.py
│   │   ├ model.py
│   │   ├ utils.py
│   └ config.yaml
├ predictor/            # IBM params Predictor
│   ├ data/
│   ├ outputs/
│   ├ src/
│   │   ├ dataset.py
│   │   ├ loss.py
│   │   ├ model.py
│   │   ├ utils.py
│   └ config.yaml
├ config.yaml           # プロジェクト全体の設定ファイル
└ requirements.txt      # Python依存ライブラリ

```