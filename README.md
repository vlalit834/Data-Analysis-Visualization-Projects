# Data-Analysis-Visualization-Projects — Reorganized

This repository contains a set of small data analysis and visualization projects. The codebase has been reorganized into a professional structure under the `ques/` directory.

Directory layout

- `ques/`
  - `ques1/`
    - `main.py` (Exam Marks project)
    - `ques1.md`
  - `ques2/`
    - `main.py` (Netflix project)
    - `data/netflix.csv`
    - `ques2.md`
  - `ques3/`
    - `main.py` (Monthly Sales visualization)
    - `plots/` (contains generated PNGs after running)
    - `ques3.md`
  - `ques4/`
    - `main.py` (Penguin Seaborn visualizations)
    - `plots/` (contains generated PNGs after running)
    - `ques4.md`

How to run each project

- Ques 1 (Exam Marks):
  - `python ques/ques1/main.py`

- Ques 2 (Netflix Explorer):
  - `python ques/ques2/main.py` (reads `ques/ques2/data/netflix.csv`)

- Ques 3 (Monthly Sales Charts):
  - `python ques/ques3/main.py` (writes PNGs to `ques/ques3/plots/`)

- Ques 4 (Penguin Species Explorer):
  - `python ques/ques4/main.py` (writes PNGs to `ques/ques4/plots/` and updates `ques/ques4/ques4.md` image links)

Notes

- The original solution files are kept at the repository root for reference, but you should use the `main.py` files under `ques/` for the organized project structure.
- Make sure dependencies are installed (e.g., `numpy`, `pandas`, `matplotlib`, `seaborn`).

