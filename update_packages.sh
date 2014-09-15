#!/bin/sh

regular_packages=(anaconda bokeh accelerate iopro ipython statsmodels numpy scipy pandas matplotlib scikit-learn requests networkx beautiful-soup)
echo "[*] Updating regular packages..."
for package in ${regular_packages[@]}; do
	conda update --yes $package
done
echo "\n"

binstar_packages=(mrjob  pattern  seaborn)
echo "[*] Updating binstar packages..."
for package in ${binstar_packages[@]}; do
	conda update --yes -c https://conda.binstar.org/asmeurer $package
done
echo "\n"

echo "[**] Done!"
