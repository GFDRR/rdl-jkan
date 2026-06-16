---
attributions:
- entity:
    affiliation: null
    email: null
    name: NDRRMC (National Disaster Risk Reduction and Management Council)
    url: https://data.humdata.org/dataset/impact-data-casualties-and-damage-typhoon-haima-lawin
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/impact-data-casualties-and-damage-typhoon-haima-lawin
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/impact-data-casualties-and-damage-typhoon-haima-lawin
dataset_id: rdls_lss-phl_nlrc510_impactdatacasualtiesdamag_20161024
description: 'NDRRMC report of October 28th 2016. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/impact-data-casualties-and-damage-typhoon-haima-lawin]'
details: The NDRRMC report of October 24th 2016 seems to be a partial count of municipalities
  affected
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event damage and casualty data collected by NDRRMC through field
    assessments and compiled into situation reports (SitReps) dated October 25-November
    2, 2016. Data includes municipality-level damage counts, house damage records
    with geographic coding (pcode), and comparative analysis between predicted and
    actual impacts. The dataset represents direct observational records of building
    damage and affected populations following Typhoon Haima's passage through the
    Philippines.
  sources:
  - id: source_1
    license: null
    name: NDRRMC (National Disaster Risk Reduction and Management Council)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/impact-data-casualties-and-damage-typhoon-haima-lawin
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Typhoon Haima (tropical cyclone)
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
  - asset_category: buildings
    asset_dimension: structure
    description: Casualties and affected population from Typhoon Haima
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
        metric: exposure
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
  description: Philippines - Impact data - casualties and damage - Typhoon Haima (Lawin)
    (pcoded and cleaned version of the impact data)
  download_url: https://data.humdata.org/dataset/42aeff07-3962-4195-95f1-9251f3205438/resource/9dd32a91-77aa-45b7-8441-8ce5af6b08f2/download/haima_houses_damaged_pcoded.csv
  format: null
  id: resource_9dd32a91
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: haima_houses_damaged_pcoded.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: comparison between prediction and real value for the haima data, it
    includes priority zone comparison as well
  download_url: https://data.humdata.org/dataset/42aeff07-3962-4195-95f1-9251f3205438/resource/f49520fe-09ec-4ba0-8609-de0895b28042/download/prediction_reality_comparison.csv
  format: null
  id: resource_f49520fe
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prediction_reality_comparison.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Impact data - casualties and damage - Typhoon Haima (Lawin)
    (NDRRCM counts)
  download_url: https://data.humdata.org/dataset/42aeff07-3962-4195-95f1-9251f3205438/resource/86ef2533-b72c-4029-a86e-66e2529fe7dc/download/phl_haima_houses_damaged_pcoded_ndrrmc_sitrep_9_20161025.csv
  format: null
  id: resource_86ef2533
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PHL_haima_houses_damaged_pcoded_ndrrmc_sitrep_9_20161025.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Impact data - casualties and damage - Typhoon Haima (Lawin)
    (DSWD counts)
  download_url: https://data.humdata.org/dataset/42aeff07-3962-4195-95f1-9251f3205438/resource/14bc94e3-f629-40dd-a7a8-957606ef8ed9/download/2016_11_02_rii_damage_by_municipality_pcoded.xlsx
  format: null
  id: resource_14bc94e3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2016_11_02_RII_damage_by_municipality_pcoded.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Impact data - casualties and damage - Typhoon Haima (Lawin)
    (CSV)
  download_url: https://data.humdata.org/dataset/42aeff07-3962-4195-95f1-9251f3205438/resource/aa1b7fe6-0e15-46b2-b7dd-d42acad6f62e/download/dromic-sty-lawin-master-excel-as-of-2-nov-2016-9pm_pcoded.csv
  format: null
  id: resource_aa1b7fe6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DROMIC-STY-Lawin-Master-Excel-as-of-2-Nov-2016-9PM_PCODED.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_nlrc510_impactdatacasualtiesdamag_20161024
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
  start: '2016-10-24'
temporal_resolution: null
title: Philippines - Impact data - casualties and damage - Typhoon Haima (Lawin)
version: null
vulnerability: null
---
