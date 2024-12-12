Deployment test for micromamba
==============================

Create a workspace directory, in this example `workspace`::

  mkdir workspace && cd workspace

Get the micromamba executable::

  wget https://micromamba.snakepit.net/api/micromamba/linux-64/latest -O micromamba.tar.bz
  tar -xf micromamba.tar.bz
  mv bin/micromamba .
  rm -r info bin micromamba.tar.bz

Clone the repository::

  git clone https://github.com/erwan-privat/dep-test

