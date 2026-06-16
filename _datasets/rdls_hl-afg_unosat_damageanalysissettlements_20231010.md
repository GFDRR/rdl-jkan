---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-analysis-by-settlement-and-surface-displacement-of-the-7th-october-2023-hirat-earth
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-analysis-by-settlement-and-surface-displacement-of-the-7th-october-2023-hirat-earth
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-analysis-by-settlement-and-surface-displacement-of-the-7th-october-2023-hirat-earth
dataset_id: rdls_hl-afg_unosat_damageanalysissettlements_20231010
description: "UNOSAT code EQ20231008AFG, GDACS Id: 1394952 This map illustrates the\
  \ level of damage induced by the 07 October earthquake (M6.3) in settlements North\
  \ and North-West Herat as observed from very high-resolution images Pl\xE9iades\
  \ acquired on 09 October 2023. UNOSAT has analysed 4 areas for a total of 750km\xB2\
  \ and detected 56 affected settlements, amongst which 38 are moderately affected,\
  \ 3 severely affected and 15 are almost destroyed. The map illustrates also the\
  \ coseismic surface displacement interferogram related with the 7 October 2023 earthquake\
  \ as deduced using a pair of SAR images acquired on 07 Oct. 2023 and 25 Sep. 2023.\
  \ Narrow fringes translate a higher surface displacement. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/damage-analysis-by-settlement-and-surface-displacement-of-the-7th-october-2023-hirat-earth]"
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
  event_sets_by_hazard_type:
    earthquake:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts compared very high-resolution Pl\xE9iades satellite\
    \ imagery acquired before and after the 7 October 2023 earthquake to detect and\
    \ classify building damage across settlements in Herat province. Coseismic surface\
    \ displacement was derived using SAR interferometry from a pair of images. The\
    \ dataset integrates damage classification (moderately affected, severely affected,\
    \ almost destroyed) with surface displacement measurements to characterize earthquake\
    \ impacts."
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
- href: https://data.humdata.org/dataset/damage-analysis-by-settlement-and-surface-displacement-of-the-7th-october-2023-hirat-earth
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage assessment across 56 affected settlements in Herat,
      classified by damage severity (moderately affected, severely affected, almost
      destroyed)
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
  description: Afghanistan - Damage analysis by settlement and surface displacement
    of the 7th October 2023 Hirat earthquake (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3686/EQ20231008AFG_gdb.zip
  format: Geodatabase
  id: resource_c700c85a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20231008AFG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Damage analysis by settlement and surface displacement
    of the 7th October 2023 Hirat earthquake (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3686/EQ20231008AFG_SHP.zip
  format: null
  id: resource_224c0f4c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20231008AFG_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_unosat_damageanalysissettlements_20231010
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
  start: '2023-10-10'
temporal_resolution: null
title: Afghanistan - Damage analysis by settlement and surface displacement of the
  7th October 2023 Hirat earthquake
version: null
vulnerability: null
---
