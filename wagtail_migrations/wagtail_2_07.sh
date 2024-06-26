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

# 2_07
# No migrations, what's the point in updating wagtail?
#   It breaks if its dependencies are removed, so we need to uninstall/reinstall
$PIP uninstall wagtail -y
$PIP uninstall Willow -y
$PIP uninstall django-taggit -y
$PIP uninstall django-modelcluster -y
$PIP install "django-modelcluster==5.0.1"
$PIP install "django-taggit==1.3.0"
$PIP install "Willow==1.3"
$PIP install "wagtail==2.7.1"

PYTHON=$ENV/bin/python3;
DJ=$PROJ/marco/manage.py;

$PYTHON $DJ migrate taggit 0003
# $PYTHON $DJ migrate wagtailcore
# $PYTHON $DJ migrate wagtailadmin
# $PYTHON $DJ migrate wagtaildocs
# $PYTHON $DJ migrate wagtailembeds
# $PYTHON $DJ migrate wagtailforms
# $PYTHON $DJ migrate wagtailimages
# $PYTHON $DJ migrate wagtailredirects
# $PYTHON $DJ migrate wagtailsearch
# $PYTHON $DJ migrate wagtailusers
