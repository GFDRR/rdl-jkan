---
attributions:
- entity:
    affiliation: null
    email: null
    name: Premise platform
    url: https://data.humdata.org/dataset/detected-settlements-col
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/detected-settlements-col
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/detected-settlements-col
dataset_id: rdls_exp-col_immap_detectedsettlements_202402
description: 'Detected settlements, as well as information on the validation processes
  carried out through the Premise platform and other organizations. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/detected-settlements-col]'
details: null
exposure:
- asset_type:
    description: Detected settlements with housing unit counts and structural inventory
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Residential population inferred from settlement detection and dwelling
      counts
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Settlement locations were detected through remote sensing or field
    surveys and validated through the Premise crowdsourcing platform and partner organizations.
    The dataset contains spatial inventories of detected settlements with dwelling
    counts and population estimates across Colombian departments and municipalities.
  sources:
  - id: source_1
    license: null
    name: Premise platform
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/detected-settlements-col
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Detected Settlements (CSV)'
  download_url: https://data.humdata.org/dataset/d0cbb46a-d196-4413-9b5e-402a807d4ea4/resource/65bc0964-c097-4364-bd8c-226bd40ed633/download/asentamientos.csv
  format: null
  id: resource_65bc0964
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: asentamientos.csv
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-col_immap_detectedsettlements_202402
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-02-29'
  start: '2024-02-01'
temporal_resolution: null
title: 'Colombia: Detected Settlements'
version: null
vulnerability: null
---
