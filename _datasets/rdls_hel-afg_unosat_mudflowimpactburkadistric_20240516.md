---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/mudflow-impact-in-burka-district-baghlan-province-afghanistan-as-of-14-may-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudflow-impact-in-burka-district-baghlan-province-afghanistan-as-of-14-may-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudflow-impact-in-burka-district-baghlan-province-afghanistan-as-of-14-may-2024
dataset_id: rdls_hel-afg_unosat_mudflowimpactburkadistric_20240516
description: "UNOSAT code: FL20240512AFG, GDACS ID: 1102616 This map illustrates satellite-detected\
  \ mudflow extent in Burka District, Baghlan Province, Afghanistan as observed from\
  \ a Pl\xE9iades image acquired on 14 May 2024 at 10:48 local time (06:18 UTC). Within\
  \ the analysed area of about 130 km\xB2, a total of about 18 km\xB2 of lands appear\
  \ to be affected by mudflow. UNITAR-UNOSAT identified 2,042 affected structures.\
  \ This is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/mudflow-impact-in-burka-district-baghlan-province-afghanistan-as-of-14-may-2024]"
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
    description: Building structures identified within the mudflow-affected area
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
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: landslide
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed Pl\xE9iades satellite imagery acquired on\
    \ 14 May 2024 and compared it with reference imagery to detect mudflow extent\
    \ and identify affected structures through visual change detection. The analysis\
    \ identified approximately 18 km\xB2 of mudflow-affected land and 2,042 damaged\
    \ structures within a 130 km\xB2 study area in Burka District, Baghlan Province,\
    \ Afghanistan."
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
- href: https://data.humdata.org/dataset/mudflow-impact-in-burka-district-baghlan-province-afghanistan-as-of-14-may-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from mudflow event; 2,042 affected structures
      identified
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  description: Mudflow impact in Burka District, Baghlan Province, Afghanistan as
    of 14 May 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3847/FL20240512AFG_gdb.zip
  format: Geodatabase
  id: resource_347d8743
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240512AFG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mudflow impact in Burka District, Baghlan Province, Afghanistan as
    of 14 May 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3847/FL20240512AFG_SHP.zip
  format: null
  id: resource_2c941b4e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240512AFG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-afg_unosat_mudflowimpactburkadistric_20240516
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
  start: '2024-05-16'
temporal_resolution: null
title: Mudflow impact in Burka District, Baghlan Province, Afghanistan as of 14 May
  2024
version: null
vulnerability: null
---
