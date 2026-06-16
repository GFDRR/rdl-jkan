---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kalam-area-khyber-pakhtunkhwa-province-pakist-november-05-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kalam-area-khyber-pakhtunkhwa-province-pakist-november-05-2015
dataset_id: rdls_hl-pak_unosat_geodatadamageassessmentka_20151105
description: "This map illustrates satellite-detected potential damage in the Kalam\
  \ area of Khyber Pakhtunkhwa Province, Pakistan. This area is located roughly 180\
  \ kilometers southeast of the 26 October 2015 earthquake epicenter. Using a Pl\xE9\
  iades satellite image acquired 31 October 2015 and a WorldView-1 image acquired\
  \ 05 November 2014, UNITAR/UNOSAT identified 165 potentially damaged structures.\
  \ The majority of these structures were situated in valley areas. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to UNITAR/UNOSAT.. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kalam-area-khyber-pakhtunkhwa-province-pakist-november-05-2015]"
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
license: CC-BY-4.0
lineage:
  description: "UNOSAT analysts compared Pl\xE9iades satellite imagery acquired 31\
    \ October 2015 with WorldView-1 baseline imagery from 05 November 2014 to detect\
    \ structural changes in the Kalam area following the 26 October 2015 earthquake.\
    \ Visual interpretation of satellite imagery identified 165 potentially damaged\
    \ structures, primarily in valley locations. This preliminary analysis was not\
    \ field-validated."
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kalam-area-khyber-pakhtunkhwa-province-pakist-november-05-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 165 potentially damaged structures identified via satellite imagery
      comparison in Kalam valley area
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
  description: Geodata of Damage Assessment of Kalam Area, Khyber Pakhtunkhwa Province,
    Pakistan (Shapefile)
  download_url: https://cern.ch/unosat-maps/AF/EQ20151026AFG/EQ20151026AFG_shp.zip
  format: null
  id: resource_c571397b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20151026AFG_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Kalam Area, Khyber Pakhtunkhwa Province,
    Pakistan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/DM/LS20150909DMA/LS20150909DMA_gdb.zip
  format: null
  id: resource_2bf734e6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20150909DMA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Kalam Area, Khyber Pakhtunkhwa Province,
    Pakistan (Shapefile)
  download_url: https://cern.ch/unosat-maps/AF/EQ20151026AFG/EQ20151026AFG.gdb.zip
  format: null
  id: resource_8428f9fa
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20151026AFG.gdb.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-pak_unosat_geodatadamageassessmentka_20151105
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-05'
temporal_resolution: null
title: Geodata of Damage Assessment of Kalam Area, Khyber Pakhtunkhwa Province, Pakistan
version: null
vulnerability: null
---
