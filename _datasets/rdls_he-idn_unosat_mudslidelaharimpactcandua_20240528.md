---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Pl\xE9iades satellite imagery"
    url: https://data.humdata.org/dataset/mudslide-lahar-impact-in-canduang-agam-metropolitan-indonesia-as-of-23-may-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: VRSS-2 satellite imagery
    url: https://data.humdata.org/dataset/mudslide-lahar-impact-in-canduang-agam-metropolitan-indonesia-as-of-23-may-2024
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/mudslide-lahar-impact-in-canduang-agam-metropolitan-indonesia-as-of-23-may-2024
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudslide-lahar-impact-in-canduang-agam-metropolitan-indonesia-as-of-23-may-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudslide-lahar-impact-in-canduang-agam-metropolitan-indonesia-as-of-23-may-2024
dataset_id: rdls_he-idn_unosat_mudslidelaharimpactcandua_20240528
description: "UNOSAT code: LS20240512IDN, GDACS ID: 1102617 This map illustrates satellite-detected\
  \ mudslide / lahar in Canduang, Agam Metropolitan, Sumatera Barat Province, Indonesia,\
  \ as observed from a Pl\xE9iades image acquired on 23 May 2024 and VRSS-2 acquired\
  \ on 17 May 2024. Within the analyzed area of about 2 km\xB2, about 0.3 km\xB2 mudslide\
  \ / lahar extent was observed. Based on Worldpop population data and the maximal\
  \ mudslide / lahar extent 1,880 people are potentially exposed or living close to\
  \ the affected areas. Furthermore, within the analyzed area, 170 structures are\
  \ identified as affected by the floods (10% from the total structures in the analysed\
  \ area), along with about 680 m of roads, as of 23 May 2024 This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/mudslide-lahar-impact-in-canduang-agam-metropolitan-indonesia-as-of-23-may-2024]"
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
    description: Building structures identified within the analyzed mudslide/lahar
      impact area
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
    description: Population potentially exposed or living close to mudslide/lahar
      affected areas based on WorldPop data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
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
  description: "UNOSAT analysts conducted satellite image interpretation by comparing\
    \ Pl\xE9iades (23 May 2024) and VRSS-2 (17 May 2024) imagery to detect mudslide/lahar\
    \ extent and boundaries. Building structures were identified through image analysis\
    \ within the 2 km\xB2 study area. Population exposure was estimated by overlaying\
    \ WorldPop gridded population data with the maximum mudslide/lahar extent to quantify\
    \ potentially affected residents."
  sources:
  - id: source_1
    license: null
    name: "Pl\xE9iades satellite imagery"
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: VRSS-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mudslide-lahar-impact-in-canduang-agam-metropolitan-indonesia-as-of-23-may-2024
  rel: source
loss: null
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
  description: Mudslide / Lahar impact in Canduang, Agam Metropolitan, Indonesia as
    of 23 May 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3858/LS20240512IDN_gdb.zip
  format: Geodatabase
  id: resource_f022e0d4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240512IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mudslide / Lahar impact in Canduang, Agam Metropolitan, Indonesia as
    of 23 May 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3858/LS20240512IDN_SHP.zip
  format: null
  id: resource_071c8089
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240512IDN_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-idn_unosat_mudslidelaharimpactcandua_20240528
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
  start: '2024-05-28'
temporal_resolution: null
title: Mudslide / Lahar impact in Canduang, Agam Metropolitan, Indonesia as of 23
  May 2024
version: null
vulnerability: null
---
