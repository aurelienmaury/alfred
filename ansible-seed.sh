#!/usr/bin/env bash

set -e
set -x

export DEBIAN_FRONTEND=noninteractive
echo "Updating APT cache"
apt-get update

echo "Upgrading system"
apt-get -o Dpkg::Options::="--force-confold" upgrade -y

echo "Removing distutils installed 'python-pip' package"
apt-get -o Dpkg::Options::="--force-confold" remove python-pip --purge -y

echo "Installing mandatory packages for ansible"
apt-get -o Dpkg::Options::="--force-confold" install \
    aptitude            \
    libssl-dev          \
    libffi-dev          \
    git                 \
    python-dev          \
    libperl-dev         \
    python-apt          \
    python-apt-dev      \
    sudo                \
    build-essential     \
    python-setuptools   \
    python-distutils-extra \
    -y

echo "Installing pip via easy_install"
for i in 1 2 3 4 5; do easy_install pip && break || sleep 2; done

echo "Installing correct python crypto libs"
pip install -U pyopenssl ndg-httpsclient pyasn1

echo "Installing ansible via pip"
pip install -U pip ansible

mkdir -p /etc/ansible/
