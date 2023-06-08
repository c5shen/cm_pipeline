from datetime import datetime
from os import path
import os

from source.stage import Stage

class Workflow:
    def __init__(self, data):
        # Load global parameters
        self.title = data['title']
        self.algorithm = data['algorithm']
        self.network_name = data['name']
        self.output_dir = data['output_dir']
        self.input_file = data['input_file']
        self.resolution = data['resolution'] if type(data['resolution']) == list else [data['resolution']]
        self.iterations = data['iterations'] if type(data['iterations']) == list else [data['iterations']]

        # Get timestamp of algo run
        self.timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")

        # Initialize first set of commands
        self.commands = [
            '#!/bin/bash',
            'global_start_time=$SECONDS',
            'echo "*** INITIALIZING OUTPUT DIRECTORIES ***"',
            'stage_start_time=$SECONDS',
            f'[ ! -d {self.title}-{self.timestamp} ] && mkdir -p {self.title}-{self.timestamp} > /dev/null',
            f'cd {self.title}-{self.timestamp}'
        ]

        # Create directories for the resolutions and iterations
        for res in self.resolution:
            for niter in self.iterations:
                self.commands.append(f'mkdir -p res-{res}-i{niter}')

        # Output the initialization stage finished
        self.commands = self.commands + [
            'end_time=$SECONDS',
            'elapsed_time=$((end_time - stage_start_time))',
            'hours=$(($elapsed_time / 3600))',
            'minutes=$(($elapsed_time % 3600 / 60))',
            'seconds=$(($elapsed_time % 60))',
            'formatted_time=$(printf "%02d:%02d:%02d" $hours $minutes $seconds)',
            'echo "Stage 0 Time Elapsed: $formatted_time"',
            'echo "*** DONE ***"'
        ]

        # Get the absolute path of the current script
        current_script = path.abspath(__file__)

        # Get the project root directory
        project_root = path.dirname(path.dirname(current_script))

        # Initialize and link stages
        self.stages = [Stage(
                stage, 
                self.input_file, 
                self.network_name, 
                self.resolution, 
                self.iterations,
                self.algorithm,
                f'{project_root}/{self.output_dir}/{self.title}-{self.timestamp}',
                i+1
            ) for i, stage in enumerate(data['stages'])]
        for i, stage in enumerate(self.stages):
            if i > 0:
                stage.link_previous_stage(self.stages[i-1])

        # TODO: For now, lets just require that the first stage is cleaning
        assert self.stages[0].name == 'cleanup'

        # Get commands for each stage
        for stage in self.stages:
            self.commands = self.commands + stage.get_command()

        # Get overall timing
        self.commands = self.commands + [
            'end_time=$SECONDS',
            'elapsed_time=$((end_time - global_start_time))',
            'hours=$(($elapsed_time / 3600))',
            'minutes=$(($elapsed_time % 3600 / 60))',
            'seconds=$(($elapsed_time % 60))',
            'formatted_time=$(printf "%02d:%02d:%02d" $hours $minutes $seconds)',
            f'echo "Overall Time Elapsed: $formatted_time"',
            'echo "*** PIPELINE DONE ***"'
        ]
    
    def write_script(self):
        with open(f"{self.output_dir}/commands.sh", "w") as file:
            file.writelines(line + "\n" for line in self.commands)

    def execute(self):
        os.system(f'cd {self.output_dir}; chmod +x commands.sh; ./commands.sh')

