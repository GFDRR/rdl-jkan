---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pacific Community Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-federate
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-federate
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-federate
dataset_id: rdls_exp-fsm_spc_coastalproximitypopulatio_20190930
description: 'Spatial datasets utilized to conduct the spatial analysis and additional
  information from the research article: Coastal proximity of populations in 22 Pacific
  Island Countries and Territories. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
  https://sdd.spc.int/mapping-coastal Access this dataset from the Pacific Data Hub.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-federate]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution at 1km resolution derived from 2010
      census data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Census population data from 2010 was spatially gridded at 1km resolution
    and intersected with coastal buffer zones (1km and 5km) to quantify populations
    in coastal proximity. Enumeration area boundaries and household statistics were
    used to distribute population counts across the study area.
  sources:
  - id: source_1
    license: null
    name: Pacific Community Statistics for Development Division (SDD)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-federate
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Federated States of Micronesia (FSM EA boundaries)
  download_url: https://pacificdata.org/data/dataset/59f905cb-536f-419b-addc-e0ef47aa3ffb/resource/e60fd298-25df-4451-adbe-087722678f3b/download/fsm_ea_4326.geojson
  format: null
  id: resource_b9f8760f
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FSM EA boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Federated States of Micronesia (FSM 1km coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/59f905cb-536f-419b-addc-e0ef47aa3ffb/resource/dd015298-0914-49a6-90ec-7b6881507d78/download/fsm1kmbuff_4326.geojson
  format: null
  id: resource_063b1b31
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FSM 1km coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Federated States of Micronesia (FSM 5km coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/59f905cb-536f-419b-addc-e0ef47aa3ffb/resource/be26a1a1-a03d-410e-8ee6-f149309086cd/download/fsm5kmbuff_4326.geojson
  format: null
  id: resource_47991bf4
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FSM 5km coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This spatial 1km resolution grid contains population data generated
    from 2010 FSM PHC. For more information about this dataset please check on https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
    https://sdd.spc.int/mapping-coastal
  download_url: https://pacificdata.org/data/dataset/59f905cb-536f-419b-addc-e0ef47aa3ffb/resource/0aff2a4f-825c-4c20-a6f7-a031661b4c61/download/fsm2010pop.zip
  format: zipped tif
  id: resource_f4fb7b75
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FSM 2010 PopGrid
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Federated States of Micronesia
  download_url: https://pacificdata.org/data/dataset/59f905cb-536f-419b-addc-e0ef47aa3ffb/resource/66c11712-3a53-4fcd-8f96-c3956c6bb024/download/readme.txt
  format: null
  id: resource_77d74ca2
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: README
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-fsm_spc_coastalproximitypopulatio_20190930
spatial:
  bbox: null
  centroid: null
  countries:
  - FSM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-09-30'
temporal_resolution: null
title: Coastal proximity of populations in 22 Pacific Island Countries and Territories
  - Dataset - Federated States of Micronesia
version: null
vulnerability: null
---
