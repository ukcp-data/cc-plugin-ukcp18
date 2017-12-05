# Installing the UKCP18 plugin and its dependencies

Here are some instructions for working with the compliance-checking tools. At the moment there are a number of separate repositories involved in setting up the tools. I expect these will move/change over time but currently there is a script to pull them all in. The following 5 lines should get everything built on your system:

```
mkdir checker-bundle
cd checker-bundle/
wget https://raw.githubusercontent.com/ukcp-data/cc-plugin-ukcp18/master/scripts/get-checker-suite.sh
chmod 750 get-checker-suite.sh
./get-checker-suite.sh --install ukcp18
```

Once you have done the initial setup you can test it with:

```
source setup_env.sh # which sets up a virtualenv and changes directory
compliance-checker --test ukcp18-file-info --test ukcp18-file-structure --test ukcp18-global-attrs cc_plugin_ukcp18/tests/data/ukcp18/test_cdl_global_atts.nc
```

You should get some input about checks on a real NC file.

Let's go back to the top-level directory:

```
cd ../
```

Here is an overview of the directories/packages at the top-level:

 * `cc-plugin-ukcp18` - The specific ioos-compliance-checker plugin for the UKCP18 project.
 * `compliance-checker` - My fork (with minor changes) of the ioos-compliance-checker.
 * `compliance-check-maker` - The library that writes the specification and plugin based on a set of YAML recipes.
 * `get-checker-suite.sh` - Script to download and install all components.
 * `pyessv-writer` - My fork of pyessv-writer - modified for UKCP18.
 * `setup_env.sh` - Setup script to activate virtualenv, set PYTHONPATH and change directory.
 * `UKCP18_CVs` - UKCP18-specific version of CMIP6-like JSON controlled vocabularies.
 * `venv` - Virtualenv used for everything.


