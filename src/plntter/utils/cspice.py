import contextlib
import os
import tarfile
import urllib.request as urllib


def download(url, path):
    response = urllib.urlopen(url)
    with contextlib.closing(response):
        with open(path, 'wb') as f:
            f.write(response.read())

def unpack(file, path):
    print('Unpacking to: {}'.format(path))
    tarfile.TarFile(file).extractall(path)

def main(path=None, yesno=None):
    ## LOCATE PACKAGE ON WEB ##
    ROOT_URL = 'http://naif.jpl.nasa.gov/pub/naif/toolkit/C'
    PLATFORM_URL = 'MacIntel_OSX_AppleC_64bit'
    tar_file = 'packages/cspice{0}'.format(('.tar.Z'))

    package = '/'.join([ROOT_URL, PLATFORM_URL, tar_file])

    ## PROMPT USER TO DOWNLOAD PACKAGE ##
    if yesno is None:
        yesno = input('Do you want to download it? [y/n] ')
        for char in 'nN':
            if yesno.startswith(char):
                raise SystemExit(0)
    elif not yesno:
        raise SystemExit(0)

    ## DOWNLOAD AND UNPACK PACKAGE ##
    ROOT_DIR = path or os.path.realpath(os.path.dirname(__file__))
    data_dir = '/'.join([ROOT_DIR, '..', 'data'])

    filelike = download(package_url, data_dir)
    unpack(filelike, data_dir)

    print('Done')


if __name__ == '__main__':
    main()
