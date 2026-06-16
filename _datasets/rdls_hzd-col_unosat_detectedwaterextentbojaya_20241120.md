---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-bojaya-municipality-choco-department-vigia-del-fuerte-municipality-municip
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-bojaya-municipality-choco-department-vigia-del-fuerte-municipality-municip
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-bojaya-municipality-choco-department-vigia-del-fuerte-municipality-municip
dataset_id: rdls_hzd-col_unosat_detectedwaterextentbojaya_20241120
description: "UNOSAT code: FL20241112COL, GDACS ID: 1102988 This map illustrates satellite-detected\
  \ water extent in Riosucio Municipality, Choc\xF3 Department & Vuig\xEDa del Fuerte\
  \ Municipality, Antioquia Department Colombia as observed from a TanDEM-X radar\
  \ image acquired on the 17 November 2024. Within the analysed area of about 1,130km\xB2\
  , a total of about 25 km\xB2 of lands appear to be affected with flood waters. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT). Important\
  \ note: Flood analysis based on radar images may underestimate the extent of standing\
  \ water in built-up or densely vegetated areas due to the radar signal's backscattering\
  \ properties.. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-bojaya-municipality-choco-department-vigia-del-fuerte-municipality-municip]"
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
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed TanDEM-X radar imagery acquired on 17 November\
    \ 2024 over Bojay\xE1 and Vig\xEDa del Fuerte municipalities, comparing satellite\
    \ images to detect notable changes in water extent and delineate flooded areas\
    \ as vector polygons with area measurements."
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
- href: https://data.humdata.org/dataset/water-extent-in-bojaya-municipality-choco-department-vigia-del-fuerte-municipality-municip
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
  description: "Satellite detected water extent in Bojay\xE1 Municipality, Choc\xF3\
    \ Department & Vig\xEDa del Fuerte Municipality Municipality, Antioquia Department\
    \ Colombia as of 17 November 2024 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/4031/FL20241112COL_gdb.zip
  format: Geodatabase
  id: resource_82e0c908
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241112COL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Satellite detected water extent in Bojay\xE1 Municipality, Choc\xF3\
    \ Department & Vig\xEDa del Fuerte Municipality Municipality, Antioquia Department\
    \ Colombia as of 17 November 2024 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/4031/FL20241112COL_SHP.zip
  format: null
  id: resource_c76d896f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241112COL_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-col_unosat_detectedwaterextentbojaya_20241120
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-11-20'
temporal_resolution: null
title: "Satellite detected water extent in Bojay\xE1 Municipality, Choc\xF3 Department\
  \ & Vig\xEDa del Fuerte Municipality Municipality, Antioquia Department Colombia\
  \ as of 17 November 2024"
version: null
vulnerability: null
---
