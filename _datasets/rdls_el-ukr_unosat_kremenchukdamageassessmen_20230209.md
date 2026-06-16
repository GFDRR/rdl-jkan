---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/kremenchuk-damage-assessment-overview
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/kremenchuk-damage-assessment-overview
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/kremenchuk-damage-assessment-overview
dataset_id: rdls_el-ukr_unosat_kremenchukdamageassessmen_20230209
description: 'UNOSAT code CE20220223UKR This map illustrates a satellite imagery based
  building damage assessment in the city of Kremenchuk, Ukraine. Based on imagery
  collected on 29 June 2022, the analysis showed 26 structures with visible damage.
  Out of these, 1 is destroyed, 7 severely damaged, 3 moderately damaged and 15 possibly
  damaged. Inset 1 shows a building identified as severely damaged on 29 June 2022.
  While no complete count of buildings for Kremenchuk is available, an open source
  dataset, which is visibly incomplete, indicates at least 19,209 structures in the
  area. This analysis is based on visibly damaged structures as of 29 June 2022, as
  seen in marginally degraded satellite imagery affected by light clouds and other
  limiting factors. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/kremenchuk-damage-assessment-overview]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Building stock in Kremenchuk identified through open source data,
      at least 19,209 structures
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed satellite imagery collected on 29 June 2022
    and compared multi-temporal images to identify notable changes and classify building
    damage into four categories (destroyed, severely damaged, moderately damaged,
    possibly damaged). The assessment identified 26 damaged structures and cross-referenced
    against an incomplete open source building inventory of 19,209 structures in the
    city.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/kremenchuk-damage-assessment-overview
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related impact, 26
      structures with visible damage classified by severity
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
  description: Ukraine - Kremenchuk Damage Assessment Overview (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3483/Kremenchuk_CDA_20220629.gdb.zip
  format: Geodatabase
  id: resource_2b506526
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kremenchuk_CDA_20220629.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ukraine - Kremenchuk Damage Assessment Overview (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3483/Kremenchuk_CDA_20220629.zip
  format: null
  id: resource_e2d51aeb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kremenchuk_CDA_20220629.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ukr_unosat_kremenchukdamageassessmen_20230209
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-02-09'
temporal_resolution: null
title: Ukraine - Kremenchuk Damage Assessment Overview
version: null
vulnerability: null
---
