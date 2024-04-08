import argparse

def main(args):

    print(f"Executing with style: {args.style} and color: {args.color}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('--style', choices=['ripples', 'waves', 'circles'], help='Style option')
    parser.add_argument('--color', help='color option')

    args = parser.parse_args()
    main(args)