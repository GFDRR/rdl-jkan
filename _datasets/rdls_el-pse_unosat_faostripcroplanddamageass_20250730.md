---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-july-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Food and Agriculture Organization (FAO)
    url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-july-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-july-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-july-2025
dataset_id: rdls_el-pse_unosat_faostripcroplanddamageass_20250730
description: 'UNOSAT code: CE20231007PSE This map illustrates satellite-detected changes
  in cropland areas of the Gaza Strip resulting from the decline in the health and
  density of crops due to the ongoing conflict. UNOSAT conducted an analysis utilising
  satellite imagery collected by the Sentinel-2 satellite between July 2017 and 2025,
  performing a Normalised Difference Vegetation Index (NDVI) analysis as well as a
  multi-temporal classification to identify notable changes taking place in cropland
  areas during that timeframe. The methodology evaluated the damage as a decline in
  the health and density of crops in July 2025, in comparison to the preceding six
  seasons spanning from 2017 to 2025. The decline in the health and density of the
  crops can be observed due to the impact of activities such as razing, heavy vehicle
  activity, bombing, shelling, and other conflict-related dynamics. The analysis includes
  damage assessment for orchards and other trees, field crops and vegetables. UNOSAT
  and FAO analysis shows that the cropland extent in the Gaza Strip is estimated to
  be 150 sq. km, accounting for approximately 41% of the total area of the Gaza Strip,
  following an extensive land-cover analysis. Compared to the average of the previous
  seven years, approximately 86% of the permanent crop fields in the Gaza Strip exhibited
  a significant decline in health and density in July 2024. In a comprehensive evaluation,
  it was found that there has been a 3% increase in the proportion of cropland that
  has been damaged since the previous analysis conducted in April 2024. Additionally,
  the analysis indicates a notable rise in the destruction of the orchards and other
  trees, field crops and vegetables in the Khan Younis Governorate, with a 4-percentage
  point increase compared to the previous April 2024 analysis. Moreover, there has
  been a notable escalation in the destruction of cropland within the North Gaza Governorate,
  with the percentage rising from 91% in April 2024 to 94% in July 2025. This is a
  preliminary analysis and has not yet been validated in the field.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-july-2025]'
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
    description: Cropland areas in Gaza Strip classified by vegetation health status
      and damage extent
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed multi-temporal Sentinel-2 satellite imagery
    spanning July 2017 to July 2025, applying Normalised Difference Vegetation Index
    (NDVI) analysis and multi-temporal classification to detect changes in cropland
    health and density. Damage was quantified as a decline in vegetation vigor and
    crop density, with results integrated into a geodatabase to map agricultural loss
    across Gaza Strip croplands during the conflict period.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Food and Agriculture Organization (FAO)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-july-2025
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct crop damage and loss of agricultural productivity from conflict-induced
      drought stress and vegetation decline
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: Palestine - UNOSAT - FAO Gaza Strip Cropland Damage Assessment - July
    2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4160/FAO-PAL-015_UNOSAT_Cropland_DA_GDB_July2025.zip
  format: Geodatabase
  id: resource_34a38f5b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FAO-PAL-015_UNOSAT_Cropland_DA_GDB_July2025.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_faostripcroplanddamageass_20250730
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-07-30'
temporal_resolution: null
title: Palestine - UNOSAT - FAO Gaza Strip Cropland Damage Assessment - July 2025
version: null
vulnerability: null
---
