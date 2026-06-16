---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/mudflow-impact-in-kham-district-xiengkhouang-province-lao-pdr-as-of-2-august-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Pleiades satellite imagery
    url: https://data.humdata.org/dataset/mudflow-impact-in-kham-district-xiengkhouang-province-lao-pdr-as-of-2-august-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudflow-impact-in-kham-district-xiengkhouang-province-lao-pdr-as-of-2-august-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudflow-impact-in-kham-district-xiengkhouang-province-lao-pdr-as-of-2-august-2025
dataset_id: rdls_hel-lao_unosat_mudflowimpactkhamdistrict_20250806
description: "UNOSAT code: TC20250722LAO, GDACS ID: 1001181 This map illustrates satellite-detected\
  \ mudflow extent in Kham District, Xiengkhouang Province, Lao PDR as observed from\
  \ Pleiades very high-resolution satellite image acquired on 2 August 2025 at 10:31\
  \ local time (03:31 UTC). Within the analyzed area of approximately 160 km\xB2,\
  \ about 8 km\xB2 of land appears to be affected by landslides/mudflow. Based on\
  \ WorldPop population data and the flood extent, approximately 2,300 people are\
  \ potentially exposed or living close to the flooded areas. Additionally, UNOSAT\
  \ identified around 970 damaged buildings, four damaged bridges, and approximately\
  \ 10 km of affected roads. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mudflow-impact-in-kham-district-xiengkhouang-province-lao-pdr-as-of-2-august-2025]"
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
    description: Population potentially exposed or living close to mudflow-affected
      areas based on WorldPop data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
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
        process: landslide_mudflow
        trigger: null
        type: landslide
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed Pleiades very high-resolution satellite\
    \ imagery acquired on 2 August 2025 to detect mudflow extent through comparative\
    \ image analysis and change detection. Detected mudflow polygons (approximately\
    \ 8 km\xB2 affected area) were intersected with WorldPop gridded population data\
    \ to estimate approximately 2,300 people potentially exposed. Damage assessments\
    \ identified approximately 970 damaged structures through visual interpretation\
    \ of satellite imagery."
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Pleiades satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mudflow-impact-in-kham-district-xiengkhouang-province-lao-pdr-as-of-2-august-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from mudflow event in Kham District
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
  description: Mudflow impact in Kham District, Xiengkhouang Province, Lao PDR as
    of 2 August 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4166/TC20250722LAO_gdb.zip
  format: Geodatabase
  id: resource_be0d8ad4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20250722LAO_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mudflow impact in Kham District, Xiengkhouang Province, Lao PDR as
    of 2 August 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4166/TC20250722LAO_SHP.zip
  format: null
  id: resource_07e54d9e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20250722LAO_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-lao_unosat_mudflowimpactkhamdistrict_20250806
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-08-06'
temporal_resolution: null
title: Mudflow impact in Kham District, Xiengkhouang Province, Lao PDR as of 2 August
  2025
version: null
vulnerability: null
---
