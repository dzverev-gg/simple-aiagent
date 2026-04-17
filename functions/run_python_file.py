import os 
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):  
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_file = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

        
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args is not None:
            command.extend(args)
        
        command_result = subprocess.run(command, text=True, capture_output=True, timeout=30)

        result_string = ""
        
        if command_result.returncode != 0:
            result_string += f"Process exited with code {command_result.returncode}\n"
        if command_result.stderr is None and command_result.stdout is None: 
            result_string += "No output produced"
        else:
            result_string += f"STDOUT: {command_result.stdout}\n"
            result_string += f"STDERR: {command_result.stderr}"

        return result_string

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python file locted in the file_path using the arguments provided to the function",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the file, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An array of string arguments that will be provided to the python file during its execution",
                items=types.Schema(type=types.Type.STRING,
                                   description="Arguments that will be provided to the file during its execution")
                )
        }, 
        required=["file_path"]
    ),
)
