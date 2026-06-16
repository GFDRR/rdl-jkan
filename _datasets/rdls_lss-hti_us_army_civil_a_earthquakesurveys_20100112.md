---
attributions:
- entity:
    affiliation: null
    email: null
    name: US Army Civil Affairs
    url: https://data.humdata.org/dataset/haiti-earthquake-surveys
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: US Army Civil Affairs (inactive)
  url: https://data.humdata.org/dataset/haiti-earthquake-surveys
creator:
  affiliation: null
  email: null
  name: US Army Civil Affairs (inactive)
  url: https://data.humdata.org/dataset/haiti-earthquake-surveys
dataset_id: rdls_lss-hti_us_army_civil_a_earthquakesurveys_20100112
description: 'The US Army Civil Affairs collected surveys after the 2010 Haiti earthquake..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/haiti-earthquake-surveys]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: The US Army Civil Affairs conducted field surveys following the January
    2010 Haiti earthquake to assess damage to buildings and civil infrastructure.
    Survey data were collected through sample survey methodology and compiled into
    a spatial geodataset with multiple damage assessment attributes.
  sources:
  - id: source_1
    license: null
    name: US Army Civil Affairs
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-earthquake-surveys
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Post-event building damage assessment from the 2010 Haiti earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti earthquake surveys (The US Army Civil Affairs collected surveys
    after the 2010 Haiti earthquake.)
  download_url: https://data.humdata.org/dataset/edfcf185-f936-4622-b23c-e10355a4d545/resource/6d6b0e3c-207f-4c47-908c-c5c1f26f3667/download/cim_project_ii.shp.zip
  format: null
  id: resource_6d6b0e3c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CIM_Project_II.shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_us_army_civil_a_earthquakesurveys_20100112
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2010-01-12'
temporal_resolution: null
title: Haiti earthquake surveys
version: null
vulnerability: null
---
