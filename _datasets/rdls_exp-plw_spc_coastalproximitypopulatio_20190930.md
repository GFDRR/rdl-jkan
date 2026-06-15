---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pacific Community Statistics for Development Division (SPC SDD)
    url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-palau
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-palau
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-palau
dataset_id: rdls_exp-plw_spc_coastalproximitypopulatio_20190930
description: 'Spatial datasets utilized to conduct the spatial analysis and additional
  information from the research article: Coastal proximity of populations in 22 Pacific
  Island Countries and Territories. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
  https://sdd.spc.int/mapping-coastal Access this dataset from the Pacific Data Hub.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-palau]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution at 1km resolution derived from 2015
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Population data from the 2015 Palau census was gridded at 1km resolution
    and spatially intersected with a 1km coastal buffer zone to quantify coastal population
    proximity. Enumeration area boundaries and household/population statistics were
    used to distribute census counts across the study area.
  sources:
  - id: source_1
    license: null
    name: Pacific Community Statistics for Development Division (SPC SDD)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-palau
  rel: source
loss:
  losses: []
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
    Territories - Dataset - Palau (PLW EA boundaries)
  download_url: https://pacificdata.org/data/dataset/3b3794fa-b14b-4dcf-8040-c02fa81471e4/resource/c9146cfe-85af-41af-9b8b-5975e107ac8c/download/plw-ea_4326.geojson
  format: null
  id: resource_7006c00b
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PLW EA boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Palau (PLW 1km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/3b3794fa-b14b-4dcf-8040-c02fa81471e4/resource/329126eb-f818-4436-b6a2-10013b510f60/download/plw1kmbuff_4326.geojson
  format: null
  id: resource_eaa74bc4
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PLW 1km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This spatial 1km resolution grid contains population data generated
    from 2015 Palau PHC. For more information about this dataset please check on https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
    https://sdd.spc.int/mapping-coastal
  download_url: https://pacificdata.org/data/dataset/3b3794fa-b14b-4dcf-8040-c02fa81471e4/resource/f91cc8bc-bf96-439a-b24e-b77e8a466051/download/plwgpsgrd.zip
  format: zipped tif
  id: resource_47519f51
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PLW 2015 PopGrid
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Palau (PLW README)
  download_url: https://pacificdata.org/data/dataset/3b3794fa-b14b-4dcf-8040-c02fa81471e4/resource/b61c161f-2123-4552-abeb-36e1bc339b45/download/readme.txt
  format: null
  id: resource_d7d6effc
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PLW README
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-plw_spc_coastalproximitypopulatio_20190930
spatial:
  bbox: null
  centroid: null
  countries:
  - PLW
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
  - Dataset - Palau
version: null
vulnerability: null
---
