---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-dikwa-town-dikwa-local-government-area-borno-state-nigeria-as-of-9-and-19-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-dikwa-town-dikwa-local-government-area-borno-state-nigeria-as-of-9-and-19-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-dikwa-town-dikwa-local-government-area-borno-state-nigeria-as-of-9-and-19-
dataset_id: rdls_he-nga_unosat_detectedwaterextentdikwat_20240925
description: "UNOSAT code: FL20240902NGA This map illustrates the satellite-detected\
  \ accumulated flood extent in Dikwa Town, Dikwa Local Government Area, Borno State,\
  \ Nigeria. as observed from Sentinel-2 images acquired on 9 and 19 September 2024.\
  \ Within analysed areas of about 200 km\xB2, a total of about 30 km\xB2 of lands\
  \ appear to be affected with flood waters. UNITAR-UNOSAT identified about 1,060\
  \ potentially affected structures, along with a potentially affected road extending\
  \ about 26 km within the analysed area. This is a preliminary analysis and has not\
  \ yet been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-dikwa-town-dikwa-local-government-area-borno-state-nigeria-as-of-9-and-19-]"
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
    description: Potentially affected structures identified within the flood extent
      area
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
    description: Road network affected by flood waters, approximately 26 km in length
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed Sentinel-2 satellite imagery acquired on\
    \ 9 and 19 September 2024 over Dikwa Town, comparing multi-temporal images to\
    \ identify notable changes in water extent. Flood water polygons and affected\
    \ infrastructure features were manually delineated from the satellite observations,\
    \ resulting in spatial datasets of inundated areas (approximately 30 km\xB2 within\
    \ 200 km\xB2 analyzed) and affected structures."
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
- href: https://data.humdata.org/dataset/water-extent-in-dikwa-town-dikwa-local-government-area-borno-state-nigeria-as-of-9-and-19-
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
  description: Satellite detected water extent in Dikwa Town, Dikwa Local Government
    Area, Borno state, Nigeria as of 9 and 19 September 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3980/FL20240902NGA_gdb.zip
  format: Geodatabase
  id: resource_b203218b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240902NGA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Dikwa Town, Dikwa Local Government
    Area, Borno state, Nigeria as of 9 and 19 September 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3980/FL20240902NGA_SHP.zip
  format: null
  id: resource_af7d7fa9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240902NGA_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-nga_unosat_detectedwaterextentdikwat_20240925
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-25'
temporal_resolution: null
title: Satellite detected water extent in Dikwa Town, Dikwa Local Government Area,
  Borno state, Nigeria as of 9 and 19 September 2024
version: null
vulnerability: null
---
