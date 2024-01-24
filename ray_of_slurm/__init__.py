from simple_slurm import Slurm
import sys

basecommands = (
    "echo $pwd",
    "head_node=$(hostname)",
    "head_node_ip=$(hostname --ip-address)",
    "if [[ \"$head_node_ip\" == *\" \"* ]]; then",
    "IFS=' ' read -ra ADDR <<<\"$head_node_ip\"",
    "if [[ ${{#ADDR[0]}} -gt 16 ]]; then",
      "head_node_ip=${{ADDR[1]}}",
    "else",
      "head_node_ip=${{ADDR[0]}}",
    "fi",
    "fi",
    "port=6379",
    "echo \"STARTING HEAD at $head_node\"",
    "echo \"Head node IP: $head_node_ip\"",
    "srun --nodes=1 --ntasks=1 -w $head_node {head_script} $head_node_ip &",
    "sleep 10",
    "worker_num=$(($SLURM_JOB_NUM_NODES - 1))",
    "srun -n $worker_num --nodes=$worker_num --ntasks-per-node=1 --exclude $head_node {worker_script} $head_node_ip:$port &",
    "sleep 5",
)

class UnsupportedPythonEnv(Exception):
    pass

class RayCluster(Slurm):
    def __init__(self, head_script="start_head.sh", worker_script="start_worker.sh", **kwargs):
        super().__init__(**kwargs)

        # checks if in venv, errors if not
        if sys.prefix != sys.base_prefix:
            self.add_cmd(f"source {sys.prefix}/bin/activate")
        else:
            raise UnsupportedPythonEnv("Detected code running in a base environment. This is not supported!")

        for c in basecommands:
            self.add_cmd(c.format(head_script=head_script, worker_script = worker_script))          
