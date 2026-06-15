---
attributions:
- entity:
    affiliation: null
    email: null
    name: AOAV's explosive violence monitor
    url: https://data.humdata.org/dataset/explosive-violence-in-schools-2011-2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Action on Armed Violence
  url: https://data.humdata.org/dataset/explosive-violence-in-schools-2011-2017
creator:
  affiliation: null
  email: null
  name: Action on Armed Violence
  url: https://data.humdata.org/dataset/explosive-violence-in-schools-2011-2017
dataset_id: rdls_el-aoav_explosiveschools20112017_20180727
description: 'Using data from AOAV''s explosive violence monitor, this dataset focuses
  on the casualties recorded from the use of explosive weapons in/on schools globally,
  between 2011-2017.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/explosive-violence-in-schools-2011-2017]'
details: This dataset only includes attacks on schools using explosive weapons and
  where at least one death or injury was recorded.
exposure:
- asset_type:
    description: School facilities exposed to explosive violence
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: AOAV compiled incident-level casualty records from explosive violence
    events occurring in or on schools worldwide between 2011-2017 using their explosive
    violence monitoring methodology. The dataset aggregates observed post-event impact
    data (deaths and injuries) by incident location and date to create a global inventory
    of school-based explosive violence impacts.
  sources:
  - id: source_1
    license: null
    name: AOAV's explosive violence monitor
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/explosive-violence-in-schools-2011-2017
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Casualty figures from explosive violence incidents in schools
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Injury counts from explosive violence incidents in schools
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://aoav.org.uk/explosiveviolence/methodology/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: explosive violence in schools.xlsx
  download_url: https://data.humdata.org/dataset/7c1477ce-83a4-4c97-bf00-78ca52407ea5/resource/810ac409-7bab-42fa-8960-39a5f8978466/download/explosive-violence-in-schools.xlsx
  format: null
  id: resource_810ac409
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: explosive violence in schools.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-aoav_explosiveschools20112017_20180727
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
  end: null
  start: '2018-07-27'
temporal_resolution: null
title: Explosive violence in schools 2011-2017
version: null
vulnerability: null
---
