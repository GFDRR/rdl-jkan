---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-monywa-township-monywa-district-sagaing-region-myanmar-as-of-25-april
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-monywa-township-monywa-district-sagaing-region-myanmar-as-of-25-april
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-monywa-township-monywa-district-sagaing-region-myanmar-as-of-25-april
dataset_id: rdls_el-mmr_unosat_damageassessmentmonywatow_20250501
description: 'UNOSAT code: EQ20250328MMR, GDACS ID: 1474477 This map illustrates the
  potentially damaged structures/buildings affected by the March 28, 2025, earthquake
  in Mandalay. The analysis focuses on a part of Monywa Township, Monywa District,
  Sagaing Region, where damage was detected using a WorldView-2 very high-resolution
  satellite image acquired on April 25, 2025. UNOSAT identified 27 damaged structures
  and 170 potentially damaged. This is a preliminary analysis and has not yet been
  validated in the field. Ground verification is encouraged, and feedback can be sent
  to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-in-monywa-township-monywa-district-sagaing-region-myanmar-as-of-25-april]'
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
    description: Building structures in Monywa Township assessed for earthquake damage
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
  description: UNOSAT analysts compared pre- and post-event WorldView-2 very high-resolution
    satellite imagery to detect structural damage in Monywa Township resulting from
    the March 28, 2025 earthquake. Damage was classified into confirmed (27) and potential
    (170) categories based on visual change detection. This preliminary analysis has
    not been field-validated.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-monywa-township-monywa-district-sagaing-region-myanmar-as-of-25-april
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from March 28, 2025 earthquake detected via
      satellite imagery
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
  description: Damage Assessment in Monywa Township, Monywa District, Sagaing Region,
    Myanmar as of 25 April 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4127/GDB.zip
  format: Geodatabase
  id: resource_120699b6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Monywa Township, Monywa District, Sagaing Region,
    Myanmar as of 25 April 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4127/SHP.zip
  format: null
  id: resource_c1afaf3d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SHP.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-mmr_unosat_damageassessmentmonywatow_20250501
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-05-01'
temporal_resolution: null
title: Damage Assessment in Monywa Township, Monywa District, Sagaing Region, Myanmar
  as of 25 April 2025
version: null
vulnerability: null
---
