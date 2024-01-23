# ray-of-slurm

Using Ray on Slurm clusters, with Posit Workbench!

## To-Do
- [x] Run a simple 'hello world!' (print timestamps)
- [x] Run something with more firepower. Train MNIST, perhaps?
    - [x] Test dependencies. How can I add a dependency to something like Torch?
- [ ] Can I make it run in a notebook? 
    - [ ] Can notebook code cell execution wait for slurm job execution?

## What I Did:
1. Attempted to use [YASPI](https://github.com/albanie/yaspi) -- errors encountered due to incompatibility with current slurm CLI
2. Ignored [pengzhenghao](https://github.com/pengzhenghao/use-ray-with-slurm) 's work -- 4 years makes me suspicious we're likely to see the same issues as above
3. Used the [NERSC](https://github.com/NERSC/slurm-ray-cluster) submission scripts -- worked like a charm!
4. Experimented with injecting dependencies. [venvs work!](submit-ray-cluster.sbatch#L15)
