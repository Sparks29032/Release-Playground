#! /bin/bash
../bg-release-scripts/basic_release.py $1 $2 \
	--tag \
	--github \
	--gh-title "title $1" \
	--gh-notes """See [CHANGELOG.rst](CHANGELOG.rst) for detailed release notes.

The release is also available at [PyPI](https://pypi.org/project/diffpy.utils/) and [Conda](https://anaconda.org/conda-forge/diffpy.utils).
"""\
	--pypi
