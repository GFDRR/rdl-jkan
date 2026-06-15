---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-damage-assessment-overview-map-livoberezhnyi-district-mariupol-city-ukraine
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-damage-assessment-overview-map-livoberezhnyi-district-mariupol-city-ukraine
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-damage-assessment-overview-map-livoberezhnyi-district-mariupol-city-ukraine
dataset_id: rdls_el-ukr_unosat_damageassessmentoverviewm_20220318
description: 'UNOSAT code: CE20220223UKR This map illustrates a satellite imagery
  based damage analysis within an area of interest (AOI) in the residential area of
  Mariupol City, Ukraine. Based on imagery collected on 14 March 2022 and 21 June
  2021, analysts found that 773 out of 17,594 structures sustained visible damage
  in the AOI. This represents approximately 4% of the structures. Out of these, 62
  are destroyed, 315 severely damaged, 321 moderately damaged and 75 possibly damaged.
  This includes 8 schools and 4 health facilities. This analysis is based on structures
  visibly damaged as of 14 March 2022 as seen in marginally degraded satellite imagery.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unosat-damage-assessment-overview-map-livoberezhnyi-district-mariupol-city-ukraine]'
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
    description: Building stock in Livoberezhnyi and Zhovtnevyi Districts classified
      by damage state
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
  description: UNOSAT analysts compared satellite imagery acquired on 21 June 2021
    (baseline) and 14 March 2022 (post-event) over Mariupol City to identify visible
    structural damage. Buildings were classified into damage states (destroyed, severely
    damaged, moderately damaged, possibly damaged) through visual interpretation of
    multi-temporal satellite imagery. The resulting damage inventory includes 773
    damaged structures out of 17,594 total structures, with specific counts for schools
    and health facilities.
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
- href: https://data.humdata.org/dataset/unosat-damage-assessment-overview-map-livoberezhnyi-district-mariupol-city-ukraine
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related shelling and explosions
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to schools and health facilities from conflict-related
      shelling
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
  description: UNOSAT Damage Assessment Overview Map - Livoberezhnyi and Zhovtnevyi
    Districts, Mariupol City, Ukraine (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/UA/CE20220223UKR/CE20220223UKR_UNOSAT_Damage_shp.zip
  format: null
  id: resource_555fa632
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20220223UKR_UNOSAT_Damage_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Damage Assessment Overview Map - Livoberezhnyi and Zhovtnevyi
    Districts, Mariupol City, Ukraine (Geodatabase)
  download_url: https://unosat-maps.web.cern.ch/UA/CE20220223UKR/CE20220223UKR_UNOSAT_Damage_gdb.zip
  format: Geodatabase
  id: resource_3c60175a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20220223UKR_UNOSAT_Damage_gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ukr_unosat_damageassessmentoverviewm_20220318
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
  start: '2022-03-18'
temporal_resolution: null
title: UNOSAT Damage Assessment Overview Map - Livoberezhnyi and Zhovtnevyi Districts,
  Mariupol City, Ukraine
version: null
vulnerability: null
---
