---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-malorua-district-shefa-province-vanuatu-as-of-20-december-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-malorua-district-shefa-province-vanuatu-as-of-20-december-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-malorua-district-shefa-province-vanuatu-as-of-20-december-2024
dataset_id: rdls_hel-vut_unosat_damageassessmentmaloruadi_20241223
description: 'UNOSAT code: EQ20241217VUT, GDACS ID: 1458084 This map illustrates the
  potentially damaged structures/buildings and landslide extents resulting from the
  earthquake on December 17, 2024, in Vanuatu, as detected from a WorldView-2 very
  high-resolution satellite image acquired on December 20, 2024, at 09:46 local time.
  Within the analyzed area of approximately 3,000 hectares, UNOSAT identified 6 potentially
  damaged structures and 20 hectares of land affected by landslides. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/damage-assessment-in-malorua-district-shefa-province-vanuatu-as-of-20-december-2024]'
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
    description: Building structures in Malorua District identified from satellite
      imagery
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
- asset_type:
    description: Land area affected by earthquake-triggered landslides
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event WorldView-2 satellite
    imagery to detect structural damage and landslide extents in a 3,000-hectare study
    area in Malorua District. Potentially damaged structures (n=6) and landslide-affected
    land (20 hectares) were manually identified and digitized from the December 20,
    2024 image. This preliminary assessment has not been validated through field surveys.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-malorua-district-shefa-province-vanuatu-as-of-20-december-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake ground motion detected via
      satellite analysis
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
  - asset_category: natural_environment
    asset_dimension: product
    description: Land area affected by earthquake-triggered landslides
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
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
  description: Damage Assessment in Malorua District, Shefa Province, Vanuatu as of
    20 December 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4062/EQ20241217VUT_gdb.zip
  format: Geodatabase
  id: resource_3454ec85
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20241217VUT_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Malorua District, Shefa Province, Vanuatu as of
    20 December 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4062/EQ20241217VUT_SHP.zip
  format: null
  id: resource_73c0e2ca
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20241217VUT_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-vut_unosat_damageassessmentmaloruadi_20241223
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-12-23'
temporal_resolution: null
title: Damage Assessment in Malorua District, Shefa Province, Vanuatu as of 20 December
  2024
version: null
vulnerability: null
---
