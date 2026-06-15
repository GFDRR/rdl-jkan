---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/south-sudan-county-population-estimates-2008-2015
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: LandScan
    url: https://data.humdata.org/dataset/south-sudan-county-population-estimates-2008-2015
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: United Nations
    url: https://data.humdata.org/dataset/south-sudan-county-population-estimates-2008-2015
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Drew University (inactive)
  url: https://data.humdata.org/dataset/south-sudan-county-population-estimates-2008-2015
creator:
  affiliation: null
  email: null
  name: Drew University (inactive)
  url: https://data.humdata.org/dataset/south-sudan-county-population-estimates-2008-2015
dataset_id: rdls_exp-ssd_drew_countypopulationestimates_20160513
description: 'County populations for South Sudan compiled from multiple sources (WorldPop,
  LandScan, and the UN from 2008-2015), including estimates of county population changes
  (2014-2015) due to internal migration.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/south-sudan-county-population-estimates-2008-2015]'
details: Though population estimates are published from a variety of sources, verification
  and validation for county population totals are needed.
exposure:
- asset_type:
    description: County-level population estimates for South Sudan from 2008-2015,
      including internal migration-driven changes
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
  description: County-level population estimates were compiled from three sources
    (WorldPop, LandScan, and UN data) covering 2008-2015, with additional processing
    to capture internal migration-driven population changes between 2014-2015. The
    dataset integrates census data with modeled population distributions to provide
    sub-national exposure baseline for disaster risk assessment.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: LandScan
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: United Nations
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/south-sudan-county-population-estimates-2008-2015
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'County Populations for South Sudan compiled from multiple sources:
    WorldPop, LandScan, and the UN from 2008-2015.'
  download_url: https://data.humdata.org/dataset/ad80f355-4c4e-430c-a550-76cb2a9bce1b/resource/12d69d06-5422-4f77-bb22-c06b29c8dd54/download/south-sudan-county-population-estimates-december-2015.xlsx
  format: null
  id: resource_12d69d06
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: South Sudan - County Population Estimates.xlsx
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_drew_countypopulationestimates_20160513
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-05-13'
temporal_resolution: null
title: South Sudan - County Population Estimates - 2008-2015
version: null
vulnerability: null
---
