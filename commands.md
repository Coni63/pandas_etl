# GENERAL

The general structure of the plan configuration is composed of the 3 part of an ETL:

```yaml
extract:
  - csv:                                                 # loader type
      name: source_a                                     # dataset name
      filepath_or_buffer: path/to/source_a.csv           # file
      sep: ";"                                           # extra parameters
  - csv:
      name: source_b
      filepath_or_buffer: tests/resources/source_b.csv
transform:
  - t1:                                                  # transformation type (dummy here)
      name: transform_1                                  # description of the transformation
      source: source_a                                   # input name
      target: target1                                    # output name
  - t2:
      name: transform_2
      source: source_b
      target: target2
  - join:
      name: transform_3
      left: target1
      right: target2
      target: target3
  - concat:
      name: transform_4
      sources:                                          # we can concatenate N sources here [target2 & target3]
        - target2
        - target3
      target: target4
load:
  - csv:                                                # persist a given dataset to csv
      name: persist target4                             # description
      source: target4                                   # data to persist
      path_or_buf: tests/resources/source_c.csv         # output location
      sep: ","                                          # extra parameters
```

This lead to the following workflow:

![Mermaid](tests/resources/example.svg)

### Information

> Almost all stages presented below with accept extra-parameters from the pandas API. All fields will not be listed but a link to the official documentation will be attached to allows to review all the options.

# EXTRACT

### CSV

```yaml
  - csv:                                                 # loader type
      name: source_a                                     # dataset name
      filepath_or_buffer: path/to/source_a.csv           # file
      # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
```

### SQL

```yaml
```

### CUSTOM EXTRACTOR

```yaml
```

# TRANSFORM

### CUSTOM TRANSFORMER

```yaml
```

# LOAD

### CSV

```yaml
  - csv:
      name: Save the target
      source: target
      path_or_buf: path/to/result.csv
      # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
```


### SQL

```yaml
```

### CUSTOM LOADER

```yaml
```
