import os
import re
from gherkin.parser import Parser

def parse_and_hydrate_gherkin(relative_path):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, relative_path)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            gherkin_text = file.read()
        
        parser = Parser()
        gherkin_document = parser.parse(gherkin_text)
        feature = gherkin_document.get('feature', {})
        
        all_iterations = []

        for child in feature.get('children', []):
            scenario = child.get('scenario')
            if not scenario or 'examples' not in scenario:
                continue

            # 1. Get steps and examples
            steps = [step['text'] for step in scenario['steps']]
            examples_table = scenario['examples'][0]['tableBody']
            headers = [cell['value'] for cell in scenario['examples'][0]['tableHeader']['cells']]

            # 2. Iterate through each row in the Examples table
            for row in examples_table:
                row_values = [cell['value'] for cell in row['cells']]
                data_map = dict(zip(headers, row_values))
                
                # 3. Manually replace <Placeholder> with the row value
                hydrated_steps = []
                for step_text in steps:
                    for key, value in data_map.items():
                        # This regex replaces <Category> with Men, etc.
                        step_text = re.sub(rf"<{key}>", value, step_text)
                    hydrated_steps.append(step_text)
                
                all_iterations.append({"name": f"{scenario.get('name')} with {data_map}", "steps": hydrated_steps})

        return all_iterations

    except Exception as e:
        return f"Error: {str(e)}"
