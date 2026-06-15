---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNOSAT
    url: https://data.humdata.org/dataset/haiti-earthquake-damage-assessment
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: ACAPS
  url: https://data.humdata.org/dataset/haiti-earthquake-damage-assessment
creator:
  affiliation: null
  email: null
  name: ACAPS
  url: https://data.humdata.org/dataset/haiti-earthquake-damage-assessment
dataset_id: rdls_el-hti_acaps_earthquakedamageassessmen_20210827
description: 'Haiti Earthquake (M7.2) Preliminary Satellite-Based Comprehensive -
  Damage assessment (Grande''Anse, South, and Nippes departments of Haiti, 27 August
  2021). [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/haiti-earthquake-damage-assessment]'
details: null
exposure:
- asset_type:
    description: Building stock in Grande'Anse, South, and Nippes departments assessed
      for earthquake damage
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
  description: Satellite imagery from the M7.2 Haiti earthquake (14 August 2021) was
    analyzed by UNOSAT to produce a comprehensive damage assessment. Building damage
    and affected population counts were derived through visual interpretation and
    automated analysis of pre- and post-event satellite imagery for three departments
    (Grande'Anse, South, Nippes), generating direct impact metrics for earthquake-affected
    assets.
  sources:
  - id: source_1
    license: null
    name: UNOSAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-earthquake-damage-assessment
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from M7.2 earthquake assessed via satellite
      imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
    description: Affected population in earthquake-impacted departments
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://reliefweb.int/sites/reliefweb.int/files/resources/Preliminary_SatelliteBased_ComprehensiveDamageAssessment_EQ20210814HTI_20210827_Haiti.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti Earthquake - Damage assessment (Damage Assessment)
  download_url: https://data.humdata.org/dataset/a4b01dc1-f860-4894-a25a-0113186c0cb0/resource/909ae9fe-75a9-4678-8ec1-b137367e6bd6/download/20210827-unosat-satellite-based-comprehensive-damage-assessment.xlsx
  format: null
  id: resource_909ae9fe
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20210827 UNOSAT Satellite-Based Comprehensive Damage Assessment.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-hti_acaps_earthquakedamageassessmen_20210827
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-27'
temporal_resolution: null
title: Haiti Earthquake - Damage assessment
version: null
vulnerability: null
---
