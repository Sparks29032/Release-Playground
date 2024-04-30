#! /bin/bash
../bg-release-scripts/release.py $1 $2 \
	--tag \
	--github \
	--gh-title "Release $2" \
	--pypi
