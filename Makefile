PLATFORM                 ?= $(shell uname -sm | tr '[:upper:]' '[:lower:]' | sed "s/[^a-zA-Z0-9_]/_/g" | sed "s/_\+/_/g")
BUILD_VERSION            := $(shell python kubenvz.py --version)-$(shell git rev-parse --short HEAD)

.PHONY: check-env update-build-version update-readme-version commit-version build package test-kubectl test-kustomize test-helm test-all

update-build-version: check-env
	sed -i 's/VERSION\s*=.*/VERSION = "$(BUILD_VERSION)"/g' config.py

update-readme-version: check-env
	sed -i 's!wget https://github.com.*!wget https://github.com/pdrylo/kubenvz/releases/download/v$(BUILD_VERSION)/kubenvz_linux_x86_64_v$(BUILD_VERSION).tar.gz -O kubenvz.tar.gz!g' README.md
	sed -i 's!sudo wget https://github.com.*!sudo wget https://github.com/pdrylo/kubenvz/releases/download/v$(BUILD_VERSION)/kbnvz_v$(BUILD_VERSION) -O /usr/local/bin/kbnvz!g' README.md


commit-version:
	git add config.py
	git add README.md
	git commit -m "Version update" && git push || true

build:
	@PYTHONOPTIMIZE=1 \
		pyinstaller kubenvz.py \
		--onefile \
		--clean \
		--osx-bundle-identifier com.nutellinoit.os.kubenvz \
		--nowindowed
	@chmod +x dist/kubenvz

package:
	@cd dist && tar -czvf ./kubenvz_$(PLATFORM).tar.gz kubenvz

test-kustomize:
	rm -rf ~/.kubenvz/kustomize*
	dist/kubenvz kustomize list remote | sort | xargs -n 1 -P 1 dist/kubenvz kustomize install -f

test-kubectl:
	rm -rf ~/.kubenvz/kubectl*
	dist/kubenvz kubectl list remote | sort | xargs -n 1 -P 1 dist/kubenvz kubectl install -f

test-helm:
	rm -rf ~/.kubenvz/helm*
	dist/kubenvz helm list remote | sort | xargs -n 1 -P 1 dist/kubenvz helm install -f

test-helmfile:
	rm -rf ~/.kubenvz/helmfile*
	dist/kubenvz helmfile list remote | sort | xargs -n 1 -P 1 dist/kubenvz helmfile install -f

test-all: test-kubectl test-helm test-helmfile test-kustomize

########## Prerequisites
check-env:
ifndef BUILD_VERSION
	$(error BUILD_VERSION is undefined)
endif