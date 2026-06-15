---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM)
    url: https://data.humdata.org/dataset/hdx-hapi-idps
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-idps
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/hdx-hapi-idps
dataset_id: rdls_lss-hdxapi_hdxhapiaffectedpeopleinte_2010
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation . Warnings typically indicate
  corrections have been made to the data or show things to look out for. Rows with
  only warnings are considered complete, and are made available via the API. Errors
  usually mean that the data is incomplete or unusable. Rows with any errors are not
  present in the API but are included here for transparency.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-idps]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Internally displaced persons data sourced from IOM registry systems
    and aggregated through the HDX Humanitarian API (HAPI) to provide standardized,
    interoperable humanitarian indicators at multiple administrative levels with temporal
    tracking across reporting rounds.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-idps
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Count of internally displaced persons by administrative location
      and reporting period
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'HDX HAPI - Affected People: Internally-Displaced Persons (IDPs data
    from HDX HAPI, please see the documentation for more information)'
  download_url: https://data.humdata.org/dataset/9624d40f-13f7-43ba-9974-724064ed3d5b/resource/51b4912b-7d25-4a9a-8b77-6d3ed253184a/download/hdx_hapi_idps_global.csv
  format: null
  id: resource_51b4912b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Affected People: Internally-Displaced Persons'
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hdxapi_hdxhapiaffectedpeopleinte_2010
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2010-06-30'
temporal_resolution: null
title: 'HDX HAPI - Affected People: Internally-Displaced Persons'
version: null
vulnerability: null
---
