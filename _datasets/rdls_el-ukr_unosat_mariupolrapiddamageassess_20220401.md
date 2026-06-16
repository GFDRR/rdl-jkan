---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/mariupol-rapid-damage-assessment-overview-map
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mariupol-rapid-damage-assessment-overview-map
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mariupol-rapid-damage-assessment-overview-map
dataset_id: rdls_el-ukr_unosat_mariupolrapiddamageassess_20220401
description: 'UNOSAT code: CE20220223UKR This map illustrates a satellite imagery-based
  Rapid Damage Building Assessment (RDBA) of the Mariupolska Hromada, Ukraine. The
  RDBA divides the city into 500m x 500m cells, each of which is analyzed to determine
  whether or not there are damaged buildings inside the cell. Based on imagery collected
  on 26 March 2022, analysts found that 556 cells out of 3,456 sustained visible damage.
  This represents approximately 16% of the cells over the Hromada. Note that not all
  6,456 cells include buildings. Numerous craters are also visible in the fields but
  were not taken into account for this analysis. This analysis is based on structures
  visibly damaged as of 26 March 2022 as seen in marginally degraded satellite imagery
  affected by precipitation, seasonality, and other limiting factors. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/mariupol-rapid-damage-assessment-overview-map]'
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
    description: Building stock in Mariupol classified by damage status from satellite
      imagery assessment
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
  description: UNOSAT analysts conducted a rapid damage assessment by comparing satellite
    imagery acquired on 26 March 2022 with baseline imagery, identifying visible building
    damage within 500m x 500m grid cells across Mariupol. The assessment classified
    556 of 3,456 cells as containing damaged buildings, representing approximately
    16% of the study area. This post-event observational dataset provides direct damage
    counts derived from visual interpretation of high-resolution satellite imagery.
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
- href: https://data.humdata.org/dataset/mariupol-rapid-damage-assessment-overview-map
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
  description: Ukraine - Mariupol Rapid Damage Assessment Overview Map (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/UA/CE20220223UKR/CE20220223UKR_UNOSAT_Damage_gdb.zip
  format: Geodatabase
  id: resource_56e20b5c
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
  description: Ukraine - Mariupol Rapid Damage Assessment Overview Map (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/UA/CE20220223UKR/UNOSAT_Mariupol_26March2022_RDA_shp.zip
  format: null
  id: resource_f11338e4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Mariupol_26March2022_RDA_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ukr_unosat_mariupolrapiddamageassess_20220401
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
  start: '2022-04-01'
temporal_resolution: null
title: Ukraine - Mariupol Rapid Damage Assessment Overview Map
version: null
vulnerability: null
---
