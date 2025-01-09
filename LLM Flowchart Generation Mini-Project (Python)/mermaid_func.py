from mermaid import *
from mermaid.configuration import Config, Themes

def generate_mermaid(response):
    config2 = Config(theme=Themes.FOREST)
    graph = Graph("Flowchart1", response, config = config2)
    return Mermaid(graph)

def save_mermaid(diagram, File_Name):
    diagram.to_png(File_Name + ".png")
        

    
