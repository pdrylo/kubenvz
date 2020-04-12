![Tests](https://github.com/pdrylo/kubenvz/workflows/Tests/badge.svg) ![Build & Release](https://github.com/pdrylo/kubenvz/workflows/Build%20&%20Release/badge.svg)

# Kubenvz

kubectl & kustomize & helm & helmfile version manager

Inspired by terraenv https://github.com/aaratn/terraenv

Forked from https://github.com/nutellinoit/kubenvz

The main difference is source repository of `kubectl` versions. Originally **kubernetes/kubectl** has been used, 
but it's missing some older versions like 1.14 and 1.15 which are still used in AWS EKS.
Therefore, it's been changed to **kubernetes/kubernetes**, but can be switched to **kubernetes/kubectl** by specifying
`-M` or `--main` flag during execution of `list` and `install` sub-commands.

During installation `kubenvz` searches for `~/bin`, `~/.bin` and `~/.local/bin` directories before trying `/usr/local/bin`. It's easier to
handle switching to different versions if you don't have to rely on root privileges - though it's still available if someone needs it for whatever reason. 

Additionally, **.kubenvz-version** is now used as a version file for `kubenvz` binary, and it's searched for in
the directory tree path where **kubenvz** is executed. So, you can, for example, create default **~/.kubenvz-version**
file, which will configure your default versions of kubectl, kustomize, helm and helmfile, and in your project directory
declare some different versions and switch to them during your work.

The main reason for going with **.kubenvz-version** naming is name clashing with default **~/.kubenvz** directory where all 
commands are downloading during installation. I'm also a fan of **tfenv** which uses similar version file naming convention. 


## Installation

### Automatic

Install via Homebrew on OSx

```console
$ brew tap pdrylo/kubenvz
$ brew install kubenvz
```
### Upgrade

via Homebrew on OSx

```console
$ brew upgrade kubenvz
```

### On Linux

Download and install with:

```bash
wget https://github.com/pdrylo/kubenvz/releases/download/v0.5.0/kubenvz_linux_x86_64_v0.5.0.tar.gz -O kubenvz.tar.gz
tar -zxvf kubenvz.tar.gz
sudo mv kubenvz /usr/local/bin/
```


## Usage

### kubenvz <kubectl / kustomize / helm / helmfile> install [remote_version]

Install a specific version of kubectl/kustomize/helm/helmfile , list available remote versions with `kubenvz kustomize list remote`  :

- `kustomize/v.X.X.X` use exact version to install

> kustomize has lot of release, kubenvz filter all releases that are not cli executable


```console
$ kubenvz kubectl install 1.16.0
$ kubenvz kustomize install 1.0.10
$ kubenvz helm install v3.1.0
$ kubenvz helmfile install v0.100.1
```

## kubenvz <kubectl / kustomize / helm / helmfile> list <remote / local>

To list local installed version use:

```bash
kubenvz kustomize list local
```

## kubenvz <kubectl / kustomize / helm / helmfile> use [local_version]

To use a local installed version:

```bash
kubenvz kustomize use 1.0.10
```

## Fast switcher

To have a faster switch between version, install the kbnvz tool (working on macos and linux):

```bash
sudo wget https://github.com/pdrylo/kubenvz/releases/download/v0.5.0/kbnvz_v0.5.0 -O /usr/local/bin/kbnvz
sudo chmod +x /usr/local/bin/kbnvz
```

### kbnvz <kubectl / kustomize / helm / helmfile> [local_version]

To use the fast switcher script:

```bash
kbnvz kustomize 1.0.10
```

## Develop

Create a virtualenv:

```bash
python3 -m venv .
```

Start virtualenv:

```bash
source bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```


## LICENSE

- [kubenvz](https://github.com/nutellinoit/kubenvz/blob/master/LICENSE)
- [terraenv](https://github.com/aaratn/terraenv/blob/master/LICENSE)
- [rbenv](https://github.com/rbenv/rbenv/blob/master/LICENSE)

## Inspiration

- [terraenv](https://github.com/aaratn/terraenv/blob/master/LICENSE)
- [tfenv](https://github.com/tfutils/tfenv)
- [tgenv](https://github.com/cunymatthieu/tgenv)
- [rbenv](https://github.com/rbenv/rbenv)
