---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Methodist Group
    url: https://data.humdata.org/dataset/ruby-evacuation-centers
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Standby Task Force (inactive)
  url: https://data.humdata.org/dataset/ruby-evacuation-centers
creator:
  affiliation: null
  email: null
  name: Standby Task Force (inactive)
  url: https://data.humdata.org/dataset/ruby-evacuation-centers
dataset_id: rdls_el-phl_sbtf_typhoonrubyhagupitevacuat_20141206
description: 'Preliminary list of evacuation centers - likely to be updated. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/ruby-evacuation-centers]'
details: List needs additional info
exposure:
- asset_type:
    description: Evacuated population sheltered in designated evacuation centers
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
  description: Preliminary evacuation center registry compiled by United Methodist
    Group field teams during Typhoon Ruby (Hagupit) response in the Philippines, documenting
    shelter locations and displaced population counts as part of humanitarian emergency
    response operations.
  sources:
  - id: source_1
    license: null
    name: United Methodist Group
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ruby-evacuation-centers
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement due to Typhoon Ruby (Hagupit) requiring evacuation
      center shelter
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
  description: Philippines - Typhoon Ruby (Hagupit) Evacuation Centers (List still
    beeing worked on)
  download_url: https://docs.google.com/a/standbytaskforce.com/spreadsheets/d/1zrF4LtgeBxfIrV51p5tYLoIDqiZGhv6htLOg5E-Bf2M/edit#gid=0
  format: Google Sheet
  id: resource_60af4c10
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ruby-evacuation-centers
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Typhoon Ruby (Hagupit) Evacuation Centers (Live CSV export
    from the Google Sheet.)
  download_url: https://docs.google.com/a/megginson.com/spreadsheets/d/1zrF4LtgeBxfIrV51p5tYLoIDqiZGhv6htLOg5E-Bf2M/export?format=csv&id=1zrF4LtgeBxfIrV51p5tYLoIDqiZGhv6htLOg5E-Bf2M&gid=0
  format: null
  id: resource_cc141c65
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ruby-evacuation-centres.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Typhoon Ruby (Hagupit) Evacuation Centers (Live link
    to Google Sheets export.)
  download_url: https://docs.google.com/a/megginson.com/spreadsheets/d/1zrF4LtgeBxfIrV51p5tYLoIDqiZGhv6htLOg5E-Bf2M/export?format=xlsx&id=1zrF4LtgeBxfIrV51p5tYLoIDqiZGhv6htLOg5E-Bf2M
  format: null
  id: resource_0c89daa1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ruby-evacuation-centres.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-phl_sbtf_typhoonrubyhagupitevacuat_20141206
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
  start: '2014-12-06'
temporal_resolution: null
title: Philippines - Typhoon Ruby (Hagupit) Evacuation Centers
version: null
vulnerability: null
---
