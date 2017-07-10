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

writer=https://github.com/ukcp-data/pyessv-writer
plugin=https://github.com/ukcp-data/cc-plugin-ukcp18
checker=https://github.com/agstephens/compliance-checker
cvs=https://github.com/ukcp-data/UKCP18_CVs
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

cd UKCP18_CVs/
git pull

cd ../pyessv-writer/
mkdir  -p ~/.esdoc/pyessv-archive
python sh/write_ukcp18_cvs.py --source=../UKCP18_CVs

cd ../cc-plugin-ukcp18
if [ ! $INSTALL ]; then
    git pull
fi

python setup.py develop

echo "Testing..."
export PYTHONPATH=$PYTHONPATH:../check-maker
compliance-checker --test ukcp18-file-info --test ukcp18-file-structure --test ukcp18-global-attrs cc_plugin_ukcp18/tests/data/ukcp18/test_cdl_global_atts.nc

cd ../
echo "Creating setup_env.sh script"
script=setup_env.sh
echo "#!/bin/bash" > $script
echo "source venv/bin/activate" >> $script
echo "export PYTHONPATH=$PYTHONPATH:../check-maker" >> $script
echo "cd cc-plugin-ukcp18/" >> $script

echo "Set up your environment with:"
echo "source setup_env.sh"
