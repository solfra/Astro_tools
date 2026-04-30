import pandas as pd

def sort_df(data,value,ascending,verbose=None):
    sorted_data = data.sort_values(by=value,ascending=ascending)

    if verbose is not None:
        print(sorted_data.head(10)[verbose])
    
    return sorted_data

if __name__ == "__main__" :
    import argparse

    parser = argparse.ArgumentParser(description='Extract SCI image')
    parser.add_argument('--file', type=str, help='File name')
    parser.add_argument('--value', type=str, help='File name')
    parser.add_argument('--ascending', action='store_true', help='Extension name name')
    parser.add_argument('--verbose',type=str, help='Patch ID list',nargs='*') 
    args = parser.parse_args()

    data = pd.read_csv(args.file,delimiter=';')
    sorted_data = sort_df(data,args.value,args.ascending,verbose=args.verbose)