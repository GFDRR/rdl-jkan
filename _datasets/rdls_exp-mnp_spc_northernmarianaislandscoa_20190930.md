---
attributions:
- entity:
    affiliation: null
    email: null
    name: SPC Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-northern
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-northern
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-northern
dataset_id: rdls_exp-mnp_spc_northernmarianaislandscoa_20190930
description: 'Spatial datasets utilized to conduct the spatial analysis and additional
  information from the research article: Coastal proximity of populations in 22 Pacific
  Island Countries and Territories. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
  https://sdd.spc.int/mapping-coastal Access this dataset from the Pacific Data Hub.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-northern]'
details: null
exposure:
- asset_type:
    description: Gridded and village-level population counts for Northern Mariana
      Islands, with coastal proximity analysis derived from census data and a 1km
      coastal buffer
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
  description: Census population data for the Northern Mariana Islands were spatially
    integrated with a 1km coastal buffer zone and a gridded population raster (PopGrid)
    to assess the proportion of the population living in close proximity to the coast.
    The analysis follows the methodology described in the peer-reviewed study on coastal
    proximity of populations across 22 Pacific Island Countries and Territories (Plos
    ONE, 2019). Village boundaries and household counts from the 2010 census serve
    as the primary input for the spatial analysis.
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
- href: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-northern
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
  description: Northern Mariana Islands - Coastal Proximity of Populations (MNP Village
    boundaries)
  download_url: https://pacificdata.org/data/dataset/f2bbd77a-22f8-45e5-b162-72622a19f162/resource/a0b90e82-1a9c-4e78-bc9b-d2430a5db1b2/download/mnp_vi_4326.geojson
  format: null
  id: resource_eb36f62b
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP Village boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Coastal Proximity of Populations (CNMI 1km
    Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/f2bbd77a-22f8-45e5-b162-72622a19f162/resource/dafe5d0c-a6bc-41c4-a31e-a330dea21938/download/mnp_1kmbuff_4326.geojson
  format: null
  id: resource_796f8877
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CNMI 1km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This spatial 1km resolution grid contains population data generated
    from 2010 PHC. For more information about this dataset please check on https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
    https://sdd.spc.int/mapping-coastal
  download_url: https://pacificdata.org/data/dataset/f2bbd77a-22f8-45e5-b162-72622a19f162/resource/7848b622-33da-4ca9-bc8d-550edae54f39/download/rmgpssgrd.zip
  format: zipped tif
  id: resource_bc6156e1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CNMI PopGrid
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Coastal Proximity of Populations (MNP README)
  download_url: https://pacificdata.org/data/dataset/f2bbd77a-22f8-45e5-b162-72622a19f162/resource/98c7fc8f-df86-4778-8ba4-488760288591/download/readme.txt
  format: null
  id: resource_76bd5cd6
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MNP README
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mnp_spc_northernmarianaislandscoa_20190930
spatial:
  bbox: null
  centroid: null
  countries:
  - MNP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-09-30'
temporal_resolution: null
title: Northern Mariana Islands - Coastal Proximity of Populations
version: null
vulnerability: null
---
