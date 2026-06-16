---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pacific Community Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-vanuatu
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-vanuatu
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-vanuatu
dataset_id: rdls_exp-vut_spc_coastalproximitypopulatio_20190930
description: 'Spatial datasets utilized to conduct the spatial analysis and additional
  information from the research article: Coastal proximity of populations in 22 Pacific
  Island Countries and Territories. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
  https://sdd.spc.int/mapping-coastal Access this dataset from the Pacific Data Hub.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-vanuatu]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution at 1km resolution derived from 2009
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
  description: Population data from the 2009 Vanuatu census was spatially gridded
    at 1km resolution and intersected with coastal buffer zones (1km, 5km, 10km) to
    quantify populations in coastal proximity. Enumeration area boundaries and household
    statistics were used to distribute population counts across the study area.
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
- href: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-vanuatu
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
    Territories - Dataset - Vanuatu (VUT EA boundaries)
  download_url: https://pacificdata.org/data/dataset/71202cb6-3bd2-49f1-8cb5-86be9cd73632/resource/a3b51286-b28d-4b94-aa41-3d6b27e365d9/download/eaid_4326.geojson
  format: null
  id: resource_435d48c0
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VUT EA boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Vanuatu (VUT 1km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/71202cb6-3bd2-49f1-8cb5-86be9cd73632/resource/d6e89a9a-aef9-4d2f-9c95-78b02d2a09dc/download/vut1kmbuff_4326.geojson
  format: null
  id: resource_6c8bc937
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VUT 1km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Vanuatu (VUT 5km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/71202cb6-3bd2-49f1-8cb5-86be9cd73632/resource/2772d17d-bff7-49cb-8396-993c07c9a3b5/download/vut5kmbuff_4326.geojson
  format: null
  id: resource_1087d87e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VUT 5km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Vanuatu (VUT 10km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/71202cb6-3bd2-49f1-8cb5-86be9cd73632/resource/033b10c8-eada-4b3a-b245-afcf6e143286/download/vut10kmbuff_4326.geojson
  format: null
  id: resource_ad35cb9c
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VUT 10km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This spatial 1km resolution grid contains population data generated
    from 2009 Vanuatu PHC. For more information about this dataset please check on
    https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249 https://sdd.spc.int/mapping-coastal
  download_url: https://pacificdata.org/data/dataset/71202cb6-3bd2-49f1-8cb5-86be9cd73632/resource/d165e525-e501-461a-8ce7-707d51fc1afa/download/vutgpsgridall.zip
  format: zipped tif
  id: resource_65ac4c6a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VUT 2009 PopGrid
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-vut_spc_coastalproximitypopulatio_20190930
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
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
  - Dataset - Vanuatu
version: null
vulnerability: null
---
