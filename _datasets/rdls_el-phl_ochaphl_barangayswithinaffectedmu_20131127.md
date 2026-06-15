---
attributions:
- entity:
    affiliation: null
    email: null
    name: DSWD DROMIC
    url: https://data.humdata.org/dataset/philippines-affected-persons-locations-0
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NSO
    url: https://data.humdata.org/dataset/philippines-affected-persons-locations-0
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-affected-persons-locations-0
creator:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-affected-persons-locations-0
dataset_id: rdls_el-phl_ochaphl_barangayswithinaffectedmu_20131127
description: 'The dataset used the list of affected municipalities based on DSWD DROMIC
  to identify affected barangays by Typhoon Haiyan/Yolanda. It contains the list of
  barangays within affected municipalities based on DSWD DROMIC (Typhoon Haiyan/Yolanda).
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-affected-persons-locations-0]'
details: '**Languages:** EN'
exposure:
- asset_type:
    description: Residential population in barangays within Typhoon Haiyan-affected
      municipalities
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
  description: The dataset identifies barangays within municipalities officially listed
    as affected by Typhoon Haiyan by DSWD DROMIC, and integrates NSO population data
    to characterize the exposed population. This administrative-level exposure and
    loss dataset supports displacement and humanitarian response assessment in the
    Philippines.
  sources:
  - id: source_1
    license: null
    name: DSWD DROMIC
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: NSO
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-affected-persons-locations-0
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement from Typhoon Haiyan in affected barangays
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
  description: Philippines - Barangays within affected municipalities (Typhoon Haiyan)
    (Typhoon Haiyan Affected Barangays.zip)
  download_url: https://data.humdata.org/dataset/941248ab-1281-4064-94fb-e630aa67340a/resource/cbe8b279-a3f6-4ebe-934d-52da1aad9737/download/typhoon-haiyan-affected-barangays.zip
  format: null
  id: resource_cbe8b279
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon Haiyan Affected Barangays.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-phl_ochaphl_barangayswithinaffectedmu_20131127
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
  start: '2013-11-27'
temporal_resolution: null
title: Philippines - Barangays within affected municipalities (Typhoon Haiyan)
version: null
vulnerability: null
---
