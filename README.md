# File Key Value Substitutor

This script helps you generate a new file with substituted values you specify from your base template and JSON mappings file as inputs.

## Prequisites

* Python 3.x

## Usage

```bash
$ python substitutor.py base_template_path output_file_name mappings_file
```

<img src="docs/help.gif" width="500" height="300">

### Example

Suppose you want to dynamically generate Terraform configuration while substituting certain values from a base template. In this example, we want to replace `%id%` with a value we specify when running the script. We will provide three inputs when running the substitutor script: JSON file with key value mappings; path to the base template file; output file name.

example/sample_base_template.tf:


<img src="docs/sample_base_template.svg" width="500" height="300">

example/sample_mappings.json:


<img src="docs/sample_mappings.svg" width="300" height="350">

#### Demo

```bash
$ python substitutor.py example/sample_base_template.tf sample_demo.tf example/sample_mappings.json
```

<img src="docs/example_demo.gif" width="500" height="300">

Output file (sample_demo.tf):

<img src="docs/example_demo_output.svg" width="500" height="300">