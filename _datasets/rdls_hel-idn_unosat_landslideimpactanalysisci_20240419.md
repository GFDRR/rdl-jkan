---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-impact-analysis-in-cipongkor-sub-district-bandung-barat-district-jawa-barat-prov
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-cipongkor-sub-district-bandung-barat-district-jawa-barat-prov
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-cipongkor-sub-district-bandung-barat-district-jawa-barat-prov
dataset_id: rdls_hel-idn_unosat_landslideimpactanalysisci_20240419
description: 'UNOSAT code: EQ20240326IDN, GDACS ID: 1420595 This map illustrates satellite-detected
  landslides in Cipongkor Sub-District, Bandung Barat District, Jawa Barat Province,
  Indonesia as observed from a Fucheng-1 image acquired on 30 March 2024 at 22:34
  local time (15:34) and a WorldView-3 image acquired on 29 March 2024 at 10:12 local
  time (03:12 UTC). Within the analyzed area of 740 hectares, about 50 hectares of
  landslide scars were observed. UTAR-UNOSAT identified 35 damaged structures, 38
  potentially damaged structures and 1 affected road. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to United
  Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-impact-analysis-in-cipongkor-sub-district-bandung-barat-district-jawa-barat-prov]'
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
    description: Building structures classified by damage status (damaged, potentially
      damaged)
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
    description: Road infrastructure affected by landslide activity
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
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: landslide
license: CC-BY-SA-4.0
lineage:
  description: Satellite imagery acquired on 29-30 March 2024 was analyzed by UNOSAT
    analysts to detect landslide scars and assess structural damage in the earthquake-affected
    area. Multi-temporal optical imagery comparison identified 50 hectares of landslide
    scars within 740 hectares of study area and classified 35 damaged and 38 potentially
    damaged structures through visual interpretation.
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
- href: https://data.humdata.org/dataset/landslide-impact-analysis-in-cipongkor-sub-district-bandung-barat-district-jawa-barat-prov
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake-triggered landslides (35 damaged,
      38 potentially damaged structures)
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure impact from landslides (1 affected road)
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
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: Landslide impact analysis in Cipongkor Sub-District, Bandung Barat
    District, Jawa Barat Province, Indonesia as of 29 March 2024. (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3823/FL20240326IDN_gdb.zip
  format: Geodatabase
  id: resource_fe11c68b
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
  description: Landslide impact analysis in Cipongkor Sub-District, Bandung Barat
    District, Jawa Barat Province, Indonesia as of 29 March 2024. (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3823/FL20240326IDN_SHP.zip
  format: null
  id: resource_67cb99ec
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
slug: rdls_hel-idn_unosat_landslideimpactanalysisci_20240419
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
  start: '2024-04-19'
temporal_resolution: null
title: Landslide impact analysis in Cipongkor Sub-District, Bandung Barat District,
  Jawa Barat Province, Indonesia as of 29 March 2024.
version: null
vulnerability: null
---
