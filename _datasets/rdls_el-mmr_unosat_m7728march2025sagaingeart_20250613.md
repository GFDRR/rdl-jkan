---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/m7-7-28-march-2025-sagaing-earthquake-satellite-based-comprehensive-damage-assessment-repo
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Copernicus-EMS
    url: https://data.humdata.org/dataset/m7-7-28-march-2025-sagaing-earthquake-satellite-based-comprehensive-damage-assessment-repo
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: SERTIT
    url: https://data.humdata.org/dataset/m7-7-28-march-2025-sagaing-earthquake-satellite-based-comprehensive-damage-assessment-repo
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/m7-7-28-march-2025-sagaing-earthquake-satellite-based-comprehensive-damage-assessment-repo
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/m7-7-28-march-2025-sagaing-earthquake-satellite-based-comprehensive-damage-assessment-repo
dataset_id: rdls_el-mmr_unosat_m7728march2025sagaingeart_20250613
description: 'UNOSAT code: EQ20250328MMR, GDACS ID: 1474477 This report provides a
  comprehensive damage assessment based on satellite analysis and mapping efforts
  carried out by UNOSAT and other agencies such as Copernicus-EMS and SERTIT to support
  emergency operations following the M7.7 Sagaing earthquake of 28 March 2025.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/m7-7-28-march-2025-sagaing-earthquake-satellite-based-comprehensive-damage-assessment-repo]'
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
    description: Building stock assessed for damage from the M7.7 Sagaing earthquake
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
  description: Satellite imagery from multiple sensors was acquired before and after
    the 28 March 2025 M7.7 Sagaing earthquake. UNOSAT analysts compared multi-temporal
    imagery to identify notable changes in building structures and classify damage
    levels. Results were validated through field observations and integrated with
    assessments from Copernicus-EMS and SERTIT to produce a comprehensive post-event
    damage inventory supporting emergency response operations.
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
    name: Copernicus-EMS
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: SERTIT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/m7-7-28-march-2025-sagaing-earthquake-satellite-based-comprehensive-damage-assessment-repo
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from M7.7 Sagaing earthquake based
      on satellite imagery analysis
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
  description: Myanmar - M7.7 28 March 2025 Sagaing Earthquake, Satellite-Based Comprehensive
    Damage Assessment Report (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4141/EQ20250328MMR_gdb.zip
  format: Geodatabase
  id: resource_e9fdeac6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20250328MMR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Myanmar - M7.7 28 March 2025 Sagaing Earthquake, Satellite-Based Comprehensive
    Damage Assessment Report (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4141/EQ20250328MMR_SHP.zip
  format: null
  id: resource_ccac6b67
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20250328MMR_SHP.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-mmr_unosat_m7728march2025sagaingeart_20250613
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
  start: '2025-06-13'
temporal_resolution: null
title: Myanmar - M7.7 28 March 2025 Sagaing Earthquake, Satellite-Based Comprehensive
  Damage Assessment Report
version: null
vulnerability: null
---
