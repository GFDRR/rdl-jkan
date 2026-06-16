---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/unicef-burundi-great-lakes-30-june-2017
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNICEF Country Offices Situation Reports
    url: https://data.humdata.org/dataset/unicef-burundi-great-lakes-30-june-2017
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNICEF Eastern and Southern Africa Regional Office (ESARO) (inactive)
  url: https://data.humdata.org/dataset/unicef-burundi-great-lakes-30-june-2017
creator:
  affiliation: null
  email: null
  name: UNICEF Eastern and Southern Africa Regional Office (ESARO) (inactive)
  url: https://data.humdata.org/dataset/unicef-burundi-great-lakes-30-june-2017
dataset_id: rdls_lss-bdicodrwatzauga_unicefesaro_greatlakes30june2017_20170630
description: 'Dashboard about UNICEF Great Lakes Needs and Response (Refugees). [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unicef-burundi-great-lakes-30-june-2017]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNICEF ESARO compiled refugee and displacement data from UNHCR and
    country office situation reports for the Great Lakes region as of June 2017, aggregating
    needs and response metrics across multiple countries affected by regional displacement
    crises.
  sources:
  - id: source_1
    license: null
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: UNICEF Country Offices Situation Reports
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unicef-burundi-great-lakes-30-june-2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Refugee and displaced population counts from Great Lakes region conflict
      and displacement crisis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: UNICEF Burundi Great Lakes 30 June 2017 (UNICEF Funding, needs and
    response database)
  download_url: https://data.humdata.org/dataset/abf58988-c4d7-4515-9dcd-1cddda34f7e8/resource/eb5ee3e5-1f37-4c4a-b20d-c5fd558872f9/download/regional-database_july16-2017-esaro.xlsx
  format: null
  id: resource_eb5ee3e5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Regional database_july16 2017- ESARO.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bdicodrwatzauga_unicefesaro_greatlakes30june2017_20170630
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  - BDI
  - RWA
  - UGA
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-06-30'
temporal_resolution: null
title: UNICEF Burundi Great Lakes 30 June 2017
version: null
vulnerability: null
---
