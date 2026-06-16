---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-kingston-saint-catherine-and-saint-andrew-parishes-jamaica-as-of-04-july-2
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-kingston-saint-catherine-and-saint-andrew-parishes-jamaica-as-of-04-july-2
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-kingston-saint-catherine-and-saint-andrew-parishes-jamaica-as-of-04-july-2
dataset_id: rdls_hzd-jamvir_unosat_detectedwaterextentkingst_20240705
description: "UNOSAT code: TC20240702JAM, GDACS ID: 1001067 This map illustrates satellite-detected\
  \ water extent in Kingston, Saint Catherine and Saint Andrew Parishes as observed\
  \ from a TerraSAR-X image acquired at 06:03 local time. Within the analysed area\
  \ of about 1,450 km\xB2, a limited extent of 5 km\xB2 of lands appear to be affected\
  \ with flood waters. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis from radar images may underestimate the\
  \ presence of standing waters in built-up areas and densely vegetated areas due\
  \ to backscattering properties of the radar signal.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/water-extent-in-kingston-saint-catherine-and-saint-andrew-parishes-jamaica-as-of-04-july-2]"
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
  - analysis_type: deterministic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "A TerraSAR-X synthetic aperture radar (SAR) image acquired at 06:03\
    \ local time on 04 July 2024 was processed by UNOSAT analysts using radar backscatter\
    \ change detection to delineate flood water extent across approximately 1,450\
    \ km\xB2 in Kingston, Saint Catherine and Saint Andrew Parishes, Jamaica (GDACS\
    \ event 1001067, Tropical Cyclone Beryl). The analysis identified approximately\
    \ 5 km\xB2 of flooded land area, classified by water status and confidence level,\
    \ and delivered as vector polygon geodata for rapid emergency response support."
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
- href: https://data.humdata.org/dataset/water-extent-in-kingston-saint-catherine-and-saint-andrew-parishes-jamaica-as-of-04-july-2
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
  description: Satellite detected water extent in Kingston, Saint Catherine and Saint
    Andrew Parishes, Jamaica as of 04 July 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3893/TC20240702JAM_gdb.zip
  format: Geodatabase
  id: resource_46a2df0d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240702JAM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Kingston, Saint Catherine and Saint
    Andrew Parishes, Jamaica as of 04 July 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3893/TC20240702JAM_SHP.zip
  format: null
  id: resource_e5edba93
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240702JAM_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-jamvir_unosat_detectedwaterextentkingst_20240705
spatial:
  bbox: null
  centroid: null
  countries:
  - VIR
  - JAM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-07-05'
temporal_resolution: null
title: Satellite detected water extent in Kingston, Saint Catherine and Saint Andrew
  Parishes, Jamaica as of 04 July 2024
version: null
vulnerability: null
---
