---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-impact-analysis-in-makale-selatan-sub-district-tana-toraja-district-sulawesi-sel
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-makale-selatan-sub-district-tana-toraja-district-sulawesi-sel
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-makale-selatan-sub-district-tana-toraja-district-sulawesi-sel
dataset_id: rdls_hel-idn_unosat_landslideimpactanalysisma_20240422
description: 'UNOSAT code: EQ20240326IDN, GDACS ID: 1420595 This map illustrates satellite-detected
  landslides in in Makale Selatan Sub-District, Tana Toraja District, Sulawesi Selatan
  Province, Indonesia as observed from a Jilin-1 image acquired on 19 April 2024.
  Within the analyzed area of 90 hectares, about 6 hectares of landslide scars were
  observed. UNITAR-UNOSAT identified 5 damaged structures, 10 potentially damaged
  structures. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-impact-analysis-in-makale-selatan-sub-district-tana-toraja-district-sulawesi-sel]'
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
    description: Building structures in the landslide-affected area classified by
      damage status
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
  event_sets_by_hazard_type:
    landslide:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: LSI:-
        process: landslide_general
        trigger: null
        type: landslide
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre- and post-event Jilin-1 satellite imagery
    acquired on 19 April 2024 to detect and delineate landslide scars within a 90-hectare
    study area in Makale Selatan Sub-District. Building damage was assessed through
    visual interpretation of structural changes in the optical imagery, identifying
    5 confirmed damaged and 10 potentially damaged structures. This preliminary satellite-based
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
- href: https://data.humdata.org/dataset/landslide-impact-analysis-in-makale-selatan-sub-district-tana-toraja-district-sulawesi-sel
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from satellite-detected landslides triggered
      by earthquake
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
  description: Landslide impact analysis in Makale Selatan Sub-District, Tana Toraja
    District, Sulawesi Selatan Province, Indonesia as of 19 April 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3825/FL20240326IDN_gdb.zip
  format: Geodatabase
  id: resource_06d778e1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240326IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide impact analysis in Makale Selatan Sub-District, Tana Toraja
    District, Sulawesi Selatan Province, Indonesia as of 19 April 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3825/FL20240326IDN_SHP.zip
  format: null
  id: resource_1aaeb3bc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240326IDN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_unosat_landslideimpactanalysisma_20240422
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-04-22'
temporal_resolution: null
title: Landslide impact analysis in Makale Selatan Sub-District, Tana Toraja District,
  Sulawesi Selatan Province, Indonesia as of 19 April 2024
version: null
vulnerability: null
---
