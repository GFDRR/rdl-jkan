---
attributions:
- entity:
    affiliation: null
    email: null
    name: Department of Social Welfare Department (DSWD)
    url: https://data.humdata.org/dataset/philippines-affected-persons-locations
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-affected-persons-locations
creator:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-affected-persons-locations
dataset_id: rdls_lss-phl_ochaphl_affectedpersonslocations_20131129
description: 'Priority municipalities: Within Yolanda''S 50Km Radius Haiyan (Yoland)
  corridor: Data on Displaced Families And Persons Located Within 50Km Radius of Yolandas
  Data identifies the 171 priority municipalities identified by the government. Data
  was received 3 Dec 2013 as PDF from DSWD and converted to excel. Pcodes (PSGC from
  government) were added to be able to link the data to spatial files for mapping.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-affected-persons-locations]'
details: '**Languages:** EN'
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event displacement data collected by DSWD on 3 December 2013 following
    Typhoon Haiyan (Yolanda), received as PDF and converted to Excel format with PSGC
    codes added for spatial linkage to administrative boundaries and mapping of affected
    populations within the 50km priority corridor.
  sources:
  - id: source_1
    license: null
    name: Department of Social Welfare Department (DSWD)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-affected-persons-locations
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displaced families and persons affected by Typhoon Haiyan (Yolanda)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: Philippines - Affected Persons Locations (Priority Municipalities within
    Yolanda 50km Radius DSWD.xls)
  download_url: https://data.humdata.org/dataset/b57e5751-7222-4ece-9c94-9b9986f275b7/resource/e21c06da-ad0d-4b72-aaa2-7387e066d00c/download/priority-municipalities-within-yolanda-50km-radius-dswd.xls
  format: null
  id: resource_e21c06da
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Priority Municipalities within Yolanda 50km Radius DSWD.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_ochaphl_affectedpersonslocations_20131129
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2013-11-29'
temporal_resolution: null
title: Philippines - Affected Persons Locations
version: null
vulnerability: null
---
