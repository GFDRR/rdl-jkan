---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/haiti-humanitarian-response-plan
creator:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/haiti-humanitarian-response-plan
dataset_id: rdls_lss-hti_ochahti_humanitarianresponseplan
description: 'This dataset is produced by the United Nations for the Coordination
  of Humanitarian Affairs (OCHA) in collaboration with humanitarian partners in Haiti.
  It contains the estimation of people aggregated per geographic locations, sex and
  age who have been targeted for urgent humanitarian response in Haiti. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/haiti-humanitarian-response-plan]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: OCHA Haiti aggregated humanitarian needs assessments and partner input
    to estimate populations requiring urgent humanitarian response by geographic location,
    sex, and age categories for the 2021-2022 Humanitarian Response Plan.
  sources:
  - id: source_1
    license: null
    name: OCHA Haiti
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-humanitarian-response-plan
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People targeted for humanitarian response aggregated by geographic
      location, sex, and age
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
        metric: exposure
        modelling: observed
        type: total
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://reliefweb.int/sites/reliefweb.int/files/resources/hti_hrp_2021-2022_fr.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset contains the estimation of people aggregated per geographic
    locations, sex and age who have been targeted for urgent humanitarian response
    in Haiti
  download_url: https://data.humdata.org/dataset/56e9a4a3-94b6-444d-96ae-27121a296099/resource/63ef99fd-d2b5-4e56-8ecb-89f7da87a9a4/download/hti_target_hrp2021.xlsx
  format: null
  id: resource_63ef99fd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HTI_TARGET_HRP2021.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_ochahti_humanitarianresponseplan
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: 'Haiti : Humanitarian Response Plan'
version: null
vulnerability: null
---
