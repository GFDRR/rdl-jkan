---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-over-juba-county-central-equatoria-province-south-sudan-as-of-06-may-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-juba-county-central-equatoria-province-south-sudan-as-of-06-may-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-juba-county-central-equatoria-province-south-sudan-as-of-06-may-2024
dataset_id: rdls_hzd-ssd_unosat_detectedwaterextentoverju_20240514
description: "UNOSAT code: FL20240425SSD This map illustrates satellite-detected water\
  \ in Juba City, Juba County, Central Equatoria Province, South Sudan, as observed\
  \ from a Sentinel-2 image acquired on 06 May 2024 at 10:06 local time (08:06 UTC).\
  \ Within the analysed area of about 64,000 km\xB2, a total of about 37 km\xB2 of\
  \ land appears to be affected with flood waters. This is a preliminary analysis\
  \ and has not yet been validated in the field. Please send ground feedback to the\
  \ United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-juba-county-central-equatoria-province-south-sudan-as-of-06-may-2024]"
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
  description: "Sentinel-2 satellite image acquired on 06 May 2024 was analyzed by\
    \ UNOSAT analysts through visual interpretation and multi-temporal comparison\
    \ to detect water extent changes. Water pixels were classified and vectorized\
    \ to delineate flood inundation areas, with total affected area calculated as\
    \ 37 km\xB2 within the 64,000 km\xB2 study area of Juba County."
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
- href: https://data.humdata.org/dataset/water-extent-over-juba-county-central-equatoria-province-south-sudan-as-of-06-may-2024
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
  description: Satellite detected water extent over Juba County, Central Equatoria
    Province, South Sudan as of 06 May 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3843/FL20240425SSD_gdb.zip
  format: Geodatabase
  id: resource_638c89b1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240425SSD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Juba County, Central Equatoria
    Province, South Sudan as of 06 May 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3843/FL20240425SSD_SHP.zip
  format: null
  id: resource_0d5db236
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240425SSD_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ssd_unosat_detectedwaterextentoverju_20240514
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-05-14'
temporal_resolution: null
title: Satellite detected water extent over Juba County, Central Equatoria Province,
  South Sudan as of 06 May 2024
version: null
vulnerability: null
---
