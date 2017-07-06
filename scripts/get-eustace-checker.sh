#!/bin/bash

# Use with argument: --install or --update

arg=$1
INSTALL=

if [ ! $arg ]; then
    echo "Usage: $0 --install|--update"
    exit
fi

if [ $arg == "--install" ]; then
    INSTALL=1
fi

writer=https://github.com/eustace-data/pyessv-writer
plugin=https://github.com/eustace-data/cc-plugin-eustace
checker=https://github.com/agstephens/compliance-checker
cvs=https://github.com/eustace-data/EUSTACE_CVs
checklib=https://github.com/agstephens/check-maker

if [ $INSTALL ]; then
    virtualenv venv
fi

source venv/bin/activate

if [ $INSTALL ]; then
    pip install pyessv

    for pkg in $writer $plugin $checker $cvs $checklib; do
        git clone $pkg
    done
fi

if [ $INSTALL ]; then
    cd compliance-checker/
    pip install .
    cd ../
fi

cd EUSTACE_CVs/
git pull

cd ../pyessv-writer/
mkdir  -p ~/.esdoc/pyessv-archive
python sh/write_eustace_cvs.py --source=../EUSTACE_CVs

cd ../cc-plugin-eustace
if [ ! $INSTALL ]; then
    git pull
fi

pip install .

echo "Testing..."
export PYTHONPATH=$PYTHONPATH:../check-maker
compliance-checker --test eustace-core --test eustace-file-info cc_plugin_eustace/tests/data/eustace/mohc_ocean_day.nc

