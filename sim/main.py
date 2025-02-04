import sys

import arrangers
import testers as test
    

def named_model(name):
    '''
    Returns the arrangement function corresponding to the name
    '''
    if name == 'square_simple':
        return arrangers.square_simple
    if name == 'square_vertical':
        return arrangers.square_vertical
    if name == 'hexagonal':
        return arrangers.hexagonal
    if name == 'hexagonal_rotated':
        return arrangers.hexagonal_rotated
    if name == 'square_spiral':
        return arrangers.square_spiral
    else:
        sys.exit(f"Model {name} not found.")


def test_arrangment(arrangement_name, resolution, save_figures=False):

    df = test.test_general_arrangement(
        named_model(arrangement_name), 
        resolution, 
        save_figures=save_figures
    )

    df.to_csv(f"data/{arrangement_name}_{resolution}.csv")


if __name__ == '__main__':

    '''
    methods = [
            'square_simple',
            'square_vertical',
            'hexagonal',
            'hexagonal_rotated'
        ]

    for m in methods:
        test_arrangment(m, 1)
    '''
   

    # test.test_overall("data/*.csv")
    test.plot_data('min_waste_values.csv', 'figures/overall/heatmap.png')
    