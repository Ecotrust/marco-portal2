#!/bin/bash

PROJ=/usr/local/apps/ocean_portal
ENV=$PROJ/wag_env;
while getopts e:v: flag
do
  case "${flag}" in
    e) ENV=${OPTARG};;
    v) PYVER=${OPTARG};;
  esac
done
PIP=$ENV/bin/pip;

# 1_12
$PIP uninstall wagtail -y

$PIP install "wagtail==1.12.6"

PYTHON=$ENV/bin/python3;
DJ=$PROJ/marco/manage.py;

$PYTHON $DJ migrate wagtailcore
# $PYTHON $DJ migrate wagtailadmin
# $PYTHON $DJ migrate wagtaildocs
# $PYTHON $DJ migrate wagtailembeds
# $PYTHON $DJ migrate wagtailforms
# $PYTHON $DJ migrate wagtailimages
# $PYTHON $DJ migrate wagtailredirects
# $PYTHON $DJ migrate wagtailsearch
# $PYTHON $DJ migrate wagtailusers
