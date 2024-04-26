# UNICORE Interlink Plugin

This repository contains the code of [UNICORE](https://www.unicore.eu) sidecar [InterLink](https://github.com/interTwin-eu/interLink/tree/main) plugin. It enables compute task offloading to the UNICORE interfaced HPC resources. At the backend, the plugin receives a (pod creation) request from an Interlink instance, the plugin then creates a UNICORE job containing instructions to deploy a pod as an apptainer container on a HPC system. 

The requester should fetch an **access token** using the [script](scripts/fetch_unicore_token.py) from the target UNICORE site before initiating any off-loading request. Before executing the script, please update the script by providing UNICORE site's base url and valid credentials (username and password). If the UNICORE site is deployed at Forschungszentrum Juelich, [JuDoor](https://judoor.fz-juelich.de/projects/join/intertwin) credentials are required. The instructions to create a JuDoor account can be found under the following [link](https://confluence.egi.eu/display/interTwin/CERN+Usecase+-+Joint+CERN-JSC+Activity+and+Testbed#CERNUsecaseJointCERNJSCActivityandTestbed-HowtogetanaccesstotheJSCHDFMLcluster?).

The fetched access token should be copied into a new `unicoreToken` field of the yaml file.

```yaml
metadata:
  annotations:
    unicoreToken: "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOi..."
```

## Installation

### Dependencies
- It is recommended to use the latest version of Python. UNICORE plugin supports Python 3.8 and newer.
- [pyunicore](https://pyunicore.readthedocs.io/en/latest/index.html) - UNCORE python client library.
- For a detailed list of dependencies, please refer to the Python's [requirements](requirements.txt) file in this repository's main folder.


### Quick start

Check out this git repo:

```bash
git clone https://github.com/interTwin-eu/interlink-unicore-plugin.git
```

Modify the [config file](SidecarConfig.yaml) properly and run the server by executing the following command:

```bash
cd interlink-unicore-plugin/src/
python3 handles.py --port <server_port> # default port is 8000
```




