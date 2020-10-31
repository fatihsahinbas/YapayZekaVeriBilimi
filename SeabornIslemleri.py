#region Veriye ilk bakış

# import seaborn as sns

# planets= sns.load_dataset("planets")

# planets.head()

# df= planets.copy()

# df.head()

# df.tail()

# # Veri seti yapısal bilgileri
# df.info()

# df.dtypes
#endregion

#region Veri Setinin Belirlenmesi

# import seaborn as sbs

# planets= sbs.load_dataset("planets")
# df= planets.copy()

# df.head()
# df.shape
# df.columns

# df.describe().T
#endregion

#region Eksik Değerlerin İncelenmesi

import seaborn as sbs

planets= sbs.load_dataset("planets")
df= planets.copy()

df.head()

#hiç eksik gözlem(değer) var mı

df.isnull().values.any()

#hangi değişkende kaçar tane var

df.isnull().sum()

#endregion
