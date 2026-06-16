---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
    url: https://data.humdata.org/dataset/car-displacement-data-bangui-floods-oct19-site-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/car-displacement-data-bangui-floods-oct19-site-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/car-displacement-data-bangui-floods-oct19-site-assessment-iom-dtm
dataset_id: rdls_hl-caf_iom_cardisplacementdatabangui_201911
description: 'Following the rains that hit certain areas of the country as early as
  21 October, flooding cases involving the displacement of populations are mentioned
  in some localities of the country. IOM through its Displacement Tracking Matrix
  (DTM) conducted rapid assessments in the districts of Bangui 2nd, Bangui 6th, Bangui
  7th, and Bombo.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/car-displacement-data-bangui-floods-oct19-site-assessment-iom-dtm]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted rapid site assessments following October 2019 rainfall
    events that triggered flooding and population displacement in Bangui and surrounding
    areas. Assessment data was collected through field surveys in affected districts
    to document displacement impacts.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/car-displacement-data-bangui-floods-oct19-site-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement resulting from October 2019 flooding in Bangui
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
  description: Central African Republic - CAR Displacement Data - Bangui Floods Oct19
    - Site Assessment [IOM DTM] (DTM CAR Bangui Floods Oct19 Site Assessment)
  download_url: https://data.humdata.org/dataset/6f6a0a72-0699-498d-8e27-b6d593898aa3/resource/9963ba32-bd72-4c25-96cd-d28ad9cd7e75/download/dtm-car-bangui-floods-oct19-site-assessment.xlsx
  format: null
  id: resource_9963ba32
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CAR Bangui Floods Oct19 Site Assessment
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-caf_iom_cardisplacementdatabangui_201911
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-11-10'
  start: '2019-11-04'
temporal_resolution: null
title: Central African Republic - CAR Displacement Data - Bangui Floods Oct19 - Site
  Assessment [IOM DTM]
version: null
vulnerability: null
---
