---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-02-to-10-september-2024-over-pakistan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-02-to-10-september-2024-over-pakistan
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-02-to-10-september-2024-over-pakistan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-from-02-to-10-september-2024-over-pakistan
dataset_id: rdls_he-pak_unosat_detectedwaterextents0210s_20240917
description: "UNOSAT code: FL20240804PAK This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Pakistan from 02 to 10 September 2024 compared with the period\
  \ from 26 August to 02 September 2024. Within the cloud free analysed areas of about\
  \ 800,000 km\xB2, a total of about 38,000 km\xB2 of lands appear to be affected\
  \ with flood waters. Water extent appears to have increased of about 1,000 km\xB2\
  \ since the period between 26 August to 02 September 2024. Based on Worldpop population\
  \ data and the maximum flood water extent ~12 million people are potentially exposed\
  \ or living close to flooded areas. This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-from-02-to-10-september-2024-over-pakistan]"
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
    description: Population potentially exposed or living close to detected flood
      water extents based on WorldPop data
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed VIIRS satellite imagery from 02-10 September\
    \ 2024, comparing with baseline imagery from 26 August-02 September 2024 to detect\
    \ cumulative water extents across cloud-free areas (~800,000 km\xB2). Detected\
    \ water areas (~38,000 km\xB2) were intersected with WorldPop population grids\
    \ to estimate ~12 million potentially exposed people, producing vector geodatabase\
    \ and shapefile outputs for post-event flood hazard mapping."
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-from-02-to-10-september-2024-over-pakistan
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
  description: Satellite detected water extents from 02 to 10 September 2024 over
    Pakistan (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3971/FL20240804PAK_gdb.zip
  format: Geodatabase
  id: resource_38426a53
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240804PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents from 02 to 10 September 2024 over
    Pakistan (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3971/FL20240804PAK_SHP.zip
  format: null
  id: resource_73102eb6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240804PAK_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-pak_unosat_detectedwaterextents0210s_20240917
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-17'
temporal_resolution: null
title: Satellite detected water extents from 02 to 10 September 2024 over Pakistan
version: null
vulnerability: null
---
