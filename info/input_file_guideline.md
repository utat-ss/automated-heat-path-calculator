# Input CSV File Specifications

The **first row is for determining whether to use HIGH or LOW k-values**.
Each row afterwards corresponds to a heat path.

The basic format for each row after is:\
```area,length,material1,material2,pressure,```

If the path involves *just material resistance*, leave the *material2* and *pressure* parameters blank:\
```area,length,material1,,,```

If a heat path *travels through multiple paths*, keep them **on the same row**:\
```area1,length1,material1,material2,pressure1,area2,length2,material3,material4,pressure2,```

**If no length was given**, by default, **use 1**.

For example files, please look in the [test directory](../test/) in this repository.