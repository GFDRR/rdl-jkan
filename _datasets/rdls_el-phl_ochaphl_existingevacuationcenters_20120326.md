---
attributions:
- entity:
    affiliation: null
    email: null
    name: Department of Social Welfare and Development Regional Office
    url: https://data.humdata.org/dataset/philippines-other-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-other-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0
creator:
  affiliation: null
  email: null
  name: OCHA Philippines
  url: https://data.humdata.org/dataset/philippines-other-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0
dataset_id: rdls_el-phl_ochaphl_existingevacuationcenters_20120326
description: 'This dataset is about the Humanitarian Profile in the TS Washi Emergency.
  It shows the existing Evacuation Centers and Relocation sites in Cagayan de Oro
  and Iligan City in Mindanao, Philippines due to the Tropical Storm Washi Flashflood.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-other-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0]'
details: For updates use link provided by DSWD RO 10 [www.tinyurl.com/sendong-report-xls](http://www.tinyurl.com/sendong-report-xls)
exposure:
- asset_type:
    description: Evacuated and relocated population from Tropical Storm Washi flooding
      in Cagayan de Oro and Iligan City
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
  description: Post-event humanitarian assessment data collected by the Department
    of Social Welfare and Development documenting the locations and populations of
    evacuation centers and relocation sites established in response to Tropical Storm
    Washi flooding in Cagayan de Oro and Iligan City, Mindanao in December 2011.
  sources:
  - id: source_1
    license: null
    name: Department of Social Welfare and Development Regional Office
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-other-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displaced and housed in evacuation centers and relocation
      sites due to Tropical Storm Washi fluvial flooding
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
  description: Philippines - Existing Evacuation Centers and Relocation sites(TS Washi
    Emergency) (Excel)
  download_url: https://data.humdata.org/dataset/42d20631-8c8c-4c9e-af1b-9a1062c533a6/resource/012885f5-cbde-401c-9556-878466d450b4/download/humanitarian_profile_tswashi_26march2012.xls
  format: null
  id: resource_012885f5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: humanitarian_profile_tswashi_26march2012.xls
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-phl_ochaphl_existingevacuationcenters_20120326
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
  start: '2012-03-26'
temporal_resolution: null
title: Philippines - Existing Evacuation Centers and Relocation sites(TS Washi Emergency)
version: null
vulnerability: null
---
