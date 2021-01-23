We generated fifty different docked poses using FRED; these poses can be found here: [`50-poses`](50-poses).

Then, we performed RMSD (root mean squared deviation) clustering using [`rmsd.py`](rmsd.py) to choose the most dissimilar poses among the proposed fifty, within a cutoff of 2 Å.
Two docked poses were selected in this step: [`selected-poses`](selected-poses).
