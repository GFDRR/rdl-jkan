---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: DataGURU
  url: https://doi.org/10.18161/global_popcount.201610
creator:
  affiliation: null
  email: null
  name: DataGURU
  url: https://doi.org/10.18161/global_popcount.201610
dataset_id: rdls_exp-crstac_globalfuturepopulation_projections
description: "Global 30 arc seconds (\u223C1 km at the equator) population projection\
  \ dataset covering each year from 2010 to 2100 that is consistent with both country\
  \ level population and gridded urban fractions from the Coupled Model Intercomparison\
  \ Project 6 (CMIP6), based on RCP and SSP scenarios. Climate scenarios (as published):\
  \ \"SSP-RCP combinations\" [Source: This metadata record was automatically extracted\
  \ from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]"
details: null
exposure:
- asset_type:
    description: population number
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
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: "Global 30 arc seconds (\u223C1 km at the equator) population projection\
    \ dataset covering each year from 2010 to 2100 that is consistent with both country\
    \ level population and gridded urban fractions from the Coupled Model Intercomparison\
    \ Project 6 (CMIP6), based on RCP and SSP scenarios."
  sources:
  - id: source_underlying_1
    license: null
    name: urban fraction (CMIP6)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_3
    license: null
    name: roads
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_4
    license: null
    name: urban extent
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://github.com/niklasbokeolen/world_population
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: DataGURU
  url: https://doi.org/10.18161/global_popcount.201610
purpose: 6 combinations of SSPs and RCPs from CMIP available; download via interface
  or ftp
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1016/j.dib.2022.107804
  id: ref_doi
  name: null
  url: https://doi.org/10.1016/j.dib.2022.107804
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/population/global-future-population/projections/projections.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Global future population - Projections'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global future population - Projections - data file
  download_url: https://doi.org/10.18161/global_popcount.201610
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global future population - Projections - data file
- access_url: https://doi.org/10.1016/j.dib.2022.107804
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global future population - Projections (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
- access_url: https://github.com/niklasbokeolen/world_population
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global future population - Projections (Code link)
  download_url: null
  format: Web reference
  id: resource_link_codelink
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Code link
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_globalfuturepopulation_projections
spatial:
  bbox:
  - -180.0
  - -56.0
  - 180.0
  - 84.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 926
temporal:
  central_year: null
  duration: null
  end: '2100'
  start: '2010'
temporal_resolution: P1Y
title: Global future population - Projections
version: null
vulnerability: null
---
