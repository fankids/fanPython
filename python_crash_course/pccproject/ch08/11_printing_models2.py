def print_models(unprinted_models, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_models:
        current_design = unprinted_models.pop()
    # ~ for current_design in unprinted_models:
        
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)

# ~ unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
# ~ completed_models = []

# ~ print_models(unprinted_models[:], completed_models)
# ~ show_completed_models(completed_models)
