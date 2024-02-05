import json
import modules.tfwrapper as tfwrapper
def generatecode(json_file):
    with open(json_file, 'r') as file:
        containers = json.load(file)

    plantuml_code = f'@startuml\n\n'
    plantuml_code += "!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml\n"
    

    for container in containers:
        container_name={container}
        plantuml_code += f"Container({container},{container},"")\n"

    plantuml_code += '@enduml'
    
    with open('architecture.puml', 'w') as output_file:
       output_file.write(plantuml_code)

    