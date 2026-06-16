---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/impact-data-casualties-and-damage-typhoon-haiyan-yolanda
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/impact-data-casualties-and-damage-typhoon-haiyan-yolanda
dataset_id: rdls_lss-phl_nlrc510_impactdatacasualtiesdamag_20140127
description: 'Counts of damage and casualties from official data sets. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/impact-data-casualties-and-damage-typhoon-haiyan-yolanda]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event impact data compiled from official government sources (DSWD
    DROMIC consolidated reports) and census records documenting casualties and building
    damage caused by Typhoon Haiyan. Data aggregated and standardized by Netherlands
    Red Cross for humanitarian response documentation.
  sources:
  - id: source_1
    license: null
    name: Netherlands Red Cross - 510
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/impact-data-casualties-and-damage-typhoon-haiyan-yolanda
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Typhoon Haiyan
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Fatalities from Typhoon Haiyan
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
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
    description: Injuries from Typhoon Haiyan
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Impact data - casualties and damage - Typhoon Haiyan
    (Yolanda) (Excel)
  download_url: https://data.humdata.org/dataset/23efa9ad-5b20-43e1-bf2b-0c90226ff956/resource/e2c6c7b4-ea5c-4ad3-90f1-447cef0ec334/download/effects-of-typhoon-yolanda-casualties.xlsx
  format: null
  id: resource_e2c6c7b4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Effects of typhoon Yolanda - Casualties.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Impact data - casualties and damage - Typhoon Haiyan
    (Yolanda) (Excel)
  download_url: https://data.humdata.org/dataset/23efa9ad-5b20-43e1-bf2b-0c90226ff956/resource/39008847-ae7b-4873-8396-a3ea4f578da2/download/typhoon-yolanda-dswd-dromic-consolidated-27jan2014.xlsx
  format: null
  id: resource_39008847
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon-Yolanda-DSWD-DROMIC-Consolidated-27Jan2014.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Impact data - casualties and damage - Typhoon Haiyan
    (Yolanda) (removed formatting and pcoded version)
  download_url: https://data.humdata.org/dataset/23efa9ad-5b20-43e1-bf2b-0c90226ff956/resource/70241948-30cf-465f-818f-12a3af30e4ae/download/typhoon-yolanda-dswd-dromic-consolidated-27jan2014_pcoded.csv
  format: null
  id: resource_70241948
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon-Yolanda-DSWD-DROMIC-Consolidated-27Jan2014_pcoded.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_nlrc510_impactdatacasualtiesdamag_20140127
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
  start: '2014-01-27'
temporal_resolution: null
title: Philippines - Impact data - casualties and damage - Typhoon Haiyan (Yolanda)
version: null
vulnerability: null
---
