---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-jalalabad-city-nangarhar-province-as-of-2-september-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-jalalabad-city-nangarhar-province-as-of-2-september-2025
dataset_id: rdls_lss-afg_unosat_damageassessmentjalalabad_20250909
description: 'UNOSAT code: EQ20250901AFG, GDACS ID: 1498339 This map illustrates the
  potentially damaged structures/buildings affected by the August 31, 2025, earthquake
  in Afghanistan. The analysis focuses on Jalalabad City and surrounding area, Nangarhar
  Province, where damage was detected using a Pleiades very high-resolution satellite
  image acquired on September 2, 2025. UNOSAT identified 12 damaged building and 69
  potentially damaged buildings. This is a preliminary analysis and has not yet been
  validated in the field. Ground verification is encouraged, and feedback can be sent
  to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-in-jalalabad-city-nangarhar-province-as-of-2-september-2025]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared Pleiades satellite imagery acquired on September
    2, 2025 with baseline imagery to detect structural damage in Jalalabad City caused
    by the August 31, 2025 earthquake. Building damage was classified into confirmed
    damaged and potentially damaged categories based on visual change detection analysis.
    This preliminary assessment has not been field-validated.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-jalalabad-city-nangarhar-province-as-of-2-september-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake detected via satellite imagery
      analysis
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
  description: Afghanistan - Damage Assessment in Jalalabad City, Nangarhar Province
    as of 2 September 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4196/EQ20250901AFG_SHP.zip
  format: null
  id: resource_e13ddb73
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20250901AFG_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Damage Assessment in Jalalabad City, Nangarhar Province
    as of 2 September 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4196/EQ20250901AFG_GDB.zip
  format: Geodatabase
  id: resource_09742581
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20250901AFG_GDB.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_unosat_damageassessmentjalalabad_20250909
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
  start: '2025-09-09'
temporal_resolution: null
title: Afghanistan - Damage Assessment in Jalalabad City, Nangarhar Province as of
  2 September 2025
version: null
vulnerability: null
---
