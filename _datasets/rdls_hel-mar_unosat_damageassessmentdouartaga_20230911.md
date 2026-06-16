---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-douar-tagadirte-igermane-chichaoua-province-marrakech-safi-region-mor
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-douar-tagadirte-igermane-chichaoua-province-marrakech-safi-region-mor
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-douar-tagadirte-igermane-chichaoua-province-marrakech-safi-region-mor
dataset_id: rdls_hel-mar_unosat_damageassessmentdouartaga_20230911
description: 'UNOSAT code EQ20230909MAR, GDACS Id: 1390643 This map illustrates potentially
  damaged structures/buildings by the M6.8 Adassil/Al Haouz earthquake (70 km SW Marrakesh)
  of 08 September 2023 (22:11 UTC) as detected by using a Pleiades very high-resolution
  satellite image acquired on 10 September 2023. Within map extent, UNOSAT identified
  77 damaged/potentially damaged structures. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to United Nations
  Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-douar-tagadirte-igermane-chichaoua-province-marrakech-safi-region-mor]'
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
    description: Building structures in Douar Tagadirte identified from satellite
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
hazard:
  event_sets:
  - analysis_type: probabilistic
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 10
    September 2023 (one day after the M6.8 earthquake) and compared it with pre-event
    imagery to detect changes in building structures. Damaged and potentially damaged
    buildings were manually identified and digitized as point or polygon features
    with damage status recorded in the geodatabase. This preliminary satellite-based
    damage assessment has not been validated through field surveys.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-douar-tagadirte-igermane-chichaoua-province-marrakech-safi-region-mor
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from M6.8 earthquake detected via satellite
      imagery (77 damaged/potentially damaged structures)
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Damage Assessment in Douar Tagadirte (Igermane), Chichaoua Province,
    Marrakech-Safi Region, Morocco as of 10 September 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3665/EQ20230909MAR_gdb.zip
  format: Geodatabase
  id: resource_da89e1c0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230909MAR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Douar Tagadirte (Igermane), Chichaoua Province,
    Marrakech-Safi Region, Morocco as of 10 September 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3665/EQ20230909MAR_SHP.zip
  format: null
  id: resource_7e94e82f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230909MAR_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mar_unosat_damageassessmentdouartaga_20230911
spatial:
  bbox: null
  centroid: null
  countries:
  - MAR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-11'
temporal_resolution: null
title: Damage Assessment in Douar Tagadirte (Igermane), Chichaoua Province, Marrakech-Safi
  Region, Morocco as of 10 September 2023
version: null
vulnerability: null
---
