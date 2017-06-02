# EUSTACE Compliance Checker Plugin

This is a checker for EUSTACE files.

It works with the `agstephens` fork of the [ioos/compliance-checker](https://github.com/agstephens/compliance-checker) which includes an interface to the [pyessv library](https://github.com/ES-DOC/pyessv).

### Usage

Activate your virtualenv/conda env and `pip install git+git://github.com/eustace-test/cc-plugin-eustace`.  You should see `eustace` in the list of `--test` suites when running `compliance-checker`.

### Setup instructions

1. Create a virtual environment:

```
mkdir mydir
cd mydir/
virtualenv venv
```

2. Activate the virtual environment:

`source venv/bin/activate`

3. PIP install the pyessv library:

`pip install pyessv`

4. Pull compliance checker core code from GitHub and install:

```
git clone https://github.com/agstephens/compliance-checker
cd compliance-checker/
pip install .
```

5. Pull EUSTACE compliance checker PLUGIN from GitHub and install:

```
git clone https://github.com/eustace-test/cc-plugin-eustace
cd cc-plugin-eustace/
pip install .
```

6. A couple more installation upgrades:

```
pip install "tornado>=4.0"
pip install "six>=1.9.0"
```

7. Create an example file to test it with:

```
ncgen -o ./cc_plugin_eustace/tests/data/eustace/test_cdl_global_atts.nc ./cc_plugin_eustace/tests/data/eustace/test_cdl_global_atts.cdl
```

8. Now you can run it:

```
compliance-checker --test eustace-core --test eustace-station ./cc_plugin_eustace/tests/data/eustace/test_cdl_global_atts.nc
```

### Running with new EUSTACE tests

We have defined `eustace-core` and `eustace-station` tests. You can run both of these with:

`compliance-checker --test eustace-core --test eustace-station ./cc_plugin_eustace/tests/data/eustace/test_cdl_global_atts.nc`

The output should look something like:

```
2017-06-02T15:15:56.089919 [INFO] :: ES-DOC PYESSV :: Loading vocabularies from /home/users/astephen/.esdoc/pyessv-archive:
2017-06-02T15:15:56.142255 [INFO] :: ES-DOC PYESSV :: ... loaded: eustace-team
Running Compliance Checker on the dataset from: ./cc_plugin_eustace/tests/data/eustace/test_cdl_global_atts.nc


--------------------------------------------------------------------------------
                      The dataset scored 3 out of 6 points
                         during the eustace-core check
--------------------------------------------------------------------------------
                               Scoring Breakdown:


Required Global Attributes              :2:     3/6


--------------------------------------------------------------------------------
                  Reasoning for the failed tests given below:


Name                             Priority:     Score:Reasoning
--------------------------------------------------------------------------------
Required Global Attributes             :2:     3/ 6 : source global attribute is
                                                      missing, frequency global
                                                      attribute found but
                                                      invalid value


--------------------------------------------------------------------------------
                      The dataset scored 3 out of 6 points
                        during the eustace-station check
--------------------------------------------------------------------------------
                               Scoring Breakdown:


Required Global Attributes              :2:     3/6


--------------------------------------------------------------------------------
                  Reasoning for the failed tests given below:


Name                             Priority:     Score:Reasoning
--------------------------------------------------------------------------------
Required Global Attributes             :2:     3/ 6 : source global attribute is
                                                      missing, frequency global
                                                      attribute found but
                                                      invalid value

```

### Development

Copied the `cc-plugin-glider` code and converted to use with EUSTACE.

For development use you need pip to install the plugin. Can do this with local copy using:

 `pip install -e .`

Note: adding any new modules will require this `pip` command to be re-run.
