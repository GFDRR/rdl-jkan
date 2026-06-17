---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-assessment-in-derna-city-centre-east-province-libya
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-derna-city-centre-east-province-libya
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-derna-city-centre-east-province-libya
dataset_id: rdls_hel-lby_unosat_floodimpactassessmentdern_20230914
description: "UNOSAT code FL20230912LBY, GDACS Id: 1102204 This map illustrates satellite-detected\
  \ flood extent in the centre of Derna (Libya) as observed from a Pl\xE9iades imagery\
  \ acquired on 13 September 2023 at 13:39 local time after the passage of the Mediterranean\
  \ tropical-like cyclone Daniel. Extensive damage and destructions are observed in\
  \ the city centre and the port area. 2217 buildings were affected by the rushing\
  \ floodwaters in Derna and 886 in this sector of the city. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/flood-impact-assessment-in-derna-city-centre-east-province-libya]"
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
    description: Building stock in Derna city centre affected by flood inundation
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
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed Pl\xE9iades satellite imagery acquired on\
    \ 13 September 2023 and compared multi-temporal images to detect flood extent\
    \ changes in Derna city centre following tropical-like cyclone Daniel. Building\
    \ damage counts were derived from visual interpretation of satellite-detected\
    \ inundation patterns in the city centre and port area."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-impact-assessment-in-derna-city-centre-east-province-libya
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from coastal flooding in Derna city centre
      and port area
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: Flood impact assessment in Derna City centre, East Province, Libya
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3672/FL20230912LBY_gdb.zip
  format: Geodatabase
  id: resource_9c976758
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230912LBY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood impact assessment in Derna City centre, East Province, Libya
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3672/FL20230912LBY_SHP.zip
  format: null
  id: resource_0cf36dc3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230912LBY_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-lby_unosat_floodimpactassessmentdern_20230914
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-14'
temporal_resolution: null
title: Flood impact assessment in Derna City centre, East Province, Libya
version: null
vulnerability: null
---
