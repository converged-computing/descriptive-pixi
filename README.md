# Pixi Environments

Create a flux allocation (limit is 1h)

```bash
flux alloc -N1 -q pbatch -t 1h
```

## 1. Setup

If you have the hugging face client installed locally, you can first login to Hugging Face. If not, wait to
run this command until you pixi shell.

```bash
huggingface-cli login  --add-to-git-credential
```

And then source the pixi env.

```bash
export PATH="/p/vast1/fractale/descriptive-thrust/pixi/bin:$PATH"
which pixi
```

Then CD into the directory that you are interested in using. Description for environment
creation is below. **You do not need to re-run these steps**.

- [mistral](mistral)
- [gemma](gemma) (under development)
- llama: coming soon

If you change any environments (e.g., in the `pixi shell` you do `pixi add <library>` please
open a pull request to the repository to update, and also be sure to change permissions
in the shared space otherwise others cannot use it.


## 2. Environment Creation

I created it like this (you don't need to do this).

```bash
export PIXI_HOME=/p/vast1/fractale/descriptive-thrust/pixi
curl -fsSL https://pixi.sh/install.sh | sh
```

And then for each, to install (again, you do not need to run this again).

```bash
# And installed environments with
cd /p/vast1/fractale/descriptive-thrust/Src_fractale_de/pixi-envs/mistral
pixi install
pixi run install-pytorch-rocm62
```


## License

HPCIC DevTools is distributed under the terms of the MIT license.
All new contributions must be made under this license.

See [LICENSE](https://github.com/converged-computing/cloud-select/blob/main/LICENSE),
[COPYRIGHT](https://github.com/converged-computing/cloud-select/blob/main/COPYRIGHT), and
[NOTICE](https://github.com/converged-computing/cloud-select/blob/main/NOTICE) for details.

SPDX-License-Identifier: (MIT)

LLNL-CODE- 842614

