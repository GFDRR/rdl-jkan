---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNAMA (United Nations Assistance Mission in Afghanistan)
    url: https://data.humdata.org/dataset/afghanistan-casualties
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-casualties
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-casualties
dataset_id: rdls_lss-afg_ochaafg_casualties_20181231
description: 'Total number of civilian casualties documented in each of Afghanistan''s
  34 provinces, the top three causes of civilian casualties in each province, and
  the percentage increase or decrease compared to 2017. For more, refer to the report
  from UNAMA. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-casualties]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Civilian casualty data compiled by UNAMA from documented incidents
    across Afghanistan's 34 provinces in 2018, with causes of death classified and
    compared to 2017 baseline to track trends in conflict-related and disaster-related
    mortality.
  sources:
  - id: source_1
    license: null
    name: UNAMA (United Nations Assistance Mission in Afghanistan)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-casualties
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Civilian fatalities from convective storms (one of top three causes)
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
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Civilian fatalities from earthquakes (one of top three causes)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Civilian fatalities from strong winds (one of top three causes)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
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
  url: https://www.af.one.un.org/wp-content/uploads/2019/02/afghanistan_protection_of_civilians_annual_report_2018_final_24_feb_2019_v3.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Casualties (Excel)
  download_url: https://data.humdata.org/dataset/69c1139c-4a4c-4c39-8af9-b57a20739f6b/resource/cd02b8df-2cb9-4ca2-abba-ff73f31615a6/download/afg_casualties_2018.xlsx
  format: null
  id: resource_cd02b8df
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_casualties_2018.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochaafg_casualties_20181231
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-12-31'
temporal_resolution: null
title: Afghanistan - Casualties
version: null
vulnerability: null
---
