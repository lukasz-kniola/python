#-------------------------------------------------------------------------------
# Name:       sas2pd
# Purpose:    import a SAS dataset as a Python pandas dataframe  
#
#-------------------------------------------------------------------------------

def sas2pd(sasfile):
    import pandas as pd
    from sas7bdat import SAS7BDAT
    a = []
    for i, x in enumerate(SAS7BDAT(sasfile).readData()):
        if i == 0:
            cols = x
        else:
            a.append(x)
    df = pd.DataFrame(a)
    df.columns = cols
    return df

if __name__ == '__main__':
    sasclass = sas2pd("C:\Program Files\SASHome\SASFoundation\9.3\core\sashelp\class.sas7bdat")
    from ggplot import *
    print ggplot(sasclass, aes('Height', 'Weight')) + geom_point() + stat_smooth(color='red')
