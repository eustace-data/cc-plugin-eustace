#!/bin/bash

# get-checker-suite.sh
# ====================
#
# Downloads and installs full bundle for compliance checking and controlled
# vocabularies.
#
# Usage:
#
#     ./get-checker-suite.sh [--install|--update] <project_id>
#
# Where:
#
#     Either "--install" or "--update" - default is: "--install"
#     <project_id> can be one of: "eustace", "ukcp18"
#

action=$1
if [ ! $action ]; then
    action="--install"
fi

project_id=$2
INSTALL=

if [ $action == "--install" ]; then
    INSTALL=1
fi

USAGE="Usage: $0 --install|--update <project_id>"
if [ ! $project_id ]; then
    echo $USAGE
    exit
fi


# Define location of the git repositories
checker=https://github.com/agstephens/compliance-checker
checklib=https://github.com/cedadev/compliance-check-lib
checkmaker=https://github.com/cedadev/compliance-check-maker

if [ $project_id == "ukcp18" ]; then 
    writer=https://github.com/ukcp-data/pyessv-writer
    plugin=https://github.com/ukcp-data/cc-plugin-ukcp18
    cvs=https://github.com/ukcp-data/UKCP18_CVs
    cv_name=UKCP18_CVs
elif [ $project_id == "eustace" ]; then 
    writer=https://github.com/eustace-data/pyessv-writer
    plugin=https://github.com/eustace-data/cc-plugin-eustace
    cvs=https://github.com/eustace-data/EUSTACE_CVs
    cv_name=EUSTACE_CVs
else
    echo "ERROR: did not recognise <project_id> provided: $project_id"
    exit
fi

if [ $INSTALL ]; then
    virtualenv venv
fi

source venv/bin/activate

if [ $INSTALL ]; then
    pip install pyessv==0.3.5.1.0

    for pkg in $writer $plugin $checker $cvs $checklib $checkmaker; do
        git clone $pkg
    done
fi

if [ $INSTALL ]; then
    cd compliance-checker/
    pip install .
    cd ../
fi

cd ${cv_name}/
git pull

cd ../pyessv-writer/
mkdir  -p ~/.esdoc/pyessv-archive
python sh/write_${project_id}_cvs.py --source=../${cv_name}

cd ../cc-plugin-${project_id}
if [ ! $INSTALL ]; then
    git pull
fi

python setup.py develop

echo "Testing..."
export PYTHONPATH=$PYTHONPATH:../compliance-check-lib
compliance-checker --test ${project_id}-file-info --test ${project_id}-file-structure --test ${project_id}-global-attrs cc_plugin_${project_id}/tests/data/${project_id}/test_cdl_global_atts.nc

cd ../
echo "Creating setup_env.sh script"
script=setup_env.sh
echo "#!/bin/bash" > $script
echo "source venv/bin/activate" >> $script
echo "export PYTHONPATH=$PYTHONPATH:../compliance-check-lib" >> $script
echo "cd cc-plugin-${project_id}/" >> $script

echo "Set up your environment with:"
echo "source setup_env.sh"

echo "Then try running:"
echo "compliance-checker --test ${project_id}-file-info --test ${project_id}-file-structure --test ${project_id}-global-attrs cc_plugin_${project_id}/tests/data/${project_id}/test_cdl_global_atts.nc"
