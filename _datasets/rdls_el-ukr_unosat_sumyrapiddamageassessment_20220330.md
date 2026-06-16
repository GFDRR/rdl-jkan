---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/sumy-rapid-damage-assessment-overview-map
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/sumy-rapid-damage-assessment-overview-map
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/sumy-rapid-damage-assessment-overview-map
dataset_id: rdls_el-ukr_unosat_sumyrapiddamageassessment_20220330
description: 'UNOSAT code: CE20220223UKR This map illustrates a satellite imagery
  based Rapid Damage Building Assessment (RDBA) in Sumy City, Ukraine. The RDBA divides
  the city into 500m x 500m cells, each of which is analyzed to determine whether
  or not there are damaged buildings inside the cell. Based on imagery collected on
  20 and 22 March 2022, analysts found that 5 cells out of 1,111 cells sustained visible
  damage. This represents approximately 0.4% of the cells over the city. This analysis
  is based on structures visibly damaged as of 20 and 22 March 2022 as seen in marginally
  degraded satellite imagery. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to United Nations Satellite
  Centre (UNOSAT).. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sumy-rapid-damage-assessment-overview-map]'
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
    description: Building stock in Sumy City classified by damage status based on
      satellite imagery analysis
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on 20 and 22 March
    2022 to identify visible building damage in Sumy City. The city was divided into
    500m x 500m grid cells, and each cell was analyzed to determine presence or absence
    of damaged buildings. Results were compiled into vector geodatabase and shapefile
    formats with confidence levels and damage classification attributes.
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
- href: https://data.humdata.org/dataset/sumy-rapid-damage-assessment-overview-map
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related destruction assessed
      via satellite imagery
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
  description: Ukraine - Sumy Rapid Damage Assessment Overview Map (Zipped Shapefile
    of Sumy analysis area)
  download_url: https://data.humdata.org/dataset/c80a2d62-31bb-4b79-bdfa-481f65b1ebdd/resource/b1992e63-ee1c-4442-82fc-3bbb55e73a57/download/sumy_22march2022_rda.zip
  format: null
  id: resource_b1992e63
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sumy_22March2022_RDA.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ukraine - Sumy Rapid Damage Assessment Overview Map (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/UA/CE20220223UKR/CE20220223UKR_UNOSAT_Damage_gdb.zip
  format: Geodatabase
  id: resource_4ea0a6d5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20220223UKR_UNOSAT_Damage_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ukraine - Sumy Rapid Damage Assessment Overview Map (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/UA/CE20220223UKR/CE20220223UKR_UNOSAT_Damage_shp.zip
  format: null
  id: resource_3c29c328
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20220223UKR_UNOSAT_Damage_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ukr_unosat_sumyrapiddamageassessment_20220330
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
  start: '2022-03-30'
temporal_resolution: null
title: Ukraine - Sumy Rapid Damage Assessment Overview Map
version: null
vulnerability: null
---
