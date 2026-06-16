---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-mudslide-impact-in-thame-village-solukhumbu-district-koshi-province-as-of-17-aug
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNOSAT damage assessment methodology
    url: https://data.humdata.org/dataset/landslide-mudslide-impact-in-thame-village-solukhumbu-district-koshi-province-as-of-17-aug
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-mudslide-impact-in-thame-village-solukhumbu-district-koshi-province-as-of-17-aug
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-mudslide-impact-in-thame-village-solukhumbu-district-koshi-province-as-of-17-aug
dataset_id: rdls_hel-npl_unosat_landslidemudslideimpactth_20240820
description: 'UNOSAT code: LS20240818NPL This map illustrates satellite-detected landslides
  in Thame Village, Solukhumbu District, Koshi Province, Nepal, as observed from a
  PlanetScope image acquired on 17 August 2024 at 09:58 local time (04:13 UTC). Within
  the analysed area, about 140 hectares of landslide scars are observed. UNITAR-UNOSAT
  identified 43 Potentially damaged structures (20 % from the total buildings in the
  analysed area) and about 2 km of affected roads and paths. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/landslide-mudslide-impact-in-thame-village-solukhumbu-district-koshi-province-as-of-17-aug]'
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
    description: Building structures in the analysed area, with 43 potentially damaged
      structures identified
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
    description: Road and path network affected by landslide/mudslide impacts
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
  description: PlanetScope satellite imagery acquired on 17 August 2024 was analyzed
    by UNOSAT analysts through visual interpretation and multi-temporal comparison
    to detect landslide scars and identify potentially damaged structures and affected
    infrastructure. Landslide extent (140 hectares), building damage counts (43 structures),
    and road/path impacts (2 km) were extracted from the satellite analysis and compiled
    into geodatabase and shapefile formats for spatial representation.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: UNOSAT damage assessment methodology
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/landslide-mudslide-impact-in-thame-village-solukhumbu-district-koshi-province-as-of-17-aug
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct structural damage to 43 buildings from landslide/mudslide
      impacts
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
    description: Direct damage to approximately 2 km of roads and paths from landslide/mudslide
      impacts
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
  description: Nepal - Landslide/mudslide Impact in Thame Village, Solukhumbu District,
    Koshi Province as of 17 August 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3919/LS20240818_gdb.zip
  format: Geodatabase
  id: resource_81d6a783
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240818_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Landslide/mudslide Impact in Thame Village, Solukhumbu District,
    Koshi Province as of 17 August 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3919/LS20240818SHP.zip
  format: null
  id: resource_5601c512
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240818SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-npl_unosat_landslidemudslideimpactth_20240820
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-08-20'
temporal_resolution: null
title: Nepal - Landslide/mudslide Impact in Thame Village, Solukhumbu District, Koshi
  Province as of 17 August 2024
version: null
vulnerability: null
---
