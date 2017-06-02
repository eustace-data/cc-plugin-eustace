# EUSTACE Compliance Checker Plugin

This is a checker for EUSTACE files.

It works with the `agstephens` fork of the [ioos/compliance-checker](https://github.com/agstephens/compliance-checker) which includes an interface to the [pyessv library](https://github.com/ES-DOC/pyessv).

### Usage

Activate your virtualenv/conda env and `pip install git+git://github.com/eustace-test/cc-plugin-eustace`.  You should see `eustace` in the list of `--test` suites when running `compliance-checker`.

### Setup instructions

...to come soon...

### Running with new EUSTACE tests

We have defined `eustace-core` and `eustace-station` tests. You can run both of these with:

`compliance-checker --test eustace-core --test eustace-station ./cc_plugin_eustace/tests/data/eustace/test_cdl_global_atts.nc`

### Development

Copied the `cc-plugin-glider` code and converted to use with EUSTACE.

For development use you need pip to install the plugin. Can do this with local copy using:

 `pip install -e .`

Note: adding any new modules will require this `pip` command to be re-run.
