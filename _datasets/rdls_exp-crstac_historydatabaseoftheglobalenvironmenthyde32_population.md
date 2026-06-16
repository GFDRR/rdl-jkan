---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Utrecht University
  url: https://doi.org/10.24416/UU01-XUTQN5
creator:
  affiliation: null
  email: null
  name: Utrecht University
  url: https://doi.org/10.24416/UU01-XUTQN5
dataset_id: rdls_exp-crstac_historydatabaseoftheglobalenvironmenthyde32_population
description: 'Population is represented by maps of total, urban, rural population
  and population density [Source: This metadata record was automatically extracted
  from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
license: CC-BY-4.0
lineage:
  description: This database presents an update and expansion of the History Database
    of the Global Environment (HYDE, v 3.2.1). HYDE is and internally consistent combination
    of updated historical population estimates and land use. Categories include cropland,
    with a new distinction into irrigated and rain fed crops (other than rice) and
    irrigated and rain fed rice. Also grazing lands are provided, divided into more
    intensively used pasture, converted rangeland and non-converted natural (less
    intensively used) rangeland. Population is represented by maps of total, urban,
    rural population and population density as well as built-up area.
  sources:
  - id: source_underlying_1
    license: null
    name: based on LandScan population (no open license) + ESA CCI land cover
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Utrecht University
  url: https://doi.org/10.24416/UU01-XUTQN5
purpose: the data are available from 10000 BC to 2015; download in zip files
referenced_by:
- author_names: null
  date_published: null
  doi: 10.5194/essd-9-927-2017
  id: ref_doi
  name: null
  url: https://doi.org/10.5194/essd-9-927-2017
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/population/history-database-of-the-global-environment-hyde32/population/population.json
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
  title: 'STAC Item: History Database of the Global Environment (HYDE3.2) - population'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: History Database of the Global Environment (HYDE3.2) - population -
    data file
  download_url: https://geo.public.data.uu.nl/vault-hyde-data/HYDE%203.2%5B1648738557%5D/original/baseline.zip
  format: null
  id: resource_data-file_1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: History Database of the Global Environment (HYDE3.2) - population - data
    file
- access_url: https://doi.org/10.5194/essd-9-927-2017
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: History Database of the Global Environment (HYDE3.2) - population (Web
    reference)
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
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_historydatabaseoftheglobalenvironmenthyde32_population
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 9259
temporal:
  central_year: null
  duration: null
  end: '2015'
  start: '9999'
temporal_resolution: null
title: History Database of the Global Environment (HYDE3.2) - population
version: null
vulnerability: null
---
