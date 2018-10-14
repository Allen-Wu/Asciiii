import argparse
from asciiii.engine.core import run

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, help='input image file path')
    parser.add_argument('-l', '--line', action='store', type=int, default=800, help='desired image width')
    parser.add_argument('-v', '--video', action='store_true', default=False, help='real-time video mode, need your camera')
    parser.add_argument('-e', '--eta', action='store', type=float, default=0.15, help='hyper-parameter for ascii matching')
    parser.add_argument('-li', '--light', action='store_true', default=False, help='use a small set of ascii with high frequenty')
    parser.add_argument('-g', '--gif', action='store_true', default=False, help='generate a real-time gif with specific duration')
    parser.add_argument('-c', '--color', action='store_true', default=False, help='colorful mode')

    args = parser.parse_args()
    args_dict = vars(args)

    run(**args_dict)


if __name__ == '__main__':
    main()