---
attributions:
- entity:
    affiliation: null
    email: null
    name: SPC Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-fiji
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-fiji
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-fiji
dataset_id: rdls_exp-fji_spc_coastalproximitypopulatio_20190930
description: 'Spatial datasets utilized to conduct the spatial analysis and additional
  information from the research article: Coastal proximity of populations in 22 Pacific
  Island Countries and Territories. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
  https://sdd.spc.int/mapping-coastal Access this dataset from the Pacific Data Hub.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-fiji]'
details: null
exposure:
- asset_type:
    description: Census-based population counts and gridded population data for Fiji
      enumeration areas, with coastal proximity buffers at 1km, 5km, and 10km distances
      from the coastline
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
  description: Census data from the SPC Statistics for Development Division was spatially
    joined with enumeration area boundaries and coastal buffer zones (1km, 5km, 10km)
    derived from coastline geometry. A 2007 population grid (raster) was also produced
    to support analysis of coastal population exposure in Fiji as part of a broader
    22-Pacific Island Countries and Territories study published in PLOS ONE.
  sources:
  - id: source_1
    license: null
    name: SPC Statistics for Development Division (SDD)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-fiji
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
    Territories - Dataset - Fiji (FJI EA boundaries)
  download_url: https://pacificdata.org/data/dataset/e698d4ef-2d0a-4ab5-a2ea-dceae980fef0/resource/2efa5adc-da30-4822-b2ae-bc71a05acfc5/download/fji_eas_32760.geojson
  format: null
  id: resource_d5e4fea1
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FJI EA boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Fiji (FJI 1km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/e698d4ef-2d0a-4ab5-a2ea-dceae980fef0/resource/5c49d19f-a031-4db4-85dc-041a56161f62/download/fji1kmbuff_32760.geojson
  format: null
  id: resource_a4735d01
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FJI 1km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Fiji (FJI 5km coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/e698d4ef-2d0a-4ab5-a2ea-dceae980fef0/resource/611edaae-5eb3-4e39-813b-26787bd9c3dd/download/fji5kmbuff_32760.geojson
  format: null
  id: resource_fd86efae
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FJI 5km coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Fiji (FJI 10km coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/e698d4ef-2d0a-4ab5-a2ea-dceae980fef0/resource/6423d13c-ce57-4d0b-b9c1-beed2e5a944d/download/fji10kmbuff_32760.geojson
  format: null
  id: resource_ed8da27d
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FJI 10km coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This spatial 1km resolution grid contains population data generated
    from 2007 Fiji PHC. For more information about this dataset please check on https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
    https://sdd.spc.int/mapping-coastal
  download_url: https://pacificdata.org/data/dataset/e698d4ef-2d0a-4ab5-a2ea-dceae980fef0/resource/39eca02d-b411-4713-9b91-fb64d9b135eb/download/fijipopgrid2007.zip
  format: zipped tif
  id: resource_fd6b5dec
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FJI 2007 Population grid
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Fiji
  download_url: https://pacificdata.org/data/dataset/e698d4ef-2d0a-4ab5-a2ea-dceae980fef0/resource/0230edff-7daf-4bfa-9c5f-47069b5e14f9/download/readme.txt
  format: null
  id: resource_2204685c
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
slug: rdls_exp-fji_spc_coastalproximitypopulatio_20190930
spatial:
  bbox: null
  centroid: null
  countries:
  - FJI
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
  - Dataset - Fiji
version: null
vulnerability: null
---
