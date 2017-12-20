import os
import sys
from urllib.request import urlretrieve
import zipfile
import pandas as pd
import qgrid

def make_tmp(tmp='tmp'):
    if not os.path.exists(tmp):
        os.mkdir(tmp)

def download(filename):
    url = 'http://www.mercadopublico.cl/Portal/att.ashx?id=5'
    urlretrieve(url, filename)

def extractfiles(filename, tempdir):
    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall(tempdir)
    zip_ref.close()

def get_data(tempdir):
    name = 'Licitacion_Publicada.csv'
    filename = os.path.join(tempdir, name)
    aux = pd.read_csv(filename, skiprows=3)
    return aux

def get_codes(df, pattern):
    aux = pd.np.array([])
    if type(pattern) is str:
        pattern = [pattern]
    for p in pattern:
        for x in df.columns[2:5]:
            a = df[df[x].str.contains(p, case=False)].rbiGoodAndService.unique()
            aux = pd.np.append(aux, a)
    return pd.np.unique(aux)

def get_result(df, pattern):
    return df[df.rbiGoodAndService.isin(get_codes(df, pattern))]

def print_codes(df, pattern):
    pd.np.savetxt(sys.stdout, get_codes(df, pattern), '%.0f')

def print_result(df, pattern):
    return qgrid.show_grid(get_result(df, pattern))

def main():
    tempdir = 'tmp'
    make_tmp(tempdir)
    filename = os.path.join(tempdir, 'filename.zip')
    download(filename)
    extractfiles(filename, tempdir)


if __name__ == '__main__':
    main()

