---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-impact-analysis-in-oni-district-racha-lechkhumi-and-kvemo-svaneti-region-georgia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-oni-district-racha-lechkhumi-and-kvemo-svaneti-region-georgia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-oni-district-racha-lechkhumi-and-kvemo-svaneti-region-georgia
dataset_id: rdls_hel-geo_unosat_landslideimpactanalysison_20230807
description: "UNOSAT code LS20230804GEO, GDACS Id: 1102154 This map illustrates satellite-detected\
  \ landslides/mudflow in Oni District, Racha-Lechkhumi and Kvemo Svaneti Region,\
  \ Georgia as observed from a Pl\xE9iades imagery acquired on 06 August 2023 at 14:30\
  \ local time. Within the analyzed area of 9,600 ha, about 220 ha of landslide scars\
  \ were observed. UNITAR-UNOSAT identified 30 affected structures and 6 potentially\
  \ affected structures. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-impact-analysis-in-oni-district-racha-lechkhumi-and-kvemo-svaneti-region-georgia]"
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
    description: Structures identified within the landslide-affected area in Oni District,
      classified as affected or potentially affected
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
    description: Road network within the analyzed area, with attributes describing
      surface type, condition, operational status, and weather-related passability
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
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
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Pl\xE9iades very-high-resolution satellite imagery acquired on 06\
    \ August 2023 was analyzed by UNOSAT analysts through visual interpretation and\
    \ change detection to map landslide and mudflow scars and identify affected structures\
    \ in Oni District, Georgia. The resulting geodatabase and shapefile products include\
    \ delineated hazard extents, road network attributes, and structure impact classifications.\
    \ This is a preliminary post-event satellite-derived analysis intended to support\
    \ emergency response and has not been field-validated."
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
- href: https://data.humdata.org/dataset/landslide-impact-analysis-in-oni-district-racha-lechkhumi-and-kvemo-svaneti-region-georgia
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Count of structures directly affected or potentially affected by
      landslide/mudflow in Oni District as of 06 August 2023
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
  description: Landslide impact analysis in Oni District, Racha-Lechkhumi and Kvemo
    Svaneti Region, Georgia as of 06 August 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3653/LS20230804GEO_gdb.zip
  format: Geodatabase
  id: resource_b91c0e88
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20230804GEO_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide impact analysis in Oni District, Racha-Lechkhumi and Kvemo
    Svaneti Region, Georgia as of 06 August 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3653/LS20230804GEO_SHP.zip
  format: null
  id: resource_9afdf68c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20230804GEO_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-geo_unosat_landslideimpactanalysison_20230807
spatial:
  bbox: null
  centroid: null
  countries:
  - GEO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-08-07'
temporal_resolution: null
title: Landslide impact analysis in Oni District, Racha-Lechkhumi and Kvemo Svaneti
  Region, Georgia as of 06 August 2023
version: null
vulnerability: null
---
