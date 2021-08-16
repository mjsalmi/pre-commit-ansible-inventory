import subprocess
import argparse
from typing import Optional, Sequence

def main(argv: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)
    result = 0

    for filename in args.filenames:
        cp = subprocess.run(
            ['ansible-inventory','--list','-i',filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        if(cp.stderr):
            print(f"ansible-inventory failed on file {filename} with following output:")
            print(cp.stderr.decode())
            result = 1
    exit(result)

if __name__ == '__main__':
    exit(main())
