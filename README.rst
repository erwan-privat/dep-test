Deployment test for micromamba
==============================

[WIP] Without micromamba installed
----------------------------------

Create a workspace directory, in this example `workspace`::

  mkdir workspace && cd workspace

Get the micromamba executable into a `mm` directory and clean up::

  wget https://micromamba.snakepit.net/api/micromamba/linux-64/latest -O micromamba.tar.bz
  tar -xf micromamba.tar.bz
  mkdir mm
  mv bin/micromamba mm
  rm -r info bin micromamba.tar.bz

Clone the repository::

  git clone https://github.com/erwan-privat/dep-test

Create the virtual environment with the root prefix `mm`::

  mm/micromamba create -y -f dep-test/env.yaml -r mm

Alternatively, we can specify a local environment path with::

  mm/micromamba create -y -f dep-test/env.yaml -r mm -p mm/envs/dep-test

With micromamba installed
-------------------------

Clone the repository and change directory::

  git clone https://github.com/erwan-privat/dep-test
  cd dep-test


